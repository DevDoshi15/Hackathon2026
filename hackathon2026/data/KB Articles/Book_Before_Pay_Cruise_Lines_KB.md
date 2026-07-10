URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000129667704/en

ID: 80395000129667704
# Knowledge Base: Book Before Pay Cruise Lines (Nitro Booking API)

## Overview

Some cruise lines use third-party payment providers to process credit
card payments. Because these providers require a valid booking reference
before a payment can be associated with the reservation, **the booking
must be created before any payment is submitted**.

For these cruise lines, attempting to include payment information during
the Create Booking request does **not** process the payment.

------------------------------------------------------------------------

# Business Background

Unlike most suppliers where payment can be included during booking
creation, these cruise lines require the following sequence:

1.  Create Booking
2.  Receive Booking Reference
3.  Submit payment using a subsequent Modify Booking / Apply Payment
    flow

The booking reference is required by the external payment provider to
notify the cruise line that payment has been completed.

------------------------------------------------------------------------

# Cruise Lines Requiring Book Before Pay

The following suppliers currently require this behavior:

  Cruise Line
  ---------------------
  Azamara
  Explora Journeys
  Four Seasons Yachts
  Virgin Voyages
  Windstar Cruises

------------------------------------------------------------------------

# Booking Flow

## Step 1 --- Create Booking

Submit a standard Create Booking request.

Although card information may be included by the client, Nitro removes
it before sending the booking to the supplier.

The booking is still created successfully.

------------------------------------------------------------------------

## Step 2 --- API Warning

If payment information is supplied during Create Booking, Nitro returns
a warning similar to:

``` json
{
  "isSucceed": true,
  "advisories": [
    {
      "message": "Card information has been removed as it's not supported in create booking for this cruise line.",
      "description": "Payment",
      "type": "Warning"
    }
  ]
}
```

### Interpretation

-   `isSucceed: true` indicates the booking was successfully created.
-   The advisory is **not an error**.
-   Payment was **not** submitted.
-   Card information was intentionally ignored because the supplier does
    not support payment during booking creation.

------------------------------------------------------------------------

## Step 3 --- Submit Payment

After the booking reference has been created, submit payment using the
standard Modify Booking / payment workflow.

This is the supported process for these suppliers.

------------------------------------------------------------------------

# Expected Agent Behavior

When the warning below is encountered:

> Card information has been removed as it's not supported in create
> booking for this cruise line.

The agent should conclude:

-   Booking creation succeeded.
-   Payment was intentionally skipped.
-   This is expected supplier behavior.
-   A subsequent payment request is required.

The agent should **not** classify this warning as a booking failure.

------------------------------------------------------------------------

# Business Rules

1.  Booking must exist before payment is processed.
2.  External payment providers require a booking reference.
3.  Payment during Create Booking is ignored for supported suppliers.
4.  Nitro returns a warning instead of an error.
5.  Clients should always submit payment after booking creation.

------------------------------------------------------------------------

# Troubleshooting

### Payment missing after Create Booking

Verify whether the supplier is one of the Book Before Pay cruise lines.

### Warning about removed card information

This is expected behavior and does not indicate booking failure.

### Booking created but balance unpaid

Submit payment using the Modify Booking / Apply Payment process after
receiving the booking reference.

------------------------------------------------------------------------

# AI Agent Knowledge

The AI agent should know:

-   Book Before Pay is supplier-specific behavior.
-   The booking reference is required before payment.
-   Nitro intentionally strips payment information from Create Booking
    requests for supported suppliers.
-   The advisory returned is informational, not an error.
-   Payment must always be submitted after booking creation.
-   The booking remains valid even when payment is skipped.

------------------------------------------------------------------------

# Search Keywords

Book Before Pay, Create Booking, Payment Warning, Modify Booking
Payment, Third Party Payment Provider, Booking Reference Required,
Azamara, Explora Journeys, Four Seasons Yachts, Virgin Voyages, Windstar
Cruises, Nitro Booking API
