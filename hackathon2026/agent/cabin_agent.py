import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from hackathon2026.models.Api import CabinIdentifierDecision
from hackathon2026.utils.env import load_project_env

CABIN_AGENT_INSTRUCTIONS = """
You extract an explicit cabin number from a travel/cruise booking prompt.

Cabin numbers are short alphanumeric tokens (e.g. "6018", "9998") explicitly labeled as a cabin in the
prompt (e.g. "cabin 6018", "cabin number 9998"). Only extract a number when the prompt explicitly labels
it as a cabin. Do not use numbers that refer to guest counts, ages, dates, or prices.

If no explicit cabin number is mentioned, leave cabin_number unset.
"""


def create_cabin_agent():
    load_project_env()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", CABIN_AGENT_INSTRUCTIONS),
            ("human", "{prompt}"),
        ]
    )
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    return prompt | model.with_structured_output(CabinIdentifierDecision)


async def decide_cabin_number_with_agent(prompt: str) -> CabinIdentifierDecision:
    final_output = await create_cabin_agent().ainvoke({"prompt": prompt})

    if isinstance(final_output, CabinIdentifierDecision):
        return final_output
    if isinstance(final_output, dict):
        return _validate_cabin_decision(final_output)
    return _validate_cabin_decision_json(str(final_output))


def _validate_cabin_decision(data: dict) -> CabinIdentifierDecision:
    if hasattr(CabinIdentifierDecision, "model_validate"):
        return CabinIdentifierDecision.model_validate(data)
    return CabinIdentifierDecision.parse_obj(data)


def _validate_cabin_decision_json(data: str) -> CabinIdentifierDecision:
    if hasattr(CabinIdentifierDecision, "model_validate_json"):
        return CabinIdentifierDecision.model_validate_json(data)
    return CabinIdentifierDecision.parse_raw(data)
