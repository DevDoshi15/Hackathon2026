from pydantic import BaseModel, Field


class DiningIdentifierDecision(BaseModel):
    dining_code: str | None = Field(
        default=None,
        description="Explicit dining code mentioned in the prompt, if any.",
    )
    dining_keyword: str | None = Field(
        default=None,
        description="Free-text dining preference mentioned in the prompt, e.g. 'early seating', 'late seating', 'my time', 'anytime dining'.",
    )
    reason: str
