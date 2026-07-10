URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000047967025/en 

ID: 80395000047967025

---
# Title: Domain Table - Transportation Types
category: Domain Tables
endpoint: Multiple Booking APIs
tags:
  - transportation
  - domain-table
  - cruise
last_updated: 2026-07
---

# Domain Table: Transportation Types

## Purpose

The **Transportation Type** identifies the type of cruise product associated with a package. It is used throughout the Nitro Booking API to distinguish between cruise-only sailings, cruise tours, and cruise packages that include cruise-line air.

Applications should interpret this value to determine the correct booking flow, package type, and user experience.

---

# Transportation Types

| Value | Name | Description |
|------:|------|-------------|
| **28** | Cruise Line Tour | A cruise package that includes a land tour operated by the cruise line before or after the cruise. |
| **29** | Cruise Only | A standard cruise itinerary without any cruise-line managed land tour or air package. |
| **32** | Cruise + Cruise Line Air | A cruise package that includes cruise-line arranged airfare in addition to the cruise. |

---

# Business Rules

## Transportation Type 28 – Cruise Line Tour

Use this value when the package includes:

- Cruise itinerary
- Cruise-line managed land tour

Typical characteristics:

- Cruise Package Departure Date may differ from Cruise Departure Date.
- Cruise Package Arrival Date may differ from Cruise Arrival Date.
- Total duration includes both land and cruise portions.

---

## Transportation Type 29 – Cruise Only

Use this value for standard cruise sailings.

Typical characteristics:

- Cruise Package Departure Date equals Cruise Departure Date.
- Cruise Package Arrival Date equals Cruise Arrival Date.
- No land tour is included.

---

## Transportation Type 32 – Cruise + Cruise Line Air

Use this value when the cruise package includes airfare arranged by the cruise line.

Typical characteristics:

- Cruise itinerary
- Cruise-line airfare
- Air pricing may appear in pricing responses (supplier dependent).

---

# Integration Guidance

When processing packages:

- Use Transportation Type to determine the package category.
- Do not infer package type solely from itinerary dates.
- Validate transportation type when mapping external supplier data to Odysseus Package IDs.

---

# Best Practices

- Treat Transportation Type as an enumeration.
- Handle unknown values gracefully for forward compatibility.
- Use this field together with Package ID and itinerary information when determining booking behavior.

---

# Related Articles

- Package ID Mapping
- Cruise Sailing Availability (Live)
- Cruise Search
- Booking Flow
