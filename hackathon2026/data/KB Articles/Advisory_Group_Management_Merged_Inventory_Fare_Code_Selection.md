URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000138526711/en

ID: 80395000138526711

---

title: Advisory: Group Management Enhancement – Merged Inventory Support in Fare Code Selection
category: Release Advisory
feature: Group Management
api:

* /v2/reservation/cruise/listfarecodes
version: 1.0
last\_updated: 2026-07-10
tags:
* Group Management
* Fare Codes
* Inventory Source
* Online Inventory
* Offline Inventory
* Merged Inventory

\---

# Advisory: Group Management Enhancement – Merged Inventory Support in Fare Code Selection

## Overview

The Group Management module has been enhanced to support merged **Online (FIT/Group)** and **Offline (Local)** inventories during the Fare Code Selection process. This enhancement ensures that fare code selection is consistent with the configured **Inventory Source** and aligns with the inventory displayed throughout the booking flow.

> \*\*Reference:\*\* For additional information about Inventory Source configuration, refer to the existing knowledge base article:
> \*\*"Group Management Enhancement: Merged Online/Offline Group Category Prices and Inventory."\*\*

## What's New

### Fare Code API

The **`/v2/reservation/cruise/listfarecodes`** endpoint now returns fare codes based on the configured **Inventory Source**.

Depending on the configuration, the response may include:

* Online FIT fare codes
* Online Group fare codes
* Offline (Local) fare codes
* A merged list of Online and Offline fare codes

### Fare Code Selection Page

The Fare Code Selection page now displays fare codes from the configured inventory source.

Supported display modes include:

* Online inventory only
* Offline (Local) inventory only
* Merged Online and Offline inventories

When merged inventory is configured, fare codes from both inventory sources are presented together, allowing users to select the appropriate fare code from a single interface.

The fare code display behavior follows the configured Inventory Source, ensuring consistency with the inventory and pricing shown on the Category Selection page.

## Benefits

* Provides a unified fare code selection experience for merged inventory scenarios.
* Improves visibility of available Online and Offline fare codes.
* Ensures a consistent booking experience across Category Selection and Fare Code Selection pages.
* Eliminates discrepancies between displayed inventory and available fare codes.

## Impact

This enhancement improves the user experience for agencies using merged inventory configurations by presenting all applicable fare codes in a single view while maintaining consistency with the configured Inventory Source.

## Compatibility

This enhancement is backward compatible. Existing Online-only and Offline-only inventory configurations continue to function without any changes.

