import re

from hackathon2026.models.Api import CasualTopicDecision

REQUEST_RESPONSE_KEYWORDS = re.compile(
    r"\b(request|response|payload|endpoint|api\b|postman|json\s+body|request\s+body|response\s+body)\b",
    re.IGNORECASE,
)


def fallback_casual_topic(prompt: str, reason: str = "local fallback") -> CasualTopicDecision:
    topic = "request_response" if REQUEST_RESPONSE_KEYWORDS.search(prompt) else "kb"
    return CasualTopicDecision(topic=topic, reason=reason)
