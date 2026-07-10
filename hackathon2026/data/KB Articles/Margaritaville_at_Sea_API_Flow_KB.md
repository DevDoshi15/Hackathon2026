URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=latest#Solutions/dv/80395000138391948/en

ID: 80395000138391948
# Knowledge Base: Margaritaville at Sea -- Nitro Booking API Flow

## Overview

Margaritaville at Sea returns multiple `externalSessionInfo` objects
during Category Availability. Clients must retain these values exactly
as received and send them in every subsequent booking request. Missing,
modifying, or relocating these values causes downstream booking
failures.

## Booking Flow

ListCategories → ListCabins → CabinHold → PriceReservation →
CreateReservation

## Mandatory Tracking Values

Capture and preserve all three:

1.  `cruiseReservation.externalSessionInfo`
2.  `cruiseReservation.categories[].externalSessionInfo`
3.  `cruiseReservation.categories[].fares[].fareCode.externalSessionInfo`

Carry them forward unchanged into: - Cabin Availability - Cabin Hold -
Price Reservation - Create Reservation

Their nesting must remain identical.

## Auto Included Add-ons

Add-ons with:

``` json
"autoInclude": true
```

move from:

`categories[].fares[].addOns[]`

to

`cruiseReservation.addOns[]`

for Price Reservation and Create Reservation.

## Cabin Selection

Cabin Availability returns:

`cruiseReservation.cabins[]`

Later requests must send the selected cabin under:

`categories[].cabins[]`

including BOTH: - cabin code - cabin number

## Common Errors

-   Missing reservation externalSessionInfo
-   Missing category externalSessionInfo
-   Missing fareCode externalSessionInfo
-   Wrong nesting
-   Forgetting to move autoInclude add-ons
-   Sending cabin number without cabin code

## AI Agent Rules

-   Preserve supplier tracking values exactly.
-   Never modify externalSessionInfo.
-   Preserve hierarchy.
-   Promote only autoInclude add-ons.
-   Cabin code and cabin number are mandatory together.

## Search Keywords

Margaritaville, externalSessionInfo, Cabin Hold, Price Reservation,
Create Reservation, autoInclude, addOns, cabin code, Nitro Booking API
