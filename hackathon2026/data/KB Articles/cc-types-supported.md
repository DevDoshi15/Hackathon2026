URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000045213233/en

ID: 80395000045213233

# Domain Table: CC Types Supported

## Overview

These are the credit card types supported via the API for sending payment information to the cruise line.

## Reference Table

| Code | Card Type |
|---|---|
| VI | Visa |
| MC | Mastercard |
| AX | American Express |
| DS | Discover |

## Notes

- These codes are used specifically when sending **payment information to the cruise line** (e.g. as part of the card tokenization / payment flow described in *Nitro Booking API: Payment Options*).
- Only these four card types are supported — a card type outside this list cannot be sent to the cruise line via the API.
