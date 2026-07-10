URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000033205299/en

ID : 80395000033205299
# Rate / Fare Code Type Domain Table

## Overview

The **Rate / Fare Code Type** domain table defines the supported fare
categories used throughout the Booking API.

These values are referenced when a supplier, booking profile, or pricing
rule requires a specific fare classification.

The API expects the **Code** value rather than the display name.

------------------------------------------------------------------------

## Domain Table

  ID   Name                 Code
  ---- -------------------- ------
  0    No Restriction       NO
  1    Senior               SR
  2    Military             ML
  3    Police               PL
  4    Union                UN
  5    Teacher              TE
  6    AARP                 AA
  7    Interline            IL
  8    Residential          RE
  9    FireFighter          PF
  10   Past Passenger       PP
  11   Friends and Family   FF
  12   Net Rate             NE
  13   Agent Fare           AF
  16   Member Fare          MF

------------------------------------------------------------------------

# Field Definitions

## ID

Internal numeric identifier representing the fare code type.

## Name

Human-readable description of the fare category.

## Code

The abbreviated value expected by integrations and business rules.

------------------------------------------------------------------------

# Fare Code Descriptions

  Code   Description
  ------ --------------------
  NO     No Restriction
  SR     Senior
  ML     Military
  PL     Police
  UN     Union
  TE     Teacher
  AA     AARP
  IL     Interline
  RE     Residential
  PF     FireFighter
  PP     Past Passenger
  FF     Friends and Family
  NE     Net Rate
  AF     Agent Fare
  MF     Member Fare

------------------------------------------------------------------------

# Usage Notes

-   The Booking API generally expects the **Code** value rather than the
    display name.
-   Suppliers may support only a subset of these fare code types.
-   Supplier-specific profile matrices determine which fare codes are
    valid.
-   Validation should ensure only supported fare codes are submitted.

------------------------------------------------------------------------

# Example

``` json
{
  "fareCodeType": "SR"
}
```

This indicates that the booking should use the **Senior** fare category.

------------------------------------------------------------------------

# Common Questions

## What value should be sent in API requests?

Use the **Code** value (for example, `SR`), not the display name
(`Senior`).

## Can every supplier use every fare code?

No. Supplier profile matrices determine which fare code types are
supported.

## Is the numeric ID sent in API requests?

Generally no. The API typically uses the **Code** value.

------------------------------------------------------------------------

# Related Knowledge

-   Supplier Profile Matrix
-   Booking Request Schema
-   Pricing Rules
-   Fare Code Validation
