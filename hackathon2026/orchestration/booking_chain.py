from typing import Any

from hackathon2026.agent import (
    decide_cabin_number_with_agent,
    decide_category_code_with_agent,
    decide_dining_with_agent,
    decide_farecode_with_agent,
    decide_pos_identifier_with_agent,
)
from hackathon2026.core import BookingContext
from hackathon2026.models.Api import (
    ApiResponse,
    CabinIdentifierDecision,
    CategoryIdentifierDecision,
    DiningIdentifierDecision,
    FarecodeIdentifierDecision,
    PosIdentifierDecision,
)
from hackathon2026.models.User import UserInput
from hackathon2026.services.cabin_service import cabin_service
from hackathon2026.services.category_service import category_service
from hackathon2026.services.create_service import create_service
from hackathon2026.services.dining_service import dining_service
from hackathon2026.services.farecode_service import farecode_service
from hackathon2026.services.hold_service import hold_service
from hackathon2026.services.pos_service import pos_service
from hackathon2026.services.price_service import price_service
from hackathon2026.services.tokenize_service import tokenize_service
from hackathon2026.utils import (
    WORKFLOW_STEPS,
    fallback_cabin_number,
    fallback_category_code,
    fallback_dining,
    fallback_farecode,
    fallback_pos_identifier,
)

# apiId values (from the selected POS entry) that route into the MSC-specific sequence
# (extra farecode + dining steps, autoInclude add-on echoing) instead of the default one.
MSC_API_IDS = {"MSC"}


def _record(
    context: BookingContext,
    step: str,
    status: str,
    message: str,
    request: dict[str, Any] | None = None,
    response: dict[str, Any] | None = None,
    **extra: Any,
) -> dict[str, Any]:
    entry = {"step": step, "status": status, "message": message}
    if request is not None:
        entry["request"] = request
    if response is not None:
        entry["response"] = response
    entry.update(extra)
    context.steps.append(entry)
    return entry


class BookingOrchestrator:
    """Runs the general booking flow sequentially, fresh on every call, no state carried
    between requests:
    POS -> Category Availability (+ farecode) -> Cabin Availability -> Cabin Hold ->
    Price Reservation -> Tokenize Card -> Create Reservation w/ Payment.
    Records one entry per executed step (context.steps) - whether it succeeded, failed,
    or needs more input - so the caller can show every step reached, not just the last
    one. If the prompt explicitly names a step to stop at (step != "general"), the flow
    stops there instead of continuing further.
    """

    async def run(self, prompt: str, step: str) -> dict[str, Any]:
        requested_step = step if step in WORKFLOW_STEPS else None
        context = BookingContext()

        if not await self._resolve_identifier(prompt, context):
            return self._finalize(context)

        if not await self._do_pos(context):
            return self._finalize(context)
        if requested_step == "pos":
            return self._finalize(context)

        # MSC's own booking flow adds a Farecode Availability step before category and a
        # List Dinings step after cabin - deterministically detected from the POS record's
        # apiId (the same field tokenize_service already keys test cards off), not from the
        # prompt text.
        is_msc = ((context.pos_selected or {}).get("apiId") or "").upper() in MSC_API_IDS
        print(f"[orchestrator] scenario={'msc' if is_msc else 'default'} (apiId={(context.pos_selected or {}).get('apiId')})")

        if is_msc:
            if not await self._do_farecode(prompt, context):
                return self._finalize(context)
            if requested_step == "farecode":
                return self._finalize(context)

        if not await self._do_category(prompt, context):
            return self._finalize(context)
        if requested_step == "category":
            return self._finalize(context)

        if not await self._do_cabin(prompt, context):
            return self._finalize(context)
        if requested_step == "cabin":
            return self._finalize(context)

        if is_msc:
            if not await self._do_dining(prompt, context):
                return self._finalize(context)
            if requested_step == "dining":
                return self._finalize(context)

        if not await self._do_hold(context):
            return self._finalize(context)
        if requested_step == "cabin_hold":
            return self._finalize(context)

        if not await self._do_price(context):
            return self._finalize(context)
        if requested_step == "price":
            return self._finalize(context)

        # MSC's documented flow (standard_create_booking.md) never calls Tokenize Card -
        # it commits with Create Reservation directly, without payment.
        if not is_msc:
            if not await self._do_tokenize(context):
                return self._finalize(context)
            if requested_step == "tokenize_card":
                return self._finalize(context)

        await self._do_create(context)
        return self._finalize(context)

    def _finalize(self, context: BookingContext) -> dict[str, Any]:
        last = context.steps[-1] if context.steps else {"step": "pos", "message": "No steps were executed."}
        payload: dict[str, Any] = {
            "flow": "booking",
            "intent": "booking_workflow",
            "step": last.get("step"),
            "message": last.get("message"),
            "steps": context.steps,
        }
        if "response" in last:
            payload["response"] = last["response"]
        return payload

    async def _resolve_identifier(self, prompt: str, context: BookingContext) -> bool:
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
            _record(
                context,
                "pos",
                "needs_input",
                "I need a package id (or cruiseline id) to continue this booking. Please provide one.",
            )
            return False
        return True

    async def _do_pos(self, context: BookingContext) -> bool:
        print(f"[orchestrator] calling POS with package_id={context.package_id} cruiseline_id={context.cruiseline_id}")
        result = await pos_service.alookup(
            package_id=context.package_id,
            cruiseline_id=context.cruiseline_id,
        )
        context.pos_result = result
        print(f"[orchestrator] POS result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(
                context,
                "pos",
                "failed",
                "Point-of-sale lookup failed for this booking.",
                request=result.get("request"),
                response=result,
            )
            return False

        selection = pos_service.select_test_pos(result.get("point_of_sales", []))
        if selection["selected"] is None:
            print(f"[orchestrator] no Test-mode POS available: {selection['error']}")
            _record(context, "pos", "failed", selection["error"], request=result.get("request"), response=result)
            return False

        context.pos_selected = selection["selected"]
        print(f"[orchestrator] selected pos id={context.pos_selected.get('id')} currency={context.pos_selected.get('currency')}")
        _record(
            context,
            "pos",
            "success",
            "Point-of-sale lookup succeeded.",
            request=result.get("request"),
            response=result,
            pos_selected=context.pos_selected,
        )
        return True

    async def _do_farecode(self, prompt: str, context: BookingContext) -> bool:
        print(f"[orchestrator] calling Farecode Availability for package_id={context.package_id}")
        result = await farecode_service.alookup(package_id=context.package_id, pos=context.pos_selected)
        context.farecode_result = result
        print(f"[orchestrator] farecode result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(
                context,
                "farecode",
                "failed",
                "Farecode availability lookup failed for this booking.",
                request=result.get("request"),
                response=result,
            )
            return False

        print("[orchestrator] running farecode agent")
        farecode_decision, farecode_router_type = await self._decide_farecode(prompt)
        print(f"[orchestrator] farecode_router={farecode_router_type} requested_farecode={farecode_decision.farecode}")

        selection = farecode_service.select_farecode(result.get("fare_codes", []), farecode_decision.farecode)
        if selection["selected"] is None:
            print(f"[orchestrator] farecode selection failed: {selection['error']}")
            _record(context, "farecode", "failed", selection["error"], request=result.get("request"), response=result)
            return False

        selected_farecode = selection["selected"]
        context.farecode = selected_farecode.get("code")
        print(f"[orchestrator] farecode selected={context.farecode}")
        _record(
            context,
            "farecode",
            "success",
            "Farecode availability lookup succeeded.",
            request=result.get("request"),
            response=result,
            selected_farecode=selected_farecode,
        )
        return True

    async def _do_category(self, prompt: str, context: BookingContext) -> bool:
        if context.package_id is None:
            print("[orchestrator] category step needs a package id, only cruiseline_id is known")
            _record(context, "category", "needs_input", "Category availability needs a package id specifically. Please provide one.")
            return False

        print(f"[orchestrator] calling Category Availability for package_id={context.package_id}")
        result = await category_service.alookup(
            package_id=context.package_id,
            pos=context.pos_selected,
        )
        context.category_result = result
        print(f"[orchestrator] category result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(
                context,
                "category",
                "failed",
                "Category availability lookup failed for this booking.",
                request=result.get("request"),
                response=result,
            )
            return False

        categories = result.get("categories", [])

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
            _record(context, "category", "failed", selection["error"], request=result.get("request"), response=result)
            return False

        selected_category = selection["selected"]
        context.category_code = selected_category.get("code")
        print(f"[orchestrator] category selected={context.category_code}")

        if context.farecode:
            # MSC scenario: farecode was already resolved by a dedicated Farecode
            # Availability call before category ran - reuse it instead of deciding fresh,
            # which also validates it actually exists for this category.
            requested_farecode = context.farecode
            print(f"[orchestrator] farecode already resolved={requested_farecode}, validating against this category")
        else:
            print("[orchestrator] running farecode agent")
            farecode_decision, farecode_router_type = await self._decide_farecode(prompt)
            print(f"[orchestrator] farecode_router={farecode_router_type} requested_farecode={farecode_decision.farecode}")
            requested_farecode = farecode_decision.farecode

        fare_selection = category_service.select_farecode(selected_category.get("fares", []), requested_farecode)
        if fare_selection["selected"] is None:
            print(f"[orchestrator] farecode selection failed: {fare_selection['error']}")
            _record(
                context,
                "category",
                "failed",
                fare_selection["error"],
                request=result.get("request"),
                response=result,
                selected_category=selected_category,
            )
            return False

        selected_fare = fare_selection["selected"]
        context.farecode = (selected_fare.get("fareCode") or {}).get("code")
        print(f"[orchestrator] farecode selected={context.farecode}")

        # Some suppliers (e.g. MSC) nest addOns per fare, some flagged autoInclude - those
        # must be echoed forward as full objects into Hold/Price/Create. Harmless empty list
        # for suppliers whose fares carry no addOns at all.
        context.auto_include_addons = [
            addon for addon in (selected_fare.get("addOns") or []) if addon.get("autoInclude")
        ]
        if context.auto_include_addons:
            print(f"[orchestrator] {len(context.auto_include_addons)} autoInclude add-ons to carry forward")

        _record(
            context,
            "category",
            "success",
            "Category availability lookup succeeded.",
            request=result.get("request"),
            response=result,
            selected_category=selected_category,
            selected_fare=selected_fare,
        )
        return True

    async def _do_cabin(self, prompt: str, context: BookingContext) -> bool:
        print(
            f"[orchestrator] calling Cabin Availability for package_id={context.package_id} "
            f"category={context.category_code} farecode={context.farecode}"
        )
        result = await cabin_service.alookup(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            pos=context.pos_selected,
        )
        context.cabin_result = result
        print(f"[orchestrator] cabin result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(
                context,
                "cabin",
                "failed",
                "Cabin availability lookup failed for this booking.",
                request=result.get("request"),
                response=result,
            )
            return False

        print("[orchestrator] running cabin agent")
        cabin_decision, cabin_router_type = await self._decide_cabin_number(prompt)
        print(f"[orchestrator] cabin_router={cabin_router_type} requested_cabin={cabin_decision.cabin_number}")

        selection = cabin_service.select_cabin(
            context.package_id,
            context.category_code,
            result.get("cabins", []),
            cabin_decision.cabin_number,
        )
        if selection["selected"] is None:
            print(f"[orchestrator] cabin selection failed: {selection['error']}")
            _record(context, "cabin", "failed", selection["error"], request=result.get("request"), response=result)
            return False

        selected_cabin = selection["selected"]
        context.cabin_number = selected_cabin.get("number")
        print(f"[orchestrator] cabin selected={context.cabin_number}")
        _record(
            context,
            "cabin",
            "success",
            "Cabin availability lookup succeeded.",
            request=result.get("request"),
            response=result,
            selected_cabin=selected_cabin,
        )
        return True

    async def _do_dining(self, prompt: str, context: BookingContext) -> bool:
        print(
            f"[orchestrator] calling List Dinings for package_id={context.package_id} category={context.category_code} "
            f"farecode={context.farecode} cabin={context.cabin_number}"
        )
        result = await dining_service.alist(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            cabin_number=context.cabin_number,
            pos=context.pos_selected,
        )
        context.dining_result = result
        print(f"[orchestrator] dining result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(context, "dining", "failed", "List Dinings failed for this booking.", request=result.get("request"), response=result)
            return False

        print("[orchestrator] running dining agent")
        dining_decision, dining_router_type = await self._decide_dining(prompt)
        print(
            f"[orchestrator] dining_router={dining_router_type} requested_code={dining_decision.dining_code} "
            f"requested_keyword={dining_decision.dining_keyword}"
        )

        selection = dining_service.select_dining(
            result.get("dinings", []),
            dining_decision.dining_code,
            dining_decision.dining_keyword,
        )
        if selection["selected"] is None:
            print(f"[orchestrator] dining selection failed: {selection['error']}")
            _record(context, "dining", "failed", selection["error"], request=result.get("request"), response=result)
            return False

        context.selected_dining = selection["selected"]
        print(f"[orchestrator] dining selected={context.selected_dining.get('code')}")
        _record(
            context,
            "dining",
            "success",
            "List Dinings succeeded.",
            request=result.get("request"),
            response=result,
            selected_dining=context.selected_dining,
        )
        return True

    async def _do_hold(self, context: BookingContext) -> bool:
        print(
            f"[orchestrator] calling Hold Cabin for package_id={context.package_id} category={context.category_code} "
            f"farecode={context.farecode} cabin={context.cabin_number}"
        )
        result = await hold_service.ahold(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            cabin_number=context.cabin_number,
            pos=context.pos_selected,
            add_ons=context.auto_include_addons or None,
        )
        context.hold_result = result
        print(f"[orchestrator] hold result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(context, "cabin_hold", "failed", "Cabin hold failed for this booking.", request=result.get("request"), response=result)
            return False

        context.external_session_id = result.get("external_session_id")
        _record(context, "cabin_hold", "success", "Cabin hold succeeded.", request=result.get("request"), response=result)
        return True

    async def _do_price(self, context: BookingContext) -> bool:
        # Cabin number carries forward in context but isn't sent here - Price Reservation
        # prices at the category+fare level; cabin selection is independent (per the doc).
        print(
            f"[orchestrator] calling Price Reservation for package_id={context.package_id} "
            f"category={context.category_code} farecode={context.farecode}"
        )
        result = await price_service.aprice(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            pos=context.pos_selected,
            add_ons=context.auto_include_addons or None,
        )
        context.price_result = result
        print(f"[orchestrator] price result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(context, "price", "failed", "Price reservation failed for this booking.", request=result.get("request"), response=result)
            return False

        _record(context, "price", "success", "Price reservation succeeded.", request=result.get("request"), response=result)
        return True

    async def _do_tokenize(self, context: BookingContext) -> bool:
        amount = price_service.reservation_total(context.price_result.get("prices", []))
        currency = context.pos_selected.get("currency")
        api_id = context.pos_selected.get("apiId")
        print(f"[orchestrator] calling TokenizeCard for amount={amount} currency={currency} api_id={api_id}")

        result = await tokenize_service.atokenize(amount=amount, currency=currency, api_id=api_id)
        context.tokenize_result = result
        print(f"[orchestrator] tokenize result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(context, "tokenize_card", "failed", "Card tokenization failed for this booking.", request=result.get("request"), response=result)
            return False

        context.token = result.get("token")
        _record(
            context,
            "tokenize_card",
            "success",
            f"Card tokenized for amount {amount} {currency}.",
            request=result.get("request"),
            response=result,
        )
        return True

    async def _do_create(self, context: BookingContext) -> bool:
        amount = price_service.reservation_total(context.price_result.get("prices", []))
        currency = context.pos_selected.get("currency")
        # context.token is None for scenarios that skip Tokenize Card (e.g. MSC) - Create
        # Reservation then runs without a paymentToProcess block (see create_service.acreate).
        print(
            f"[orchestrator] calling Create Reservation for package_id={context.package_id} "
            f"category={context.category_code} farecode={context.farecode} cabin={context.cabin_number} "
            f"with_payment={bool(context.token)}"
        )

        result = await create_service.acreate(
            package_id=context.package_id,
            category_code=context.category_code,
            farecode=context.farecode,
            cabin_number=context.cabin_number,
            card_token=context.token,
            amount=amount,
            currency=currency,
            add_ons=context.auto_include_addons or None,
            dining=context.selected_dining,
            external_session_id=context.external_session_id,
        )
        context.create_result = result
        print(f"[orchestrator] create result is_succeed={result.get('is_succeed')} error={result.get('error')}")

        if not result.get("is_succeed"):
            _record(context, "create_reservation", "failed", "Booking creation failed.", request=result.get("request"), response=result)
            return False

        context.confirmation_number = result.get("confirmation_number")
        print(f"[orchestrator] booking created, confirmation_number={context.confirmation_number}")
        # Final step of the flow - only the confirmation number is surfaced in the response
        # summary, not the full create response (which includes promo rules, echoed customers,
        # etc); the full request/response is still attached below for the detail view.
        _record(
            context,
            "create_reservation",
            "success",
            f"Booking confirmed. Confirmation number: {context.confirmation_number}",
            request=result.get("request"),
            response=result,
            confirmation_number=context.confirmation_number,
        )
        return True

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

    async def _decide_dining(self, prompt: str) -> tuple[DiningIdentifierDecision, str]:
        try:
            return await decide_dining_with_agent(prompt), "openai_agent"
        except Exception as error:
            print(f"[orchestrator] dining agent failed ({error}), using local fallback")
            return fallback_dining(prompt, reason=str(error)), "local_fallback"


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
