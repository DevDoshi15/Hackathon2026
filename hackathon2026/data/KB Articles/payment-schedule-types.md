URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000047097078/en

ID: 80395000047097078

# Domain Table: Payment Schedule Types

## Overview

`PaymentScheduleTypes` is a domain enum used to classify the type of a scheduled payment within a booking's payment schedule (e.g. deposit, final payment, refund).

## Reference Table

| Value | Enum Name | Description |
|---|---|---|
| 0 | `Deposit` | Default — deposit payment |
| 1 | `Final` | Final payment |
| 2 | `Full` | Full payment |
| 3 | `Partial` | Part payment |
| 4 | `Insurance` | Insurance payment |
| 5 | `Refund` | Refund |
| 6 | `Transfer` | Transfer |
| 7 | `NonRefundableDeposit` | Non Refundable Deposit |

> **Note:** `NonRefundableDeposit` has no explicit value assigned in the source enum; as the entry immediately following `Transfer = 6`, it takes the next sequential value, `7`.

## Where This Is Used: Payment Schedules

`PaymentScheduleTypes` values appear as the `type` field within a booking's `paymentSchedules`, which is broken out into three separate schedule collections:

- `customerPaymentSchedules` — payment schedule from the customer's perspective
- `affiliatePaymentSchedules` — payment schedule from the affiliate's perspective
- `supplierPaymentSchedules` — payment schedule from the supplier's perspective

### Sample Response

```json
"paymentSchedules": {
    "customerPaymentSchedules": [
        {
            "type": 2,
            "amount": 1424.5,
            "dueDate": "11-Mar-2023"
        }
    ],
    "affiliatePaymentSchedules": [
        {
            "type": 2,
            "amount": 1424.5,
            "dueDate": "11-Mar-2023"
        }
    ],
    "supplierPaymentSchedules": [
        {
            "type": 2,
            "amount": 1257.46,
            "dueDate": "13-Mar-2023"
        }
    ]
}
```

In this example, `"type": 2` on each schedule entry corresponds to `Full` — indicating a full payment is scheduled for each of the customer, affiliate, and supplier payment views.

## Field Reference (per schedule entry)

| Field | Description |
|---|---|
| `type` | The `PaymentScheduleTypes` value indicating what kind of payment this schedule entry represents |
| `amount` | The amount due for this scheduled payment |
| `dueDate` | The date this payment is due |

## Integration Notes

- The **same booking** can have differing amounts across `customerPaymentSchedules`, `affiliatePaymentSchedules`, and `supplierPaymentSchedules` even when the `type` and `dueDate` match — as shown in the sample, the supplier amount (`1257.46`) differs from the customer/affiliate amount (`1424.5`) on the same due date. This reflects the different parties' view of the transaction (e.g. commission/markup differences) rather than an error.
- When reasoning about a booking's payment obligations, always check which of the three schedule collections (`customer`, `affiliate`, `supplier`) is relevant to the question being asked, since they are not guaranteed to be identical.
