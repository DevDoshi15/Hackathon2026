URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000110861685/en

ID: 80395000110861685

---

title: Cruise Line Air - Support for Detailed Air Reservation Information in Read Response
category: Knowledge Base
feature: Cruise Line Air
api:

* /v2/reservation/cruise/readfromsupplier
version: 1.0
last\_updated: 2026-07-10
tags:
* Cruise Line Air
* ReadFromSupplier
* Air Reservations
* Viking
* MSC

\---

# Cruise Line Air - Support for Detailed Air Reservation Information in Read Response

## Overview

Certain cruise lines, including **Viking** and **MSC**, have enhanced their booking read responses by providing detailed air reservation information.

Previously, Odysseus represented most air-related information under the **Packages** or **AddOns** hierarchy. As cruise lines now return richer air reservation details—such as flight itineraries, flight segments, airline information, fare classes, and airport details—the existing Packages and AddOns structures are no longer sufficient to accurately represent this data.

To support these enhancements, Odysseus now exposes detailed air reservation information through the **`additionalReservations`** element in the **ReadFromSupplier** response.

\---

## Supported Endpoint

**Endpoint**

`/v2/reservation/cruise/readfromsupplier`

\---

## What's New

The ReadFromSupplier response now supports a dedicated **Air** reservation object under the **additionalReservations** collection.

This enhancement allows cruise lines to return structured air reservation details, including:

* Complete flight itineraries
* Multi-segment journeys
* Flight numbers
* Operating airline information
* Marketing airline information
* Departure and arrival dates
* Departure and arrival airports
* Airport names and IATA codes
* Fare class information
* Display airline information

\---

## Response Structure

The `additionalReservations` collection may contain one or more reservation types.

For cruise line air bookings, an entry with the following structure is returned:

* `type`

  * Reservation type (Air)
* `flights`

  * Collection of flight itineraries
* `segments`

  * Individual flight legs within an itinerary

\---

## Flight Information

Each flight itinerary may contain:

|Field|Description|
|-|-|
|displayAirline|Primary airline displayed for the itinerary|
|departureArrivalInfo|Overall itinerary departure and arrival information|
|segments|Collection of flight segments|

\---

## Flight Segment Information

Each segment contains:

|Field|Description|
|-|-|
|flightNumber|Flight number|
|operatingAirline|Operating carrier|
|marketingAirline|Marketing carrier|
|departureArrivalInfo|Departure and arrival information|
|fareClass|Cabin/Fare class|

\---

## Departure and Arrival Information

The following information may be available for both the itinerary and individual segments:

* Departure date and time
* Arrival date and time
* Departure airport name
* Departure airport code
* Arrival airport name
* Arrival airport code

\---

## Business Impact

This enhancement enables consumers to display detailed flight itineraries directly from the ReadFromSupplier response without relying on Package or AddOn information.

Applications can now present:

* Complete outbound journeys
* Complete return journeys
* Connecting flights
* Airline information
* Airport details
* Fare class information

using the structured air reservation response.

\---

## Backward Compatibility

This enhancement is fully backward compatible.

* Existing Packages and AddOns functionality remains unchanged.
* Existing ReadFromSupplier response fields remain unchanged.
* The new information is provided through the optional `additionalReservations` collection.

Consumers should verify whether the `additionalReservations` element exists before processing air reservation data.

\---

## Sample Response

```json
{
  "additionalReservations": \[
    {
      "type": "Air",
      "flights": \[
        {
          "displayAirline": {
            "code": "UA",
            "name": "United Airlines"
          },
          "departureArrivalInfo": {
            "departureCity": {
              "id": "ORF",
              "airportName": "Norfolk, Virginia, United States"
            },
            "arrivalCity": {
              "id": "FLL",
              "airportName": "Fort Lauderdale, Florida, United States"
            }
          },
          "segments": \[
            {
              "flightNumber": "1926",
              "operatingAirline": {
                "code": "UA",
                "name": "United Airlines"
              },
              "marketingAirline": {
                "code": "UA",
                "name": "United Airlines"
              },
              "fareClass": {
                "type": "Economy"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

> \*\*Note:\*\* The sample response above has been shortened for readability. The actual response may include multiple flight itineraries and multiple flight segments depending on the itinerary returned by the cruise line.

\---

## Notes

* This enhancement is applicable only when the cruise line returns detailed air reservation information.
* Cruise lines may not provide all air reservation details immediately after booking creation.
* Air reservation information may become available or be updated as airline reservations are confirmed by the cruise line.
* Different cruise lines may provide different levels of air reservation detail.

