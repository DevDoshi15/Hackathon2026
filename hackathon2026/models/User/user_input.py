from pydantic import BaseModel, Field


class UserInput(BaseModel):
    prompt: str = Field(..., min_length=1, description="Booking prompt from the user or AI.")
