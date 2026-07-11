# MSC Cruises — Create Reservation Scenario

Source: Postman folder `Create Reservation > Create Reservation For MSC` (full request/response samples, packageId `1324816`, apiId `MSC`, cruiseline id `982`).

## 1. Message Sequence (start to booking)

```
1. Farecode Availability     (listfarecodes)
2. Category Availability     (listcategories)
3. Cabin Availability        (listcabins)
4. List Dinings              (listdinings)
5. Hold Cabin                (holdcabin)
6. Price Reservation         (listprices)
7. Create Reservation        (create)
```

This is the standard MSC booking flow — the reservation is **final after Create**, same as RCCL/NCL. A separate Confirm Reservation step exists for MSC but is **not part of this standard flow**; see `confirm_reservation_uk_market.md`.

## 2. MSC-Specific / Extra Requirements (MVP for this scenario)

### `externalSessionInfo.externalId` must be carried from Hold Cabin into Create Reservation
- **Hold Cabin's response** returns a session-tracking value at `data.cruiseReservation.externalSessionInfo.externalId` (e.g. `"OTA3ODY-US109558-c07f5c72-f9b8-4cae-a402-38e7ee128b88a@#$SH20261101CPVCPV"`).
- This exact value must be sent back in the **Create Reservation request**, under `cruiseReservation.externalSessionInfo.externalId` (same nesting, at the reservation level — not per-category).
- Confirmed via a live sandbox capture (Ody2 request/response tool, `WTH B2B` affiliate, packageId `1428196`): the same `externalId` string appears in Hold Cabin's response and is then present in the Create Reservation request for the same booking.
- This is conceptually similar to RCCL's group-booking `externalSessionInfo` carry-forward and MVAS's three-tier carry-forward (see `RCCL/group_reservation.md`, `MVAS/standard_create_booking.md`) but **MSC's version applies to the standard flow, not just group bookings**, and only requires a single reservation-level value (not separate per-category/per-farecode values like MVAS). Whether it must also be sent on Price Reservation's request hasn't been confirmed yet from a sample — treat it as required at least for Create until verified otherwise.

### `autoInclude` add-ons must be echoed forward on every subsequent call
- Category Availability marks certain add-ons with `autoInclude: true` (e.g. `EXP2B` "Fantastica Experience Benefits", `600` "Mineral Water and Coffee in Dining Room").
- **Explicit rule from the sample comments: wherever `autoInclude` is received, it must be sent back in the subsequent Hold Cabin, Price Reservation, and Create Reservation requests**, as full objects in `cruiseReservation.addOns[]` (not just a code reference — the sample repeats the complete add-on object: code, name, prices, startDate/endDate, type, additionalCode, combinableCodes).
- This is a carry-forward requirement **unique to MSC** among the samples reviewed — RCCL/NCL add-ons are optional selections, not mandatory echoes.

### `Insurance` object (singular, not array) — optional, only if the customer wants it
```json
"Insurance": {
    "code": "CSA2CP",
    "type": 2,
    "CustomerReferences": [ { "rph": 1 } ]
}
```
- **Not mandatory.** Unlike the `autoInclude` add-ons below, insurance is opt-in — only include this block if the customer has chosen to purchase insurance for the booking. Omit it entirely otherwise.
- When included, the insurance `code` comes from **Hold Cabin's response** `insurances[]` (MSC surfaces an available insurance product at hold time, same as RCCL/NCL per the sample comment — Carnival's equivalent comes from Fare Availability instead).
- `type: 2` = supplier insurance (a fixed classification value, not something derived per request).
- If included, add it to both **Price Reservation** (to get the priced cost of the insurance) and **Create Reservation** (to actually purchase it) under `cruiseReservation.Insurance` (note PascalCase key in the sample — likely case-insensitive binding, but shown as-is from the source).

### Auto-attached "MSC GLOBAL PROTECTION" supplier item at Hold Cabin
- Hold Cabin's response includes an auto-surfaced item: `{ "type": "Supplier", "name": "MSC GLOBAL PROTECTION" }` — confirmed from the same live sandbox capture as the `externalSessionInfo` finding above (packageId `1428196`).
- This is **distinct from** the `Insurance` object above and from the `autoInclude` add-ons — it wasn't requested by the client, and the captured screenshot was cropped above this item, so **the exact parent array/field name it lives under (e.g. `addOns[]` vs. a dedicated protections/services array) is not yet confirmed** — treat that structural detail as unverified until a fuller sample is captured.
- Practical takeaway for now: don't assume MSC's only auto-surfaced supplier product is the opt-in `Insurance` block — a "GLOBAL PROTECTION" item can appear automatically in the Hold Cabin response without being requested, and a chatbot fielding "why is there a protection plan item I didn't ask for" should point here rather than to `Insurance`.

### Full dining object echoed into Create Reservation
```json
"dinings": [
    { "id": 42, "code": "CL", "name": "Classic Late Seating", "description": "N", "status": 1, "tableSizeOptions": [] }
]
```
- Unlike a simple code selection, MSC's Create Reservation sample round-trips the **entire dining object** exactly as returned by List Dinings — not just `code`.

### Rich onboard add-on catalog surfaces at Cabin Availability
- MSC's Cabin Availability response returns a large, distinct product catalog beyond what Category Availability shows: WiFi tiers (Browse / Browse & Stream, 1–4 devices), spa treatments (massages, manicure/pedicure), photo packages (including wedding packages), beverage packages (Easy/Easy Plus/Premium Extra/Alcohol-Free), and non-refundable shipboard credit denominations.
- These are optional Create-time selections, useful for a chatbot fielding "what onboard extras can I add" — but only visible after Cabin Availability, same pattern as NCL's cabin-level add-ons.

## 3. Summary

MSC's core booking flow is the same 7-call sequence as any other cruise line, finalized at Create — no mandatory extra step after it. Three things a client must get right that don't apply elsewhere in this collection: **`externalSessionInfo.externalId` must be carried from Hold Cabin's response into Create Reservation's request** at the reservation level; **`autoInclude` add-ons must be explicitly echoed forward** into every subsequent request (Hold, Price, Create) as full objects, not just referenced by code — MSC won't infer them from what was already selected; and Create Reservation needs the **full dining object**, not just a code. **Insurance, by contrast, is optional** — only include it when the customer actively wants it — and a separate auto-attached "MSC GLOBAL PROTECTION" supplier item can also appear unrequested at Hold Cabin, distinct from both.

---
*Source: Postman collection (`Create Reservation/Create Reservation For MSC/*.md`) + `CruiselineReservationController.cs` route/feature metadata + `swagger.json` schema.*
