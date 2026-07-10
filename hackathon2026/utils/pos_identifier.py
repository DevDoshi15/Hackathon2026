import re

from hackathon2026.models.Api import PosIdentifierDecision

PACKAGE_ID_PATTERN = re.compile(r"package\s*(?:id)?\s*[:#=]?\s*(\d{3,10})", re.IGNORECASE)
CRUISELINE_ID_PATTERN = re.compile(r"cruise\s*-?\s*line\s*(?:id)?\s*[:#=]?\s*(\d{1,10})", re.IGNORECASE)


def extract_package_id(prompt: str) -> int | None:
    match = PACKAGE_ID_PATTERN.search(prompt)
    return int(match.group(1)) if match else None


def extract_cruiseline_id(prompt: str) -> int | None:
    match = CRUISELINE_ID_PATTERN.search(prompt)
    return int(match.group(1)) if match else None


def fallback_pos_identifier(prompt: str, reason: str = "local fallback") -> PosIdentifierDecision:
    package_id = extract_package_id(prompt)
    if package_id is not None:
        return PosIdentifierDecision(identifier_type="package_id", package_id=package_id, reason=reason)

    cruiseline_id = extract_cruiseline_id(prompt)
    if cruiseline_id is not None:
        return PosIdentifierDecision(identifier_type="cruiseline_id", cruiseline_id=cruiseline_id, reason=reason)

    return PosIdentifierDecision(identifier_type="none", reason=reason)
