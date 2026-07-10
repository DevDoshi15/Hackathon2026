URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000066089001/en

ID: 80395000066089001
# Knowledge Base: Guest / Customer Titles

## Overview

Odysseus supports a standard set of guest/customer titles across all
cruise suppliers. These standardized titles provide a consistent API
interface while Odysseus automatically translates them to the
supplier-specific title codes required by each cruise line.

This allows clients to use a single set of title codes regardless of
supplier implementation.

------------------------------------------------------------------------

# Scope

-   Booking API
-   Create Booking
-   Modify Booking
-   Read Booking
-   All supported cruise suppliers

------------------------------------------------------------------------

# Supported Standard Titles

  Title   Description   Category         Gender
  ------- ------------- ---------------- ---------
  MR      Mister        Adult            Male
  MRS     Missus        Adult            Female
  MS      Ms.           Adult            Female
  DOC     Doctor        Adult            Neutral
  MST     Master        Child / Infant   Male
  MIS     Miss          Child / Infant   Female

------------------------------------------------------------------------

# Translation Behavior

Odysseus manages title translation between the Booking API and each
cruise line.

Client Request → Odysseus Standard Title → Supplier-Specific Title →
Cruise Line

Similarly, when reading bookings:

Cruise Line Title → Odysseus Translation → Standard API Title

Clients do **not** need to know supplier-specific title codes.

------------------------------------------------------------------------

# Unknown Titles

If Odysseus receives a title that is **not** part of the standard
supported list, it does **not** perform validation or translation.

Instead, the title is passed directly to the supplier.

Example:

``` text
PROF
```

Processing flow:

Client → PROF → Odysseus → PROF → Cruise Line

If the supplier supports the title, processing succeeds.

If the supplier does not support the title, the supplier returns an
error.

------------------------------------------------------------------------

# Business Rules

1.  Standard titles are translated automatically.
2.  Translation is supplier-specific and managed internally by Odysseus.
3.  Unknown titles are forwarded unchanged.
4.  Odysseus does not validate unsupported title values.
5.  Supplier validation determines whether unknown titles are accepted.

------------------------------------------------------------------------

# API Impact

## Create Booking

-   Standard titles are translated.
-   Unknown titles are forwarded unchanged.

## Modify Booking

-   Same behavior as Create Booking.

## Read Booking

-   Supplier titles are translated back to Odysseus standard titles
    whenever a mapping exists.
-   Unmapped titles are returned as received.

------------------------------------------------------------------------

# Client Recommendations

-   Prefer the standard supported title codes.
-   Only use custom titles if the target supplier explicitly supports
    them.
-   Be prepared to handle supplier validation errors for unsupported
    custom titles.

------------------------------------------------------------------------

# Troubleshooting

### Booking rejected because of title

Verify that: - A standard Odysseus title is used, or - The supplier
supports the custom title.

### PROF not working

Expected behavior if the supplier does not recognize the title. Odysseus
forwards it without validation.

### Different suppliers use different title codes

Expected. Odysseus handles translation internally.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should know:

-   Odysseus exposes six standard title codes.
-   Supplier-specific mappings are handled automatically.
-   Unknown titles are not validated.
-   Unsupported custom titles may generate supplier errors.
-   Clients should prefer the standard title list.

------------------------------------------------------------------------

# Search Keywords

Guest Titles, Customer Titles, Title Mapping, MR, MRS, MS, DOC, MST,
MIS, Create Booking, Modify Booking, Read Booking, Passenger Title,
Booking API
