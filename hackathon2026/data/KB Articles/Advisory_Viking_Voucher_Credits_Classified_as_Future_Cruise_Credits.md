URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000135086122/en/Article

ID: 80395000135086122

---

title: Advisory: Viking Voucher Credits Classified as Future Cruise Credits
category: Release Advisory
supplier: Viking
version: 1.0
last\_updated: 2026-07-10
tags:

* Viking
* Future Cruise Credit
* Voucher
* FCC

\---

# Advisory: Viking Voucher Credits Classified as Future Cruise Credits

## Overview

Viking issues a **Voucher** when a paid sailing is cancelled by the cruise line. The voucher represents the value of the cancelled booking and can be applied to a future booking.

When a voucher is redeemed on a new booking, Odysseus classifies the applied amount as a **Future Cruise Credit (FCC)** rather than a cruise line discount, since it represents previously issued customer credit.

> \*\*Advance Notice:\*\* Planned release at the end of \*\*April 2026\*\*.

\---

## What's Changing

### UI

Voucher-based credits returned by Viking are displayed as **Future Cruise Credits (FCC)**.

### Booking API

Voucher-based credits are returned as **Future Cruise Credits (FCC)** instead of standard discounts.

* Applies to: **Read Reservation** response
* Classification: **Future Cruise Credit**
* **Price Item ID:** 150

\---

## Business Logic

1. Viking cancels a paid booking.
2. Viking issues a voucher equal to the booking value.
3. The traveler applies the voucher to a future booking.
4. Odysseus classifies the applied amount as an FCC rather than a discount.

This ensures previously issued credits are distinguished from promotional discounts.

\---

## Impact

* Voucher credits appear as Future Cruise Credits.
* Existing discount processing remains unchanged.
* Consumers should interpret **Price Item ID 150** as an FCC rather than a promotional discount.

\---

## Compatibility

This is a classification enhancement only. Existing booking workflows remain unchanged.

Applications displaying booking pricing should recognize **Price Item ID 150** as a Future Cruise Credit when processing Viking bookings.

