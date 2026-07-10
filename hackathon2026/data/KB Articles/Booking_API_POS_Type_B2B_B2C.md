URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000052306003/en 

ID: 80395000052306003
# Booking API: Point of Sale (POS) - Type: B2B or B2C

## Overview
This article explains the **POS Type** setting (`pos.type`) in the Booking API — the two supported values, how they're set up, and how each one changes the data returned by the API.

---

## The Two POS Types

### 1. B2B
- Meant for **agents / in-house staff / affiliates**.
- In the **Odysseus Booking Engine**, once a user is logged in to admin, the booking flow is automatically treated as **B2B**, and the corresponding B2B features/options are shown.

### 2. B2C
- Applicable **only to customers**.

### Default Behavior
- If **no `pos.type` input is provided**, the **default POS type is `B2B`**.

---

## What Happens Based on Requested POS Type

Based on the requested `pos.type` (`"B2B"` or `"B2C"`), Odysseus does the following:

1. **Selects the corresponding POS profile** based on the API / OfficeId setup.
2. **Returns a filtered list of fare codes.**
3. **Returns a filtered list of categories.**

---

## 1. Office ID / API Setup — Application Type

Odysseus supports configuring the **Office ID / API setup** with an **Application Type** of:
- **B2B Only**
- **B2C Only**
- **All** (both B2B and B2C)

Based on the requested `pos.type` in the request, Odysseus selects the **appropriate POS profile** matching that Application Type setup.

![Office ID Management — Application Type dropdown showing All, B2C Only, B2B Only](pos_office_id_application_type_setup.png)

> **Recommendation**: Only send `pos.type` in the request when it is **B2C**. When `pos.type = "B2C"` is sent, a set of B2C-specific business rules are automatically applied (see sections 2 and 3 below).

### Example Request — `pos.type: "B2C"`
```json
{
    "cruiseReservation": {
        "pos": {
            "type": "B2C"
        },
        "cruise": {
            "packageId": "{{PackageId}}"
        },
        "categories": [
            {
                "code": "BA",
                "fare": {
                    "fareCode": {
                        "code": "A1537687",
                        "type": 0,
                        "refundableType": 1
                    }
                }
            }
        ]
    }
}
```

![Example request body showing pos.type set to B2C](pos_type_b2c_request_example.png)

---

## 2. Filtered List of Fare Codes (B2C)

- In the **B2C flow**, Odysseus returns a **filtered list of fare codes** — not the full/unfiltered set that would be available in B2B.
- For details on which specific fare codes are shown in the B2C flow, see: [Fare Codes: Which Ones Are Shown in B2C](https://supportdesk.odysol.com/portal/en/kb/articles/fare-codes-which-ones-are-shown-in-b2c)

---

## 3. Filtered List of Categories (B2C vs. B2B)

- **B2C flow**: **Closed / waitlisted categories are filtered out** — they will not be returned.
- **B2B flow**: Closed / waitlisted categories **are returned**, along with their **appropriate status**.

### Example — Category List with Status Column (B2B flow)
The `status` column reflects the category's actual availability state (e.g., open, closed, waitlisted) — these rows would still be included in a **B2B** response, but filtered out in a **B2C** response if closed/waitlisted.

![Example category list showing Code, Type, Status, FareCode, and Prices columns](pos_categories_status_list_example.png)

| Column | Description |
|---|---|
| `Code` | Category code (e.g., `GL`, `SL`, `OS`, `GT`, `GB`). |
| `Type` | Category meta-type (see *Class Types / Category Types* article — e.g., `4` = Suite). |
| `Status` | Category status indicator (determines whether it would be filtered out in B2C flow if closed/waitlisted). |
| `FareCode` | Associated fare code for that category/status row. |
| `Prices` | Link/action to view prices for that category + fare code combination. |

---

## Key Takeaways

- `pos.type` accepts **`B2B`** or **`B2C`** — if omitted, defaults to **`B2B`**.
- Send `pos.type: "B2C"` **specifically and only when building a true customer-facing (B2C) flow** — sending it triggers automatic filtering business rules.
- B2C flow differs from B2B in **two concrete ways**:
  1. **Fare codes** returned are filtered (see linked fare code article for specifics).
  2. **Closed/waitlisted categories** are excluded entirely (vs. B2B, which returns them with status).
- Office ID / API setup must be configured to support the requested Application Type (**B2B Only**, **B2C Only**, or **All**) — if the requested `pos.type` doesn't match what's configured for that Office ID, the appropriate POS profile selection logic applies (see also the *Multiple Currency Support* article for related POS fallback behavior when POS doesn't match).
