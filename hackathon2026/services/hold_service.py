import uuid
from typing import Any

from hackathon2026.services.nitro_client import NitroClientError, post_nitro
from hackathon2026.services.pos_service import pos_service

HOLD_CABIN_PATH = "/v2/reservation/cruise/holdcabin"

# Same placeholder travelers used by category/cabin availability - no separate traveller
# step exists yet to source real ages from.
PLACEHOLDER_CUSTOMERS = [
    {"rph": 1, "age": 30},
    {"rph": 2, "age": 30},
]
PLACEHOLDER_CUSTOMER_REFERENCES = [
    {"rph": 1, "isPrimaryContact": True},
    {"rph": 2},
]


class HoldService:
    async def ahold(
        self,
        package_id: int,
        category_code: str,
        farecode: str,
        cabin_number: str,
        pos: dict[str, Any],
        add_ons: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        body = {
            "cruiseReservation": {
                "pos": pos_service.build_pos_payload(pos, include_currency=True),
                "customerReferences": PLACEHOLDER_CUSTOMER_REFERENCES,
                "cruise": {"packageId": package_id, "packageTourId": -1},
                "categories": [
                    {
                        "code": category_code,
                        "fare": {"fareCode": {"code": farecode}},
                        "cabins": [{"number": cabin_number}],
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
            data = await post_nitro(HOLD_CABIN_PATH, body)
        except NitroClientError as error:
            return _hold_result(request=body, error=str(error))

        if not data.get("isSucceed"):
            print(f"[hold_service] isSucceed=false, raw={data}")
            return _hold_result(request=body, raw=data, error="Cabin hold did not succeed.")

        cruise_reservation = data.get("data", {}).get("cruiseReservation", {})
        insurances = cruise_reservation.get("insurances", [])
        # MSC returns a session-tracking value here that must be echoed back into Create
        # Reservation's request (cruiseReservation.externalSessionInfo.externalId) - see
        # standard_create_booking.md. None for suppliers that don't return this.
        external_session_id = cruise_reservation.get("externalSessionInfo", {}).get("externalId")
        print(f"[hold_service] success, {len(insurances)} insurances, external_session_id={external_session_id}")
        return _hold_result(
            is_succeed=True,
            request=body,
            insurances=insurances,
            external_session_id=external_session_id,
            raw=data,
        )


def _hold_result(
    is_succeed: bool = False,
    insurances: list | None = None,
    external_session_id: str | None = None,
    request: dict | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "insurances": insurances or [],
        "external_session_id": external_session_id,
        "request": request,
        "raw": raw,
        "error": error,
    }


hold_service = HoldService()
