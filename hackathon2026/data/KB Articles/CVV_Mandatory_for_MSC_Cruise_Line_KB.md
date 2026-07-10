URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000116720063/en

ID: 80395000116720063
# Knowledge Base: CVV Mandatory for MSC Cruise Line

## Overview

MSC Cruises now requires the **Card Verification Value (CVV/CVC)** to be
provided for all credit card payments.

This requirement applies to the **Nitro Payment Tokenization API** and
enhances payment security during the booking process.

------------------------------------------------------------------------

# Scope

-   **Supplier:** MSC Cruises
-   **Impacted API:** `POST /v2/payment/TokenizeCard`
-   **Feature:** Payment tokenization prior to booking/payment
-   **Change:** `cvv` (CVC) is now mandatory

------------------------------------------------------------------------

# Business Requirement

When tokenizing a payment card for an MSC booking:

-   The request **must** include the card's CVV/CVC.
-   Requests without a CVV may fail validation or be rejected by the
    supplier/payment workflow.

This requirement applies to **all MSC bookings**.

------------------------------------------------------------------------

# API Endpoint

``` text
POST /v2/payment/TokenizeCard
```

------------------------------------------------------------------------

# Required Request Field

  -----------------------------------------------------------------------
  Field                     Required        Description
  ------------------ ---------------------- -----------------------------
  `cvv`                    Yes (MSC)        Card Verification Value
                                            (security code printed on the
                                            card).

  -----------------------------------------------------------------------

Example:

``` json
{
  "Number": "4111111111111111",
  "cvv": "123",
  "type": "VI",
  "expiration": "12/26",
  "cardHolderName": "John Doe",
  "BillingDetails": {
    "Address": {
      "Country": {
        "id": "US"
      }
    }
  }
}
```

------------------------------------------------------------------------

# Successful Response

If tokenization succeeds, the API returns a payment token.

Example:

``` json
{
  "isSucceed": true,
  "data": {
    "token": "<payment-token>"
  }
}
```

The returned token should be used in subsequent payment or booking
requests instead of transmitting raw card details.

------------------------------------------------------------------------

# Business Rules

1.  CVV is mandatory for **MSC Cruises**.
2.  The requirement applies to the **TokenizeCard** request.
3.  Tokenization should be completed before payment processing.
4.  The generated token represents the card in later API calls.

------------------------------------------------------------------------

# Client Impact

Clients integrating with MSC should:

-   Update request validation to require `cvv`.
-   Ensure UI/forms always collect the card security code.
-   Prevent TokenizeCard requests without a CVV.

Existing integrations that omit CVV should be updated.

------------------------------------------------------------------------

# Troubleshooting

### TokenizeCard request fails

Verify:

-   `cvv` is present.
-   Card number is valid.
-   Expiration date is valid.
-   Billing information is complete.

### CVV omitted

Expected behavior:

-   The request may fail validation or payment processing because MSC
    requires the CVV.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should know:

-   CVV/CVC is mandatory for all MSC bookings.
-   The change only affects the `POST /v2/payment/TokenizeCard` request.
-   A successful tokenization returns a reusable payment token.
-   Clients should collect CVV before attempting tokenization.

------------------------------------------------------------------------

# Search Keywords

MSC, CVV, CVC, Card Verification Value, TokenizeCard, Payment
Tokenization, Payment API, Nitro Payment API, Credit Card Security Code,
MSC Payment
