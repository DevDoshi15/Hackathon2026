URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000133246452/en/Article

ID: 80395000133246452

---

title: Special Service Information Consistency Update
category: Release Advisory
version: 1.0
last\_updated: 2026-07-10
tags:

* Special Services
* Booking API
* Response Enhancement

\---

# Special Service Information Consistency Update

## Overview

The Booking API has been enhanced to standardize how **Special Service** information is returned across API responses.

This update provides clearer service descriptions and improves consistency throughout the booking workflow.

## What's New

Special Service responses now return a meaningful **description** for each service instead of a generic value.

### Affected Cruise Lines

* Carnival
* Princess
* Cunard
* Holland America
* Seabourn
* P\&O
* Disney
* Virgin Voyages
* Explora

## Availability

|Environment|Availability|
|-|-|
|Sandbox \& Production|Carnival and Polar brands – March 2026 release|
|Sandbox \& Production|Disney and Virgin Voyages – After April 2026 release|

> \*\*Production Enablement:\*\* Open a support ticket to have this feature enabled in Production.

## Response Changes

### Before

```json
{
  "code":"MED\_3",
  "description":"MED",
  "type":"COGNITIVEDISABILITIES",
  "group":"Medical",
  "status":1
}
```

### After

```json
{
  "code":"MED\_3",
  "description":"COGNITIVE DISABILITIES",
  "type":"COGNITIVEDISABILITIES",
  "group":"Medical",
  "status":1
}
```

## Benefits

* Consistent Special Service descriptions
* Improved readability
* Better UI presentation
* Consistent data across booking APIs

## Notes

* No changes to **PPGR (Prepaid Gratuities)** services.
* No changes to **Complimentary Upgrade** services.
* Existing response schema remains unchanged; only the `description` value has been enhanced.

## Compatibility

This enhancement is backward compatible. Consumers can continue using existing integrations while benefiting from improved descriptions.

