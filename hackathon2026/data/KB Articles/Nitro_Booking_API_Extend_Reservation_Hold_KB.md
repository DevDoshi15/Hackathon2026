URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000054829021/en

ID: 80395000054829021
# Knowledge Base: Nitro / Booking API -- Extend Reservation Hold

## Overview

The **Extend Hold** feature allows a client to request an extension of
the first payment due date on an existing cruise reservation.

**Endpoint**

    POST /v2/reservation/cruise/ExtendHold

The actual extension period is determined by the cruise line. Odysseus
forwards the request but does not control the number of additional days
granted.

------------------------------------------------------------------------

# Scope

-   API: Extend Hold
-   Endpoint: `/v2/reservation/cruise/ExtendHold`
-   Purpose: Extend the first payment due date on a held reservation.

------------------------------------------------------------------------

# Prerequisites

Before calling **Extend Hold**, the following conditions must be met:

1.  The reservation **must be in Held status**.
2.  A **ReadBookingFromSupplier** request is mandatory.
3.  The Read Booking request must use:

``` json
"readPreferences": {
  "mode": "View"
}
```

4.  The Read Booking response must contain:
    -   `supplierSyncInfo`
    -   `apiSyncInfo`

Both values are required in the Extend Hold request.

------------------------------------------------------------------------

# Workflow

## Step 1 -- Read Booking from Supplier

Call **ReadBookingFromSupplier**.

Purpose:

-   Retrieve the latest booking state.
-   Obtain the current payment due date.
-   Retrieve synchronization tokens.

The response includes:

-   Payment schedule
-   Current payment due date
-   `supplierSyncInfo`
-   `apiSyncInfo`

Example:

Current payment due date:

    05-Aug-2025

------------------------------------------------------------------------

## Step 2 -- Submit Extend Hold

Call:

    POST /v2/reservation/cruise/ExtendHold

The request **must include**:

-   `supplierSyncInfo`
-   `apiSyncInfo`

These fields are mandatory for all supported cruise lines.

------------------------------------------------------------------------

## Step 3 -- Verify Success

Execute **ReadBookingFromSupplier** again.

Verify that the payment schedule reflects the new due date.

Example:

Previous due date:

    05-Aug-2025

Updated due date:

    06-Aug-2025

The exact extension length depends on the cruise line.

------------------------------------------------------------------------

# Business Rules

  Rule                      Requirement
  ------------------------- ------------------------------
  Reservation status        Must be Held
  ReadBookingFromSupplier   Mandatory before Extend Hold
  Read mode                 `View`
  supplierSyncInfo          Mandatory
  apiSyncInfo               Mandatory
  Extension duration        Determined by cruise line

------------------------------------------------------------------------

# Extend Hold Not Supported

Some suppliers do not support Extend Hold.

Example:

**Royal Caribbean (RCCL)**

-   Extend Hold request returns an error.
-   Hold extension is not performed.

Always verify supplier support using the **Cruise Profile Matrix --
Cruise Line / API Features Supported**.

------------------------------------------------------------------------

# Supported Cruise Lines

The following suppliers currently support Extend Hold:

-   MSC Cruises
-   Carnival Cruise Line
-   Princess Cruises
-   Cunard Cruise Line
-   Holland America Line
-   Seabourn Cruise Line

------------------------------------------------------------------------

# Recommended Client Flow

1.  Read Booking from Supplier (`mode = View`).
2.  Extract `supplierSyncInfo`.
3.  Extract `apiSyncInfo`.
4.  Confirm reservation is in Held status.
5.  Call Extend Hold.
6.  Execute Read Booking again.
7.  Verify updated payment due date.

------------------------------------------------------------------------

# Troubleshooting

### Extend Hold fails

Check:

-   Reservation is still Held.
-   Read Booking was executed immediately beforehand.
-   `supplierSyncInfo` is present.
-   `apiSyncInfo` is present.

### Payment due date unchanged

Possible causes:

-   Supplier denied extension.
-   Supplier does not support Extend Hold.
-   Maximum extension already reached.
-   Read Booking not refreshed after the request.

### RCCL returns an error

Expected behavior. Royal Caribbean does not support Extend Hold.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should know:

-   Extend Hold only works on Held reservations.
-   ReadBookingFromSupplier is always required before Extend Hold.
-   `readPreferences.mode` must be `View`.
-   Both `supplierSyncInfo` and `apiSyncInfo` are mandatory.
-   Extension duration is controlled by the supplier.
-   Success should be verified with another Read Booking request.
-   Not every cruise line supports Extend Hold.

------------------------------------------------------------------------

# Search Keywords

Extend Hold, Extend Reservation Hold, Extend Booking Hold,
ReadBookingFromSupplier, supplierSyncInfo, apiSyncInfo, Held
Reservation, Payment Due Date, Read Preferences View, Cruise Profile
Matrix, Nitro Booking API
