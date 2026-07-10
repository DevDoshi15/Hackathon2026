import random
import uuid
from typing import Any

from hackathon2026.services.nitro_client import NitroClientError, post_nitro
from hackathon2026.services.pos_service import pos_service

LIST_CATEGORIES_PATH = "/v2/reservation/cruise/listcategories"

# Best-effort convention: a category code's leading letter hints at its room type
# (e.g. "2B" -> Balcony). Not documented by the API - it's an opaque, supplier-defined
# code - but this is the common cruise-industry convention.
CATEGORY_TYPE_LETTERS = {
    "inside": "I",
    "oceanview": "O",
    "balcony": "B",
    "suite": "S",
}

# Placeholder traveler ages for shopping-phase pricing calls (category/cabin availability).
# There is no separate traveller step in this flow yet, so real ages aren't known this early.
PLACEHOLDER_CUSTOMERS = [
    {"rph": 1, "age": 30},
    {"rph": 2, "age": 30},
]


class CategoryService:
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
            data = await post_nitro(LIST_CATEGORIES_PATH, body)
        except NitroClientError as error:
            return _category_result(error=str(error))

        if not data.get("isSucceed"):
            print(f"[category_service] isSucceed=false, raw={data}")
            return _category_result(raw=data, error="Category availability lookup did not succeed.")

        categories = data.get("data", {}).get("cruiseReservation", {}).get("categories", [])
        print(f"[category_service] success, {len(categories)} categories")
        return _category_result(is_succeed=True, categories=categories, raw=data)

    def select_category(
        self,
        categories: list[dict[str, Any]],
        requested_code: str | None,
        requested_type: str | None = None,
    ) -> dict[str, Any]:
        if requested_code:
            matched = next(
                (c for c in categories if str(c.get("code", "")).upper() == requested_code.upper()),
                None,
            )
            if matched is None:
                available_codes = [category.get("code") for category in categories]
                return {
                    "selected": None,
                    "error": (
                        f"Category '{requested_code}' is not available for this package. "
                        f"Available category codes: {available_codes}"
                    ),
                }
            return {"selected": matched, "error": None}

        if requested_type:
            letter = CATEGORY_TYPE_LETTERS.get(requested_type.lower())
            matches = [c for c in categories if letter and str(c.get("code", "")).upper().startswith(letter)]
            if not matches:
                available_codes = [category.get("code") for category in categories]
                return {
                    "selected": None,
                    "error": (
                        f"No '{requested_type}' category is available for this package. "
                        f"Available category codes: {available_codes}"
                    ),
                }
            return {"selected": random.choice(matches), "error": None}

        if not categories:
            return {"selected": None, "error": "No categories are available for this package."}

        return {"selected": random.choice(categories), "error": None}

    def select_farecode(
        self,
        fares: list[dict[str, Any]],
        requested_farecode: str | None,
    ) -> dict[str, Any]:
        if requested_farecode:
            matched = next(
                (
                    fare
                    for fare in fares
                    if str((fare.get("fareCode") or {}).get("code", "")).upper() == requested_farecode.upper()
                ),
                None,
            )
            if matched is None:
                available_farecodes = [(fare.get("fareCode") or {}).get("code") for fare in fares]
                return {
                    "selected": None,
                    "error": (
                        f"Farecode '{requested_farecode}' is not available for this category. "
                        f"Available farecodes: {available_farecodes}"
                    ),
                }
            return {"selected": matched, "error": None}

        if not fares:
            return {"selected": None, "error": "No fares are available for this category."}

        return {"selected": random.choice(fares), "error": None}


def _category_result(
    is_succeed: bool = False,
    categories: list | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "categories": categories or [],
        "raw": raw,
        "error": error,
    }


category_service = CategoryService()
