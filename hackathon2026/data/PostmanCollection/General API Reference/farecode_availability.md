# Farecode Availability

## 1. API Endpoint

| | |
|---|---|
| **Route** | `POST {{BaseUrl}}/v2/reservation/cruise/listfarecodes` |
| **Controller action** | `CruiseReservationController.ListFareCodes` |
| **Required feature flag** | `Enums.Features.ListFareCodes` |
| **Auth** | Basic (`Nitro.Sandbox.ClientId` / `Nitro.Sandbox.ClientSecret`) + `SiteItemId` header |
| **Request/Response object** | Compact, cruise-line-agnostic `Reservation` object |

## 2. Use Case

Returns the live fare codes the cruise line has for a package/sailing — the first decision point in the booking flow, before category or cabin selection.

**Where it sits in the flow:**

```
ListFareCodes  →  ListCategories  →  ListCabins  →  HoldCabin  →  ListPrices  →  Create
```

Per the controller's XML remarks: this message returns fare codes as returned live by the cruise line, including any group fare codes. The list can vary by search (passenger count, residency, etc.). **It is primarily for B2B users** who want to manually present a fare code list to the traveler. B2C/direct flows can skip this call and go straight to Category Availability — Odysseus will auto-select the fare code per setup. For offline group/offline reservation flows, the response only includes fare codes that have prices on file.

## 3. Request / Response Details

### Request — minimum required elements

```json
{
    "cruiseReservation": {
        "pos": { "currency": "USD", "officeId": "O100US6797", "system": "Test" },
        "customerReferences": [
            { "rph": 1, "isPrimaryContact": true },
            { "rph": 2 }
        ],
        "cruise": { "packageId": 1310045 }
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
| `cruiseReservation.pos.currency` | string | Currency the fare prices should be quoted in. |
| `cruiseReservation.pos.officeId` / `.system` | string | **Required when the client has more than one office/profile configured for this cruise line.** Both come from the same **API Credential List (POS)** (`listpos`) response entry → `pointOfSales[].officeId` / `.system` — don't mix `officeId` from one entry with `system` from another. |
| `cruiseReservation.customerReferences[].rph` / `.isPrimaryContact` | int / bool | Maps each traveler to a passenger reference number, echoed through the whole flow. |
| `customers[].age` | int | Drives age-based fare eligibility (senior, military, resident fares, etc.). |
| `customers[].address.country.id` | string | ISO country code — drives residency-restricted fares. |

### Response — key fields returned

```json
{
  "data": {
    "cruiseReservation": {
      "fareCodes": [
        {
          "code": "BESTRATE_GRP",
          "name": "Best Rate_GRP",
          "description": "Best fare",
          "bookOnline": true,
          "isEligible": true,
          "refundableType": 1,
          "status": 1,
          "details": { "agencyDescription": "", "remarks": "Best fare" },
          "groups": [ { "code": "1179594", "name": "TLN ADD USD", "type": 2, "subType": 2 } ],
          "dynamicRules": [ { "type": 10 } ],
          "combinableFares": [ { "code": "I7996069", "type": 0, "refundableType": 2 } ]
        }
      ]
    }
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `data.cruiseReservation.fareCodes[].code` | string | **The identifier a client feeds into every downstream call** (Category, Cabin, Price, Create). |
| `.name` / `.description` | string? | Human-readable fare name and short description. |
| `.bookOnline` | bool | Whether this fare can be booked online vs. requires manual handling. |
| `.isEligible` | bool | Whether the current search context (age/residency/POS) qualifies for this fare. |
| `.refundableType` | int | Refundability classification (supplier-defined code). |
| `.specialFare` | int? | Present for promotional/group fares. |
| `.details.agencyDescription` / `.remarks` / `.fareTypeDescription` / `.qualifierCodes` | string? | Extra descriptive text — support and population vary by cruise line. |
| `.groups[]` | array | Fare grouping info (e.g. group booking codes) — populated for group/negotiated fares, empty `{}` for standard published fares. |
| `.dynamicRules[]` | array | Present only for fares subject to dynamic pricing rules. |
| `.combinableFares[]` | array | Other fare codes that can be combined with this one (e.g. BOGO/NRD pairs) — cruise-line-specific. |

## 4. Property Cross-Reference

| Property client needs | Endpoint that actually returns it | Notes |
|---|---|---|
| `fareCodes[].code` (to pass into Category/Cabin/Create) | **Farecode Availability only** | This is the canonical source. |
| Full fare code metadata (`combinableFares`, `groups`, `dynamicRules`, `isPrivate`) | **Farecode Availability** or **Farecode Details** (`getfarecodedetails`) | Farecode Details gives supplier-specific fare inclusions/exclusions text; support varies by cruise line. |
| Fare code **re-echoed per category with pricing** | **Category Availability** (`listcategories`) → `categories[].fares[].fareCode` | Category Availability nests a *trimmed* fare code (code/type/refundableType) alongside per-category prices — a client who calls Category Availability directly does not need a separate Farecode Availability call. |
| Category-level pricing | **Category Availability**, not here | Farecode Availability returns fare codes only; no category/price breakdown. |
| Cabin-level detail | **Cabin Availability** (`listcabins`), not here | Fare codes alone don't identify a physical cabin. |
| `pos.officeId` / `pos.system` | **API Credential List (POS)** (`listpos`) → `pointOfSales[].officeId` / `.system` | Only needed when the client has multiple POS/profiles set up for this cruise line — see `office_credentials_list_pos.md`. Most single-profile clients can omit both. |

**Practical rule for the chatbot:** if a client asks "what fares/rates are available for this sailing," point here (or skip straight to Category Availability for B2C flows, since it nests the same fare code data alongside pricing).

---
*Source: `CruiseReservationController.cs` (route/feature/XML remarks) + `swagger.json` (request/response schema) + Postman collection sample (`Farecode Availability/farecode_availability.md`).*
