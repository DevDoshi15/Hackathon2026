import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from hackathon2026.models.Api import CasualTopicDecision
from hackathon2026.utils.env import load_project_env

CASUAL_TOPIC_AGENT_INSTRUCTIONS = """
You classify a casual/general (non-booking) question into exactly one topic for a
cruise/travel booking API knowledge base.

Use "request_response" when the user is asking about a specific API's request or response
shape, fields, payload, endpoint, or a concrete example request/response - e.g. "what does
the cabin availability response look like", "show me the request for creating a booking",
"what fields does the price reservation response have".

Use "kb" for everything else - general policy/process/reference questions that are not
about a specific API request/response shape, e.g. "what payment schedule types exist",
"which test credit cards can I use", "what does supplier ID 982 map to".
"""


def create_casual_topic_agent():
    load_project_env()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", CASUAL_TOPIC_AGENT_INSTRUCTIONS),
            ("human", "{prompt}"),
        ]
    )
    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    return prompt | model.with_structured_output(CasualTopicDecision)


async def decide_casual_topic_with_agent(prompt: str) -> CasualTopicDecision:
    final_output = await create_casual_topic_agent().ainvoke({"prompt": prompt})

    if isinstance(final_output, CasualTopicDecision):
        return final_output
    if isinstance(final_output, dict):
        return _validate_casual_topic_decision(final_output)
    return _validate_casual_topic_decision_json(str(final_output))


def _validate_casual_topic_decision(data: dict) -> CasualTopicDecision:
    if hasattr(CasualTopicDecision, "model_validate"):
        return CasualTopicDecision.model_validate(data)
    return CasualTopicDecision.parse_obj(data)


def _validate_casual_topic_decision_json(data: str) -> CasualTopicDecision:
    if hasattr(CasualTopicDecision, "model_validate_json"):
        return CasualTopicDecision.model_validate_json(data)
    return CasualTopicDecision.parse_raw(data)
