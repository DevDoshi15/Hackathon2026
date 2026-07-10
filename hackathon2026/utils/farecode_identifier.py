import re

from hackathon2026.models.Api import FarecodeIdentifierDecision

FARECODE_PATTERN = re.compile(r"fare\s*-?\s*code\s*[:#=]?\s*([A-Za-z0-9_]{1,20})", re.IGNORECASE)


def extract_farecode(prompt: str) -> str | None:
    match = FARECODE_PATTERN.search(prompt)
    return match.group(1).upper() if match else None


def fallback_farecode(prompt: str, reason: str = "local fallback") -> FarecodeIdentifierDecision:
    farecode = extract_farecode(prompt)
    return FarecodeIdentifierDecision(farecode=farecode, reason=reason)
