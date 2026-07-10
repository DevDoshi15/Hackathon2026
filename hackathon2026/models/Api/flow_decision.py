from typing import Literal

from pydantic import BaseModel, Field


class PromptRouteDecision(BaseModel):
    flow: Literal["booking", "casual"] = Field(
        ...,
        description="booking only for booking creation or explicit booking request/response step requests.",
    )
    intent: Literal["booking_workflow", "general_question"]
    step: Literal[
        "package",
        "category",
        "cabin",
        "traveller",
        "payment",
        "confirmation",
        "general",
    ]
    reason: str
