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

        try:
            data = await post_nitro(HOLD_CABIN_PATH, body)
        except NitroClientError as error:
            return _hold_result(error=str(error))

        if not data.get("isSucceed"):
            print(f"[hold_service] isSucceed=false, raw={data}")
            return _hold_result(raw=data, error="Cabin hold did not succeed.")

        insurances = data.get("data", {}).get("cruiseReservation", {}).get("insurances", [])
        print(f"[hold_service] success, {len(insurances)} insurances")
        return _hold_result(is_succeed=True, insurances=insurances, raw=data)


def _hold_result(
    is_succeed: bool = False,
    insurances: list | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "insurances": insurances or [],
        "raw": raw,
        "error": error,
    }


hold_service = HoldService()
