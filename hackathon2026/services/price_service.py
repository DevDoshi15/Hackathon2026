import uuid
from typing import Any

from hackathon2026.services.nitro_client import NitroClientError, post_nitro
from hackathon2026.services.pos_service import pos_service

LIST_PRICES_PATH = "/v2/reservation/cruise/listprices"

# Same placeholder travelers used by category/cabin/hold, extended with the extra fields
# (name, dateOfBirth) this endpoint's minimum request includes. No separate traveller step
# exists yet to source real passenger details from.
PLACEHOLDER_CUSTOMERS = [
    {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1995",
        "age": 30,
        "address": {"country": {"id": "US"}},
    },
    {
        "rph": 2,
        "firstName": "Jane",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1995",
        "age": 30,
        "address": {"country": {"id": "US"}},
    },
]
PLACEHOLDER_CUSTOMER_REFERENCES = [
    {"rph": 1, "isPrimaryContact": True},
    {"rph": 2},
]


class PriceService:
    async def aprice(
        self,
        package_id: int,
        category_code: str,
        farecode: str,
        pos: dict[str, Any],
        add_ons: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        # Cabin number is intentionally not sent - Price Reservation prices at the
        # category+fare level; cabin selection is independent (handled by Hold Cabin).
        body = {
            "cruiseReservation": {
                "pos": pos_service.build_pos_payload(pos, include_currency=True),
                "customerReferences": PLACEHOLDER_CUSTOMER_REFERENCES,
                "cruise": {"packageId": package_id, "packageTourId": -1},
                "categories": [
                    {
                        "code": category_code,
                        "fare": {"fareCode": {"code": farecode}},
                    }
                ],
            },
            "customers": PLACEHOLDER_CUSTOMERS,
            "trackingInfo": {"token": uuid.uuid4().hex},
        }
        # autoInclude add-ons (e.g. MSC) must be echoed back as full objects here - see
        # Category Availability's addOns[].autoInclude and standard_create_booking.md.
        if add_ons:
            body["cruiseReservation"]["addOns"] = add_ons

        try:
            data = await post_nitro(LIST_PRICES_PATH, body)
        except NitroClientError as error:
            return _price_result(request=body, error=str(error))

        if not data.get("isSucceed"):
            print(f"[price_service] isSucceed=false, raw={data}")
            return _price_result(request=body, raw=data, error="Price reservation did not succeed.")

        cruise_reservation = data.get("data", {}).get("cruiseReservation", {})
        payment_schedules = cruise_reservation.get("paymentSchedules", {})
        prices = cruise_reservation.get("prices", [])
        print(f"[price_service] success, {len(prices)} price lines")
        return _price_result(is_succeed=True, request=body, payment_schedules=payment_schedules, prices=prices, raw=data)

    def reservation_total(self, prices: list[dict[str, Any]]) -> float:
        # rph == -1 marks a reservation-total line item (vs. a positive rph for one
        # passenger's share) - sum all of them to get the full amount due.
        return sum(price.get("amount", 0) for price in prices if price.get("rph") == -1)


def _price_result(
    is_succeed: bool = False,
    payment_schedules: dict | None = None,
    prices: list | None = None,
    request: dict | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "payment_schedules": payment_schedules or {},
        "prices": prices or [],
        "request": request,
        "raw": raw,
        "error": error,
    }


price_service = PriceService()
