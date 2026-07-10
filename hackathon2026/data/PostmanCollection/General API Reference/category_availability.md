# Category Availability

## 1. API Endpoint

| | |
|---|---|
| **Route** | `POST {{BaseUrl}}/v2/reservation/cruise/listcategories` |
| **Controller action** | `CruiseReservationController.ListCategories` |
| **Required feature flag** | `Enums.Features.ListCruiseCategories` |
| **Auth** | Basic (`Nitro.Sandbox.ClientId` / `Nitro.Sandbox.ClientSecret`) + `SiteItemId` header |
| **Request/Response object** | Compact, cruise-line-agnostic `Reservation` object |

## 2. Use Case

Returns every stateroom category (Inside, Oceanview, Balcony, Suite, etc.) for a package, with a price per fare code that applies to it. This is normally the **primary shopping call** most B2C flows make right after search — it doesn't require Farecode Availability first, and it doesn't require Cabin Availability after unless the client wants to let travelers pick a specific cabin number.

**Where it sits in the flow:**

```
ListFareCodes (optional, B2B)  →  ListCategories  →  ListCabins (optional)  →  HoldCabin  →  ListPrices  →  Create
```

Per the controller's XML remarks: returns categories and a list of prices per category; the response can include unavailable categories/prices that the client must track and filter; also includes any applicable/selected rules. For offline group/offline reservation flows, response is based on prices defined within Odysseus rather than a live supplier call.

## 3. Request / Response Details

### Request — minimum required elements

```json
{
    "cruiseReservation": {
        "pos": { "currency": "USD", "officeId": "O100US6797", "system": "Test" },
        "cruise": { "packageId": 1310045 },
        "fareCodes": [ { "code": "BESTPRICE" } ]
    },
    "customers": [
        { "rph": 1, "age": 52, "address": { "country": { "id": "US" }, "state": { "id": "FL" } } },
        { "rph": 2, "age": 57 }
    ],
    "trackingInfo": { "token": "EQTEMPKEN" }
}
```

| Field | Type | Notes |
|---|---|---|
| `cruiseReservation.cruise.packageId` | int | Required. |
| `cruiseReservation.pos.officeId` | string | **Required when the client has more than one office/profile configured for this cruise line.** Comes from **API Credential List (POS)** (`listpos`) response → `pointOfSales[].officeId`. |
| `cruiseReservation.pos.system` | string | Same source as `officeId` — **API Credential List (POS)** response → `pointOfSales[].system` (e.g. `"Test"` vs. a production system identifier). Must be paired with the matching `officeId` from the same `pointOfSales[]` entry, not mixed across entries. |
| `cruiseReservation.fareCodes[].code` | string | **Optional filter.** If omitted, the response returns categories priced across *all* eligible fare codes; if supplied, narrows pricing to that fare code only. Comes from Farecode Availability (or is skipped entirely — this endpoint doesn't strictly require it first). |
| `customers[].age` / `.address` | int / object | Drives age/residency-based pricing eligibility, same as Farecode Availability. |

### Response — key fields returned

```json
{
  "data": {
    "cruiseReservation": {
      "categories": [
        {
          "code": "2B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": { "code": "I1071484_GRP", "type": 0, "refundableType": 1 },
              "prices": [
                { "id": 1, "amount": 539, "type": "AVGPP", "details": { "nccfInclusive": true } },
                { "id": 3, "amount": 115, "type": "AVGPP" },
                { "id": 2, "amount": 110, "type": "AVGPP" }
              ],
              "addOns": []
            }
          ],
          "details": { "cabinCount": 10, "guarantee": false }
        }
      ]
    }
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `data.cruiseReservation.categories[].code` | string | **Category code** — the key identifier a client passes into Cabin Availability, Hold Cabin, Price Reservation, and Create. |
| `.type` | int | Category class (supplier-defined; e.g. Inside/Oceanview/Balcony/Suite tiering). |
| `.fares[].fareCode.code` | string | Fare code applicable to this category — same value space as Farecode Availability's `fareCodes[].code`. |
| `.fares[].fareCode.type` / `.refundableType` | int | Trimmed fare metadata; full metadata lives in Farecode Availability/Details. |
| `.fares[].prices[]` | array | `Price` objects: `id` (price component code), `amount`, `type` (e.g. `AVGPP` = average per person), `details.nccfInclusive`/`.taxInclusive`/etc. |
| `.fares[].addOns[]` | array | Populated only when the cruise line auto-attaches add-ons to a fare at the category level. |
| `.details.cabinCount` | int | How many cabins are available in this category — a count, not the cabin list itself. |
| `.details.guarantee` | bool? | Whether this category is guarantee-only (no cabin number until assigned by the cruise line). |
| `.location` | object | `CategoryLocation` — present for cruise lines that expose location-based category variants (see "Location" Postman scenario). |

## 4. Property Cross-Reference

| Property client needs | Endpoint that actually returns it | Notes |
|---|---|---|
| `categories[].code` (to pass downstream) | **Category Availability only** | Neither Farecode Availability nor Cabin Availability enumerate categories. |
| `categories[].fares[].fareCode.code` | **Category Availability** (nested) or **Farecode Availability** (standalone list) | Either source is valid; Category Availability already nests it, so a client who calls this endpoint does not need Farecode Availability separately. |
| Category/fare **pricing** (`prices[]`, `nccfInclusive`, etc.) | **Category Availability only** in the shopping phase | Cabin Availability's response does not repeat pricing at all. Price Reservation (`listprices`) later returns the authoritative, bookable price breakdown — use that, not this endpoint's prices, for final checkout amounts. |
| Cabin count for a category | **Category Availability** → `details.cabinCount` | This is a *count* only. For the actual cabin numbers/decks/locations, call **Cabin Availability**. |
| Individual cabin numbers, decks, obstruction, occupancy | **Cabin Availability** (`listcabins`), not here | See `cabin_availability.md`. |
| Full fare code metadata (groups, dynamic rules, combinable fares) | **Farecode Availability** or **Farecode Details** | Category Availability's nested `fareCode` object is trimmed. |
| `pos.officeId` / `pos.system` | **API Credential List (POS)** (`listpos`) → `pointOfSales[].officeId` / `.system` | Only needed when the client has multiple POS/profiles set up for this cruise line — see `office_credentials_list_pos.md`. Most clients with a single profile can omit both and let Odysseus resolve the POS automatically. |

**Practical rule for the chatbot:** if a client asks "what categories/prices are available," point here. If they ask "which specific cabins are in this category," point to Cabin Availability — this endpoint only gives a `cabinCount`, never cabin numbers.

---
*Source: `CruiseReservationController.cs` (route/feature/XML remarks) + `swagger.json` (request/response schema) + Postman collection sample (`Category Availability/category_availability.md`).*
