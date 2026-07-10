URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000102558021/en 

ID: 80395000102558021

---
# Title: Royal Caribbean and Celebrity Cruises - Extend Hold No Longer Supported
category: Supplier Changes
suppliers:
  - Royal Caribbean
  - Celebrity Cruises
endpoint: /v2/reservation/cruise/extendHold
method: POST
tags:
  - extend-hold
  - royal-caribbean
  - celebrity
  - hold-policy
last_updated: 2026-07
---

# Royal Caribbean and Celebrity Cruises - Extend Hold No Longer Supported

## Purpose

This article explains the removal of **Extend Hold** support for **Royal Caribbean** and **Celebrity Cruises** and the resulting behavior in both the Odysseus Booking Engine and Nitro Booking API.

---

# Overview

Royal Caribbean and Celebrity Cruises no longer support the **Extend Hold** operation.

Odysseus has updated its Booking Engine and Booking API to reflect this supplier change.

---

# Impact

## Booking Engine

- The **Extend Hold** option is no longer displayed on the booking dashboard.

## Booking API

Requests sent to the **Extend Hold** endpoint for these cruise lines will fail.

Typical response:

```json
{
  "isSucceed": false,
  "advisories": [
    {
      "code": "7001",
      "message": "This message is not supported by this cruise line.",
      "type": "Error"
    }
  ]
}
```

---

# Affected Suppliers

- Royal Caribbean
- Celebrity Cruises

---

# Booking Types

| Booking Type | Extend Hold Support |
|--------------|---------------------|
| FIT | ❌ Not Supported |
| Groups | ❌ Not Supported (unchanged) |

> This change only impacts FIT bookings because Extend Hold was already unavailable for Group bookings.

---

# Hold Policy Reference

Current supplier hold policy:

| Days Before Sailing | Maximum Hold Length (Days) |
|--------------------:|---------------------------:|
| 0 – 30 | 0 |
| 31 – 45 | 1 |
| 46 – 90 | 2 |
| 91+ | 5 |

These values represent the supplier's booking hold policy and do **not** imply that the Extend Hold API is available.

---

# Business Rules

- Extend Hold is not supported for Royal Caribbean.
- Extend Hold is not supported for Celebrity Cruises.
- Existing Group booking behavior is unchanged.
- Applications should not display an Extend Hold option for these suppliers.

---

# Integration Guidance

Applications should:

- Hide or disable the Extend Hold action for affected suppliers.
- Handle error code **7001** gracefully.
- Inform users that the supplier does not support extending holds.
- Follow supplier hold policies when designing booking workflows.

---

# Common Errors

| Scenario | Result |
|----------|--------|
| Extend Hold requested for Royal Caribbean | Error 7001 |
| Extend Hold requested for Celebrity | Error 7001 |
| Group booking | Not supported (no change) |

---

# Best Practices

- Check supplier capabilities before calling Extend Hold.
- Treat supplier support as feature-specific.
- Do not retry Extend Hold after receiving error code 7001.

---

# Related Articles

- Cabin Hold
- Cabin Release
- Booking Flow
- HTTP Status Codes, Errors and Advisories
