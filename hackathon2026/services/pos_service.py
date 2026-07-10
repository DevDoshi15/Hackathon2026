import random
from typing import Any

from hackathon2026.services.nitro_client import NitroClientError, post_nitro

LIST_POS_PATH = "/v2/reservation/cruise/listpos"


class PosService:
    async def alookup(
        self,
        package_id: int | None = None,
        cruiseline_id: int | None = None,
    ) -> dict[str, Any]:
        if package_id is not None:
            body = {"cruiseReservation": {"cruise": {"packageId": package_id}}}
        elif cruiseline_id is not None:
            body = {"cruiseReservation": {"cruise": {"cruiseLine": {"id": cruiseline_id}}}}
        else:
            return _pos_result(error="Either package_id or cruiseline_id is required for a POS lookup.")

        try:
            data = await post_nitro(LIST_POS_PATH, body)
        except NitroClientError as error:
            return _pos_result(error=str(error))

        if not data.get("isSucceed"):
            print(f"[pos_service] isSucceed=false, raw={data}")
            return _pos_result(raw=data, error="POS lookup did not succeed.")

        point_of_sales = data.get("data", {}).get("cruiseReservation", {}).get("pointOfSales", [])
        print(f"[pos_service] success, {len(point_of_sales)} pointOfSales entries")
        return _pos_result(is_succeed=True, point_of_sales=point_of_sales, raw=data)

    def select_test_pos(self, point_of_sales: list[dict[str, Any]]) -> dict[str, Any]:
        test_pos = [pos for pos in point_of_sales if pos.get("system") == "Test"]
        if not test_pos:
            return {"selected": None, "error": "No Test-mode point-of-sale profile was found for this package/cruiseline."}
        return {"selected": random.choice(test_pos), "error": None}

    def build_pos_payload(self, pos: dict[str, Any], include_currency: bool = False) -> dict[str, Any]:
        # Downstream endpoints only want officeId + system from the selected POS entry
        # (paired from the same pointOfSales[] entry, not mixed) - not the full object.
        payload = {"officeId": pos.get("officeId"), "system": pos.get("system")}
        if include_currency:
            payload["currency"] = pos.get("currency")
        return payload


def _pos_result(
    is_succeed: bool = False,
    point_of_sales: list | None = None,
    raw: dict | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    return {
        "is_succeed": is_succeed,
        "point_of_sales": point_of_sales or [],
        "raw": raw,
        "error": error,
    }


pos_service = PosService()
