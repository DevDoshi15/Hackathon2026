---
title: Advisory: Carnival Pricing and Promotion Optimization (PPO)
category: Release Advisory
supplier: Carnival Cruise Line
version: 1.0
last_updated: 2026-07-10
tags:
  - Carnival
  - PPO
  - Pricing
  - Promotions
  - Modify Booking
---

# Advisory: Carnival Pricing and Promotion Optimization (PPO)

## Overview

Carnival Cruise Line has introduced Pricing and Promotion Optimization (PPO) enhancements affecting booking creation, pricing, fare retrieval, and booking modification. Odysseus has been updated to support these supplier changes while maintaining compatibility with existing booking flows.

## Impact Summary

- Support for Military and Interline promotional fares using **FarePreference**.
- Correct fare type handling throughout booking and modification flows.
- Support for **Combinable Fare Codes** in Read and Modify operations.
- Improved booking modification success for passenger, dining, cabin, and insurance updates.
- Support for supplier-returned **Onboard Credit (OBC)** price items.
- Updated pricing behavior for fare and category modifications.

### Availability

| Environment | Date |
|---|---|
| Sandbox | 28 May 2026 |
| Production | 12 June 2026 |

---

# 1. Special Fare Type Handling

## Overview

Carnival now requires the **FareReference/FarePreference** node to retrieve promotional fares such as:

- Military
- Interline

Without the appropriate FarePreference, these fares are not returned.

## Requirements

Always pass:

- Correct FarePreference
- Applicable Fare Type
- Promotional Fare Code

This applies to:

- ListFareCodes
- ListCategories
- ListPrices
- Create Booking
- Modify Booking

Failure to include FarePreference may result in supplier errors such as:

> "No Offer available for selected criteria."

---

# 2. Booking Modification Enhancement

## Overview

Read responses now return:

- Guest Level Fare Code
- Booking Level Fare Code (Combinable Fare Code)

Odysseus exposes the booking-level value as the **Combinable Fare Code**.

## No Price Change Modifications

The combinable fare code should be supplied for:

- Passenger updates
- Dining changes
- Cabin changes
- Insurance updates

Without it, supplier validation may fail and modifications may be rejected.

## Price Change Modifications

Applies to:

- Fare Code changes
- Category changes

Updated fare information should be supplied. Passing the combinable fare code is recommended for best compatibility.

---

# 3. Onboard Credit (OBC) Price Item

## Overview

Carnival may now return Onboard Credit as dedicated pricing items.

Odysseus maps these to the existing price item:

- **Price Item ID:** 42
- **Description:** Inclusive Onboard Promotion

## Supported OBC Codes

| Code | Description |
|------|-------------|
| POBC | Pax OBC |
| NOBC | Any Department OBC |
| BOBC | Bar OBC |
| COBC | Camp Carnival / Cucina Del Capitan Credit |
| SOBC | Casino Onboard Credit |
| MOBC | Family On-Board Credit |
| FOBC | Family Bundle OBC |
| TOBC | Gift Shop OBC |
| IOBC | Keep in Touch OBC |
| HOBC | Photo On-Board Credit |
| XOBC | Shore Excursion Credit |
| AOBC | SPA On Board Credit |
| WOBC | Stay Connected Credit |
| KOBC | Steak House Credit |
| ROBC | BARSPA Credit |

## Example Mapping

```json
{
  "id": 42,
  "code": "NOBC",
  "amount": 200,
  "displayType": 9
}
```

---

# Action Required

Changes are required if your implementation:

- Creates bookings using Military or Interline fare codes.
- Performs booking modifications.
- Processes Carnival pricing responses.
- Displays onboard promotional credits.

---

# Compatibility

These enhancements are backward compatible but integrations should adopt FarePreference and Combinable Fare Code handling to ensure successful supplier interactions.
