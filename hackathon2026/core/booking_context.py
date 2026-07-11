from typing import Any

from pydantic import BaseModel, Field


class BookingContext(BaseModel):
    # One entry per executed step (pos/category/cabin/cabin_hold/price/tokenize_card/
    # create_reservation), in order, whether it succeeded, failed, or needs more input.
    steps: list[dict[str, Any]] = Field(default_factory=list)
    package_id: int | None = None
    cruiseline_id: int | None = None
    pos_result: dict[str, Any] | None = None
    pos_selected: dict[str, Any] | None = None
    farecode_result: dict[str, Any] | None = None
    category_code: str | None = None
    category_result: dict[str, Any] | None = None
    farecode: str | None = None
    auto_include_addons: list[dict[str, Any]] = Field(default_factory=list)
    cabin_number: str | None = None
    cabin_result: dict[str, Any] | None = None
    dining_result: dict[str, Any] | None = None
    selected_dining: dict[str, Any] | None = None
    hold_result: dict[str, Any] | None = None
    external_session_id: str | None = None
    price_result: dict[str, Any] | None = None
    token: str | None = None
    tokenize_result: dict[str, Any] | None = None
    confirmation_number: str | None = None
    create_result: dict[str, Any] | None = None
