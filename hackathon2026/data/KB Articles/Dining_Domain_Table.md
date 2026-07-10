URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000039069001/en

ID: 80395000039069001
# Dining Domain Table

## Overview

The **Dining Domain Table** defines the supported dining seating options
used by the Booking API.

These values provide standardized dining names that can be used when
supplier responses do not include a dining name.

------------------------------------------------------------------------

## Domain Table

  ID   Name
  ---- -----------------------------------
  1    First Seating
  2    Second Seating
  3    Open Seating
  4    Freestyle
  5    Personal Choice
  6    Early First 6:30 PM
  7    Early Seating Lower Level 6:15 PM
  8    Early Seating Upper Level 5:45 PM
  9    Early Second 9:00 PM
  10   Late First 7:30 PM
  11   Late Seating
  12   Late Seating 10:00PM
  13   Late Second Seating
  14   Main Seating
  15   Main Seating Lower Level 8:30PM
  16   Main Seating Upper Level 8:00PM
  17   Main Second Seating
  18   Allocated Onboard
  19   Freedom Dining
  20   Single Seating
  21   Unassigned Seating
  22   Early
  23   Third Seating
  24   My Time Dining
  25   Celebrity Select
  26   Other Dining Selection
  27   Early First
  28   Early Second
  29   8:45 Dining
  30   5:30 PM Dining
  31   8:15 PM
  32   6:30 PM
  33   6:00 PM
  34   5:15 PM
  35   5:45 PM
  36   8:00 PM
  38   Dynamic Dining
  39   Classic Main Seating
  40   Classic Late Seating
  41   Dining by Reservation
  42   Your Time Dining
  43   Anytime Dining
  44   Yacth Club
  45   Flexi Early
  46   Flexi Later
  47   Classic Early Seating
  48   Classic Second Turn
  49   My Choice
  50   Flexi
  53   Open Dining
  55   06:45 PM
  56   04:45 PM
  57   7:45PM
  59   Mid Sitting
  60   First seating - appx 5:30pm
  61   Second seating - appx 7:30pm
  62   Third seating - appx 9:15pm

------------------------------------------------------------------------

# Usage

-   The Booking API may receive dining information directly from the
    supplier.
-   Supplier responses generally include:
    -   `id`
    -   `code`
    -   `name`
    -   `status`
-   If the supplier **does not return a dining name**, applications
    should use this domain table to resolve the appropriate display name
    based on the dining ID.
-   Supplier-specific codes are **not standardized** and should not be
    used as the primary lookup value.

------------------------------------------------------------------------

# Sample Supplier Response

``` json
"dinings": [
  {
    "id": 1,
    "code": "M",
    "name": "05:30 PM",
    "status": 1
  },
  {
    "id": 2,
    "code": "2",
    "name": "08:00 PM",
    "status": 1
  },
  {
    "id": 24,
    "code": "O",
    "name": "MY TIME",
    "status": 1
  }
]
```

------------------------------------------------------------------------

# Field Definitions

  -----------------------------------------------------------------------
  Field                    Description
  ------------------------ ----------------------------------------------
  id                       Internal dining identifier. Can be mapped to
                           the Dining Domain Table.

  code                     Supplier-specific dining code. Values vary by
                           supplier.

  name                     Dining name received from the supplier. If
                           absent, use the domain table mapping.

  status                   Availability status of the dining option.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Validation Rules

-   Always prefer the supplier-provided **name** when available.
-   If **name** is missing or empty, resolve it using the Dining Domain
    Table based on **id**.
-   Do not assume supplier **code** values are consistent across
    suppliers.
-   The **id** provides the canonical mapping to the domain table.

------------------------------------------------------------------------

# Common Questions

## When should this table be used?

When a supplier response omits the dining name.

## Should applications rely on the supplier code?

No. Supplier codes are supplier-specific and are not guaranteed to be
consistent.

## Which value is considered authoritative?

The supplier-provided **name** is authoritative. If unavailable, use the
domain table.

------------------------------------------------------------------------

# Related Knowledge

-   Dining API Response
-   Booking Response Schema
-   Supplier Profile Matrix
-   Domain Tables
