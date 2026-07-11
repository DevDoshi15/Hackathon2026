import uuid
from typing import Any

import httpx

from hackathon2026.services.nitro_client import NitroClientError, post_nitro

CREATE_RESERVATION_PATH = "/v2/reservation/cruise/create"

# This is the last, heaviest call in the flow (rules engine, payment, reservation commit) -
# give it more room than the shared default before giving up.
CREATE_TIMEOUT = httpx.Timeout(connect=10.0, read=360.0, write=10.0, pool=10.0)

# Same placeholder passengers used elsewhere in this flow, extended with the address/contact
# info this endpoint's minimum request includes. No separate traveller step exists yet to
# source real passenger details from.
PLACEHOLDER_CUSTOMERS = [
    {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "address": {"country": {"id": "US"}, "state": {"id": "IL"}, "city": {"name": "Chicago"}},
        "ContactInfo": {"Email": "john@example.com", "Phone1": {"CountryCode": "1", "Number": "416-555-4566"}},
    },
    {
        "rph": 2,
        "firstName": "Jane",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "address": {"country": {"id": "US"}},
        "ContactInfo": {"Email": "jane@example.com", "Phone1": {"CountryCode": "1", "Number": "416-555-4566"}},
    },
]
PLACEHOLDER_CUSTOMER_REFERENCES = [
    {"rph": 1, "isPrimaryContact": True},
    {"rph": 2},
]


class CreateService:
    async def acreate(
        self,
        package_id: int,
        category_code: str,
        farecode: str,
        cabin_number: str,
        currency: str,
        card_token: str | None = None,
        amount: float | None = None,
        add_ons: list[dict[str, Any]] | None = None,
        dining: dict[str, Any] | None = None,
        external_session_id: str | None = None,
    ) -> dict[str, Any]:
        body = {
            "cruiseReservation": {
                # This endpoint only needs pos.currency (or pos.id), unlike category/cabin/
                # hold/price which also need officeId+system - per the doc's own comment.
                "pos": {"currency": currency},
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
        # Without a card_token, Create Reservation runs without payment (e.g. MSC's
        # documented flow never calls Tokenize Card) - see the "Create Reservation
        # (Without Payment)" scenario in create_reservation.md.
        if card_token:
            body["paymentToProcess"] = {
                "cardToken": card_token,
                "amount": amount,
                "currency": currency,
            }
        # autoInclude add-ons and the full dining object (e.g. MSC) must be echoed back
        # here - see Category/List Dinings responses and standard_create_booking.md.
        if add_ons:
            body["cruiseReservation"]["addOns"] = add_ons
        if dining:
            body["cruiseReservation"]["dinings"] = [dining]
        # MSC's session-tracking value from Hold Cabin's response must be echoed back here
        # at the reservation level - see standard_create_booking.md. Only confirmed required
        # for Create (not Price), so it's threaded through this call only.
        if external_session_id:
            body["cruiseReservation"]["externalSessionInfo"] = {"externalId": external_session_id}

        try:
            data = await post_nitro(CREATE_RESERVATION_PATH, body, timeout=CREATE_TIMEOUT)
        except NitroClientError as error:
            return _create_result(request=body, error=str(error))

        if not data.get("isSucceed"):
            print(f"[create_service] isSucceed=false, raw={data}")
            return _create_result(request=body, raw=data, error="Booking creation did not succeed.")

        confirmation_number = (
            data.get("data", {})
            .get("cruiseReservation", {})
            .get("reservationReferences", {})
            .get("confirmationNumber")
        )
        print(f"[create_service] success, confirmation_number={confirmation_number}")
        return _create_result(is_succeed=True, request=body, confirmation_number=confirmation_number, raw=data)


def _create_result(
    is_succeed: bool = False,
    confirmation_number: str | None = None,
    request: dict | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "confirmation_number": confirmation_number,
        "request": request,
        "raw": raw,
        "error": error,
    }


create_service = CreateService()
