from typing import Any

from hackathon2026.models.Api import PromptRouteDecision
from hackathon2026.models.User import UserInput

BOOKING_KEYWORDS = {
    "create booking",
    "create me a booking",
    "create a booking",
    "create new booking",
    "make booking",
    "make me a booking",
    "make a booking",
    "new booking",
    "prepare booking",
    "prepare a booking",
    "continue booking",
    "continue a booking",
    "while making booking",

}

STEP_REQUEST_KEYWORDS = {
    "give me response",
    "give response",
    "response till",
    "respond till",
    "give me request",
    "give request",
    "request till",
    "go to",
    "till",
    "until",
}

STEP_KEYWORDS = {
    # Note: "package id"/"package" are NOT here - mentioning a package id supplies
    # the identifier, it is not a request to stop at any particular step.
    "pos step": "pos",
    "point of sale": "pos",
    "office credentials": "pos",
    "farecode step": "farecode",
    "farecode availability": "farecode",
    "list farecodes": "farecode",
    "category": "category",
    "dining step": "dining",
    "list dining": "dining",
    "list dinings": "dining",
    "dining availability": "dining",
    "hold cabin": "cabin_hold",
    "cabin hold": "cabin_hold",
    "cabin": "cabin",
    "price reservation": "price",
    "payment schedule": "price",
    "price": "price",
    "tokenize card": "tokenize_card",
    "tokenize": "tokenize_card",
    "card token": "tokenize_card",
    "create reservation": "create_reservation",
    "complete booking": "create_reservation",
    "complete the booking": "create_reservation",
    "finish booking": "create_reservation",
    "confirm booking": "create_reservation",
    "confirm the booking": "create_reservation",
    "confirmation": "create_reservation",
}

# farecode and dining only apply to certain cruise-line scenarios (e.g. MSC) - they're
# simply never reached for suppliers whose flow skips them (see BookingOrchestrator.run).
WORKFLOW_STEPS = [
    "pos",
    "farecode",
    "category",
    "cabin",
    "dining",
    "cabin_hold",
    "price",
    "tokenize_card",
    "create_reservation",
]


def extract_prompt(user_input: UserInput | dict[str, Any] | str) -> str:
    if isinstance(user_input, UserInput):
        return user_input.prompt
    if isinstance(user_input, dict):
        return str(user_input.get("prompt", "")).strip()
    return str(user_input).strip()


def normalize_prompt(prompt: str) -> str:
    return " ".join(prompt.lower().split())


def is_booking_workflow(prompt: str) -> bool:
    normalized_prompt = normalize_prompt(prompt)
    has_booking_keyword = any(keyword in normalized_prompt for keyword in BOOKING_KEYWORDS)
    has_step_request = any(keyword in normalized_prompt for keyword in STEP_REQUEST_KEYWORDS) and any(
        keyword in normalized_prompt for keyword in STEP_KEYWORDS
    )

    return has_booking_keyword or has_step_request


def detect_requested_step(prompt: str) -> str:
    normalized_prompt = normalize_prompt(prompt)
    matched_steps = []

    for keyword, step in STEP_KEYWORDS.items():
        if keyword in normalized_prompt:
            matched_steps.append(step)

    if matched_steps:
        return max(matched_steps, key=WORKFLOW_STEPS.index)

    return "general"


def build_casual_response(prompt: str) -> dict[str, Any]:
    return {
        "flow": "casual",
        "intent": "general_question",
        "step": "general",
        "message": "This prompt looks like a casual or general question, not a booking workflow request.",
        "answer": "I can answer this as a general question, or you can mention booking details like package id, category, or cabin to start the booking workflow.",
        "prompt": prompt,
    }


def fallback_route_prompt(prompt: str, reason: str = "local fallback") -> PromptRouteDecision:
    if is_booking_workflow(prompt):
        return PromptRouteDecision(
            flow="booking",
            intent="booking_workflow",
            step=detect_requested_step(prompt),
            reason=reason,
        )

    return PromptRouteDecision(
        flow="casual",
        intent="general_question",
        step="general",
        reason=reason,
    )
