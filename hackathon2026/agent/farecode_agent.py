import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from hackathon2026.models.Api import FarecodeIdentifierDecision
from hackathon2026.utils.env import load_project_env

FARECODE_AGENT_INSTRUCTIONS = """
You extract an explicit fare code from a travel/cruise booking prompt.

Fare codes are alphanumeric tokens (e.g. "BESTPRICE", "I1071484_GRP") explicitly labeled as a fare code
in the prompt (e.g. "farecode BESTPRICE", "fare code I1071484_GRP"). Only extract a code when the prompt
explicitly labels a token as a fare code.

If no explicit fare code is mentioned, leave farecode unset.
"""


def create_farecode_agent():
    load_project_env()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", FARECODE_AGENT_INSTRUCTIONS),
            ("human", "{prompt}"),
        ]
    )
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    return prompt | model.with_structured_output(FarecodeIdentifierDecision)


async def decide_farecode_with_agent(prompt: str) -> FarecodeIdentifierDecision:
    final_output = await create_farecode_agent().ainvoke({"prompt": prompt})

    if isinstance(final_output, FarecodeIdentifierDecision):
        return final_output
    if isinstance(final_output, dict):
        return _validate_farecode_decision(final_output)
    return _validate_farecode_decision_json(str(final_output))


def _validate_farecode_decision(data: dict) -> FarecodeIdentifierDecision:
    if hasattr(FarecodeIdentifierDecision, "model_validate"):
        return FarecodeIdentifierDecision.model_validate(data)
    return FarecodeIdentifierDecision.parse_obj(data)


def _validate_farecode_decision_json(data: str) -> FarecodeIdentifierDecision:
    if hasattr(FarecodeIdentifierDecision, "model_validate_json"):
        return FarecodeIdentifierDecision.model_validate_json(data)
    return FarecodeIdentifierDecision.parse_raw(data)
