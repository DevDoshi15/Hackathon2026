URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000044918047/en

ID: 80395000044918047

# Release Booking with Supplier

## Overview

This message is used to **"release a lock"** with the cruise line.

- **Purpose:** To release a lock that was acquired from the supplier via a Read Booking call in `MODIFY` mode on the existing booking.
- **Pre-requisite:** A valid booking must exist, and a Read Booking with lock must have already been performed.
- **Endpoint:** `v2/reservation/Cruise/Release`

## How to Trigger Release Booking

1. Trigger a **Read Booking from Supplier** message with `"mode": "Modify"` (`v2/reservation/cruise/ReadFromSupplier`) to obtain the required tokens:
   - **Supplier Sync Token** — **RCCL only**
   - **API Sync Token**
2. Call the **Release Booking** message.

At the time of calling Release Booking, both tokens obtained above — Supplier Sync Token (RCCL only) and API Sync Token — must be passed along with the **reservation Id**.

## Response

- `"IsSucceed": true` — the booking was successfully released with the supplier.
- `"IsSucceed": false` — the release was not successful.

## Integration Notes

- The lock being released here is the one obtained by calling Read Booking **in `Modify` mode** — this flow only applies when that lock exists; it is not a general-purpose release for any booking state.
- **Supplier Sync Token is RCCL-specific.** For non-RCCL suppliers, only the API Sync Token is required/available; do not expect a Supplier Sync Token outside of RCCL.
- Always check the `IsSucceed` field in the response rather than assuming success from a 200 status alone — a `false` value indicates the release did not go through with the supplier.
