import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from hackathon2026.models.Api import CategoryIdentifierDecision
from hackathon2026.utils.env import load_project_env

CATEGORY_AGENT_INSTRUCTIONS = """
You extract stateroom category information from a travel/cruise booking prompt.

Category codes are short alphanumeric tokens (e.g. "2B", "XBO") explicitly labeled as a category in the
prompt (e.g. "category 2B", "category code XBO"). Only extract a code when the prompt explicitly labels
a token as a category.

If no explicit code is mentioned but the prompt names a descriptive room type - inside, oceanview,
balcony, or suite - extract that as category_type instead. A code always takes priority over a type
if both are mentioned.

If neither a code nor a type is mentioned, leave both unset.
"""


def create_category_agent():
    load_project_env()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", CATEGORY_AGENT_INSTRUCTIONS),
            ("human", "{prompt}"),
        ]
    )
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    return prompt | model.with_structured_output(CategoryIdentifierDecision)


async def decide_category_code_with_agent(prompt: str) -> CategoryIdentifierDecision:
    final_output = await create_category_agent().ainvoke({"prompt": prompt})

    if isinstance(final_output, CategoryIdentifierDecision):
        return final_output
    if isinstance(final_output, dict):
        return _validate_category_decision(final_output)
    return _validate_category_decision_json(str(final_output))


def _validate_category_decision(data: dict) -> CategoryIdentifierDecision:
    if hasattr(CategoryIdentifierDecision, "model_validate"):
        return CategoryIdentifierDecision.model_validate(data)
    return CategoryIdentifierDecision.parse_obj(data)


def _validate_category_decision_json(data: str) -> CategoryIdentifierDecision:
    if hasattr(CategoryIdentifierDecision, "model_validate_json"):
        return CategoryIdentifierDecision.model_validate_json(data)
    return CategoryIdentifierDecision.parse_raw(data)
