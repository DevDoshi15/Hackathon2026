URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000044850051/en

ID: 80395000044850051
# Cruise Line Insurance Price RQ

## Overview

This article documents how to add insurance to a guest and price it with the cruise line. Full request/response (RQ/RS) files are attached to the source KB article for complete context.

> **Note:** This specific example may not always be available/reproducible — it was captured on the date it was entered and reflects the supplier's response at that point in time.

## Changes in RQ File

```json
"Insurance": {
    "code": "CRCR", // Insurance code received in the Hold Cabin (for MSC, RCCL and NCL) or in Fare Availability (for Carnival) in response
    "type": 2, // supplier insurance
    "CustomerReferences": [
        {
            "rph": 1 // customer for which insurance prices are to be retrieved
        }
    ]
}
```

## Field Reference

| Field | Description |
|---|---|
| `Insurance` | The element used to request insurance pricing for a guest as part of the request. |
| `Insurance.code` | The insurance code being priced. **Source of this code depends on the supplier:** for **MSC, RCCL, and NCL** it is received in the **Hold Cabin** response; for **Carnival** it is received in the **Fare Availability** response. |
| `Insurance.type` | The insurance type. `2` = **supplier insurance** (insurance offered/underwritten by the cruise line/supplier itself). |
| `Insurance.CustomerReferences[]` | Array identifying which customer(s) the insurance price request applies to. |
| `Insurance.CustomerReferences[].rph` | The reference (RPH) of the specific customer for whom insurance prices are to be retrieved. |

## Integration Notes

- The `Insurance.code` value is **not static** — it must first be retrieved from an earlier supplier response before it can be used in this pricing request, and which response it comes from depends on the supplier:
  - **MSC / RCCL / NCL:** retrieve the insurance code from the **Hold Cabin** response.
  - **Carnival:** retrieve the insurance code from the **Fare Availability** response.
- `type: 2` in this example specifically denotes **supplier insurance**; other insurance type values may exist but are not covered by this example.
- `CustomerReferences` scopes the insurance price request to a specific guest via `rph` — multiple guests would each need their own reference entry if pricing insurance for more than one customer.
- As noted in the source article, this example is supplier- and point-in-time-dependent; do not assume the exact codes/values shown will always be reproducible in test.
