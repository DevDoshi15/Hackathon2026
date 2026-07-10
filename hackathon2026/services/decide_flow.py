import traceback
from time import perf_counter
from typing import Any

from hackathon2026.agent import decide_casual_topic_with_agent, decide_flow_with_agent
from hackathon2026.models.Api import ApiResponse, CasualTopicDecision, PromptRouteDecision
from hackathon2026.models.User import UserInput
from hackathon2026.rag import rag_answer_service, request_response_rag_service
from hackathon2026.utils import (
    build_casual_response,
    extract_prompt,
    fallback_casual_topic,
    fallback_route_prompt,
)

BOOKING_ASYNC_ONLY_MESSAGE = (
    "Live point-of-sale lookups require the async /booking endpoint. "
    "This synchronous path only supports flow classification."
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
        print(f"[decide_flow] received prompt={prompt!r}")

        try:
            route_decision = await decide_flow_with_agent(prompt)
            router_type = "openai_agent"
        except Exception as error:
            print(f"[decide_flow] flow decider agent failed: {error}")
            traceback.print_exc()
            route_decision = fallback_route_prompt(prompt, reason=str(error))
            router_type = "local_fallback"
        print(f"[decide_flow] router={router_type} flow={route_decision.flow} step={route_decision.step}")

        try:
            payload = await self._abuild_payload(prompt, route_decision, router_type)
        except Exception as error:
            print(f"[decide_flow] unexpected error while building payload: {error}")
            traceback.print_exc()
            payload = {
                "flow": route_decision.flow,
                "intent": route_decision.intent,
                "step": route_decision.step,
                "message": f"An unexpected error occurred: {error}",
                "error": True,
            }
        print(f"[decide_flow] responding step={payload.get('step')}")

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
            payload = {
                "flow": "booking",
                "intent": "booking_workflow",
                "step": route_decision.step,
                "message": BOOKING_ASYNC_ONLY_MESSAGE,
            }
        else:
            payload = build_casual_response(prompt)
            # Sync path has no LLM call - topic classification uses the local fallback only.
            topic_decision = fallback_casual_topic(prompt)
            payload["rag"] = self._rag_service_for(topic_decision.topic).answer(prompt)
            payload["casual_topic"] = {"topic": topic_decision.topic, "type": "local_fallback"}

        payload["router"] = {
            "type": router_type,
            "reason": route_decision.reason,
        }
        return payload

    async def _abuild_payload(
        self,
        prompt: str,
        route_decision: PromptRouteDecision,
        router_type: str,
    ) -> dict[str, Any]:
        if route_decision.flow == "booking":
            # Imported lazily: orchestration.booking_chain depends on services (pos/category),
            # so an eager import here would create a circular import at module load time.
            from hackathon2026.orchestration import booking_orchestrator

            payload = await booking_orchestrator.run(prompt, route_decision.step)
        else:
            payload = build_casual_response(prompt)
            topic_decision, topic_router_type = await self._decide_casual_topic(prompt)
            print(f"[decide_flow] casual_topic_router={topic_router_type} topic={topic_decision.topic}")
            payload["rag"] = self._rag_service_for(topic_decision.topic).answer(prompt)
            payload["casual_topic"] = {"topic": topic_decision.topic, "type": topic_router_type}

        payload["router"] = {
            "type": router_type,
            "reason": route_decision.reason,
        }
        return payload

    def _rag_service_for(self, topic: str):
        return request_response_rag_service if topic == "request_response" else rag_answer_service

    async def _decide_casual_topic(self, prompt: str) -> tuple[CasualTopicDecision, str]:
        try:
            return await decide_casual_topic_with_agent(prompt), "openai_agent"
        except Exception as error:
            print(f"[decide_flow] casual topic agent failed ({error}), using local fallback")
            return fallback_casual_topic(prompt, reason=str(error)), "local_fallback"


decide_flow_service = DecideFlowService()
