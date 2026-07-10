URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000119388737/en

ID: 80395000119388737
# Knowledge Base: Nitro Booking API -- Norwegian Cruise Line (NCL) Combined Fare Codes Enhancement

## Overview

Odysseus has enhanced the Nitro Booking API to correctly identify and
propagate **combinable fare codes** for Norwegian Cruise Line (NCL)
throughout the booking lifecycle.

This enhancement enables clients to understand which fare codes can be
combined with a selected fare, improving pricing accuracy, promotion
handling, and market-specific business rules.

> **Requirement:** Clients must use **NCL API Version 4** to use this
> enhancement.

------------------------------------------------------------------------

# Scope

**Supplier** - Norwegian Cruise Line (NCL)

**Required API Version** - NCL API Version 4

**Availability** - Enabled in Sandbox - Production available upon client
activation

------------------------------------------------------------------------

# Business Purpose

This enhancement allows clients to:

-   Display compatible promotions accurately.
-   Apply business rules using fare compatibility.
-   Support regional pricing models.
-   Preserve fare combinations throughout booking.

------------------------------------------------------------------------

# What are Combinable Fare Codes?

A selected fare may support one or more additional compatible fares.

Example:

``` json
"fareCode": {
  "code": "ALL4CHO2",
  "combinableFares": [
    {
      "code": "34CHO",
      "description": "Taxes Only 3-4"
    },
    {
      "code": "DISC35",
      "description": "NCL Reduce Rate Percentage Off"
    },
    {
      "code": "EASYFARE",
      "description": "Early Booking Fare"
    }
  ]
}
```

These compatible fares should accompany the selected fare throughout the
booking flow.

------------------------------------------------------------------------

# Market-Specific Behavior

## US / Canada / Great Britain

-   FLEXNET fares do **not** automatically include More At Sea (MAS)
    promotions.
-   Customers or agents may choose MAS separately.

## Australia / New Zealand

-   FLEXNET fares automatically include MAS promotions.
-   Combinable fare information reflects this regional behavior.

------------------------------------------------------------------------

# API Flow Impact

## 1. Fare Availability

Response now returns:

-   Selected fare code
-   Compatible fare codes (`combinableFares`)

Clients should retain this information.

------------------------------------------------------------------------

## 2. Category Availability

### Request

Clients must include:

``` json
"fareCodes": [
  {
    "code": "ALL4CHO2",
    "combinableFares": [
      ...
    ]
  }
]
```

Failure to include combinable fares may produce incorrect category
results.

### Response

Returns the selected fare together with compatible fares.

------------------------------------------------------------------------

## 3. Cabin Availability

**No changes**

Existing request and response remain unchanged.

------------------------------------------------------------------------

## 4. Pricing

### Request

Pricing requests should include:

-   Selected fare
-   Combinable fare list

### Response

Pricing preserves combinable fare information.

------------------------------------------------------------------------

## 5. Create Booking

### Request

Booking request must include:

-   Selected fare code
-   All combinable fares returned from previous API calls

### Response

Booking confirmation remains unchanged while preserving fare
compatibility.

------------------------------------------------------------------------

## 6. Read Booking

No request or response changes.

------------------------------------------------------------------------

# Supported APIs

  API                     Change
  ----------------------- --------
  Fare Availability       Yes
  Category Availability   Yes
  Cabin Availability      No
  Pricing                 Yes
  Create Booking          Yes
  Read Booking            No

------------------------------------------------------------------------

# Business Rules

1.  Requires NCL API Version 4.
2.  Combinable fares are supplier-provided compatibility information.
3.  Clients should preserve combinable fares throughout the booking
    flow.
4.  Category, Pricing, and Create Booking requests should include them.
5.  Cabin Availability and Read Booking remain unchanged.
6.  Enhancement is specific to Norwegian Cruise Line.
7.  Existing Royal Caribbean combinable fare functionality is
    unaffected.

------------------------------------------------------------------------

# Client Impact

Clients should:

-   Upgrade to NCL API Version 4.
-   Store combinable fares returned by Fare Availability.
-   Pass combinable fares to downstream APIs.
-   Update UI to display compatible promotions where appropriate.

------------------------------------------------------------------------

# Troubleshooting

### Category pricing appears incorrect

Verify combinable fares were included in the Category request.

### Promotion missing

Ensure:

-   Combinable fares were preserved.
-   Correct market rules are applied.

### Cabin Availability unaffected

Expected. Cabin Availability does not use this enhancement.

### Royal Caribbean behavior changed?

No. This enhancement is limited to Norwegian Cruise Line.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should know:

-   Enhancement requires NCL API Version 4.
-   `combinableFares` identify compatible promotions.
-   Clients should preserve combinable fares across Fare Availability,
    Category, Pricing, and Create Booking.
-   US/CA/GB and AU/NZ have different MAS/FLEXNET behavior.
-   Cabin Availability and Read Booking are unchanged.
-   Royal Caribbean combinable fare logic is separate and unaffected.

------------------------------------------------------------------------

# Search Keywords

NCL, Norwegian Cruise Line, Combined Fare Codes, Combinable Fares, Fare
Availability, Category Availability, Pricing API, Create Booking, NCL
API Version 4, FLEXNET, More At Sea, MAS, EASYFARE, DISC35, Booking API
