URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000033205053/en 

ID: 80395000033205053

# Odysseus NITRO Booking API Knowledge Base Blueprint

> **Purpose:** This document defines the recommended structure for the AI Agent Knowledge Base. It is designed for Retrieval-Augmented Generation (RAG), enabling the agent to answer technical, business, troubleshooting, and onboarding questions about the Odysseus NITRO Booking API.

---

# Knowledge Base Structure

```
Knowledge Base
│
├── 01 Getting Started
├── 02 Booking Flow
├── 03 API Reference
├── 04 Business Rules
├── 05 Troubleshooting
├── 06 Concepts & Domain Knowledge
├── 07 Supplier Guides
├── 08 FAQ
└── 09 Release Notes
```

---

# Standard Template (Use for Every Article)

```md
---
title:
category:
endpoint:
supplier:
tags:
depends_on:
used_by:
last_updated:
---

# Overview

## Purpose

## When to Use

## Request

## Important Fields

## Response

## Business Rules

## Dependencies

## Common Errors

## Troubleshooting

## Examples

## Related APIs

## FAQ

## Notes
```

---

# Category 1 – Getting Started

Create separate articles for:

- Introduction to Nitro Booking API
- Shopping API vs Transaction API
- Authentication
- Sandbox vs Production
- IP Whitelisting
- ClientId / ClientSecret
- Generate Token
- Refresh Token
- Domain Tables
- Static Content License

---

# Category 2 – Booking Flow

Document every step individually.

1. Cruise Search
2. Fare Availability
3. Category Availability
4. Cabin Availability
5. Cabin Details
6. Cabin Hold
7. Price Booking
8. Create Booking
9. Cancel Booking
10. Special Services

For each API explain:

- Why it exists
- Input
- Output
- Required fields
- Next API in workflow
- Common failures

---

# Category 3 – API Reference

Each endpoint should have its own article.

Include:

- HTTP Method
- Endpoint
- Authentication
- Headers
- Request Schema
- Response Schema
- Required Fields
- Optional Fields
- Examples
- Dependencies

---

# Category 4 – Business Rules

Examples:

- Profile Matrix
- Supplier-specific requirements
- Mandatory vs Optional fields
- Fare Code rules
- Category rules
- Cabin rules
- Pricing rules
- Booking validation rules
- Currency behavior
- Exchange rate handling

---

# Category 5 – Troubleshooting

One article per error.

Template:

- Error message
- Meaning
- Root cause
- Resolution
- Example
- Related APIs

Examples:

- OfficeId / API Setup Missing
- Invalid FareCode
- Cabin Unavailable
- Authentication Failed
- PackageId Not Found
- Invalid Category
- Token Expired

---

# Category 6 – Concepts

Create standalone articles for important concepts.

Examples:

- PackageId
- PackageTourId
- ItineraryId
- FareCode
- CategoryCode
- CabinNumber
- Guest
- BookingId
- OfficeId
- Profile Matrix
- Shopping API
- Transaction API

Each article should answer:

- What is it?
- Where is it generated?
- Which APIs use it?
- Common mistakes
- Example values

---

# Category 7 – Supplier Guides

One guide per supplier.

Example sections:

- Supported APIs
- Required fields
- Known limitations
- Common booking failures
- Best practices
- Sample payloads

---

# Category 8 – FAQ

Examples:

- Can Category Availability be skipped?
- Why did Cabin Hold fail?
- Why are Sandbox prices different?
- Can Sandbox create bookings?
- Why is my FareCode invalid?
- Which APIs require PackageId?

---

# Metadata Recommendations

Include metadata in every article.

```yaml
title:
category:
endpoint:
supplier:
tags:
depends_on:
used_by:
last_updated:
```

---

# Cross References

End every article with:

- Related APIs
- Related Concepts
- Related Errors
- Related Supplier Guides

---

# High-Priority Knowledge (Tribal Knowledge)

Capture knowledge that typically exists only in engineers' heads:

- Supplier quirks (e.g. RCCL fare code behavior)
- Sandbox limitations
- Production vs Sandbox differences
- Common client integration mistakes
- Frequent support ticket resolutions
- Semantic payload mismatches
- Profile Matrix rules
- Supplier capability differences

---

# AI Agent Goals

The knowledge base should enable the agent to:

- Explain APIs in plain English
- Build valid request payloads
- Diagnose booking failures
- Identify missing or invalid fields
- Explain business rules
- Recommend next API calls
- Guide onboarding clients
- Assist Support, QA, Developers, and Clients
- Reduce engineering escalations
