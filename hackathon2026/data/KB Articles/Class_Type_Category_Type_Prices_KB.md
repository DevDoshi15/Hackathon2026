URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000033205299/en

ID: 80395000033205299
# Knowledge Base: Class Type / Category Type Prices

## Overview

The **Class Type / Category Type Price** identifier is used throughout
the Booking API to classify individual price components returned in
pricing and booking responses.

Rather than relying on descriptive text alone, the API returns a numeric
**Price Type ID**. Applications should map these IDs to their
corresponding business meaning.

This mapping enables client applications, support teams, QA engineers,
and API consumers to correctly interpret cruise pricing responses.

------------------------------------------------------------------------

# Price Type Mapping

  -----------------------------------------------------------------------
  ID        Price Type                    Description
  --------- ----------------------------- -------------------------------
  0         Unknown Price Type            Default or unidentified price
                                          component.

  1         Cruise Fare                   Base cruise fare charged by the
                                          cruise line.

  2         Port Charges                  Charges imposed by
                                          embarkation/disembarkation
                                          ports.

  3         Taxes and Fees                Government taxes, regulatory
                                          fees, and mandatory taxes.

  4         Brochure Fare / Strike        Published brochure price or
            Through Fare                  original price displayed before
                                          discounts.

  7         Air Fare                      Airfare associated with the
                                          cruise package.

  8         Air Tax                       Taxes applicable to airfare.

  11        Double Occupancy Amount       Pricing based on double
                                          occupancy.

  14        Prepaid Gratuities            Mandatory or optional prepaid
                                          gratuities.

  41        Pre/Post Cruise Cruise Line   Cruise line supplied hotel,
            Packages                      land, or transfer packages
                                          before or after the cruise.

  44        Site / System Discount from   Discount applied automatically
            Rules                         by Odysseus pricing/business
                                          rules.

  48        Site / System Markup from     Markup applied automatically by
            Rules                         Odysseus pricing/business
                                          rules.

  59        Air Credit                    Credit applied when airfare is
                                          removed or credited.

  61        Agent Commission from Rules   Agent commission calculated
                                          using configured business
                                          rules.

  98        Supplier Commission from      Commission returned or
            Rules                         calculated from
                                          supplier-specific rules.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Business Usage

These identifiers are commonly used to:

-   Break down total cruise pricing.
-   Display pricing components in booking UI.
-   Calculate totals.
-   Differentiate base fare from taxes and optional charges.
-   Determine discounts, markups, and commissions.
-   Support financial reporting.

------------------------------------------------------------------------

# Pricing Categories

## Base Cruise Pricing

-   Cruise Fare (1)
-   Brochure Fare (4)
-   Double Occupancy Amount (11)

## Taxes & Mandatory Charges

-   Port Charges (2)
-   Taxes and Fees (3)
-   Air Tax (8)
-   Prepaid Gratuities (14)

## Air Components

-   Air Fare (7)
-   Air Credit (59)

## Discounts & Adjustments

-   Site/System Discount (44)
-   Site/System Markup (48)

## Commission

-   Agent Commission (61)
-   Supplier Commission (98)

------------------------------------------------------------------------

# Implementation Notes

-   Price Type IDs are stable numeric identifiers.
-   Client applications should map IDs instead of hardcoding display
    text.
-   Multiple price types may be returned within a single pricing
    response.
-   Unknown or future values should be handled gracefully.

------------------------------------------------------------------------

# Example Mapping

``` text
1  -> Cruise Fare
2  -> Port Charges
3  -> Taxes and Fees
44 -> Site/System Discount
48 -> Site/System Markup
61 -> Agent Commission
98 -> Supplier Commission
```

------------------------------------------------------------------------

# Agent Knowledge

When answering pricing questions:

-   Explain each returned Price Type ID.
-   Differentiate mandatory charges from optional components.
-   Distinguish discounts from markups.
-   Explain that commissions are informational and typically not
    customer-facing.
-   Identify unknown IDs as unmapped price types requiring validation.

------------------------------------------------------------------------

# Search Keywords

Class Type, Category Type, Price Type, Cruise Fare, Port Charges, Taxes,
Air Fare, Air Tax, Strike Through Fare, Discount, Markup, Commission,
Pricing Breakdown, Booking API
