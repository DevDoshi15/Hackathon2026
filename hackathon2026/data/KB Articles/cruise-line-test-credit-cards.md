URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000040410368/en

ID: 80395000040410368
# Cruise Line Test System Credit Cards

## Overview

This article lists the test credit card numbers available for cruise lines that accept payment in their respective test/sandbox systems. Use these when testing payment flows against a given supplier's test environment — **do not use these against production**.

## General Rules

- If **Expiration** is left blank for a given card, any date in the future can be used.
- **CVV** can be any 3-digit number, unless a specific CVV is listed in the table (some suppliers require exact values).

---

## Cruise Line API — General Test Card Data

| API | Card Type | Card Number | Exp |
|---|---|---|---|
| RCCL | Visa | 4387751111111111 | — |
| NCL | Visa | 4111111111111111 | 01/20** |
| MSC | Visa | 4900000000000086 | 12/20** |
| MSC | Visa | 4444333322221111 | 12/20** |
| Carnival | Visa | 4035529900007013 | — |
| Carnival | MasterCard | 5404000000000001 | — |

`**` in the expiration indicates any year following the given month/prefix is acceptable per the source documentation.

---

## Virgin Voyages Test Card Data

### Valid Test Cards

| Card Type | Card Number | Exp | CVV |
|---|---|---|---|
| Visa | 4111111111111111 | 2021 | 123 |
| MasterCard | 5123456789012346 | 2021 | 123 |
| Amex | 371449635398431 | 2021 | 1325 |
| Discover | 6011000990139424 | 2021 | 132 |

### Payment Fail (triggers a failed payment attempt)

| Card Type | Card Number | Amount | CVV |
|---|---|---|---|
| Visa | 4012000033330026 | 81.00 | — |
| Master | 5424180279791732 | 10.10 | — |

For these cards, the specific **amount charged** is what triggers the failure — use the exact amount listed.

### Payment Decline

| Card Type | Card Number | Exp | CVV |
|---|---|---|---|
| Discover | 6510000000001240 | — | — |

---

## Disney Cruise Line Test Card Data

### Valid Test Cards

| Card Type | Card Number | Exp | CVV | Billing Address | Billing Zip | Delay (Sec) | Status Code |
|---|---|---|---|---|---|---|---|
| JCB | 3555554915113293 | 12/25 | 709 | 24700 MCBEAN LANE | 91334 | 10 | A |
| JCB | 3566007770003064 | 12/25 | 460 | 4987 SHERBERTH RD | 35999 | 0 | A |
| AMEX | 377746902253874 | 12/25 | 5857 | 932 N FIRST ST | 79119 | 1 | A |
| AMEX | 377777263081109 | 12/25 | 8439 | 100 ABERNATHY RD | 12209 | 28 | A |
| AMEX | 377777684182882 | 12/25 | 7240 | 666 SUNSET BLVD | 92808 | 10 | A |
| DCLUB | 3855556501000005 | 12/25 | 500 | 67 BONNET CREEK | 32839 | 0 | A |
| VISA | 4003010123456780 | 12/25 | 666 | 5789 LANKERSHIM | 22019 | 0 | A |
| VISA | 4444381470024365 | 12/25 | 453 | 753 WAYLAND CT | 40507 | 1 | A |
| VISA | 4444394758408416 | 12/25 | 365 | 899 STARS ST | 75094 | 28 | A |
| MC | 5555550171357314 | 12/25 | 392 | 700 BALL ROAD | 32321 | 28 | A |
| MC | 5555558566850892 | 12/25 | 644 | 324 SEQUOIA | 92338 | 10 | A |
| DISC | 6011000999586187 | 12/25 | 822 | 333 Branson Landing | 65616 | 0 | A |
| DISC | 6011114379163822 | 12/25 | 228 | 191 N. STATE | 10022 | 0 | A |
| DISC | 6500994561258795 | 12/25 | 631 | — | — | 0 | — |
| DISC | 6501994589615736 | 12/25 | 631 | — | — | 0 | — |

**Delay (Sec)** simulates processing latency in the test environment; **Status Code A** indicates an approved/authorized response.

### Declined Test Cards

| Card Type | Card Number | Exp | CVV | Billing Address | Billing Zip | Delay (Sec) | Status Code |
|---|---|---|---|---|---|---|---|
| VISA | 4444156842216653 | 12/25 | 924 | — | — | 35 | T |
| MC | 5555559514070468 | 12/25 | 924 | — | — | 35 | T |
| AMEX | 377777102878079 | 12/25 | 5529 | — | — | 35 | T |
| DCLUB | 300000247987... *(number partially cut off in source)* | 12/25 | 408 | 13 RANGE... *(address partially cut off in source)* | 14453 | 10 | B |

**Status Code T** indicates a timeout-style decline; **Status Code B** indicates a different decline reason (specific meaning not captured in the source article — the DCLUB entry's card number and address were truncated in the original documentation and should be re-verified against the source KB before use).

---

## Silversea Test Cards

| Card Type | Card Number | Exp | CVV |
|---|---|---|---|
| Visa | 4444333322221111 | Any date greater than today's date | Any |
| Visa | 4111111111111111 | Same as above | Any |
| Mastercard | 5555555555554444 | Same as above | Any |
| AMEX | 378282246310005 | Same as above | Any |

---

## Explora Journeys — Hosted Payment Gateway Cards

Explora Journeys uses a **hosted payment gateway**, consistent with the supplier-hosted gateway model described in the Nitro Booking API Payment Options article (Option 3).

### Non-3D Test Cards

| Card Type | Card Number | Exp | CVV |
|---|---|---|---|
| Visa | 4111111111111111 | 03/2030 | 737 |
| Visa | 4444333322221111 | 03/2030 | 737 |
| Mastercard | 5555555555554444 | 03/2030 | 737 |
| JCB | 3569990010095841 | 03/2030 | 737 |
| Discover | 6011601160116611 | 03/2030 | 737 |
| Amex | 370000000000002 | 03/2030 | 7373 |
| Maestro | 6771798021000008 | 03/2030 | 737 |

### 3D Test Cards

| Card Type | Card Number | Exp | CVV |
|---|---|---|---|
| Visa | 4917610000000000 | 03/2030 | 737 |
| Amex | 4963371453984 *(15-digit number as recorded in source; note the leading digit "4" is unusual for an Amex BIN — verify against source before use)* | 03/2030 | 7373 |
| Discover | 6011111111111117 | 03/2030 | 737 |
| Diners | 30569309025904 | 03/2030 | 737 |

---

## Notes for Downstream Use

- These are **test/sandbox-only** card numbers, standard for QA and integration testing against each supplier's non-production environment — never process a live/production charge with these.
- Address and CVV requirements vary by supplier: Disney and Explora require exact CVV/expiry matches; Silversea and Virgin Voyages (valid cards) accept broader ranges ("Any" CVV, any future expiration).
- Where a source entry was cut off or ambiguous (Disney DCLUB declined card, Explora 3D Amex card), this is flagged inline — confirm against the original KB source before relying on those specific values.
