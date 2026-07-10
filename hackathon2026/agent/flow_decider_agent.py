import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from hackathon2026.models.Api import PromptRouteDecision
from hackathon2026.utils.env import load_project_env

ROUTER_AGENT_INSTRUCTIONS = """
You classify a user prompt into exactly one flow for a travel/package booking API.

Return booking only when the user is asking to create, make, continue, or prepare a booking,
or when they explicitly ask for a request/response up to a booking workflow step.

Important distinction:
- Words like category, cabin, package, or step are not enough by themselves.
- "explain category flow", "what is cabin", "how does package selection happen" are casual.
- "create me a booking with package id P123" is booking.
- "while making booking go to cabin step" is booking.
- "give me response till category step" is booking because it asks for a booking response up to a step.
- "give me request till cabin step" is booking because it asks for a booking request up to a step.

Use the furthest mentioned workflow step as step. If no step is mentioned for a booking,
use confirmation. For casual questions, use general.
"""


def create_flow_decider_agent():
    load_project_env()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", ROUTER_AGENT_INSTRUCTIONS),
            ("human", "{prompt}"),
        ]
    )
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    return prompt | model.with_structured_output(PromptRouteDecision)


async def decide_flow_with_agent(prompt: str) -> PromptRouteDecision:
    final_output = await create_flow_decider_agent().ainvoke({"prompt": prompt})

    if isinstance(final_output, PromptRouteDecision):
        return final_output
    if isinstance(final_output, dict):
        return _validate_route_decision(final_output)
    return _validate_route_decision_json(str(final_output))


def _validate_route_decision(data: dict) -> PromptRouteDecision:
    if hasattr(PromptRouteDecision, "model_validate"):
        return PromptRouteDecision.model_validate(data)
    return PromptRouteDecision.parse_obj(data)


def _validate_route_decision_json(data: str) -> PromptRouteDecision:
    if hasattr(PromptRouteDecision, "model_validate_json"):
        return PromptRouteDecision.model_validate_json(data)
    return PromptRouteDecision.parse_raw(data)
