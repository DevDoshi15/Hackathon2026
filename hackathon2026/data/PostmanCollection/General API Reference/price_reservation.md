# Price Reservation

## 1. API Endpoint

| | |
|---|---|
| **Route** | `POST {{BaseUrl}}/v2/reservation/cruise/listprices` |
| **Controller action** | `CruiseReservationController.ListPrices` |
| **Required feature flag** | `Enums.Features.ListCruisePrices` |
| **Auth** | Basic (`Nitro.Sandbox.ClientId` / `Nitro.Sandbox.ClientSecret`) + `SiteItemId` header |
| **Request/Response object** | Compact, cruise-line-agnostic `Reservation` object |

## 2. Use Case

Prices the reservation with the supplier and returns the authoritative price and **payment schedule** breakdown — the numbers a client should actually charge/display at checkout, as opposed to the indicative pricing shown in Category Availability.

**Where it sits in the flow:**

```
HoldCabin  →  ListPrices  →  Create
```

Per the controller's XML remarks: `rph: -1` in the price array is the **total for the reservation**; per-customer prices use the `rph` sent in `customerReferences`. This message can be called repeatedly through the flow as the traveler adds/removes insurance, special services, add-ons, etc. — always re-price after changing selections, don't assume Category Availability's indicative price still holds.

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
        "cruise": { "packageId": 1269434, "packageTourId": -1 },
        "categories": [
            { "code": "2B", "fare": { "fareCode": { "code": "G0737880" } } }
        ]
    },
    "customers": [
        { "rph": 1, "firstName": "John", "lastName": "Doe", "dateOfBirth": "02-Jan-1970", "age": 52, "address": { "country": { "id": "US" } } },
        { "rph": 2, "firstName": "Maria", "lastName": "Doe", "dateOfBirth": "01-Jan-1965", "age": 57, "address": { "country": { "id": "US" } } }
    ],
    "trackingInfo": { "token": "EQTEMPKEN" }
}
```

Note: no `cabins[]` selector required here — pricing is done at the category+fare level, cabin selection is independent (via Hold Cabin).

| Field | Type | Notes |
|---|---|---|
| `cruiseReservation.pos.officeId` / `.system` | string | **Required when the client has more than one office/profile configured for this cruise line.** Both come from the same **API Credential List (POS)** (`listpos`) response entry → `pointOfSales[].officeId` / `.system` — don't mix `officeId` from one entry with `system` from another. |

### Response — key fields returned

```json
{
  "data": {
    "cruiseReservation": {
      "paymentSchedules": {
        "customerPaymentSchedules": [ { "type": 2, "amount": 1424.5, "dueDate": "06-Feb-2023" } ],
        "affiliatePaymentSchedules": [ { "type": 2, "amount": 1424.5, "dueDate": "06-Feb-2023" } ],
        "supplierPaymentSchedules": [ { "type": 2, "amount": 1257.46, "dueDate": "08-Feb-2023" } ]
      },
      "prices": [
        { "id": 1, "code": "49", "amount": 1816, "rph": -1 },
        { "id": 3, "code": "18", "amount": 226.5, "details": { "isTax": true }, "rph": -1 },
        { "id": 1, "code": "49", "amount": 941, "rph": 1 },
        { "id": 1, "code": "49", "amount": 875, "rph": 2 }
      ]
    }
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `data.cruiseReservation.paymentSchedules.customerPaymentSchedules[]` | array | What the **traveler** owes and when — `type`, `amount`, `dueDate`. Use this to build a payment plan UI. |
| `.affiliatePaymentSchedules[]` | array | What the **agency/affiliate** owes — may differ from customer schedule depending on commission/markup structure. |
| `.supplierPaymentSchedules[]` | array | What Odysseus/the agency owes the **cruise line** — net of commission. |
| `data.cruiseReservation.prices[]` | array (flat, not nested per category) | Every price component (base fare, taxes, fees, discounts, commission) as a flat list, disambiguated by `rph`. |
| `.prices[].rph` | int | **`-1` = reservation total.** A positive number = that specific passenger's share (matches `customerReferences[].rph`). |
| `.prices[].code` | string | Price component code (supplier-defined — e.g. `"18"` = tax in this sample, `"49"`/`"60"` = base components). Meaning of codes is cruise-line-specific; don't hardcode interpretations across cruise lines. |
| `.prices[].details.isTax` / `.isCommission` | bool? | Flags what kind of line item this is. |
| `.prices[].display` | bool? | Whether this line item is meant to be shown to the customer, or is an internal-only component. |

## 4. Property Cross-Reference

| Property client needs | Endpoint that actually returns it | Notes |
|---|---|---|
| Indicative per-category price (rough estimate for shopping) | **Category Availability** | Used for comparing categories before committing. |
| **Authoritative** price + payment schedule (what to actually charge) | **Price Reservation only** | This is the one endpoint that returns `paymentSchedules` at all — no other endpoint in the flow does. |
| Per-passenger price breakdown | **Price Reservation** → `prices[]` filtered by `rph` | Category Availability's prices are per-category, not per-passenger; Price Reservation is the first point per-passenger amounts appear. |
| Tax/commission line items | **Price Reservation** → `prices[].details.isTax` / `.isCommission` | Not broken out this granularly anywhere upstream. |
| Category code / fare code inputs | **Category Availability** / **Farecode Availability** | Same as every other flow step — not generated here. |
| Cabin number | **Not needed for this call** | Price Reservation prices at the category+fare level; cabin selection is independent. |
| `pos.officeId` / `pos.system` | **API Credential List (POS)** (`listpos`) → `pointOfSales[].officeId` / `.system` | Only needed when the client has multiple POS/profiles set up for this cruise line — see `office_credentials_list_pos.md`. Most single-profile clients can omit both. |

**Practical rule for the chatbot:** if a client asks "how much will this cost" or "what's the payment schedule," always point to Price Reservation, never Category Availability — the category-level price is indicative only and can drift (rules, currency, timing).

---
*Source: `CruiseReservationController.cs` (route/feature/XML remarks) + `swagger.json` (request/response schema) + Postman collection sample (`Price Reservation/price_reservation.md`).*
