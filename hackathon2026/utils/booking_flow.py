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
    "while making booking"
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
    "package": "package",
    "package id": "package",
    "category": "category",
    "cabin": "cabin",
    "traveller": "traveller",
    "traveler": "traveller",
    "guest": "traveller",
    "payment": "payment",
    "confirm": "confirmation",
    "confirmation": "confirmation",
}

WORKFLOW_STEPS = [
    "package",
    "category",
    "cabin",
    "traveller",
    "payment",
    "confirmation",
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

    return "confirmation" if is_booking_workflow(prompt) else "general"


def steps_until(step: str) -> list[str]:
    if step not in WORKFLOW_STEPS:
        return []
    return WORKFLOW_STEPS[: WORKFLOW_STEPS.index(step) + 1]


def build_booking_workflow_from_step(prompt: str, requested_step: str) -> dict[str, Any]:
    if requested_step == "general":
        requested_step = "confirmation"

    completed_steps = steps_until(requested_step)

    return {
        "flow": "booking",
        "intent": "booking_workflow",
        "step": requested_step,
        "completed_steps": completed_steps,
        "message": f"Booking workflow response prepared till {requested_step} step.",
        "booking_request": {
            "prompt": prompt,
            "package_reference_required": "package" in completed_steps,
            "next_step": next_step_after(requested_step),
        },
    }


def next_step_after(step: str) -> str | None:
    if step not in WORKFLOW_STEPS:
        return WORKFLOW_STEPS[0]

    next_step_index = WORKFLOW_STEPS.index(step) + 1
    if next_step_index >= len(WORKFLOW_STEPS):
        return None
    return WORKFLOW_STEPS[next_step_index]


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
