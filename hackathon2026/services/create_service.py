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
        card_token: str,
        amount: float,
        currency: str,
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
            "paymentToProcess": {
                "cardToken": card_token,
                "amount": amount,
                "currency": currency,
            },
            "customers": PLACEHOLDER_CUSTOMERS,
            "trackingInfo": {"token": uuid.uuid4().hex},
        }

        try:
            data = await post_nitro(CREATE_RESERVATION_PATH, body, timeout=CREATE_TIMEOUT)
        except NitroClientError as error:
            return _create_result(error=str(error))

        if not data.get("isSucceed"):
            print(f"[create_service] isSucceed=false, raw={data}")
            return _create_result(raw=data, error="Booking creation did not succeed.")

        confirmation_number = (
            data.get("data", {})
            .get("cruiseReservation", {})
            .get("reservationReferences", {})
            .get("confirmationNumber")
        )
        print(f"[create_service] success, confirmation_number={confirmation_number}")
        return _create_result(is_succeed=True, confirmation_number=confirmation_number, raw=data)


def _create_result(
    is_succeed: bool = False,
    confirmation_number: str | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "confirmation_number": confirmation_number,
        "raw": raw,
        "error": error,
    }


create_service = CreateService()
