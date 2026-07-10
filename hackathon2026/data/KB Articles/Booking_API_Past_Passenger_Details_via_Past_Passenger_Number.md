URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000092795023/en 

ID: 80395000092795023

---
# Title: Booking API - Past Passenger Details via Past Passenger Number
category: Booking API
endpoint: /v2/reservation/cruise/GetPastPaxDetails
method: POST
tags:
  - past-passenger
  - loyalty
  - getpastpaxdetails
  - reservationpreferences
last_updated: 2026-07
---

# Booking API: Past Passenger Details via Past Passenger Number

## Purpose

The **GetPastPaxDetails** API supports looking up passenger information using a **Past Passenger Number** for supported cruise lines.

This enhancement allows client applications to retrieve passenger details without supplying the passenger's personal information.

> **Supported cruise lines:** NCL, MSC, and Silversea.

---

# Endpoint

```http
POST /v2/reservation/cruise/GetPastPaxDetails
```

---

# Feature Overview

Previously, sending only a `pastPaxNumber` resulted in a validation error because additional passenger information was expected.

To enable lookup by passenger number alone, a new reservation preference has been introduced.

## Required Reservation Preference

```json
"ReservationPreferences": [
  {
    "Type": "PastPaxLookupByNumber",
    "Value": true
  }
]
```

When this preference is present and set to `true`, the API performs the lookup using only the supplied **Past Passenger Number**.

---

# Request Example

```json
{
  "cruiseReservation": {
    "cruise": {
      "cruiseLine": {
        "id": 982
      }
    },
    "ReservationPreferences": [
      {
        "Type": "PastPaxLookupByNumber",
        "Value": true
      }
    ]
  },
  "customers": [
    {
      "pastPaxNumber": "240945"
    }
  ]
}
```

---

# Important Behavior

- Only the **Past Passenger Number** is required.
- Any additional passenger details supplied in the request are **ignored**.
- The API returns the passenger profile associated with the supplied number if found.

---

# Response

A successful response may include:

- Passenger name
- Date of birth
- Age
- Address
- Contact information
- Nationality
- External loyalty/member type (supplier dependent)

---

# Business Rules

- Supported only by selected cruise lines (NCL, MSC, Silversea).
- `PastPaxLookupByNumber` must be enabled.
- `pastPaxNumber` is mandatory.
- Passenger details supplied in the request are not used for the lookup.

---

# Common Errors

| Scenario | Result |
|----------|--------|
| Missing `PastPaxLookupByNumber` | Validation error |
| Invalid past passenger number | Passenger not found |
| Unsupported cruise line | Supplier or validation error |

---

# Best Practices

- Enable `PastPaxLookupByNumber` only when performing lookup by passenger number.
- Validate the cruise line supports this feature before calling the API.
- Do not send unnecessary passenger information.
- Handle cases where no matching passenger record exists.

---

# Integration Flow

```text
Select Supported Cruise Line
          │
          ▼
Provide Past Passenger Number
          │
          ▼
Set ReservationPreference:
PastPaxLookupByNumber = true
          │
          ▼
Call GetPastPaxDetails
          │
          ▼
Receive Passenger Profile
```

---

# Related Articles

- GetPastPaxDetails
- Reservation Preferences
- Booking API - How RPH Works
- Read Reservation
