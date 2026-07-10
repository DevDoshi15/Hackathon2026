import re

from hackathon2026.models.Api import CategoryIdentifierDecision

CATEGORY_CODE_PATTERN = re.compile(r"category\s*(?:code)?\s*[:#=]?\s*([A-Za-z0-9]{1,10})", re.IGNORECASE)

CATEGORY_TYPE_KEYWORDS = {
    "inside": "inside",
    "interior": "inside",
    "oceanview": "oceanview",
    "ocean view": "oceanview",
    "outside": "oceanview",
    "balcony": "balcony",
    "veranda": "balcony",
    "suite": "suite",
}


def extract_category_code(prompt: str) -> str | None:
    match = CATEGORY_CODE_PATTERN.search(prompt)
    return match.group(1).upper() if match else None


def extract_category_type(prompt: str) -> str | None:
    normalized_prompt = prompt.lower()
    for keyword, category_type in CATEGORY_TYPE_KEYWORDS.items():
        if keyword in normalized_prompt:
            return category_type
    return None


def fallback_category_code(prompt: str, reason: str = "local fallback") -> CategoryIdentifierDecision:
    category_code = extract_category_code(prompt)
    category_type = extract_category_type(prompt) if category_code is None else None
    return CategoryIdentifierDecision(category_code=category_code, category_type=category_type, reason=reason)
