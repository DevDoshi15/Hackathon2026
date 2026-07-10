from time import perf_counter
from typing import Any

from hackathon2026.agent import decide_flow_with_agent
from hackathon2026.models.Api import ApiResponse, PromptRouteDecision
from hackathon2026.models.User import UserInput
from hackathon2026.rag import rag_answer_service
from hackathon2026.utils import (
    build_booking_workflow_from_step,
    build_casual_response,
    extract_prompt,
    fallback_route_prompt,
)


class DecideFlowService:
    def decide(self, user_input: UserInput | dict[str, Any] | str) -> ApiResponse:
        start_time = perf_counter()
        prompt = extract_prompt(user_input)
        route_decision = fallback_route_prompt(prompt)
        payload = self._build_payload(prompt, route_decision, "local_fallback")

        return ApiResponse(
            status="success",
            response=payload,
            response_time_ms=round((perf_counter() - start_time) * 1000, 3),
        )

    async def adecide(self, user_input: UserInput | dict[str, Any] | str) -> ApiResponse:
        start_time = perf_counter()
        prompt = extract_prompt(user_input)

        try:
            route_decision = await decide_flow_with_agent(prompt)
            router_type = "openai_agent"
        except Exception as error:
            route_decision = fallback_route_prompt(prompt, reason=str(error))
            router_type = "local_fallback"

        payload = self._build_payload(prompt, route_decision, router_type)

        return ApiResponse(
            status="success",
            response=payload,
            response_time_ms=round((perf_counter() - start_time) * 1000, 3),
        )

    def _build_payload(
        self,
        prompt: str,
        route_decision: PromptRouteDecision,
        router_type: str,
    ) -> dict[str, Any]:
        if route_decision.flow == "booking":
            payload = build_booking_workflow_from_step(prompt, route_decision.step)
        else:
            payload = build_casual_response(prompt)
            payload["rag"] = rag_answer_service.answer(prompt)

        payload["router"] = {
            "type": router_type,
            "reason": route_decision.reason,
        }
        return payload


decide_flow_service = DecideFlowService()
