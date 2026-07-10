# Create Reservation

## 1. API Endpoint

| | |
|---|---|
| **Route** | `POST {{BaseUrl}}/v2/reservation/cruise/create` |
| **Controller action** | `CruiseReservationController.Create` |
| **Required feature flag** | `Enums.Features.CreateBooking` |
| **Auth** | Basic (`Nitro.Sandbox.ClientId` / `Nitro.Sandbox.ClientSecret`) + `SiteItemId` header |
| **Request/Response object** | Compact, cruise-line-agnostic `Reservation` object |

## 2. Use Case

Commits the booking with the cruise line and returns a confirmation number. This is the culmination of the shopping flow — everything before it (Category/Cabin/Dining/Special Services/Pricing) is discovery; this is the write that actually creates the reservation.

**Where it sits in the flow:**

```
HoldCabin  →  ListPrices  →  [TokenizeCard, if paying now]  →  Create  →  Confirm/PayToSupplier/RecordPayment
```

Per the controller's XML remarks: to create with payment, call **TokenizeCard** first to get a token for the card details, pass it in `paymentToProcess.cardToken`, and set the amount in `paymentToProcess.amount`. Without a `paymentToProcess` block, the reservation is created **without payment** (see "Create Reservation (Without Payment)" scenario).

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
        "cruise": { "packageId": 1351658 },
        "categories": [
            {
                "code": "IB",
                "fare": { "fareCode": { "code": "DISXIN" } },
                "cabins": [ { "number": "8177" } ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1, "firstName": "John", "lastName": "Doe", "dateOfBirth": "02-Jan-1970",
            "ContactInfo": { "Email": "john@domain.com", "Phone1": { "CountryCode": "1", "Number": "416-555-4566" } },
            "address": { "country": { "id": "US" }, "state": { "id": "IL" }, "city": { "name": "Chicago" } }
        },
        {
            "rph": 2, "firstName": "Maria", "lastName": "Doe", "dateOfBirth": "01-Jan-1965",
            "ContactInfo": { "Email": "maria@domain.com", "Phone1": { "CountryCode": "1", "Number": "416-555-4566" } }
        }
    ],
    "trackingInfo": { "token": "EQTEMPKEN" }
}
```

| Field | Type | Notes |
|---|---|---|
| `cruiseReservation.cruise.packageId` | int | Required. |
| `cruiseReservation.pos.officeId` / `.system` | string | **Required when the client has more than one office/profile configured for this cruise line.** Both come from the same **API Credential List (POS)** (`listpos`) response entry → `pointOfSales[].officeId` / `.system` — should match what was used throughout the shopping flow for this reservation. |
| `cruiseReservation.categories[].code` / `.fare.fareCode.code` / `.cabins[].number` | string | **All from prior discovery calls** (Category/Farecode/Cabin Availability) — this is where they finally get committed. |
| `customers[].firstName` / `.lastName` / `.dateOfBirth` | string | **Required for Create** even though optional/absent in upstream discovery calls — passenger identity is mandatory to actually book. |
| `customers[].ContactInfo.Email` / `.Phone1` | object | At least the primary/booking contact typically needs contact info — cruise-line-dependent. |
| `customers[].address` | object | Full address typically needed for the primary contact; secondary passengers can often omit it (see `rph: 2` in the sample). |
| `paymentToProcess.cardToken` / `.amount` | string / number | **Not shown in this "without payment" sample** — add this block only when paying at booking time (get the token from TokenizeCard first). |

### Response — key fields returned

```json
{
  "isSucceed": true,
  "advisories": [ { "code": "1001089", "message": "Cabin Designed For WheelChairs...", "type": "Warning" } ],
  "data": {
    "id": 75755,
    "agencyConfirmation": "ESSSCDT",
    "cruiseReservation": {
      "id": 123732,
      "status": 6,
      "reservationReferences": { "confirmationNumber": "53095316" },
      "rulesInfo": { "applicableRules": [ /* promos/discounts applied */ ] },
      "categories": [ { "id": 53666, "code": "IB", "fares": [ { "fareCode": { "code": "DISXIN" } } ] } ]
    }
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `data.id` | int | Odysseus-internal reservation ID — use this for Read/Modify/Cancel/Search calls against Odysseus. |
| `data.agencyConfirmation` | string | Agency-facing confirmation code. |
| `data.cruiseReservation.reservationReferences.confirmationNumber` | string | **The cruise-line confirmation number** — what you'd give the traveler. |
| `data.cruiseReservation.status` | int | Reservation status code (e.g. `6` = confirmed/held, per this sample — status enum values are supplier/system defined). |
| `data.cruiseReservation.rulesInfo.applicableRules[]` | array | Promotions/discounts/markups/service fees automatically applied by the rules engine — not something the client requested directly. |
| `data.cruiseReservation.categories[]` | array | Trimmed echo (id, code, fare code) — not full pricing; use Read Reservation or Price Reservation for authoritative pricing post-booking. |
| `advisories[]` | array | Cruise-line-specific warnings (e.g. accessibility notes) that don't block success but the client should surface to the traveler. |

## 4. Property Cross-Reference

| Property client needs | Endpoint that actually returns it | Notes |
|---|---|---|
| `categories[].code`, `.fare.fareCode.code`, `.cabins[].number` | **Category/Farecode/Cabin Availability** (upstream) | Create doesn't discover these — it commits already-known selections. |
| `paymentToProcess.cardToken` | **Tokenize Card** (`TokenizeCard` or `/v2/payment/TokenizeCard`) | Must be called first if paying at creation. |
| Confirmation number | **Create Reservation only** (first appearance) | This is the first endpoint in the flow where a real confirmation number exists. |
| Full, authoritative price breakdown post-booking | **Price Reservation** (before) or **Read Reservation From Supplier** (after) | Create's response only echoes a trimmed category/fare, not a price breakdown. |
| Applied promotions/rules | **Create Reservation response only** (`rulesInfo.applicableRules`) | Not visible in any discovery call before booking — rules are evaluated/applied at commit time. |
| Reservation status after creation | **Create response**, and later **Read Reservation** (Odysseus) / **Read Reservation From Supplier** | Same `status`/`reservationReferences` fields reappear in both read endpoints. |
| `pos.officeId` / `pos.system` | **API Credential List (POS)** (`listpos`) → `pointOfSales[].officeId` / `.system` | Only needed when the client has multiple POS/profiles set up for this cruise line — see `office_credentials_list_pos.md`. Most single-profile clients can omit both. |

**Practical rule for the chatbot:** if asked "why is there a promo applied that I didn't request," point to `rulesInfo.applicableRules` in the Create response — these are supplier/rules-engine driven, not client-supplied.

---
*Source: `CruiseReservationController.cs` (route/feature/XML remarks) + `swagger.json` (request/response schema) + Postman collection sample (`Create Reservation/create_reservation__without_payment_.md`).*
