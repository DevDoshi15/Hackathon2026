import random
import uuid
from typing import Any

from hackathon2026.services.nitro_client import NitroClientError, post_nitro
from hackathon2026.services.pos_service import pos_service

LIST_FARECODES_PATH = "/v2/reservation/cruise/listfarecodes"

# Placeholder traveler ages for this shopping-phase call, same as category/cabin availability.
# There is no separate traveller step in this flow yet, so real ages aren't known this early.
PLACEHOLDER_CUSTOMERS = [
    {"rph": 1, "age": 30},
    {"rph": 2, "age": 30},
]


class FarecodeService:
    async def alookup(self, package_id: int, pos: dict[str, Any]) -> dict[str, Any]:
        body = {
            "cruiseReservation": {
                "pos": pos_service.build_pos_payload(pos, include_currency=True),
                "cruise": {"packageId": package_id},
            },
            "customers": PLACEHOLDER_CUSTOMERS,
            "trackingInfo": {"token": uuid.uuid4().hex},
        }

        try:
            data = await post_nitro(LIST_FARECODES_PATH, body)
        except NitroClientError as error:
            return _farecode_result(request=body, error=str(error))

        if not data.get("isSucceed"):
            print(f"[farecode_service] isSucceed=false, raw={data}")
            return _farecode_result(request=body, raw=data, error="Farecode availability lookup did not succeed.")

        fare_codes = data.get("data", {}).get("cruiseReservation", {}).get("fareCodes", [])
        print(f"[farecode_service] success, {len(fare_codes)} fare codes")
        return _farecode_result(is_succeed=True, request=body, fare_codes=fare_codes, raw=data)

    def select_farecode(
        self,
        fare_codes: list[dict[str, Any]],
        requested_code: str | None,
    ) -> dict[str, Any]:
        if requested_code:
            matched = next(
                (fare for fare in fare_codes if str(fare.get("code", "")).upper() == requested_code.upper()),
                None,
            )
            if matched is None:
                available_codes = [fare.get("code") for fare in fare_codes]
                return {
                    "selected": None,
                    "error": (
                        f"Farecode '{requested_code}' is not available for this package. "
                        f"Available farecodes: {available_codes}"
                    ),
                }
            return {"selected": matched, "error": None}

        if not fare_codes:
            return {"selected": None, "error": "No farecodes are available for this package."}

        return {"selected": random.choice(fare_codes), "error": None}


def _farecode_result(
    is_succeed: bool = False,
    fare_codes: list | None = None,
    request: dict | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "fare_codes": fare_codes or [],
        "request": request,
        "raw": raw,
        "error": error,
    }


farecode_service = FarecodeService()
