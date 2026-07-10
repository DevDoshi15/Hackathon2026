import random
import uuid
from typing import Any

from hackathon2026.services.nitro_client import NitroClientError, post_nitro
from hackathon2026.services.pos_service import pos_service

LIST_CABINS_PATH = "/v2/reservation/cruise/listcabins"

# Placeholder traveler ages for shopping-phase pricing calls, same as category availability.
# There is no separate traveller step in this flow yet, so real ages aren't known this early.
PLACEHOLDER_CUSTOMERS = [
    {"rph": 1, "age": 30},
    {"rph": 2, "age": 30},
]

# Cabin numbers already handed out by a random pick, keyed by (package_id, category_code),
# so a fresh call doesn't keep repeating the same one. Resets once every cabin for that
# key has been visited (nothing new left to avoid). This is intentionally the only memory
# kept across requests - not a conversation store, just cabin-pick history.
_visited_cabins: dict[tuple[int, str], set[str]] = {}


class CabinService:
    async def alookup(self, package_id: int, category_code: str, farecode: str, pos: dict[str, Any]) -> dict[str, Any]:
        body = {
            "cruiseReservation": {
                "pos": pos_service.build_pos_payload(pos),
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

        try:
            data = await post_nitro(LIST_CABINS_PATH, body)
        except NitroClientError as error:
            return _cabin_result(error=str(error))

        if not data.get("isSucceed"):
            print(f"[cabin_service] isSucceed=false, raw={data}")
            return _cabin_result(raw=data, error="Cabin availability lookup did not succeed.")

        cabins = data.get("data", {}).get("cruiseReservation", {}).get("cabins", [])
        print(f"[cabin_service] success, {len(cabins)} cabins")
        return _cabin_result(is_succeed=True, cabins=cabins, raw=data)

    def select_cabin(
        self,
        package_id: int,
        category_code: str,
        cabins: list[dict[str, Any]],
        requested_number: str | None,
    ) -> dict[str, Any]:
        if requested_number:
            matched = next(
                (c for c in cabins if str(c.get("number", "")).upper() == requested_number.upper()),
                None,
            )
            if matched is None:
                available_numbers = [cabin.get("number") for cabin in cabins]
                return {
                    "selected": None,
                    "error": (
                        f"Cabin '{requested_number}' is not available for this category. "
                        f"Available cabin numbers: {available_numbers}"
                    ),
                }
            return {"selected": matched, "error": None}

        if not cabins:
            return {"selected": None, "error": "No cabins are available for this category."}

        key = (package_id, category_code)
        visited = _visited_cabins.setdefault(key, set())

        unvisited = [c for c in cabins if c.get("number") not in visited]
        if not unvisited:
            print(f"[cabin_service] all {len(cabins)} cabins already visited for {key}, resetting")
            visited.clear()
            unvisited = cabins

        selected = random.choice(unvisited)
        visited.add(selected.get("number"))
        return {"selected": selected, "error": None}


def _cabin_result(
    is_succeed: bool = False,
    cabins: list | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "cabins": cabins or [],
        "raw": raw,
        "error": error,
    }


cabin_service = CabinService()
