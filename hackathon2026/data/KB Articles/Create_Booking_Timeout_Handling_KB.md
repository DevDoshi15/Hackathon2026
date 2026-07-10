URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000067235021/en

ID:80395000067235021
# Knowledge Base: Create Booking Timeout Handling

## Overview

Booking creation with cruise line suppliers is an asynchronous process.
Occasionally, the supplier may take longer than expected to respond,
resulting in a timeout at the API level even though the booking may have
been successfully created.

Odysseus implements background monitoring and recovery logic to
determine the final booking outcome and minimize duplicate bookings.

------------------------------------------------------------------------

# Scope

-   API: Create Booking
-   Applies to: Cruise suppliers where booking creation may exceed
    normal response times
-   Purpose: Timeout handling, booking recovery, and duplicate booking
    prevention

------------------------------------------------------------------------

# Timeout Behavior

## Supplier Response Window

Odysseus waits approximately **60--90 seconds** for a response from the
cruise line.

If no response is received within this window:

-   The client may receive a timeout.
-   The booking request is **not immediately considered failed**.
-   Odysseus continues processing the request in the background.

> A timeout does **not** necessarily mean the booking failed.

------------------------------------------------------------------------

# Background Processing

After the initial timeout:

1.  Odysseus continues waiting for the supplier response.
2.  After approximately **3 additional minutes**, an automated
    monitoring process starts.
3.  The monitor checks whether the booking was successfully created with
    the supplier.
4.  If found, Odysseus updates the booking record.

------------------------------------------------------------------------

# Booking Recovery

If no confirmation number is available:

1.  Search the supplier using:
    -   Sailing information
    -   Guest information
2.  If a matching booking is found:
    -   Import supplier booking details.
    -   Update Odysseus booking.
    -   Store supplier confirmation number.

------------------------------------------------------------------------

# Create Booking API Response During Timeout

When a timeout occurs, the Create Booking API should return:

-   `IsSucceed = true`
-   `StatusId = 12`
-   Booking Status = **Pending Confirmation**
-   No `ReservationReference`
-   No `ConfirmationNumber`

This indicates that booking processing is still underway.

------------------------------------------------------------------------

# Pending Confirmation Status

  Field                  Value
  ---------------------- ----------------------
  Status                 Pending Confirmation
  StatusId               12
  IsSucceed              true
  ReservationReference   Not available
  ConfirmationNumber     Not available

------------------------------------------------------------------------

# Recommended Client Actions

## 1. Do NOT Submit Another Booking

Avoid creating duplicate bookings while confirmation is pending.

Inform the customer that the booking is being verified.

------------------------------------------------------------------------

## 2. Wait Five Minutes

Allow background monitoring sufficient time to complete.

------------------------------------------------------------------------

## 3. Execute ReadFromSupplier

After approximately **5 minutes**, call **ReadFromSupplier**.

Expected outcome:

-   Supplier confirmation number
-   Reservation details
-   Updated booking status

------------------------------------------------------------------------

## 4. Search Supplier (If Needed)

If ReadFromSupplier cannot locate the booking:

Search using guest information.

Example:

``` json
{
  "supplierId": 6,
  "pos": {
    "currency": "USD"
  },
  "SearchPreferences": {
    "CustomerFirstName": "John",
    "CustomerLastName": "Doe"
  }
}
```

The search may return one or more bookings.

Validate:

-   Guest information
-   Sailing/voyage
-   Reservation details

Once the correct booking is identified, execute ReadFromSupplier using
the supplier confirmation number to import the booking.

------------------------------------------------------------------------

# End-to-End Flow

1.  Client submits Create Booking.
2.  Supplier does not respond within 60--90 seconds.
3.  Client receives Pending Confirmation response.
4.  Odysseus continues waiting.
5.  Background monitor runs after \~3 minutes.
6.  Booking is searched and recovered if necessary.
7.  Client waits \~5 minutes.
8.  Client calls ReadFromSupplier.
9.  Booking confirmation is returned if available.

------------------------------------------------------------------------

# Troubleshooting

### Timeout received

This does not necessarily indicate failure.

### Pending Confirmation persists

-   Wait at least 5 minutes.
-   Execute ReadFromSupplier.

### Booking not found

-   Perform Supplier Search using guest details.
-   Verify voyage and guest data.
-   Import the booking via ReadFromSupplier if located.

### Duplicate bookings

Never resubmit immediately after a timeout.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should understand:

-   Timeouts are often temporary communication delays.
-   A timeout does not mean booking creation failed.
-   Pending Confirmation (StatusId 12) is an expected intermediate
    state.
-   Background monitoring attempts automatic recovery.
-   ReadFromSupplier is the preferred follow-up after five minutes.
-   Supplier Search is the fallback when no confirmation is available.
-   Prevent duplicate bookings by avoiding immediate retries.

------------------------------------------------------------------------

# Search Keywords

Create Booking, Timeout, Pending Confirmation, StatusId 12,
ReadFromSupplier, Supplier Search, Booking Recovery, Confirmation
Number, ReservationReference, Cruise Booking Timeout, Duplicate Booking
Prevention
