from typing import Any

from hackathon2026.models.Api import ApiResponse
from hackathon2026.models.User import UserInput
from hackathon2026.services import decide_flow_service


class BookingChain:
    def invoke(self, user_input: UserInput | dict[str, Any] | str) -> ApiResponse:
        return decide_flow_service.decide(user_input)

    async def ainvoke(self, user_input: UserInput | dict[str, Any] | str) -> ApiResponse:
        return await decide_flow_service.adecide(user_input)


def create_booking_chain() -> BookingChain:
    return BookingChain()


booking_chain = create_booking_chain()
