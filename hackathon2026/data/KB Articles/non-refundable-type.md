URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000033205253/en

ID: 80395000033205253
# Domain Table: Non Refundable Type

## Overview

`Non Refundable Type` is a domain value used in the Nitro Booking API to indicate the refundability status of a booking's deposit/payment. It determines whether, and to what extent, funds paid toward a booking can be returned to the guest upon cancellation.

## Reference Table

| Value | Name | Description |
|---|---|---|
| 0 | Undefined / Unknown | Refundability status has not been set or is not known |
| 1 | Refundable | The booking's deposit/payment is fully refundable |
| 2 | Non-Refundable Deposit | The deposit portion of the booking is non-refundable, though this may not necessarily apply to the full payment |
| 3 | Non-Refundable | The full booking amount is non-refundable |

## Related Domain Concepts

This table is closely related to the following `DynamicRuleTypes` values (see *Domain Tables: Dynamic Rule Types*), which represent the same non-refundable concepts as promotional/business rule types rather than a booking-level status flag:

| DynamicRuleTypes Value | Name | Description |
|---|---|---|
| 16 | `NR` | Non Refundable |
| 17 | `NRD` | Non Refundable Deposit |

## Notes

- Source system: **Nitro Booking API** (legacy ASP.NET Classic).
- When integrating or mapping this field, distinguish between the booking-level `Non Refundable Type` status (this table) and the promotional `DynamicRuleTypes` entries (`NR` / `NRD`), which represent a rule/offer applied to a fare rather than the deposit status itself. Downstream systems may need to reconcile both when determining actual refund eligibility.
