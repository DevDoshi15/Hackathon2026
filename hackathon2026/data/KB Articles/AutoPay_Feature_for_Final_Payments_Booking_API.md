URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000124226414/en/Article

ID: 80395000124226414

---

title: AutoPay Feature for Final Payments (Booking API)
category: Knowledge Base
version: 1.0
last\_updated: 2026-07-10
tags:

* AutoPay
* Final Payment
* Booking API

\---

# AutoPay Feature for Final Payments (Booking API)

> \*\*Availability:\*\* Now available in \*\*Sandbox\*\* and \*\*Production\*\*.

## Purpose

The Booking API now supports scheduling **automatic final payments** through the new `autoPayType` parameter, providing feature parity across API and UI channels.

## Supported APIs

* CreateReservation
* ApplyPayment
* ReadReservation

## Request

A new property has been added under `paymentPreferences`.

```json
"paymentPreferences": {
  "autoPayType": "Final"
}
```

When `autoPayType` is set to `"Final"`, the booking is registered for automatic final payment (when supported). If omitted, the booking follows the normal deposit/final payment process.

## Processing Flow

1. Client submits Create Reservation or Apply Payment with `"autoPayType":"Final"`.
2. Deposit payment is processed.
3. If supported and validations pass, AutoPay registration is completed.
4. ReadReservation returns the payment schedule including AutoPay status.
5. Any warnings or validation messages are returned in the API response and recorded in booking history.

## Successful Registration

When AutoPay is successfully registered:

* Advisory message returned:

  * **MSG\_AutoPay\_Success**
  * *"We have successfully scheduled the payment options chosen with the cruise line."*
* Booking is created successfully.
* Customer payment schedule includes the final payment.
* Final payment entry contains:

```json
"isAutoPay": true
```

indicating the payment will be processed automatically on the due date.

## Unsupported Cruise Lines

If the selected cruise line does not support Final AutoPay, the booking continues normally and a warning is returned indicating that Final AutoPay is not supported.

## Validation Requirements

AutoPay registration requires:

* Successful deposit payment
* Valid payment token
* Credit card expiration date later than the final payment due date

Validation failures (for example, expired card or failed deposit payment) prevent AutoPay registration and return appropriate API errors.

## Supported Cruise Lines (As of 2026-01-01)

* Royal Caribbean
* Celebrity Cruises
* Holland America Line
* Seabourn
* Princess
* Cunard

## ReadReservation

ReadReservation returns:

* Final payment amount
* Final payment due date
* Customer payment schedule
* `isAutoPay` indicator

## Notes

* AutoPay affects only the final payment.
* Deposit payment is still processed immediately.
* Clients can refer to the Odysseus Booking Engine article for equivalent UI behavior.

