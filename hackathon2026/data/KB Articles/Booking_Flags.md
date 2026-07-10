URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000064109003/en 

ID: 80395000064109003

---
# Title: Booking Flags
category: Booking API
tags:
  - booking
  - flags
  - reservation
---

# Booking Flags

## Overview

Odysseus returns **booking flags** to indicate warnings, exceptional conditions, or informational events that occur during booking creation, payment processing, or reservation synchronization.

A booking can still be successfully created even when one or more flags are returned.

> **Note**
>
> If a cruise line is explicitly mentioned below, the flag only applies to that cruise line. Otherwise, the flag applies to all supported cruise lines.

---

# Available Flags

| Flag | Applies To | API | Description |
|------|------------|-----|-------------|
| PaymentDeclined | All | Create Reservation (Payment) | Payment failed or credit card was declined although the booking may exist. |
| GuestCountChanged | All | Read Reservation | Supplier guest count differs from Odysseus guest count. |
| InstantPayBookingNotConfirmed | MSC | Create Reservation (Payment) | Instant payment booking remains pending confirmation. |
| PriceMismatch | All | Read Reservation | Supplier reservation total differs from Odysseus total. |
| PaymentPendingConfirm | All | Create Reservation (Payment) | Held booking created but payment confirmation timed out or failed. |
| PaymentScheduleChanged | All | Create Reservation | Deposit amount or due date changed after booking. |
| GroupPaymentAllocationFailed | Royal Caribbean / Celebrity | Create Reservation (Payment) | Group payment succeeded but allocation to passengers failed. |
| PaymentAllocationTimeout | Royal Caribbean / Celebrity | Create Reservation (Payment) | Payment confirmation timed out; payment treated as successful to avoid double charging. |
| FirstNameChanged | Royal Caribbean / Celebrity | Create Reservation | First name truncated to cruise line limit (18 characters). |
| LastNameChanged | Royal Caribbean / Celebrity | Create Reservation | Last name truncated to cruise line limit (18 characters). |
| MiddleNameChanged | MSC / Holland America | Create Reservation | Middle name truncated to supplier character limit (MSC: 50, Holland: 12). |
| BookingPendingConfirmation | All | Create Reservation | Booking exists in Odysseus but supplier confirmation is still pending. |

---

# Flag Details

## PaymentDeclined
Returned when payment cannot be processed due to card decline or payment failure. The booking may still exist with the supplier.

```json
{
  "type": "PaymentDeclined",
  "status": "Active"
}
```

---

## GuestCountChanged
Returned when the supplier reservation contains a different number of passengers than the Odysseus reservation.

```json
{
  "type": "GuestCountChanged",
  "status": "Active"
}
```

---

## InstantPayBookingNotConfirmed (MSC)

Certain MSC sailings require immediate payment. If payment is submitted but the supplier responds with **Pending Confirmation**, this flag is returned.

```json
{
  "type": "InstantPayBookingNotConfirmed",
  "status": "Active"
}
```

---

## PriceMismatch

Indicates that the supplier reservation total differs from the amount stored in Odysseus.

```json
{
  "type": "PriceMismatch",
  "status": "Active"
}
```

---

## PaymentPendingConfirm

A held reservation was successfully created, but payment confirmation timed out or another non-card-decline error occurred.

```json
{
  "type": "PaymentPendingConfirm",
  "status": "Active"
}
```

---

## PaymentScheduleChanged

Returned when the supplier changes the deposit amount or due date after pricing.

```json
{
  "type": "PaymentScheduleChanged",
  "status": "Active"
}
```

---

## GroupPaymentAllocationFailed (Royal Caribbean & Celebrity)

Payment was processed successfully for the group but could not be allocated to individual passengers.

```json
{
  "type": "GroupPaymentAllocationFailed",
  "status": "Active"
}
```

---

## PaymentAllocationTimeout (Royal Caribbean & Celebrity)

Supplier timed out while confirming payment. Odysseus treats the payment as successful to avoid duplicate charges.

```json
{
  "type": "PaymentAllocationTimeout",
  "status": "Active"
}
```

---

## FirstNameChanged (Royal Caribbean & Celebrity)

First name exceeded 18 characters and was truncated before being sent.

```json
{
  "type": "FirstNameChanged",
  "status": "Active"
}
```

---

## LastNameChanged (Royal Caribbean & Celebrity)

Last name exceeded 18 characters and was truncated before being sent.

```json
{
  "type": "LastNameChanged",
  "status": "Active"
}
```

---

## MiddleNameChanged (MSC & Holland America)

Returned when the middle name exceeds the supplier limit and is truncated.

```json
{
  "type": "MiddleNameChanged",
  "status": "Active"
}
```

---

## BookingPendingConfirmation

Booking has been created locally, but supplier confirmation has not yet been received.

```json
{
  "type": "BookingPendingConfirmation",
  "status": "Active"
}
```

---

# Best Practices

- Always inspect returned booking flags after Create and Read Reservation calls.
- Do not treat every flag as a failure.
- Display active flags prominently to agents.
- For payment-related flags, verify booking status with the supplier before retrying payment.
- Handle supplier-specific flags only for the applicable cruise lines.

---

# Related Articles

- HTTP Status Codes, Errors and Advisories
- Create Reservation
- Read Reservation
- Payment Processing
