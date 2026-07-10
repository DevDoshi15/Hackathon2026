from typing import Any

from pydantic import BaseModel, Field


class ApiResponse(BaseModel):
    status: str = Field(..., examples=["success"])
    response: Any
    response_time_ms: float = Field(..., ge=0)
