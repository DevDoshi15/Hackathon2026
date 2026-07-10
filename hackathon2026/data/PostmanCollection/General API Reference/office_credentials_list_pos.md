# API Credential List (POS)

## 1. API Endpoint

| | |
|---|---|
| **Route** | `POST {{BaseUrl}}/v2/reservation/cruise/listpos` |
| **Controller action** | `CruiseReservationController.ListPOS` |
| **Required feature flag** | `Enums.Features.ListPOS` (`AllowAjax = true`) |
| **Auth** | Basic (`Nitro.Sandbox.ClientId` / `Nitro.Sandbox.ClientSecret`) + `SiteItemId` header |
| **Request/Response object** | Compact, cruise-line-agnostic `Reservation` object |

## 2. Use Case

Lists the Point-of-Sale (POS) / profile ID(s) configured for a cruise line. **Only necessary if a client has more than one profile ID set up with a cruise line** — e.g. one profile for published fares and another for interline/net fares, or multiple profiles at an affiliate level.

**Where it sits in the flow:**

```
ListPOS (rare, only if multi-POS)  →  ListFareCodes / ListCategories  →  ...
```

Per the controller's XML remarks: **this message should only be used after confirmation with Odysseus**, otherwise you're adding unnecessary calls to your flow. Most integrations never need to call this — the correct POS is resolved automatically per client setup.

## 3. Request / Response Details

Two request shapes are supported — by package or by cruise line:

### Request — by package ID

```json
{
    "cruiseReservation": {
        "cruise": { "packageId": 1269434 }
    }
}
```

### Request — by cruise line ID

```json
{
    "cruiseReservation": {
        "cruise": { "cruiseLine": { "id": 982 } }
    }
}
```

| Field | Type | Notes |
|---|---|---|
| `cruiseReservation.cruise.packageId` | int | Use when you already have a specific sailing/package in context. |
| `cruiseReservation.cruise.cruiseLine.id` | int | Use when you want all POS profiles for a cruise line generally, not tied to one package. |
| — | — | Exactly one of these two selectors is required; no `customers` array needed at all for this call. |

### Response — key fields returned

```json
{
  "data": {
    "cruiseReservation": {
      "cruise": { "packageId": 1269434, "cruiseline": { "id": 8 } },
      "pointOfSales": [
        {
          "id": 2114,
          "name": "NitroAPI Sandbox - USD | O100US6797",
          "priority": 5,
          "apiId": "RCCL",
          "officeId": "O100US6797",
          "system": "Test",
          "currency": "USD",
          "type": "B2C"
        }
      ]
    }
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `data.cruiseReservation.pointOfSales[].id` | int | The POS identifier — pass this (typically via `cruiseReservation.pos.id` in other endpoints, when a client needs to force a specific profile) alongside other requests. |
| `.name` | string | Human-readable label combining sandbox/environment, currency, and office ID — useful for a UI picker if multiple POS exist. |
| `.officeId` | string | The cruise-line-facing office/agency ID tied to this POS. |
| `.currency` | string | Currency this POS is configured to transact in. |
| `.type` | enum `Any`\|`B2C`\|`B2B`\|`Undefined` | Whether this POS is for consumer-facing or trade/agent-facing sales. |
| `.apiId` | string | Which cruise-line API integration this POS routes through (e.g. `"RCCL"`, `"MSC"`). |
| `.priority` | int | Ordering hint when multiple POS profiles exist and one should be preferred by default. |
| `.agencyInfo` / `.secondaryAgencyInfo` | object | `AgencyPointOfSale` — agency code + phone, populated only for agency-specific POS setups. |

## 4. Property Cross-Reference

| Property client needs | Endpoint that actually returns it | Notes |
|---|---|---|
| `pos.id` to force a specific profile on downstream calls | **API Credential List (POS) only** | Every other endpoint accepts `cruiseReservation.pos` as an optional override; this is the only endpoint that enumerates what values are valid. |
| Default/automatic POS resolution | **Not this endpoint** — handled automatically per client setup by Odysseus | Confirmed by the controller's own remark: call this only when a client genuinely has multiple profiles and needs to pick one explicitly. |

**Practical rule for the chatbot:** this is a rarely-needed lookup call, not a step in the standard booking flow. If a client asks a general "how do I book" question, don't surface this endpoint unless they specifically mention having multiple POS/profile setups with a cruise line.

---
*Source: `CruiseReservationController.cs` (route/feature/XML remarks) + `swagger.json` (request/response schema) + Postman collection samples (`Office Credentials List (POS)/*.md`).*
