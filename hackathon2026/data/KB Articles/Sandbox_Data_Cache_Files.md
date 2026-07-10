URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000040396001/en/Article

ID: 80395000040396001

---

title: Sandbox Data Cache Files
category: Knowledge Base
product: Nitro Booking API
version: 1.0
last\_updated: 2026-07-10
tags:

* Sandbox
* Data Cache
* Nitro Booking API
* Development
* Certification

\---

# Sandbox Data Cache Files

## Overview

This article provides access to data cache files generated from the **Sandbox** environment for the Nitro Booking API. These files are intended for development, integration testing, and certification activities.

## Access

**SharePoint Folder**

https://odysseus.sharepoint.com/:f:/s/OdyShared/IgAIhQcMjyZiRJSxsmimB8q3ARCTyWYedMTL\_BotnlZj3nU?e=ap5v73

### Access Credentials

**Password**

`q$mf7$#7hLYRYLS#`

## File Contents

The Sandbox cache package contains:

* Currency data
* Sandbox sailings
* Sandbox itineraries
* Pricing cache files
* Master cache files

These files are intended for:

* API development
* Integration testing
* Client certification
* Functional validation

## Environment Differences

The cache file format is identical to the Production environment.

### Common Across Environments

* Master files
* File structure
* JSON schema

### Environment-Specific Files

The following files differ between Sandbox and Production:

* Sailing files
* Pricing files

These files are generated using Sandbox environment data.

## Additional Reference

A **JSON Cache File Definition** document accompanies the cache files and should be used as the reference for the cache structure and schema.

## Important Notes

> \*\*Site Preference Configuration\*\*
>
> - \*\*USD\*\* cache files were generated with the Site Preference value set to \*\*1 (Inclusive of Taxes)\*\*.
> - \*\*CAD\*\* and \*\*AUD\*\* cache files were generated with the Site Preference value set to \*\*0 (Exclusive of Taxes)\*\*.

Consumers should consider this configuration when validating pricing data across different currencies.

## Intended Usage

Use the Sandbox cache files for:

* Local development
* API integration
* Automated testing
* QA validation
* Certification against the Nitro Booking API

Do not use Sandbox data for production integrations.

