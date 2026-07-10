URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000111155442/en/Article

ID: 80395000111155442

---

title: Support for Mandatory Profile Indicator
category: Knowledge Base
product: Booking API
version: 1.0
last\_updated: 2026-07-10
tags:

* Booking API
* Price Reservation
* Mandatory Profile Indicators

\---

# Support for Mandatory Profile Indicator

## Overview

The Booking API now includes **Mandatory Profile Indicators** directly in the **Price Reservation** response. Previously, clients relied on the Cruise Profile Matrix to determine mandatory guest profile fields. With this enhancement, clients can dynamically identify required profile information from the API response.

## Business Logic

Odysseus maintains mandatory profile indicators based on supplier requirements and exposes them through the Booking API.

## Impacted API

* **Price Reservation**

## Supported Cruise Lines

|Cruise Line|Mandatory Profile Indicators|
|-|-|
|Ama Waterways|CitizenShip, PhoneNumber|
|Aroya Cruises|PhoneNumber, Email|
|Atlas Ocean Voyages|Address, PhoneNumber, Email (All Guests)|
|Avalon|Title, Age, Address|
|Azamara Cruises|PhoneNumber|
|Bahamas Paradise Cruise|PhoneNumber, Email|
|Celebrity Cruises|CitizenShip, Age, Title, PhoneNumber, Email|
|Celestyal Cruises|PhoneNumber|
|Cosmos|Title, Age, Address|
|Costa Cruise Line|CitizenShip, PhoneNumber, Email|
|Crystal Cruise Line|Email|
|Cunard Cruise Line|PhoneNumber|
|Disney Cruise Line|PhoneNumber|
|Explora Journeys|PhoneNumber|
|Four Seasons Yachts|PhoneNumber|
|Globus|Title, Age, Address|
|Hurtigruten Expeditions|CitizenShip, Address, Email|
|Hurtigruten Norwegian Coastal Express|Address, Email|
|Margaritaville at Sea|PhoneNumber, Email|
|MSC Cruises|CitizenShip, Residency, PhoneNumber, Email|
|Princess Cruises|PhoneNumber|
|P\&O Cruise Line (AUD/GBP/NZD)|PhoneNumber|
|Riviera River Cruises|Address, PhoneNumber, Email (All Guests)|
|Royal Caribbean|CitizenShip, Age, Title, PhoneNumber, Email|
|Silversea|Email|
|Vidanta|Address, PhoneNumber, Email (All Guests)|
|Viking Ocean/River/Expeditions|Address|
|Virgin Voyages|CitizenShip, PhoneNumber, Email|
|Windstar Cruises|PhoneNumber, Email|

## Response Behavior

The Price Reservation response returns the mandatory profile indicators applicable to the selected cruise line. Clients should use these indicators to dynamically validate guest information before booking.

Common indicators include:

* CitizenShip
* Residency
* Title
* Age
* Address
* PhoneNumber
* Email

## Sample Scenarios

### Royal Caribbean / Celebrity Cruises

Mandatory indicators may include:

* CitizenShip
* Age
* Title
* PhoneNumber
* Email

### MSC Cruises

Mandatory indicators may include:

* CitizenShip
* Residency
* PhoneNumber
* Email

## Client Guidance

1. Call the Price Reservation API.
2. Read the mandatory profile indicators returned.
3. Validate guest profile information dynamically.
4. Prompt users for any missing required fields before booking.

## Benefits

* Dynamic validation
* Reduced dependency on the Cruise Profile Matrix
* Automatic support for supplier requirement updates
* Improved integration flexibility

## Compatibility

This enhancement is backward compatible. Existing integrations continue to work without changes while allowing clients to adopt the new dynamic validation model.

