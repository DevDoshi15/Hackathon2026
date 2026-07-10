
URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=latest#Solutions/dv/80395000044642054/en/Article

ID: 80395000044642054

# Cruise + Air Booking Flow

## Overview

This article documents a sample booking flow for booking **cruise + cruise line air** together. It shows the properties added to identify a booking's transportation type as "cruise + air."

> **Important:** This sample/package may not currently work in the test environment. It is intended as a guide to the relevant properties, not a verified working request. Inline comments from the source are preserved below to explain each property.

## Sample Structure

```json
"cruiseReservation": {
    "CruiselineAir": { // mandatory element for cruise + Air
        "type": "RoundTrip",
        "GateWayCity": {
            "id": "NYC" // flight departure city
        }
    }
}
```

## Field Reference

| Field | Required? | Description |
|---|---|---|
| `CruiselineAir` | **Mandatory** for cruise + air bookings | The element that identifies the transportation type as "cruise + air." Its presence on a `cruiseReservation` is what signals the booking includes cruise line-arranged air, not just the cruise. |
| `CruiselineAir.type` | Part of `CruiselineAir` | The air trip type — sample shows `RoundTrip`. |
| `CruiselineAir.GateWayCity` | Part of `CruiselineAir` | The gateway (departure) city for the flight. |
| `CruiselineAir.GateWayCity.id` | Part of `GateWayCity` | The city code for the flight departure city — sample shows `NYC`. |

## Notes

- `CruiselineAir` is the mandatory marker element for this transportation type — its absence means the booking is cruise-only.
- This is a partial/sample snippet; only the `CruiselineAir` block within `cruiseReservation` is shown here. Additional standard `cruiseReservation` fields (sailing, cabin, guests, etc.) would still apply alongside this block in a full booking request.
- Since the package is flagged as not currently functional in test, treat this as a **forward-looking reference for property names and structure**, not a request to submit as-is until confirmed working.
