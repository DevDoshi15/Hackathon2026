URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000045697282/en

ID: 80395000045697282

# Pay to Supplier: Apply Payment after Cruise Booking Is Created

## Overview

This message is used once a booking is created and a payment needs to be applied to it. The payment could be a **first**, **supplemental**, or **final** payment.

> **Pre-requisite:** A booking must already exist in Odysseus for this message to work.

- **Endpoint:** `/v2/reservation/cruise/paytosupplier`

## The 3 Key Steps to Making a Payment on an Existing Booking

1. **Read/Retrieve Booking** — see the [Read/Retrieve Booking message article](https://supportdesk.odysol.com/portal/en/kb/articles/read-retrieve-booking-message) for details.
2. **Tokenize Card**
3. **Pay to Supplier** (the message documented in this article)

## Sample Request

```json
{
    "id": 65961,
    "cruiseReservation": {
        "id": 113941,
        "syncInfo": {
            "supplierSyncInfo": {
                "token": "892a04",
                "lastSyncOn": "13-Feb-2023 18:26:05",
                "lastModifiedOn": "13-Feb-2023 18:41:00"
            },
            "apiSyncInfo": {
                "token": "o6oFsxkO20gaTeZ5y3VDQYPCOeMhLkJJ",
                "sessionId": "79e64d1a-75cb-4143-83c2-39e3212e4249",
                "lastSyncOn": "13-Feb-2023 18:26:14"
            }
        }
    },
    "paymentToProcess": {
        "cardToken": "5734a680-cec9-4bd4-addb-585013bbd7ee",
        "amount": 1333.46,
        "currency": "USD"
    }
}
```

## Field Reference

| Field | Description |
|---|---|
| `id` | Odysseus-level reservation identifier |
| `cruiseReservation.id` | The cruise reservation identifier |
| `cruiseReservation.syncInfo` | Sync information block obtained from a prior Read/Retrieve Booking (`ReadFromSupplier`) call — **see below for handling recommendation** |
| `syncInfo.supplierSyncInfo` | Supplier-provided sync token; only present for certain suppliers (see notes below) |
| `syncInfo.apiSyncInfo` | Odysseus (API-level) sync token; always present, time-limited |
| `paymentToProcess.cardToken` | The tokenized card reference obtained from the Tokenize Card step |
| `paymentToProcess.amount` | The payment amount to charge |
| `paymentToProcess.currency` | The currency of the payment |

## ApiSyncInfo

- Always returned in the `ReadFromSupplier` response.
- This is **Odysseus's own sync information** and **expires after 30 minutes**.
- If this token is used in `PayToSupplier` after the 30-minute window, a **token expiration error** will be returned.

## SupplierSyncInfo

- Only returned when the **cruise line itself** provides this information in the Read Booking call.
- Currently only returned for **RCCL cruise lines (Royal Caribbean and Celebrity)** — and, until its migration to Seaware, **Azamara** as well.
- For RCCL, this information is returned specifically when `ReadFromSupplier` is called with `mode=Pay` or `mode=Modify`.
- Odysseus uses `SupplierSyncInfo` **internally** to release the booking with the cruise line after payment has been processed.

## Recommended Practice

To avoid confusion about which sync fields apply to which supplier, **always pass back the entire `SyncInfo` node** (both `supplierSyncInfo` and `apiSyncInfo`, whichever are present) from the `ReadFromSupplier` response directly into the `PayToSupplier` request — rather than selectively constructing it.

## Integration Notes

- The 30-minute expiration on `apiSyncInfo` means the Read Booking → Tokenize Card → Pay to Supplier sequence should be completed promptly; a stale `apiSyncInfo` token will cause the payment call to fail with a token expiration error.
- `supplierSyncInfo` will be `null`/absent for suppliers other than RCCL (Royal Caribbean, Celebrity) and Azamara (pre-Seaware migration) — do not treat its absence as an error for other suppliers.
- Booking release with the supplier after payment is handled internally by Odysseus using `supplierSyncInfo` — clients do not need to separately call Release Booking for RCCL/Azamara after a successful payment.
