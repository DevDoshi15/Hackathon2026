# Dining Availability

## 1. API Endpoint

| | |
|---|---|
| **Route** | `POST {{BaseUrl}}/v2/reservation/cruise/listdinings` |
| **Controller action** | `CruiseReservationController.ListDining` |
| **Required feature flag** | `Enums.Features.ListDinings` |
| **Auth** | Basic (`Nitro.Sandbox.ClientId` / `Nitro.Sandbox.ClientSecret`) + `SiteItemId` header |
| **Request/Response object** | Compact, cruise-line-agnostic `Reservation` object |

## 2. Use Case

Returns the available dining seating options (e.g. early/late seating, "my time dining") for a specific category and cabin, so the traveler can pick a preference before or during booking.

**Where it sits in the flow:**

```
ListCabins  →  ListDinings (optional)  →  HoldCabin  →  ListPrices  →  Create
```

Per the controller's XML remarks: **support for this message can vary by cruise line** — some cruise lines don't expose dining as a separate call at all.

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
      {
        "code": "2B",
        "fare": { "fareCode": { "code": "G0737880" } },
        "cabins": [ { "number": "9330" } ]
      }
    ]
  },
  "customers": [
    { "rph": 1, "age": 52 },
    { "rph": 2, "age": 57 }
  ],
  "trackingInfo": { "token": "EQTEMPKEN" }
}
```

| Field | Type | Notes |
|---|---|---|
| `cruiseReservation.cruise.packageId` | int | Required. |
| `cruiseReservation.pos.officeId` / `.system` | string | **Required when the client has more than one office/profile configured for this cruise line.** Both come from the same **API Credential List (POS)** (`listpos`) response entry → `pointOfSales[].officeId` / `.system` — don't mix `officeId` from one entry with `system` from another. |
| `cruiseReservation.categories[].code` / `.fare.fareCode.code` / `.cabins[].number` | string | **All from upstream calls.** Dining options can vary by which category/cabin is selected (e.g. suite-only dining venues), so all three selectors are needed even though this is still a shopping-phase call, before Hold Cabin. |

### Response — key fields returned

```json
{
  "data": {
    "cruiseReservation": {
      "dinings": [
        { "id": 1, "code": "M", "name": "05:15 PM", "status": 1, "tableSizeOptions": [] },
        { "id": 2, "code": "2", "name": "08:00 PM", "status": 1, "tableSizeOptions": [] },
        { "id": 24, "code": "O", "name": "MY TIME", "status": 1, "tableSizeOptions": [] }
      ]
    }
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `data.cruiseReservation.dinings[].code` | string | The identifier a client passes into Create Reservation's dining selection. |
| `.name` | string | Human-readable seating time/type, e.g. `"05:15 PM"`, `"MY TIME"`. |
| `.status` | int | **`1` = available (shopping-time)** in this sample. Note: the same field returns a different value (e.g. `7`) once a dining is actually confirmed on a booking — see Read Reservation From Supplier. |
| `.tableSizeOptions[]` | array | Table size choices, empty in this sandbox response — populated for cruise lines that support table-size selection. |
| `.gratuityRequired` | bool | Whether this dining option carries mandatory gratuity — schema-only field, not populated in this sample. |
| `.diningRoom` | object | `DiningRoom` — `type`, `name`, `maxCapacity` — populated for cruise lines that expose specific dining room assignment. |
| `.seatings[]` | array | `DiningSeating` — `startTime`, `endTime`, `mealType` — a more granular seating breakdown than the flat `name` field, cruise-line-dependent. |
| `.smokingInfo` | object | Rare for dining; inherited from the shared schema shape used across cabin/dining objects. |

## 4. Property Cross-Reference

| Property client needs | Endpoint that actually returns it | Notes |
|---|---|---|
| `categories[].code`, `.fare.fareCode.code`, `.cabins[].number` (inputs) | **Category/Farecode/Cabin Availability** | Same upstream dependency chain as every other post-cabin-selection call. |
| Dining option codes/names (shopping) | **Dining Availability only** | Category Availability and Cabin Availability never surface dining data. |
| Confirmed dining assignment after booking | **Read Reservation From Supplier** (`dinings[].status` = confirmed code, not `1`) | Same nested field name and shape, different semantic — don't assume `status: 1` always means "available"; check context (pre- vs. post-booking). |
| `pos.officeId` / `pos.system` | **API Credential List (POS)** (`listpos`) → `pointOfSales[].officeId` / `.system` | Only needed when the client has multiple POS/profiles set up for this cruise line — see `office_credentials_list_pos.md`. Most single-profile clients can omit both. |

**Practical rule for the chatbot:** dining status codes are context-dependent — `1` typically means "available to select" in the shopping response; a different status appears once dining is actually confirmed on a created reservation. Flag this ambiguity rather than hardcoding a universal status-code meaning.

---
*Source: `CruiseReservationController.cs` (route/feature/XML remarks) + `swagger.json` (request/response schema) + Postman collection sample (`Dining Availability/dining_availability.md`).*
