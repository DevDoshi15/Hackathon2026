URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=latest#Solutions/dv/80395000044565147/en/Article

ID: 80395000044565147
# Nitro Booking API: Special Service Request Change — Feb 1, 2023

## Overview

As of **February 1, 2023**, the Nitro Booking API's **List Special Services** response added support for returning **amount and breakdown type pricing** for the `PrePaidGratuities` special service.

## What Changed

Previously, special service entries in the List Special Services response did not carry pricing detail. Now, when pricing is available for a special service, a `prices` array is included on that special service entry, containing the amount and how that amount breaks down.

This pricing support is specifically noted for **`PrePaidGratuities`** (code `GRATS`). Not all special services will include a `prices` array — it appears **"when available."**

## Response Structure

The List Special Services response is a list of special service entries. Most entries (e.g. celebration/occasion types like `Honeymoon`) look as they did before — no pricing. `PrePaidGratuities` is the entry that now carries the new `prices` array alongside it, as shown together below:

```json
{
    "code": "H",
    "name": "Honeymoon",
    "description": "OCC",
    "type": "Celebration",
    "associationType": "PAX"
},
{
    "code": "GRATS",
    "name": "PrePaidGratuities",
    "type": "PrePaidGratuities",
    "prices": [
        {
            "amount": 83.94,
            "breadownType": "TOTAL"
        }
    ]
}
```

## Field Reference

| Field | Location | Description |
|---|---|---|
| `code` | Special service object | Short identifier for the special service (e.g. `GRATS` for PrePaidGratuities, `H` for Honeymoon) |
| `name` | Special service object | Display name of the special service |
| `type` | Special service object | Category/type of special service (e.g. `Celebration`, `PrePaidGratuities`) |
| `description` | Special service object | Additional descriptor (e.g. `OCC` for occasion-type services); not present on all entries |
| `associationType` | Special service object | Indicates what the special service is associated with (e.g. `PAX` for passenger-level association); not present on all entries |
| `prices` | Special service object | **New.** Array of pricing entries, present only when pricing is available for that special service |
| `amount` | `prices[]` entry | The price amount (numeric, e.g. `83.94`) |
| `breadownType` | `prices[]` entry | The breakdown type for the amount (e.g. `TOTAL`) |

> **Note:** The field is spelled `breadownType` (not `breakdownType`) in the actual API response — this is the literal field name returned by the API, not a typo to be corrected on the consuming side.

## Integration Notes

- Consumers of the List Special Services response should treat `prices` as **optional/conditional** on each special service entry — only check for it, don't assume it's always present.
- `PrePaidGratuities` (`GRATS`) is the special service type explicitly confirmed to support this pricing breakdown as of this change.
- The breakdown type observed so far is `TOTAL`; other breakdown type values were not specified in this change but may be introduced by the API in the future — treat `breadownType` as an extensible/open value rather than a fixed enum until confirmed otherwise.
