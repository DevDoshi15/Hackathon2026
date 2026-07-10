from typing import Any

from hackathon2026.agent import (
    decide_cabin_number_with_agent,
    decide_category_code_with_agent,
    decide_farecode_with_agent,
    decide_pos_identifier_with_agent,
)
from hackathon2026.core import BookingContext
from hackathon2026.models.Api import (
    ApiResponse,
    CabinIdentifierDecision,
    CategoryIdentifierDecision,
    FarecodeIdentifierDecision,
    PosIdentifierDecision,
)
from hackathon2026.models.User import UserInput
from hackathon2026.services.cabin_service import cabin_service
from hackathon2026.services.category_service import category_service
from hackathon2026.services.create_service import create_service
from hackathon2026.services.hold_service import hold_service
from hackathon2026.services.pos_service import pos_service
from hackathon2026.services.price_service import price_service
from hackathon2026.services.tokenize_service import tokenize_service
from hackathon2026.utils import (
    WORKFLOW_STEPS,
    fallback_cabin_number,
    fallback_category_code,
    fallback_farecode,
    fallback_pos_identifier,
)


def _payload(step: str, message: str, response: dict[str, Any] | None = None, **extra: Any) -> dict[str, Any]:
    payload = {"flow": "booking", "intent": "booking_workflow", "step": step, "message": message}
    if response is not None:
        payload["response"] = response
    payload.update(extra)
    return payload


class BookingOrchestrator:
    """Runs the general booking flow sequentially, fresh on every call, no state carried
    between requests:
    POS -> Category Availability (+ farecode) -> Cabin Availability -> Cabin Hold ->
    Price Reservation -> Tokenize Card -> Create Reservation w/ Payment.
    If the prompt explicitly names a step to stop at (step != "general"), the flow stops
    there and reports that step's own result instead of continuing further. Each response
    only carries the most recent API call's result, not the full accumulated chain.
    """

    async def run(self, prompt: str, step: str) -> dict[str, Any]:
        requested_step = step if step in WORKFLOW_STEPS else None
        context = BookingContext()

        early_exit = await self._resolve_identifier(prompt, context)
        if early_exit:
            return early_exit

        early_exit = await self._run_pos(context)
        if early_exit:
            return early_exit

        early_exit = self._select_pos(context)
        if early_exit:
            return early_exit

        if requested_step == "pos":
            print("[orchestrator] requested step is pos, stopping here")
            return _payload(
                "pos",
                "Point-of-sale lookup succeeded.",
                context.pos_result,
                pos_selected=context.pos_selected,
            )

        early_exit, selected_category = await self._run_category(prompt, context)
        if early_exit:
            return early_exit

        early_exit, selected_fare = await self._select_farecode(prompt, context, selected_category)
        if early_exit:
            return early_exit

        if requested_step == "category":
            print("[orchestrator] requested step is category, stopping here")
            return _payload(
                "category",
                "Category availability lookup succeeded.",
                context.category_result,
                selected_category=selected_category,
                selected_fare=selected_fare,
            )

        early_exit, cabins = await self._run_cabin(context)
        if early_exit:
            return early_exit

        early_exit, selected_cabin = await self._select_cabin(prompt, context, cabins)
        if early_exit:
            return early_exit

        if requested_step == "cabin":
            print("[orchestrator] requested step is cabin, stopping here")
            return _payload(
                "cabin",
                "Cabin availability lookup succeeded.",
                context.cabin_result,
                selected_cabin=selected_cabin,
            )

        early_exit = await self._run_hold(context)
        if early_exit:
            return early_exit

        if requested_step == "cabin_hold":
            print("[orchestrator] requested step is cabin_hold, stopping here")
            return _payload("cabin_hold", "Cabin hold succeeded.", context.hold_result)

        early_exit = await self._run_price(context)
        if early_exit:
            return early_exit

        if requested_step == "price":
            print("[orchestrator] requested step is price, stopping here")
            return _payload("price", "Price reservation succeeded.", context.price_result)

        early_exit = await self._run_tokenize(context)
        if early_exit:
            return early_exit

        if requested_step == "tokenize_card":
            print("[orchestrator] requested step is tokenize_card, stopping here")
            return _payload("tokenize_card", "Card tokenization succeeded.", context.tokenize_result)

        return await self._run_create(context)

    async def _resolve_identifier(self, prompt: str, context: BookingContext) -> dict[str, Any] | None:
        print("[orchestrator] resolving package/cruiseline id from prompt")
        pos_decision, pos_router_type = await self._decide_pos_identifier(prompt)
        print(
            f"[orchestrator] pos_router={pos_router_type} identifier_type={pos_decision.identifier_type} "
            f"package_id={pos_decision.package_id} cruiseline_id={pos_decision.cruiseline_id}"
        )

        if pos_decision.identifier_type == "package_id" and pos_decision.package_id:
            context.package_id = pos_decision.package_id
        elif pos_decision.identifier_type == "cruiseline_id" and pos_decision.cruiseline_id:
            context.cruiseline_id = pos_decision.cruiseline_id

        if context.package_id is None and context.cruiseline_id is None:
            print("[orchestrator] no identifier found, asking user for a package id")
            return _payload("pos", "I need a package id (or cruiseline id) to continue this booking. Please provide one.")
        return None

    async def _run_pos(self, context: BookingContext) -> dict[str, Any] | None:
        print(f"[orchestrator] calling POS with package_id={context.package_id} cruiseline_id={context.cruiseline_id}")
        context.pos_result = await pos_service.alookup(
            package_id=context.package_id,
            cruiseline_id=context.cruiseline_id,
        )
        print(f"[orchestrator] POS result is_succeed={context.pos_result.get('is_succeed')} error={context.pos_result.get('error')}")

        if not context.pos_result.get("is_succeed"):
            print("[orchestrator] POS lookup failed, returning failure payload")
            return _payload("pos", "Point-of-sale lookup failed for this booking.", context.pos_result)
        return None

    def _select_pos(self, context: BookingContext) -> dict[str, Any] | None:
        print("[orchestrator] selecting a Test-mode POS entry")
        selection = pos_service.select_test_pos(context.pos_result.get("point_of_sales", []))
        if selection["selected"] is None:
            print(f"[orchestrator] no Test-mode POS available: {selection['error']}")
            return _payload("pos", selection["error"], context.pos_result)

        context.pos_selected = selection["selected"]
        print(f"[orchestrator] selected pos id={context.pos_selected.get('id')} currency={context.pos_selected.get('currency')}")
        return None

    async def _run_category(
        self,
        prompt: str,
        context: BookingContext,
    ) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        if context.package_id is None:
            print("[orchestrator] category step needs a package id, only cruiseline_id is known")
            return _payload("category", "Category availability needs a package id specifically. Please provide one."), None

        print(f"[orchestrator] calling Category Availability for package_id={context.package_id}")
        context.category_result = await category_service.alookup(
            package_id=context.package_id,
            pos=context.pos_selected,
        )
        print(
            f"[orchestrator] category result is_succeed={context.category_result.get('is_succeed')} "
            f"error={context.category_result.get('error')}"
        )

        if not context.category_result.get("is_succeed"):
            return _payload("category", "Category availability lookup failed for this booking.", context.category_result), None

        categories = context.category_result.get("categories", [])

        print("[orchestrator] running category agent")
        category_decision, category_router_type = await self._decide_category_code(prompt)
        print(
            f"[orchestrator] category_router={category_router_type} requested_code={category_decision.category_code} "
            f"requested_type={category_decision.category_type}"
        )

        selection = category_service.select_category(
            categories,
            category_decision.category_code,
            category_decision.category_type,
        )
        if selection["selected"] is None:
            print(f"[orchestrator] category selection failed: {selection['error']}")
            return _payload("category", selection["error"], context.category_result), None

        context.category_code = selection["selected"].get("code")
        print(f"[orchestrator] category selected={context.category_code}")
        return None, selection["selected"]

    async def _select_farecode(
        self,
        prompt: str,
        context: BookingContext,
        selected_category: dict[str, Any],
    ) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        fares = selected_category.get("fares", [])

        print("[orchestrator] running farecode agent")
        farecode_decision, farecode_router_type = await self._decide_farecode(prompt)
        print(f"[orchestrator] farecode_router={farecode_router_type} requested_farecode={farecode_decision.farecode}")

        selection = category_service.select_farecode(fares, farecode_decision.farecode)
        if selection["selected"] is None:
            print(f"[orchestrator] farecode selection failed: {selection['error']}")
            return _payload("category", selection["error"], context.category_result), None

        selected_fare = selection["selected"]
        context.farecode = (selected_fare.get("fareCode") or {}).get("code")
        print(f"[orchestrator] farecode selected={context.farecode}")
        return None, selected_fare

    async def _run_cabin(
        self,
        context: BookingContext,
    ) -> tuple[dict[str, Any] | None, list[dict[str, Any]] | None]:
        print(
            f"[orchestrator] calling Cabin Availability for package_id={context.package_id} "
            f"category={context.category_code} farecode={context.farecode}"
        )
        context.cabin_result = await cabin_service.alookup(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            pos=context.pos_selected,
        )
        print(
            f"[orchestrator] cabin result is_succeed={context.cabin_result.get('is_succeed')} "
            f"error={context.cabin_result.get('error')}"
        )

        if not context.cabin_result.get("is_succeed"):
            return _payload("cabin", "Cabin availability lookup failed for this booking.", context.cabin_result), None

        return None, context.cabin_result.get("cabins", [])

    async def _select_cabin(
        self,
        prompt: str,
        context: BookingContext,
        cabins: list[dict[str, Any]],
    ) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        print("[orchestrator] running cabin agent")
        cabin_decision, cabin_router_type = await self._decide_cabin_number(prompt)
        print(f"[orchestrator] cabin_router={cabin_router_type} requested_cabin={cabin_decision.cabin_number}")

        selection = cabin_service.select_cabin(
            context.package_id,
            context.category_code,
            cabins,
            cabin_decision.cabin_number,
        )
        if selection["selected"] is None:
            print(f"[orchestrator] cabin selection failed: {selection['error']}")
            return _payload("cabin", selection["error"], context.cabin_result), None

        context.cabin_number = selection["selected"].get("number")
        print(f"[orchestrator] cabin selected={context.cabin_number}")
        return None, selection["selected"]

    async def _run_hold(self, context: BookingContext) -> dict[str, Any] | None:
        print(
            f"[orchestrator] calling Hold Cabin for package_id={context.package_id} category={context.category_code} "
            f"farecode={context.farecode} cabin={context.cabin_number}"
        )
        context.hold_result = await hold_service.ahold(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            cabin_number=context.cabin_number,
            pos=context.pos_selected,
        )
        print(f"[orchestrator] hold result is_succeed={context.hold_result.get('is_succeed')} error={context.hold_result.get('error')}")

        if not context.hold_result.get("is_succeed"):
            return _payload("cabin_hold", "Cabin hold failed for this booking.", context.hold_result)
        return None

    async def _run_price(self, context: BookingContext) -> dict[str, Any] | None:
        # Cabin number carries forward in context but isn't sent here - Price Reservation
        # prices at the category+fare level; cabin selection is independent (per the doc).
        print(
            f"[orchestrator] calling Price Reservation for package_id={context.package_id} "
            f"category={context.category_code} farecode={context.farecode}"
        )
        context.price_result = await price_service.aprice(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            pos=context.pos_selected,
        )
        print(f"[orchestrator] price result is_succeed={context.price_result.get('is_succeed')} error={context.price_result.get('error')}")

        if not context.price_result.get("is_succeed"):
            return _payload("price", "Price reservation failed for this booking.", context.price_result)
        return None

    async def _run_tokenize(self, context: BookingContext) -> dict[str, Any] | None:
        amount = price_service.reservation_total(context.price_result.get("prices", []))
        currency = context.pos_selected.get("currency")
        api_id = context.pos_selected.get("apiId")
        print(f"[orchestrator] calling TokenizeCard for amount={amount} currency={currency} api_id={api_id}")

        context.tokenize_result = await tokenize_service.atokenize(amount=amount, currency=currency, api_id=api_id)
        print(
            f"[orchestrator] tokenize result is_succeed={context.tokenize_result.get('is_succeed')} "
            f"error={context.tokenize_result.get('error')}"
        )

        if not context.tokenize_result.get("is_succeed"):
            return _payload("tokenize_card", "Card tokenization failed for this booking.", context.tokenize_result)

        context.token = context.tokenize_result.get("token")
        return None

    async def _run_create(self, context: BookingContext) -> dict[str, Any]:
        amount = price_service.reservation_total(context.price_result.get("prices", []))
        currency = context.pos_selected.get("currency")
        print(
            f"[orchestrator] calling Create Reservation for package_id={context.package_id} "
            f"category={context.category_code} farecode={context.farecode} cabin={context.cabin_number}"
        )

        context.create_result = await create_service.acreate(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            cabin_number=context.cabin_number,
            card_token=context.token,
            amount=amount,
            currency=currency,
        )
        print(
            f"[orchestrator] create result is_succeed={context.create_result.get('is_succeed')} "
            f"error={context.create_result.get('error')}"
        )

        if not context.create_result.get("is_succeed"):
            return _payload("create_reservation", "Booking creation failed.", context.create_result)

        context.confirmation_number = context.create_result.get("confirmation_number")
        print(f"[orchestrator] booking created, confirmation_number={context.confirmation_number}")
        # Final step of the flow - only the confirmation number is returned, not the
        # full create response (which includes promo rules, echoed customers, etc).
        return _payload(
            "create_reservation",
            f"Booking confirmed. Confirmation number: {context.confirmation_number}",
            {"confirmation_number": context.confirmation_number},
        )

    async def _decide_pos_identifier(self, prompt: str) -> tuple[PosIdentifierDecision, str]:
        try:
            return await decide_pos_identifier_with_agent(prompt), "openai_agent"
        except Exception as error:
            print(f"[orchestrator] POS identifier agent failed ({error}), using local fallback")
            return fallback_pos_identifier(prompt, reason=str(error)), "local_fallback"

    async def _decide_category_code(self, prompt: str) -> tuple[CategoryIdentifierDecision, str]:
        try:
            return await decide_category_code_with_agent(prompt), "openai_agent"
        except Exception as error:
            print(f"[orchestrator] category agent failed ({error}), using local fallback")
            return fallback_category_code(prompt, reason=str(error)), "local_fallback"

    async def _decide_farecode(self, prompt: str) -> tuple[FarecodeIdentifierDecision, str]:
        try:
            return await decide_farecode_with_agent(prompt), "openai_agent"
        except Exception as error:
            print(f"[orchestrator] farecode agent failed ({error}), using local fallback")
            return fallback_farecode(prompt, reason=str(error)), "local_fallback"

    async def _decide_cabin_number(self, prompt: str) -> tuple[CabinIdentifierDecision, str]:
        try:
            return await decide_cabin_number_with_agent(prompt), "openai_agent"
        except Exception as error:
            print(f"[orchestrator] cabin agent failed ({error}), using local fallback")
            return fallback_cabin_number(prompt, reason=str(error)), "local_fallback"


booking_orchestrator = BookingOrchestrator()


class BookingChain:
    def invoke(self, user_input: UserInput | dict[str, Any] | str) -> ApiResponse:
        from hackathon2026.services import decide_flow_service

        return decide_flow_service.decide(user_input)

    async def ainvoke(self, user_input: UserInput | dict[str, Any] | str) -> ApiResponse:
        from hackathon2026.services import decide_flow_service

        return await decide_flow_service.adecide(user_input)


def create_booking_chain() -> BookingChain:
    return BookingChain()


booking_chain = create_booking_chain()
