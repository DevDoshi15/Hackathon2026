URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000044850001/en

ID: 80395000044850001

# Category: Upgrade Offer

## Overview

This article documents how a cruise line may return a **category upgrade offer** within the category response, and what that response structure looks like. Full request/response (RQ/RS) files are attached to the source KB article for complete context.

> **Note:** This specific example may not always be available/reproducible — it was captured on the date it was entered and reflects the supplier's response at that point in time.

## Sample Structure

```json
"code": "8E", // Berth Category
"type": 3,
"fares": [
    {
        "status": 1,
        "upgradeFrom": "8C", // Upgrade Offer
        "fareCode": {
            "code": "PNS",
            "type": 0,
            "refundableType": 1
        },
        "prices": [
            {
                "id": 1,
                "amount": 624,
                "type": "AVGPP"
            },
            {
                "id": 3,
                "amount": 119.86,
                "type": "AVGPP"
            },
            {
                "id": 2,
                "amount": 119,
                "type": "AVGPP"
            }
        ],
        "addOns": []
    },
    {
        "status": 1,
        "upgradeFrom": "8D", // Upgrade Offer
        "fareCode": {
            "code": "PNS",
            "type": 0,
            "refundableType": 1
        },
        "prices": [
            {
                "id": 1,
                "amount": 634,
                "type": "AVGPP"
            },
            {
                "id": 3,
                "amount": 119.86,
                "type": "AVGPP"
            },
            {
                "id": 2,
                "amount": 119,
                "type": "AVGPP"
            }
        ],
        "addOns": []
    }
]
```

## How to Read This

The response is for **category `8E`** (a Berth Category, `type: 3`). Inside its `fares` array, each fare entry represents a distinct **upgrade offer path into category 8E**, not just a plain fare:

- The first fare entry has `upgradeFrom: "8C"` — this fare represents an offer to upgrade from category `8C` into category `8E`, priced at the amounts listed.
- The second fare entry has `upgradeFrom: "8D"` — this fare represents a separate offer to upgrade from category `8D` into category `8E`, priced differently from the `8C` offer.

In other words: the same target category (`8E`) can carry **multiple upgrade offers simultaneously**, one per originating category, each with its own fare code, pricing, and status — all nested under that target category's `fares` array.

## Field Reference

| Field | Description |
|---|---|
| `code` | The category code being returned (target/destination category of the upgrade) — here `8E` |
| `type` | Category type; `3` indicates a Berth Category |
| `fares[]` | Array of fare entries for this category; when an upgrade offer applies, each entry represents one upgrade path |
| `fares[].status` | Fare status indicator (`1` observed in this example) |
| `fares[].upgradeFrom` | **Key upgrade-offer indicator.** The category code this fare is offering an upgrade *from* — its presence signals this fare entry represents an upgrade offer rather than a standard fare |
| `fares[].fareCode.code` | The fare code applied to this offer (e.g. `PNS`) |
| `fares[].fareCode.type` | Fare code type |
| `fares[].fareCode.refundableType` | Refundability of the fare — see *Domain Tables: Non Refundable Type* for value meanings |
| `fares[].prices[]` | Array of price components for this fare offer |
| `fares[].prices[].id` | Identifier for the specific price component |
| `fares[].prices[].amount` | The numeric price amount |
| `fares[].prices[].type` | Price breakdown type — `AVGPP` observed here (Average Per Person Price) |
| `fares[].addOns` | Add-ons associated with this fare offer (empty array in this example) |

## Integration Notes

- The presence of `upgradeFrom` on a fare entry is the signal to treat that fare as an **upgrade offer** rather than a standard category fare — consumers should check for this field rather than assuming all fares under a category are standard.
- A single target category can have **multiple upgrade offers** from different source categories at different price points simultaneously (as shown: `8C → 8E` and `8D → 8E` both appearing under category `8E`).
- Each upgrade offer carries its own independent `fareCode`, `prices`, and `addOns` — pricing is not assumed to be shared across upgrade offers even when they target the same category.
- As noted in the source article, availability of upgrade offers is supplier- and point-in-time-dependent; do not assume this exact response will always be reproducible in test.
