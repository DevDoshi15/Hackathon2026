import re

from hackathon2026.models.Api import DiningIdentifierDecision

DINING_CODE_PATTERN = re.compile(r"dining\s*code\s*[:#=]?\s*([A-Za-z0-9]{1,10})", re.IGNORECASE)

DINING_KEYWORDS = ["early seating", "late seating", "my time", "anytime dining", "flexible dining"]


def extract_dining_code(prompt: str) -> str | None:
    match = DINING_CODE_PATTERN.search(prompt)
    return match.group(1).upper() if match else None


def extract_dining_keyword(prompt: str) -> str | None:
    normalized = prompt.lower()
    for keyword in DINING_KEYWORDS:
        if keyword in normalized:
            return keyword
    return None


def fallback_dining(prompt: str, reason: str = "local fallback") -> DiningIdentifierDecision:
    dining_code = extract_dining_code(prompt)
    dining_keyword = extract_dining_keyword(prompt) if not dining_code else None
    return DiningIdentifierDecision(dining_code=dining_code, dining_keyword=dining_keyword, reason=reason)
