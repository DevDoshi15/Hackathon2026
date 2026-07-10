URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000044918001/en

ID: 80395000044918001
# Confirm Booking with Supplier: No Payment

## Overview

This message is used to **"confirm" the booking with the cruise line** without sending any payment information. It simply asks the supplier to change the booking status to "confirm," while payment continues to be managed directly with the cruise line outside of this message.

- **Purpose:** To confirm the booking with the supplier.
- **Pre-requisite:** A valid booking must already exist.
- **Endpoint:** `v2/reservation/cruise/Confirm`

## How to Trigger Confirm Booking

1. Trigger a **Read Booking from Supplier** message first, in order to obtain a token — the **API Sync Token**.
2. When calling **Confirm Booking**, pass the **API Sync Token** along with the **reservation Id**.
3. The response returns the booking details along with the **updated booking status**.

## Supplier Support

- This message is currently supported **only for MSC Cruises**.
- It is typically used in **markets outside of North America**.

## Integration Notes

- No credit card / payment data is transmitted as part of this message — it is a **status-change-only** operation. Payment is handled separately, directly with the cruise line.
- The **API Sync Token** is a required pre-condition: it must be freshly obtained via a Read Booking from Supplier call before Confirm Booking can be called — it is not something that can be reused arbitrarily or skipped.
- Do not use this flow for suppliers other than MSC Cruises, or assume it applies to North American markets, since both are explicitly scoped/limited in the current support.
