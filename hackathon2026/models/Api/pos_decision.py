from typing import Literal

from pydantic import BaseModel, Field


class PosIdentifierDecision(BaseModel):
    identifier_type: Literal["package_id", "cruiseline_id", "none"] = Field(
        ...,
        description="Which identifier, if any, the prompt explicitly supplied for a POS lookup.",
    )
    package_id: int | None = Field(default=None, ge=1)
    cruiseline_id: int | None = Field(default=None, ge=1)
    reason: str
