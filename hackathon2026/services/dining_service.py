import random
import uuid
from typing import Any

from hackathon2026.services.nitro_client import NitroClientError, post_nitro
from hackathon2026.services.pos_service import pos_service

LIST_DININGS_PATH = "/v2/reservation/cruise/ListDinings"

# Placeholder traveler ages for this shopping-phase call, same as category/cabin availability.
# There is no separate traveller step in this flow yet, so real ages aren't known this early.
PLACEHOLDER_CUSTOMERS = [
    {"rph": 1, "age": 30},
    {"rph": 2, "age": 30},
]


class DiningService:
    async def alist(
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
            data = await post_nitro(LIST_DININGS_PATH, body)
        except NitroClientError as error:
            return _dining_result(request=body, error=str(error))

        if not data.get("isSucceed"):
            print(f"[dining_service] isSucceed=false, raw={data}")
            return _dining_result(request=body, raw=data, error="List Dinings did not succeed.")

        dinings = data.get("data", {}).get("cruiseReservation", {}).get("dinings", [])
        print(f"[dining_service] success, {len(dinings)} dinings")
        return _dining_result(is_succeed=True, request=body, dinings=dinings, raw=data)

    def select_dining(
        self,
        dinings: list[dict[str, Any]],
        requested_code: str | None,
        requested_keyword: str | None = None,
    ) -> dict[str, Any]:
        if requested_code:
            matched = next(
                (d for d in dinings if str(d.get("code", "")).upper() == requested_code.upper()),
                None,
            )
            if matched is None:
                available_codes = [dining.get("code") for dining in dinings]
                return {
                    "selected": None,
                    "error": (
                        f"Dining '{requested_code}' is not available for this selection. "
                        f"Available dining codes: {available_codes}"
                    ),
                }
            return {"selected": matched, "error": None}

        if requested_keyword:
            matched = next(
                (d for d in dinings if requested_keyword.lower() in str(d.get("name", "")).lower()),
                None,
            )
            if matched is None:
                available_names = [dining.get("name") for dining in dinings]
                return {
                    "selected": None,
                    "error": (
                        f"No dining matching '{requested_keyword}' is available for this selection. "
                        f"Available dining options: {available_names}"
                    ),
                }
            return {"selected": matched, "error": None}

        if not dinings:
            return {"selected": None, "error": "No dining options are available for this selection."}

        return {"selected": random.choice(dinings), "error": None}


def _dining_result(
    is_succeed: bool = False,
    dinings: list | None = None,
    request: dict | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "dinings": dinings or [],
        "request": request,
        "raw": raw,
        "error": error,
    }


dining_service = DiningService()
