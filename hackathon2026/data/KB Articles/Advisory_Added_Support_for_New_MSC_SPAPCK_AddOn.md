URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000137525570/en

ID: 80395000137525570

---

title: Advisory: Added Support for New MSC Add-On Category Type (SPAPCK)
category: Release Advisory
supplier: MSC
api:

* ListAddOns
* ListPrices
* CreateBooking
* ReadBooking
version: 1.0
last\_updated: 2026-07-10
tags:
* MSC
* Add-On
* SPAPCK
* Enum 35
* Release Notes

\---

# Advisory: Added Support for New MSC Add-On Category Type (SPAPCK)

## Overview

Odysseus now supports MSC's newly introduced **SPAPCK** Add-On category by adding support for **Add-On Type Enum 35**. This enhancement ensures compatibility with MSC's latest upgrade option and allows customers to retrieve, price, create, and read bookings that include this new Add-On type.

## What's New

The platform now recognizes and processes the **SPAPCK (Enum 35)** Add-On type across the following API operations.

### ListAddOns

* SPAPCK Add-Ons are now included in **ListAddOns** responses whenever they are available for a sailing.

### ListPrices

* Pricing requests now support SPAPCK Add-Ons.
* Pricing responses correctly calculate and return pricing for bookings containing this Add-On, enabling accurate quote generation.

### CreateBooking

* Bookings that include SPAPCK Add-Ons can now be successfully created and submitted to MSC.

### ReadBooking

* Bookings containing SPAPCK Add-Ons are fully supported when retrieving booking details through the **ReadBooking** API.

## Action Required

Customers who maintain custom Add-On validation, mappings, or business logic based on Add-On types should review their implementation and add support for **Enum 35 (SPAPCK)** where applicable.

## Compatibility

This enhancement is fully backward compatible. Since a new Add-On type has been introduced without modifying any existing Add-On types or behavior, no changes are required unless your implementation explicitly validates or maps Add-On type values.

## Release Schedule

|Environment|Release Timeline|
|-|-|
|Sandbox|Second week of July|
|Production|Third week of July|



