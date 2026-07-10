from typing import Literal

from pydantic import BaseModel, Field


class PromptRouteDecision(BaseModel):
    flow: Literal["booking", "casual"] = Field(
        ...,
        description="booking only for booking creation or explicit booking request/response step requests.",
    )
    intent: Literal["booking_workflow", "general_question"]
    step: Literal[
        "pos",
        "category",
        "cabin",
        "cabin_hold",
        "price",
        "tokenize_card",
        "create_reservation",
        "general",
    ]
    reason: str
