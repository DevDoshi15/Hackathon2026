URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000081865001/en 

ID: 80395000081865001

---
# Title: How to Opt for Non-Refundable Deposit (NRD) Discount for Regent Seven Seas through Nitro API
category: Supplier Guide
supplier: Regent Seven Seas Cruises
endpoint:
  - AddOns Availability
  - Create Reservation
  - Read Reservation From Supplier
tags:
  - regent
  - nrd
  - addon
  - create-booking
last_updated: 2026-07
---

# How to Opt for Non-Refundable Deposit (NRD) Discount for Regent Seven Seas

## Purpose

This guide explains how to determine whether a **Non-Refundable Deposit (NRD) Discount** is available, how to apply it during booking, and how to verify that it has been successfully applied.

> **Applicability:** This enhancement is supported **only for Regent Seven Seas Cruises**.

---

# Overview

The booking flow consists of three steps:

1. Check NRD availability using **AddOns Availability**
2. Include the NRD add-on during **Create Reservation**
3. Verify the applied discount using **Read Reservation From Supplier**

---

# Step 1 – Check NRD Availability

## API

**AddOns Availability**

Provide:

- PackageId
- Category Code
- Fare Code

If the selected fare supports the NRD discount, the response contains an add-on similar to:

```json
{
  "code": "NRDDiscount",
  "name": "Make the deposit Non-Refundable for additional savings.",
  "description": "Get Nonrefundable Deposit Saving",
  "prices": [
    {
      "amount": -314.95,
      "type": "AVGPP"
    },
    {
      "amount": -629.90,
      "type": "TOTAL"
    }
  ]
}
```

### Interpretation

- Presence of **NRDDiscount** means the fare is eligible.
- Negative amounts represent the discount value.

### If NRD Is Not Returned

The selected combination is not eligible.

Try changing:

- PackageId
- Category Code
- Fare Code

---

# Step 2 – Book Using the NRD Discount

## API

**Create Reservation**

Include the complete **NRDDiscount** add-on object returned by the AddOns Availability API in the `addOns` collection.

The reservation will then be created with the NRD discount applied.

---

# Step 3 – Verify the Applied Discount

## API

**Read Reservation From Supplier**

Provide:

- Confirmation Number
- Cruise Line ID

If the booking was created successfully with the discount, the response will include the same **NRDDiscount** object within the reservation's `addOns` section.

Presence of this object confirms the NRD discount has been applied.

---

# Business Rules

- Supported only for **Regent Seven Seas Cruises**.
- The add-on must first be obtained from AddOns Availability.
- Do not manually construct the NRD add-on.
- Only fares returning `NRDDiscount` are eligible.
- Verification should always be performed using Read Reservation From Supplier.

---

# Common Mistakes

## Manually Creating the Add-on

Always reuse the supplier-provided object.

---

## Assuming Every Fare Supports NRD

Eligibility depends on:

- Package
- Category
- Fare Code

---

## Skipping Verification

Always confirm the applied add-on using Read Reservation From Supplier.

---

# Best Practices

- Query AddOns Availability immediately before booking.
- Preserve the returned add-on object without modification.
- Store the confirmation number for later verification.
- Display the discount separately in booking summaries when appropriate.

---

# Integration Flow

```text
AddOns Availability
        │
        ▼
NRDDiscount Available?
        │
        ├── No → Choose different Package / Category / Fare
        │
        └── Yes
              │
              ▼
Create Reservation (include addOn)
              │
              ▼
Read Reservation From Supplier
              │
              ▼
Verify NRDDiscount exists in addOns
```

---

# Related Articles

- AddOns Availability
- Create Reservation
- Read Reservation From Supplier
- Pricing API
- Supplier AddOns
