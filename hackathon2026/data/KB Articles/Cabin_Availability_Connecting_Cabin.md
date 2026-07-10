URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000052793031/en

ID: 80395000052793031
# Cabin Availability: Connecting Cabin

## Overview
This article explains how **connecting cabins** are returned via the Cabin Availability API response.

---

## Important Notes

- **Cabin availability varies by sailing** and is **not controlled by Odysseus**.
  - To confirm connecting cabin availability, you must **reach out to the cruise line directly**, or **try multiple sailings**.
- **Connecting cabins are only supported by some cruise lines.**
  - For the latest supported list, check the: [Cruise Profile Matrix: Cruise Line / API Features Supported](https://supportdesk.odysol.com/portal/en/kb/articles/cruise-profile-matrix-cruise-line-api-features-supported)
- **Cruise lines currently known to support search of connecting cabins** (as of this article):
  - **Royal Caribbean**
  - **Celebrity**
  - ⚠️ This list may not be exhaustive/current — always verify against the Cruise Profile Matrix linked above.

---

## Example Cabin Availability Response (Connecting Cabin)

```json
{
    "number": "3518",
    "connectingCabinNumber": "3516",
    "isGuarantee": true,
    "beds": [
        {
            "code": "A",
            "name": "2C",
            "description": "Apart",
            "type": 281
        },
        {
            "code": "T",
            "name": "2C",
            "description": "Together",
            "type": 282
        }
    ],
    "deck": {
        "id": 12146,
        "name": "Deck 3",
        "description": "Staterooms."
    },
    "occupancy": {
        "min": 0,
        "max": 2
    }
}
```

---

## Field Definitions

| Field | Description |
|---|---|
| `number` | The cabin number of this specific cabin (e.g., `"3518"`). |
| `connectingCabinNumber` | The cabin number of the **connecting cabin** paired with this one (e.g., `"3516"`). Presence of this field indicates the cabin has a connecting counterpart. |
| `isGuarantee` | Boolean indicating whether this is a **guarantee cabin** (specific cabin not assigned yet) vs. a confirmed/assigned cabin number. |
| `beds` | Array of bed configuration options for the cabin. |
| `beds[].code` | Short code for the bed configuration (e.g., `"A"` for Apart, `"T"` for Together). |
| `beds[].name` | Bed configuration name/label (e.g., `"2C"`). |
| `beds[].description` | Human-readable description of the bed configuration (e.g., `"Apart"`, `"Together"`). |
| `beds[].type` | Numeric type code for the bed configuration (e.g., `281` = Apart, `282` = Together — based on this example). |
| `deck` | Object describing the deck the cabin is located on. |
| `deck.id` | Internal deck identifier. |
| `deck.name` | Deck name/label (e.g., `"Deck 3"`). |
| `deck.description` | Deck description (e.g., `"Staterooms."`). |
| `occupancy` | Object describing min/max occupancy for the cabin. |
| `occupancy.min` | Minimum occupancy allowed for the cabin. |
| `occupancy.max` | Maximum occupancy allowed for the cabin. |

---

## Key Takeaways

- A cabin is identified as having a connecting cabin when the `connectingCabinNumber` field is present and populated — this references the specific cabin number of its connecting counterpart.
- Connecting cabin availability is **sailing-specific** and **cruise-line-controlled**, not something Odysseus can guarantee or control.
- Only **Royal Caribbean** and **Celebrity** are currently confirmed to support connecting cabin search — always check the Cruise Profile Matrix for the most current list before relying on this feature for other cruise lines.
- The `beds` array can describe multiple configuration options (e.g., "Apart" vs. "Together") relevant to connecting cabin setups, since connecting cabins may need beds configured together or apart depending on the booking.
