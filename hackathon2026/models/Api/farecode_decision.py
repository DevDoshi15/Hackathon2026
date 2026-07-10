from pydantic import BaseModel, Field


class FarecodeIdentifierDecision(BaseModel):
    farecode: str | None = Field(
        default=None,
        description="Explicit fare code mentioned in the prompt, if any.",
    )
    reason: str
