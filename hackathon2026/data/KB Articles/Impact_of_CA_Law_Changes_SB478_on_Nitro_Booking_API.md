URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000082820215/en

ID: 80395000082820215

---
# Title: Impact of CA Law Changes (SB 478) on Nitro Booking API
category: Regulatory Compliance
effective_date: 2024-07-01
tags:
  - california
  - sb478
  - pricing
  - category-availability
  - pricing-api
last_updated: 2026-07
---

# Impact of CA Law Changes (SB 478) on Nitro Booking API

## Purpose

This article explains the Nitro Booking API changes introduced to comply with **California SB 478**, effective **July 1, 2024**.

The objective of these changes is to present pricing in a manner that aligns with California pricing transparency requirements while preserving the overall trip total.

---

# Rollout

- Sandbox Availability: Around **June 12, 2024**
- Effective Date: **July 1, 2024**

---

# Impacted Cruise Lines

Currently impacted:

- Cunard
- Holland America
- Princess
- Seabourn

Pending additional supplier information:

- Carnival
- Costa

---

# Summary of Changes

The overall booking total **does not change**.

Instead, certain non-commissionable fees are redistributed between pricing components.

Major additions include:

- RCFE (Included Fees)
- IGVT (Government Taxes)
- GVTF (Taxes on Hotel/Add-ons)

---

# Category Availability Changes

## Before

Cruise Fare (AVGPP)

- Amount: 4119

Taxes & Fees

- Amount: 260

Total

- 4379

## After

Cruise Fare (AVGPP)

- Amount: 4272.52

Included Fees

- 153.52
- Returned in `includedFees`
- Already included in Cruise Fare
- Non-commissionable

Taxes

- 106.48

Port Charges (NCCF)

- 245

Total

- 4379 (unchanged)

---

## New Field

### includedFees

Returned inside the Cruise Fare price item.

Example

```json
{
  "id": 1,
  "amount": 4272.52,
  "includedFees": 153.52
}
```

Business Rules

- Included in Cruise Fare amount
- Non-commissionable
- Represents RCFE from supplier

---

# Pricing API Changes

## Before

| Code | Description |
|------|-------------|
| AMCT | Cruise Fare |
| NCFR | Port Charges |
| TXFS | Taxes |

Total

```
AMCT + TXFS
```

---

## After

| Code | Description |
|------|-------------|
| AMCT | Cruise Fare (includes RCFE) |
| RCFE | Included Fees |
| NCFR | Port Charges |
| IGVT | Government Taxes |

Total

```
AMCT + IGVT
```

Although the price distribution changes, the overall total remains identical.

---

# Add-on Pricing Changes

For bookings containing optional packages (for example transfers or hotel packages):

## Before

- AMCT
- NCFR
- TXFS
- PKGS

## After

- AMCT
- RCFE
- NCFR
- IGVT
- GVTF
- PKGS

### GVTF

Represents taxes applied to hotel stays or other optional packages.

Unlike previous responses, two tax entries may now exist:

- IGVT
- GVTF

Both may share the same Price ID while having different pricing codes.

---

# Important Business Rules

- Booking totals remain unchanged.
- Cruise Fare now includes RCFE.
- RCFE is non-commissionable.
- Taxes are split into multiple components.
- Optional package pricing remains separate.
- Client integrations should not assume a single tax line item.
- Client integrations should not assume Price IDs are unique without considering the pricing code.

---

# Integration Impact

Applications should:

- Support the new `includedFees` field.
- Parse RCFE pricing items.
- Support multiple tax records (IGVT and GVTF).
- Preserve pricing code when grouping prices.
- Continue calculating totals using returned values instead of assumptions.

---

# Common Mistakes

## Assuming TXFS is the only tax

Incorrect.

Taxes may now be split across:

- IGVT
- GVTF

---

## Ignoring RCFE

RCFE is already included in Cruise Fare.

It should not be added again when calculating totals.

---

## Treating Price ID as Unique

Multiple pricing records may share the same Price ID but have different pricing codes.

Use both:

- Price ID
- Pricing Code

to uniquely identify a pricing component.

---

# Best Practices

- Always consume pricing exactly as returned.
- Display Included Fees when required by business rules.
- Preserve all pricing components individually.
- Validate pricing integrations against both Sandbox and Production after SB478 rollout.

---

# Related Articles

- Category Availability Price Breakdown Types
- Pricing API
- HTTP Status Codes
- Rules Engine Pricing
