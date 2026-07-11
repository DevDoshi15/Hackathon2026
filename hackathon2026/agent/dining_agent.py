import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from hackathon2026.models.Api import DiningIdentifierDecision
from hackathon2026.utils.env import load_project_env

DINING_AGENT_INSTRUCTIONS = """
You extract a dining preference from a travel/cruise booking prompt.

Two kinds of preference are possible:
1. An explicit dining code (e.g. "dining CL", "dining code CE") - only extract when explicitly
   labeled as a dining code.
2. A free-text seating preference such as "early seating", "late seating", "my time",
   "anytime dining", "flexible dining" - extract the phrase as dining_keyword when the prompt
   expresses this kind of preference, even without the word "dining code".

If neither is mentioned, leave both fields unset.
"""


def create_dining_agent():
    load_project_env()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", DINING_AGENT_INSTRUCTIONS),
            ("human", "{prompt}"),
        ]
    )
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    return prompt | model.with_structured_output(DiningIdentifierDecision)


async def decide_dining_with_agent(prompt: str) -> DiningIdentifierDecision:
    final_output = await create_dining_agent().ainvoke({"prompt": prompt})

    if isinstance(final_output, DiningIdentifierDecision):
        return final_output
    if isinstance(final_output, dict):
        return _validate_dining_decision(final_output)
    return _validate_dining_decision_json(str(final_output))


def _validate_dining_decision(data: dict) -> DiningIdentifierDecision:
    if hasattr(DiningIdentifierDecision, "model_validate"):
        return DiningIdentifierDecision.model_validate(data)
    return DiningIdentifierDecision.parse_obj(data)


def _validate_dining_decision_json(data: str) -> DiningIdentifierDecision:
    if hasattr(DiningIdentifierDecision, "model_validate_json"):
        return DiningIdentifierDecision.model_validate_json(data)
    return DiningIdentifierDecision.parse_raw(data)
