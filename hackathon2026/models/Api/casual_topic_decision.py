from typing import Literal

from pydantic import BaseModel


class CasualTopicDecision(BaseModel):
    topic: Literal["kb", "request_response"]
    reason: str
