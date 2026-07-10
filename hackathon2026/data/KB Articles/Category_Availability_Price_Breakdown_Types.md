URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000045823001/en 

ID: 80395000045823001

---
# Title: Category Availability - Price Breakdown Types
category: Business Rules
endpoint: Category Availability
tags:
  - pricing
  - category-availability
  - price-breakdown
  - fare
  - commission
last_updated: 2026-07
---

# Category Availability - Price Breakdown Types

## Purpose

This article explains the various **Price Breakdown Types** returned by the **Category Availability** API and how they should be interpreted.

A Category Availability response contains multiple **Price Items** (Cruise Fare, Taxes, NCCF, Commission, etc.). Each Price Item may contain multiple **Price Breakdown Types** depending on occupancy and supplier support.

---

# Key Concept

A **Price ID identifies the pricing component**, while the **Price Type identifies how that pricing component is calculated**.

Therefore, the **same Price ID can appear multiple times** with different Price Types.

Example:

```json
{ "id": 1, "type": "AVGPP" }

{ "id": 1, "type": "ADDADT" }

{ "id": 1, "type": "ADDCHD" }
```

All three records represent **Cruise Fare (Price ID = 1)** but different pricing breakdowns.

---

# Price Breakdown Types

| Type | Definition |
|------|------------|
| TOTAL | Total price for all passengers. |
| AVGPP | Average price per passenger. |
| AVGPN | Total amount divided by the number of nights. |
| AVGPPPN | Average price per passenger per night. |
| SINGLE | Single occupancy fare returned by the cruise line. |
| DOUBLE | Double occupancy fare returned by the cruise line. |
| ADDADT | Additional adult fare (after double occupancy). |
| ADDCHD | Additional child fare (after double occupancy). |

> **Note:** `AVGPN` and `AVGPPPN` are generally **not used in the Cruise Booking Flow**.

Supplier support for SINGLE, DOUBLE, ADDADT and ADDCHD varies by cruise line.

---

# Calculation Examples

## Example 1

Total Price = **$1,500**

Guests = **2**

| Breakdown | Value |
|-----------|------:|
| TOTAL | 1500 |
| AVGPP | 750 |

---

## Example 2

Total Price = **$1,500**

Guests = **3**

| Breakdown | Value |
|-----------|------:|
| TOTAL | 1500 |
| AVGPP | 500 |

---

# Price Breakdown per Price Item

Price breakdowns are returned **per Price Item**, not once for the entire response.

Examples include:

- Cruise Fare
- NCCF (Non-Commissionable Cruise Fare)
- Taxes and Fees
- Supplier Commission
- Site Discount
- Site Markup
- Other itemized charges

Each price item may contain one or more breakdown types.

---

# Category Price Types

| Price ID | Description |
|---------:|-------------|
| 1 | Cruise Fare |
| 2 | Port Charges / NCCF |
| 3 | Taxes and Fees |
| 4 | Brochure Fare / Strike Through Fare |
| 7 | Cruise Line Air Fare |
| 8 | Cruise Line Air Tax |
| 14 | Prepaid Gratuities |
| 44 | Site / System Discount (Rules Engine) |
| 48 | Site / System Markup (Rules Engine) |
| 59 | Cruise Line Air Credit |
| 61 | Agent Commission (Rules Engine) |
| 98 | Supplier Commission |

---

# Reading the Response

Example:

```json
{
    "id": 1,
    "amount": 587.50,
    "type": "AVGPP"
}

{
    "id": 1,
    "amount": 426,
    "type": "ADDADT"
}

{
    "id": 1,
    "amount": 426,
    "type": "ADDCHD"
}
```

Interpretation:

- All three records have **Price ID = 1 (Cruise Fare)**.
- Each record represents a different pricing breakdown.
- Do **not** overwrite one value with another simply because the Price ID is the same.

---

# Common Mistakes

## Treating Price ID as Unique

Incorrect:

```
Dictionary<int, Price>
```

This causes later entries with the same Price ID to overwrite earlier ones.

## Ignoring Price Type

Always identify a price using the combination:

```
Price ID + Price Type
```

This uniquely identifies each price breakdown.

## Assuming Every Supplier Returns Every Breakdown

Supplier implementations vary.

Some suppliers return only:

- TOTAL
- AVGPP

Others additionally return:

- SINGLE
- DOUBLE
- ADDADT
- ADDCHD

---

# Best Practices

- Treat **Price ID + Price Type** as a composite key.
- Preserve all price breakdowns returned by the supplier.
- Handle missing breakdown types gracefully.
- Use AVGPP for most customer-facing pricing displays unless business rules specify otherwise.
- Do not assume every supplier supports all breakdown types.

---

# Related Articles

- Category Availability
- Pricing API
- Fare Code
- Rules Engine
- Supplier Commission
- NCCF
- Taxes and Fees
