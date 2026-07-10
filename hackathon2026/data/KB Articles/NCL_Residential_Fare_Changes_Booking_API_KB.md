URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000111380420/en

ID: 80395000111380420
# Knowledge Base: NCL Residential Fare Changes - Booking API

## Overview

Norwegian Cruise Line (NCL) updated the way **Resident Fare** discounts
are determined.

Previously, a **Past Guest Number** was required to qualify for resident
fare discounts. Effective after the July 1 update, this is no longer
required.

Odysseus Booking API supports this supplier change with **no client-side
integration changes**, other than removing the requirement to supply a
past guest number when retrieving resident fares.

------------------------------------------------------------------------

# Scope

**Supplier** - Norwegian Cruise Line (NCL)

**Applies To** - Booking API - Fare Availability - Resident Fare Pricing

**Markets** - United States (US) - Canada (CA)

------------------------------------------------------------------------

# Previous Behavior

To receive Resident Fare pricing:

-   A valid US/Canadian resident state had to be supplied.
-   A Past Guest Number was also required.
-   Without the Past Guest Number, resident fare discounts were not
    returned.

------------------------------------------------------------------------

# New Behavior

## 1. Past Guest Number No Longer Required

Resident fare discounts are now available **without** providing a Past
Guest Number.

Clients should no longer treat the Past Guest Number as mandatory when
searching for resident fares.

------------------------------------------------------------------------

## 2. Resident Fare Returned Based on State

Resident fare pricing and resident fare codes are returned whenever a
**valid state/province** is supplied.

For API clients, the state must be included in the booking/pricing
request.

Requirements: - Valid US state or Canadian province - No Past Guest
Number required

------------------------------------------------------------------------

## 3. State vs Past Guest Number Precedence

If both are provided:

-   User supplies a state code.
-   User supplies a Past Guest Number.

NCL ignores the user-supplied state.

Instead, NCL uses the **state associated with the customer's profile**
linked to the Past Guest Number.

Priority:

1.  Customer profile state (linked to Past Guest Number)
2.  User supplied state (ignored)

------------------------------------------------------------------------

# Business Rules

  -----------------------------------------------------------------------
  Scenario                                Result
  --------------------------------------- -------------------------------
  Valid state only                        Resident fare returned

  Past Guest Number only                  Uses resident state from
                                          customer profile

  Valid state + Past Guest Number         Customer profile state
                                          overrides request state

  Invalid or unsupported state            Resident fare not returned
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Client Impact

No API contract changes are required.

Clients should:

-   Stop requiring Past Guest Number for resident fares.
-   Continue sending a valid residency state.
-   Expect resident pricing whenever eligibility requirements are met.

------------------------------------------------------------------------

# Fare Availability

Odysseus has upgraded the Fare Availability messaging from:

-   V3 → V4

This change has **no functional impact** to API consumers.

------------------------------------------------------------------------

# Important Notes

-   Applies only to US and Canadian markets.
-   Past Guest Number is now optional for resident fare eligibility.
-   When both state and Past Guest Number are provided, the customer
    profile takes precedence.
-   Existing integrations continue to work.

------------------------------------------------------------------------

# Troubleshooting

### Resident fare not returned

Verify:

-   Valid US/Canadian state supplied.
-   State is eligible for resident fares.
-   If Past Guest Number is present, verify the customer's stored state.
-   Remember that profile state overrides request state.

### Incorrect resident pricing

Check whether:

-   A Past Guest Number was sent.
-   The stored customer profile contains a different state than the
    request.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should know:

-   Resident fares no longer require a Past Guest Number.
-   Valid residency state is sufficient.
-   Customer profile state overrides request state whenever a Past Guest
    Number is supplied.
-   Applies only to US and Canada.
-   Fare Availability V4 upgrade has no customer-facing impact.

------------------------------------------------------------------------

# Search Keywords

NCL, Norwegian Cruise Line, Resident Fare, Residential Fare, Past Guest
Number, Resident Discount, State Code, Fare Availability V4, Booking
API, US Resident Fare, Canada Resident Fare
