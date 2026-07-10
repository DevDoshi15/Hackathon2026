URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000117427642/en

ID: 80395000117427642
# Knowledge Base: Instant Confirm Bookings -- How to Identify and Book

## Overview

Most cruise lines allow bookings to be created without immediate
payment. However, certain sailings require **instant confirmation**,
meaning payment is mandatory at the time of booking.

This article explains how the Nitro Booking API exposes or handles
instant confirmation requirements for supported cruise lines and how
clients should respond.

------------------------------------------------------------------------

# Scope

**Suppliers**

-   MSC Cruises
-   Costa Cruises
-   AMA Waterways (supports instant confirm concept; supplier-specific
    behavior may vary)

**Impacted APIs**

-   ListFareCodes
-   ListCategories
-   Create Reservation (Create Booking)

------------------------------------------------------------------------

# What is an Instant Confirm Booking?

An **Instant Confirm Booking** is a sailing where payment is required
immediately during booking.

If payment is not provided:

-   Some suppliers create only a quote.
-   Others reject the booking entirely.

Behavior depends on the supplier.

------------------------------------------------------------------------

# MSC Cruises

## Identifying Mandatory Payment

MSC is currently the only supplier that exposes an API indicator before
booking.

The `ListFareCodes` and `ListCategories` responses may contain:

``` json
"reservationIndicators": {
  "mandatoryIndicators": [
    {
      "type": "Payment",
      "value": true
    }
  ]
}
```

### Interpretation

  Indicator             Meaning
  --------------------- ----------------------------------------
  `"type": "Payment"`   Payment requirement indicator
  `"value": true`       Payment is mandatory (Instant Confirm)

------------------------------------------------------------------------

## Booking Behavior

### Payment Not Required

-   Booking can be created without payment.
-   Cabin is held.
-   Booking is confirmed normally.

### Payment Required and Payment Not Sent

MSC still creates a record, but:

-   Booking is saved as a **Quote**.
-   Selected cabin is released.
-   A **Guarantee (GUA)** cabin is assigned.
-   Booking is **not considered confirmed** by MSC.

### Business Impact

Although a booking record exists, the cruise line does **not** recognize
it as a confirmed reservation until payment requirements are satisfied.

------------------------------------------------------------------------

# Costa Cruises

## Identification

Costa **does not** provide an advance indicator showing whether payment
is mandatory.

Clients cannot determine instant confirmation requirements before Create
Booking.

------------------------------------------------------------------------

## Booking Behavior

If payment is required but omitted:

-   Booking request fails.
-   No confirmed booking is created.

### Example Error

**Error Code**

    5438

**Messages**

    No option allowed. Payment required. Immediate conf. needed

or

    No option is allowed. Immediate confirmation needed

------------------------------------------------------------------------

# AMA Waterways

AMA Waterways supports instant confirmation scenarios. The
supplier-specific mechanism for determining payment requirements may
differ. Clients should follow supplier-specific booking rules where
applicable.

------------------------------------------------------------------------

# Supplier Comparison

  ------------------------------------------------------------------------
  Supplier      Upfront Indicator         Booking Without Payment
  ------------- ------------------------- --------------------------------
  MSC           Yes                       Quote created; cabin released;
                (`mandatoryIndicators`)   GUA assigned

  Costa         No                        Booking fails with error 5438

  AMA Waterways Supplier-specific         Follow supplier rules
  ------------------------------------------------------------------------

------------------------------------------------------------------------

# Recommended Client Flow

1.  Retrieve fare/category information.
2.  For MSC, inspect `reservationIndicators.mandatoryIndicators`.
3.  If payment is mandatory:
    -   Collect payment before Create Booking.
4.  Submit Create Reservation.
5.  Handle supplier-specific outcomes.

------------------------------------------------------------------------

# Troubleshooting

### MSC booking created but cabin changed

Likely cause: - Mandatory payment sailing booked without payment. -
Original cabin released and replaced with a GUA cabin.

### Costa booking failed

Verify: - Whether the sailing requires immediate confirmation. - Payment
information was included.

### No payment indicator returned

Only MSC currently provides an upfront payment indicator.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should know:

-   Instant Confirm means payment is mandatory during booking.
-   MSC exposes a payment indicator before booking.
-   Costa does not expose an advance indicator.
-   MSC creates a quote without payment on mandatory-payment sailings.
-   Costa rejects bookings without required payment (error 5438).
-   GUA (Guarantee) cabins indicate the originally selected cabin was
    released.

------------------------------------------------------------------------

# Search Keywords

Instant Confirm, Mandatory Payment, MSC, Costa, AMA Waterways,
reservationIndicators, mandatoryIndicators, Payment Indicator, Quote
Booking, GUA Cabin, Error 5438, Immediate Confirmation, Create
Reservation, Nitro Booking API
