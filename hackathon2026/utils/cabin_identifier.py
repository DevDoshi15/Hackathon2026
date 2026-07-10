import re

from hackathon2026.models.Api import CabinIdentifierDecision

CABIN_NUMBER_PATTERN = re.compile(r"cabin\s*(?:number|no)?\s*[:#=]?\s*([A-Za-z0-9]{1,10})", re.IGNORECASE)


def extract_cabin_number(prompt: str) -> str | None:
    match = CABIN_NUMBER_PATTERN.search(prompt)
    return match.group(1).upper() if match else None


def fallback_cabin_number(prompt: str, reason: str = "local fallback") -> CabinIdentifierDecision:
    cabin_number = extract_cabin_number(prompt)
    return CabinIdentifierDecision(cabin_number=cabin_number, reason=reason)
