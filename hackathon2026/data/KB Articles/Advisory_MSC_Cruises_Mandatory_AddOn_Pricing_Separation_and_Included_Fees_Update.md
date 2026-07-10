URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000133942042/en/Article

ID: 80395000133942042

---

title: Advisory: MSC Cruises Mandatory Add-On Pricing Separation and Included Fees Update
category: Release Advisory
supplier: MSC Cruises
version: 1.0
last\_updated: 2026-07-10
tags:

* MSC
* IncludedFees
* Pricing
* Category Availability

\---

# Advisory: MSC Cruises Mandatory Add-On Pricing Separation and Included Fees Update

## Overview

Odysseus has enhanced the Booking API to improve how **MSC Cruises** pricing information is structured and returned.

Mandatory add-on charges are now separated from the base fare and exposed through a dedicated **IncludedFees** field in the **Category Availability** response.

## What's Changed

### Mandatory Add-On Pricing Separation

Mandatory add-on charges are no longer embedded within the base fare representation.

Instead, these charges are returned in a dedicated **IncludedFees** collection.

### IncludedFees

The **IncludedFees** field contains mandatory add-on charges that are already included in the total category price.

> \*\*Important:\*\* Values returned in `IncludedFees` are informational only. They are already included in the total fare and \*\*must not be added again\*\* during price calculations.

## Client Impact

No changes are required for total price calculations.

Clients may optionally use the `IncludedFees` field to:

* Display a more detailed fare breakdown.
* Improve pricing transparency for end users.
* Clearly distinguish mandatory add-on charges from the base fare.

## API Impact

**Affected Endpoint**

* Category Availability

**Response Enhancement**

* New `IncludedFees` field available in the Category Availability response.
* Overall pricing calculations remain unchanged.

## Best Practices

* Continue using the total category price for pricing calculations.
* Treat `IncludedFees` as informational.
* Do not add IncludedFees amounts to the total price.
* Use IncludedFees only when displaying pricing breakdowns.

## Compatibility

This enhancement is fully backward compatible.

Existing integrations continue to function without modification while optionally benefiting from the additional pricing detail provided by the `IncludedFees` field.

