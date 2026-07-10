URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000053643055/en

ID: 80395000053643055
# Knowledge Base: Nitro / Booking API -- `externalSessionInfo`

## Overview

`externalSessionInfo` is a supplier-generated object returned by some
cruise lines during the booking flow. Clients **must preserve this
object exactly as received and send it in subsequent requests** whenever
it is returned.

Failure to propagate `externalSessionInfo` may result in pricing
discrepancies, booking failures, or supplier validation errors.

> **Important:** Odysseus does not generate this value. It is supplied
> by the cruise line and must be treated as an opaque token.

------------------------------------------------------------------------

# Business Rule

Whenever a response contains:

``` json
"externalSessionInfo": { ... }
```

Store the entire object and include it unchanged in the next applicable
Booking API request.

Do **not** modify, recreate, or omit it.

------------------------------------------------------------------------

# Why it matters

The information contained within `externalSessionInfo` is required by
certain cruise lines to:

-   Maintain booking session context
-   Preserve supplier state
-   Validate pricing
-   Associate downstream requests with the original supplier session

If omitted, suppliers may:

-   Return incorrect prices
-   Reject booking requests
-   Lose booking context
-   Fail cabin selection or add-on processing

------------------------------------------------------------------------

# General Guidance

`externalSessionInfo` may appear in different locations depending on the
cruise line.

Clients should not hardcode its location.

Instead:

1.  Detect it wherever it appears.
2.  Preserve the entire object.
3.  Pass it to the next applicable request.

Odysseus cannot guarantee which suppliers will continue to return it or
where it may appear in future API versions.

------------------------------------------------------------------------

# Supplier Examples

## Uniworld

### Returned In

Category Availability Response

    Categories
     └── externalSessionInfo

### Must be passed to

1.  Cabin Availability Request
2.  Cabin Hold Request
3.  Create Booking Without Payment Request

Flow:

Category Availability Response → Cabin Availability → Cabin Hold →
Create Booking (No Payment)

------------------------------------------------------------------------

## MSC Cruises

### Returned In

Category Availability Response

    Fares
     └── AddOns
          └── externalSessionInfo

### Must be passed to

1.  Price Booking Request
2.  Create Booking Without Payment Request

Flow:

Category Availability Response → Price Booking → Create Booking (No
Payment)

------------------------------------------------------------------------

# Cruise Lines Mentioned

-   Royal Caribbean Group
-   Uniworld
-   MSC Cruises

Other suppliers may return this parameter in future.

------------------------------------------------------------------------

# API Impact Matrix

  -----------------------------------------------------------------------
  API                            Action
  ------------------------------ ----------------------------------------
  Category Availability Response Capture externalSessionInfo if present

  Cabin Availability Request     Pass through (Uniworld)

  Cabin Hold Request             Pass through (Uniworld)

  Price Booking Request          Pass through (MSC AddOns)

  Create Booking Without Payment Pass through

  Other Requests                 Pass if previously supplied and
                                 applicable
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Client Responsibilities

-   Preserve the complete object.
-   Do not modify values.
-   Treat as supplier-owned session metadata.
-   Continue passing until the booking flow ends or the supplier stops
    returning it.

------------------------------------------------------------------------

# Troubleshooting

## Booking fails after Category Availability

Verify `externalSessionInfo` was forwarded.

## Price changes unexpectedly

Check that supplier session information was preserved.

## Can I generate this value?

No. It must originate from the supplier response.

## Is the location always the same?

No. It varies by cruise line and API message.

------------------------------------------------------------------------

# AI Agent Knowledge

The AI agent should know:

-   `externalSessionInfo` is supplier-generated session state.
-   Preserve it exactly as received.
-   Pass it into subsequent booking requests.
-   Its location differs by supplier.
-   Missing values may cause booking or pricing failures.
-   Do not interpret or modify its contents.

------------------------------------------------------------------------

# Search Keywords

externalSessionInfo, Booking API, session token, supplier session,
Uniworld, MSC, RCCL, Category Availability, Cabin Availability, Cabin
Hold, Price Booking, Create Booking, booking context, Nitro API
