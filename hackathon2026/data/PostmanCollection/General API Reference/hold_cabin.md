# Hold Cabin (Temporary)

## 1. API Endpoint

| | |
|---|---|
| **Route** | `POST {{BaseUrl}}/v2/reservation/cruise/holdcabin` |
| **Controller action** | `CruiseReservationController.HoldCabin` |
| **Required feature flag** | `Enums.Features.HoldCabin` |
| **Auth** | Basic (`Nitro.Sandbox.ClientId` / `Nitro.Sandbox.ClientSecret`) + `SiteItemId` header |
| **Request/Response object** | Compact, cruise-line-agnostic `Reservation` object |

## 2. Use Case

Places a **temporary hold** with the cruise line on a specific category + fare code + cabin combination, reserving it while the traveler completes the booking flow (entering passenger details, add-ons, payment). Hold duration varies by cruise line and is not returned in this response — the client must track it separately per the cruise profile matrix.

**Where it sits in the flow:**

```
ListCategories  →  ListCabins  →  HoldCabin  →  ListPrices  →  Create  →  ReleaseCabin (only if abandoning)
```

Per the controller's XML remarks: this message can also include insurance or other key details useful in the reservation flow.

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
                "cabins": [ { "number": "9998" } ]
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
| `cruiseReservation.cruise.packageId` / `.packageTourId` | int | Required. |
| `cruiseReservation.pos.officeId` / `.system` | string | **Required when the client has more than one office/profile configured for this cruise line.** Both come from the same **API Credential List (POS)** (`listpos`) response entry → `pointOfSales[].officeId` / `.system` — don't mix `officeId` from one entry with `system` from another. |
| `cruiseReservation.categories[].code` | string | **Not generated here** — from Category Availability. |
| `cruiseReservation.categories[].fare.fareCode.code` | string | **Not generated here** — from Category Availability or Farecode Availability. |
| `cruiseReservation.categories[].cabins[].number` | string | **Not generated here** — from Cabin Availability. This is the specific cabin being held. If the category is guarantee-only, this may be omitted and the supplier auto-assigns later. |

### Response — key fields returned

```json
{
  "data": {
    "cruiseReservation": {
      "insurances": [ { "code": "CRCR" } ],
      "cruise": { "packageId": 1269434 }
    }
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `data.cruiseReservation.insurances[]` | array | `Insurance` objects — some cruise lines auto-attach a mandatory or default insurance product the moment a hold is placed; check `code`/`name`/`amount`. |
| *(no `categories` or `cabins` echoed back)* | — | The sample response for Hold Cabin does not re-echo the held category/cabin/fare code — the request is your confirmation of what was held. If your integration needs to confirm hold state, use **Read Reservation From Supplier** with `readPreferences.mode: "Modify"` afterward. |

## 4. Property Cross-Reference

| Property client needs | Endpoint that actually returns it | Notes |
|---|---|---|
| `categories[].code` | **Category Availability** | See `category_availability.md`. |
| `categories[].fare.fareCode.code` | **Farecode Availability** or **Category Availability** | Either source works. |
| `categories[].cabins[].number` | **Cabin Availability** (`listcabins`) | The specific cabin number to hold. |
| Confirmation that the hold succeeded / what's actually on hold | **This endpoint's `isSucceed`/`advisories`**, or a follow-up **Read Reservation From Supplier** call | Hold Cabin's success response doesn't repeat back the held cabin/category — don't expect to parse cabin details from this response. |
| Auto-attached insurance on hold | **Hold Cabin only** (surfaces here first) | Some cruise lines populate `insurances[]` automatically at hold time, before the client ever calls a dedicated insurance/special-service endpoint. |
| Releasing this same hold | **Release Cabin** (`releasecabin`) | See `release_cabin.md` — takes the identical `categories[].cabins[].number` selector. |
| `pos.officeId` / `pos.system` | **API Credential List (POS)** (`listpos`) → `pointOfSales[].officeId` / `.system` | Only needed when the client has multiple POS/profiles set up for this cruise line — see `office_credentials_list_pos.md`. Most single-profile clients can omit both. |

**Practical rule for the chatbot:** Hold Cabin is a write/mutation call, not a lookup — its response confirms success/failure and any side-effect data (like auto-insurance), not a restatement of what was requested.

---
*Source: `CruiseReservationController.cs` (route/feature/XML remarks) + `swagger.json` (request/response schema) + Postman collection sample (`Hold Cabin/hold_cabin.md`).*
