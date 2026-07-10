# Cabin Availability

## 1. API Endpoint

| | |
|---|---|
| **Route** | `POST {{BaseUrl}}/v2/reservation/cruise/listcabins` |
| **Controller action** | `CruiseReservationController.ListCabins` |
| **Required feature flag** | `Enums.Features.ListCruiseCabins` |
| **Auth** | Basic (`Nitro.Sandbox.ClientId` / `Nitro.Sandbox.ClientSecret`) + `SiteItemId` header |
| **Request/Response object** | Compact, cruise-line-agnostic `Reservation` object (same shape used by nearly every reservation-flow endpoint) |

## 2. Use Case

Cabin Availability returns the actual bookable cabins (cabin number, deck, location, occupancy range, bed/bath configuration, obstruction/guarantee flags) for **one already-selected category + fare code combination** on a package.

**Where it sits in the flow:**

```
ListFareCodes  →  ListCategories  →  ListCabins  →  ... →  HoldCabin  →  ListPrices  →  Create
```

A client calls this endpoint **after** narrowing down to a specific category and fare code (from Category Availability), when they need to let the traveler pick a physical cabin rather than accept a guaranteed/auto-assigned category. Support for this message can vary by cruise line — some suppliers only return guarantee-level availability and no cabin-level picks, per the controller's XML remarks ([CruiseReservationController.cs:238](../../../../Projects/NitroAPI/src/NitroAPI/Controllers/V2/Reservation/CruiseReservationController.cs)).

## 3. Request / Response Details

### Request — minimum required elements

```json
{
    "cruiseReservation": {
        "pos": { "officeId": "O100US6797", "system": "Test" },
        "cruise": {
            "packageId": 1310045,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "XBO",
                "fare": {
                    "fareCode": {
                        "code": "BESTPRICE"
                    }
                }
            }
        ]
    },
    "customers": [
        { "rph": 1, "age": 52, "address": { "country": { "id": "US" } } },
        { "rph": 2, "age": 57 }
    ],
    "trackingInfo": { "token": "EQTEMPKEN" }
}
```

| Field | Type | Notes |
|---|---|---|
| `cruiseReservation.cruise.packageId` | int | Required. Identifies the sailing/package. |
| `cruiseReservation.cruise.packageTourId` | int | Use `-1` when not applicable. |
| `cruiseReservation.pos.officeId` / `.system` | string | **Required when the client has more than one office/profile configured for this cruise line.** Both come from the same **API Credential List (POS)** (`listpos`) response entry → `pointOfSales[].officeId` / `.system` — don't mix `officeId` from one entry with `system` from another. |
| `cruiseReservation.categories[].code` | string | **Not generated here** — must come from a prior Category Availability call. |
| `cruiseReservation.categories[].fare.fareCode.code` | string | **Not generated here** — must come from a prior Farecode Availability (or Category Availability) call. |
| `customers[].rph` | int | Reference number per passenger, echoed back in the response. |
| `customers[].age` | int | Drives age-based cabin/occupancy eligibility. |
| `customers[].address.country.id` | string | ISO country code; affects residency-based rules for some cruise lines. |

### Response — key fields returned

```json
{
  "isSucceed": true,
  "data": {
    "cruiseReservation": {
      "cabins": [
        {
          "number": "6018",
          "location": "Port",
          "occupancy": { "min": 0, "max": 3 }
        }
      ]
    }
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `data.cruiseReservation.cabins[].number` | string | The bookable cabin number — the key identifier passed into Hold Cabin next. |
| `data.cruiseReservation.cabins[].location` | string? | e.g. `Port`, `Starboard`, `Forward`, `Aft` — support varies by cruise line. |
| `data.cruiseReservation.cabins[].occupancy.min` / `.max` | int? | Min/max guests the cabin can hold. |
| `data.cruiseReservation.cabins[].deck` | object/string | Deck the cabin is on — shape varies by cruise line (some return a code, some a full `Deck` object with `id`/`code`/`name`/`description`). |
| `data.cruiseReservation.cabins[].category` | object | `CabinCategory` — `code` + `upgradeFrom`, present only if the supplier reports a category shift for that cabin. |
| `data.cruiseReservation.cabins[].smokingInfo` | object | `allowed` (bool), `description`. |
| `data.cruiseReservation.cabins[].obstruction` | object | `isObstructed` (bool), `percent` (int) — see Obstructed Cabin Indicator scenario. |
| `data.cruiseReservation.cabins[].beds[]` / `.bathOptions[]` | array | Configuration options, present only for cruise lines that expose bed/bath selection at this stage. |
| `data.cruiseReservation.cabins[].isGuarantee` | bool | True when the "cabin" is actually a guarantee placeholder, not an assigned physical cabin. |

## 4. Property Cross-Reference — where does each field actually come from?

This is the part that matters most for a chatbot answering "why don't I see prices/fare details in the cabin list?" — **Cabin Availability does not repeat data you already fetched upstream.** It assumes the category and fare code were already chosen.

| Property client needs | Endpoint that actually returns it | Notes |
|---|---|---|
| `categories[].code` (which category to query cabins for) | **Category Availability** (`listcategories`) → `data.cruiseReservation.categories[].code` | Cabin Availability's request just echoes this code back in; it does not enumerate categories itself. |
| `categories[].fare.fareCode.code` | **Farecode Availability** (`listfarecodes`) → `data.cruiseReservation.fareCodes[].code`, or already present per-category in **Category Availability**'s `categories[].fares[].fareCode.code` | Either source works — Category Availability already nests the fare code under each category, so a client who called that endpoint doesn't need a separate Farecode Availability call. |
| Category pricing / fare rules / fare `details` | **Category Availability** only | Cabin Availability's response `cabins[]` carries no `prices`, `fares`, or `details` block at all — pricing is deliberately not repeated here. Use Price Reservation (`listprices`) for authoritative, bookable pricing later in the flow. |
| Cabin number, deck, location, occupancy, obstruction, guarantee flag | **Cabin Availability only** | This is the one endpoint in the flow that returns physical-cabin-level detail. Neither Category Availability nor Price Reservation return cabin numbers. |
| Full fare code metadata (refundable type, groups, dynamic rules, combinable fares) | **Farecode Availability** (`listfarecodes`) or **Farecode Details** (`getfarecodedetails`) | Cabin Availability's request only needs the fare *code string* — it doesn't need or return the fare code's full metadata. |
| `pos.officeId` / `pos.system` | **API Credential List (POS)** (`listpos`) → `pointOfSales[].officeId` / `.system` | Only needed when the client has multiple POS/profiles set up for this cruise line — see `office_credentials_list_pos.md`. Most single-profile clients can omit both. |

**Practical rule for the chatbot:** if a client asks for cabin-level detail (number/deck/location/occupancy), point to Cabin Availability. If they ask about price or fare rules, point to Category Availability / Price Reservation — Cabin Availability will not have that data even though it accepts a `fare` object in its request.

---
*Source: `CruiseReservationController.cs` (route/feature/XML remarks) + `swagger.json` (request/response schema) + Postman collection sample (`Cabin Availability/Location/*.md`).*
