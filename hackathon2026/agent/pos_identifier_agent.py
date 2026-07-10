import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from hackathon2026.models.Api import PosIdentifierDecision
from hackathon2026.utils.env import load_project_env

POS_IDENTIFIER_AGENT_INSTRUCTIONS = """
You extract the identifier needed for a point-of-sale (POS) lookup from a travel/cruise booking prompt.

The POS lookup needs exactly one of:
- a package id (identifier_type "package_id")
- a cruiseline id (identifier_type "cruiseline_id")

Only extract a number when the prompt explicitly labels it as a package id ("package id", "package #", "package")
or a cruiseline id ("cruiseline id", "cruise line id", "cruise line"). Never use numbers that refer to guest counts,
cabin counts, ages, dates, prices, or any other unrelated quantity.

If the prompt mentions both a package id and a cruiseline id, prefer package_id.
If neither is explicitly mentioned, use identifier_type "none" and leave both ids unset.
"""


def create_pos_identifier_agent():
    load_project_env()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", POS_IDENTIFIER_AGENT_INSTRUCTIONS),
            ("human", "{prompt}"),
        ]
    )
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    return prompt | model.with_structured_output(PosIdentifierDecision)


async def decide_pos_identifier_with_agent(prompt: str) -> PosIdentifierDecision:
    final_output = await create_pos_identifier_agent().ainvoke({"prompt": prompt})

    if isinstance(final_output, PosIdentifierDecision):
        return final_output
    if isinstance(final_output, dict):
        return _validate_pos_decision(final_output)
    return _validate_pos_decision_json(str(final_output))


def _validate_pos_decision(data: dict) -> PosIdentifierDecision:
    if hasattr(PosIdentifierDecision, "model_validate"):
        return PosIdentifierDecision.model_validate(data)
    return PosIdentifierDecision.parse_obj(data)


def _validate_pos_decision_json(data: str) -> PosIdentifierDecision:
    if hasattr(PosIdentifierDecision, "model_validate_json"):
        return PosIdentifierDecision.model_validate_json(data)
    return PosIdentifierDecision.parse_raw(data)
