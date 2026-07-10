from pydantic import BaseModel, Field


class CabinIdentifierDecision(BaseModel):
    cabin_number: str | None = Field(
        default=None,
        description="Explicit cabin number mentioned in the prompt, if any.",
    )
    reason: str
