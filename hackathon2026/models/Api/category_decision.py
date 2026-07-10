from typing import Literal

from pydantic import BaseModel, Field


class CategoryIdentifierDecision(BaseModel):
    category_code: str | None = Field(
        default=None,
        description="Explicit category code mentioned in the prompt, if any.",
    )
    category_type: Literal["inside", "oceanview", "balcony", "suite"] | None = Field(
        default=None,
        description="Descriptive room type mentioned in the prompt, if any (used only when no explicit code is given).",
    )
    reason: str
