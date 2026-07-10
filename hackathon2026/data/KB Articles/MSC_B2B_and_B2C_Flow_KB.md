URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000113036121/en

ID: 80395000113036121
# Knowledge Base: MSC B2B and B2C Flow

## Overview

MSC Cruises has introduced an optional **SalesChannel** field in the
**Create Reservation** request of the Nitro Booking API. This field
identifies whether the booking originated from a Business-to-Consumer
(B2C) or Business-to-Business (B2B) sales channel, improving data
clarity and reporting.

> **Impacted API:** Create Reservation (Create Booking)

------------------------------------------------------------------------

# Scope

-   Supplier: MSC Cruises
-   API: Create Reservation
-   Request Section: `cruiseReservation.pos`
-   Field: `SalesChannel`
-   Applies only to **Create Booking**
-   Ignored during **Modify Booking**

------------------------------------------------------------------------

# SalesChannel Field

Location:

``` json
"cruiseReservation": {
  "pos": {
    "SalesChannel": 1
  }
}
```

The field is optional.

## Supported Values

    Value Booking Flow
  ------- ----------------------------
        1 B2C (Business-to-Consumer)
        2 B2B (Business-to-Business)

------------------------------------------------------------------------

# B2C Flow

## Request

``` json
"pos": {
  "apiId": "MSC",
  "SalesChannel": 1
}
```

Meaning:

-   Booking originated from a consumer-facing channel.
-   Sent to MSC during Create Reservation.

Expected Result:

-   Booking is created successfully.
-   Standard Create Reservation response is returned.
-   Response does not echo the `SalesChannel` field.

------------------------------------------------------------------------

# B2B Flow

## Request

``` json
"pos": {
  "apiId": "MSC",
  "SalesChannel": 2
}
```

Meaning:

-   Booking originated from a travel agency or business partner.
-   Sent to MSC during Create Reservation.

Expected Result:

-   Booking is created successfully.
-   Standard Create Reservation response is returned.
-   Response does not include `SalesChannel`.

------------------------------------------------------------------------

# Modify Booking Behavior

**Do not send `SalesChannel` during Modify Booking.**

If included:

-   Odysseus ignores the field.
-   The value is **not transmitted** to MSC.
-   No error is generated.

  Operation        SalesChannel Processed
  ---------------- ------------------------
  Create Booking   Yes
  Modify Booking   No (Ignored)

------------------------------------------------------------------------

# Business Rules

1.  `SalesChannel` is optional.
2.  Supported values are only:
    -   `1` = B2C
    -   `2` = B2B
3.  Field is applicable only to Create Reservation.
4.  Responses are unchanged regardless of the value supplied.
5.  Omitting the field preserves existing behavior.

------------------------------------------------------------------------

# API Behavior

## Request

-   Read `SalesChannel` from `cruiseReservation.pos`.
-   Pass the value to MSC during Create Reservation.

## Response

-   Normal booking response.
-   No additional response fields related to SalesChannel.
-   Booking confirmation and reservation information are unaffected.

------------------------------------------------------------------------

# Client Impact

No breaking changes.

Existing clients:

-   Continue working without changes.
-   May begin sending `SalesChannel` to improve booking classification.

------------------------------------------------------------------------

# Troubleshooting

### SalesChannel not reflected in response

Expected behavior. The response does not return this field.

### SalesChannel sent during Modify

Expected behavior. Odysseus ignores the field and does not forward it to
MSC.

### Invalid value

Only `1` and `2` are supported. Any other value should be treated as
invalid by the client before submission.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should know:

-   `SalesChannel` is optional.
-   It exists only in the Create Reservation request.
-   `1` represents B2C.
-   `2` represents B2B.
-   It improves booking classification for MSC.
-   Modify Booking ignores the field.
-   Responses are identical regardless of SalesChannel value.

------------------------------------------------------------------------

# Search Keywords

MSC, SalesChannel, B2B, B2C, Create Reservation, Create Booking, Modify
Booking, POS, MSC Booking API, Booking Flow Classification
