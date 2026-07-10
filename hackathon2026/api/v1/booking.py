from fastapi import APIRouter

from hackathon2026.models.Api import ApiResponse
from hackathon2026.models.User import UserInput
from hackathon2026.orchestration.booking_chain import booking_chain

router = APIRouter(tags=["booking"])


@router.post("/booking", response_model=ApiResponse)
async def create_booking(user_input: UserInput) -> ApiResponse:
    if hasattr(booking_chain, "ainvoke"):
        return await booking_chain.ainvoke(user_input)
    return booking_chain.invoke(user_input)
