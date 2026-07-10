import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from hackathon2026.models.Api import PromptRouteDecision
from hackathon2026.utils.env import load_project_env

ROUTER_AGENT_INSTRUCTIONS = """
You classify a user prompt into exactly one flow for a travel/cruise booking API.

Return booking only when the user is asking to create, make, continue, or prepare a booking,
or when they explicitly ask for a request/response up to a booking workflow step.

Important distinction:
- Words like category, cabin, package, or step are not enough by themselves.
- "explain category flow", "what is cabin", "how does package selection happen" are casual.
- "create me a booking with package id P123" is booking.
- "while making booking go to cabin step" is booking.
- "give me response till category step" is booking because it asks for a booking response up to a step.
- "give me request till cabin step" is booking because it asks for a booking request up to a step.

The booking workflow has exactly these steps, in this order:
1. pos - resolve the point-of-sale for the sailing (from a package id or cruiseline id).
2. category - pick a stateroom category and fare code.
3. cabin - pick a specific cabin number.
4. cabin_hold - place a temporary hold on that cabin.
5. price - get the authoritative price and payment schedule.
6. tokenize_card - tokenize a credit card for payment.
7. create_reservation - commit the booking with payment and get a confirmation number.

There is no step called "package" - mentioning a package id (e.g. "with package id P123")
only supplies the identifier used to resolve the pos step; it is never itself a request to
stop there. Only set step to "pos" when the user explicitly asks to stop at that stage, e.g.
"till pos step" or "till point of sale" - not just because a package id was mentioned.

Use the furthest EXPLICITLY mentioned step as step - e.g. "till cabin hold step" -> cabin_hold,
"till price reservation" -> price, "till tokenize card"/"till card token" -> tokenize_card,
"till create reservation"/"till confirmation"/"complete the booking"/"confirm the booking" ->
create_reservation. Do not infer create_reservation just because the user asked to "create a
booking" in general - that phrase alone starts the flow, it doesn't request the final step.

If no step is explicitly mentioned for a booking, use general - the booking flow will then run
all the way through on its own, all the way to create_reservation. For casual questions, also
use general.
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
