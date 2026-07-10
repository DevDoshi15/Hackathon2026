URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000137438237/en/Article

ID: 80395000137438237


---

title: Booking API Timeout Specification
category: Knowledge Base
product: Nitro Booking API
version: 1.0
last\_updated: 2026-07-10
tags:

* Booking API
* Timeout
* Gateway
* Supplier
* Performance

\---

# Booking API Timeout Specification

## Introduction

This document defines the timeout configuration for the Odysseus Booking API within the cruise vertical.

Timeouts are enforced at two distinct architectural layers:

|Layer|Description|
|-|-|
|Application Layer (Nitro → WS)|Maximum time the Booking API waits for a response from the WS layer. Visible to API consumers.|
|Gateway Layer (WS → Supplier)|Per-message, per-supplier timeout from the WS application to the cruise line backend. Supplier overrides apply per message type.|

Where a supplier-specific override is defined, it supersedes the system default for that message type. Otherwise, the system default applies.

\---

# Application Layer — Message Timeouts

These timeouts apply at the Nitro → WS boundary.

|API / Endpoint|Timeout|
|-|-|
|Fare Code Availability|45s|
|Fare Code Details|45s|
|Category Availability|45s|
|Cabin Availability|45s|
|Package Availability|45s|
|Transfer Availability|45s|
|Get Cabin Details|45s|
|Special Services|45s|
|ListDinings|25s|
|AddOns Availability|25s|
|List Cruise Line Airports|45s|
|Office Credential List (POS)|45s|
|Past Passenger Lookup|45s|
|Create Reservation|90s|
|Modify Reservation|45s|
|Read Reservation|45s|
|Read Reservation From Supplier|45s|
|Release Reservation|45s|
|Cancel Reservation|45s|
|Confirm Reservation|45s|
|Cabin Hold|45s|
|Cabin Release|45s|
|Price Reservation|45s|
|ApplyPayment|45s|
|RecordPayment|45s|
|Search Reservation with Supplier|45s|
|Search Reservation|45s|
|Extend Reservation Hold|45s|
|Cruise Price Cancelation|45s|
|Reservation History (Odysseus Only)|45s|
|Reservation History (Supplier)|45s|

\---

# Timeout Design Principles

## Standard (45s)

Applied to the majority of API operations to balance responsiveness with network and processing overhead.

## Extended (90s)

Reserved for Create Reservation, which requires pricing locks, inventory allocation, and supplier confirmation.

## Reduced (25s)

Applied to lightweight lookup operations such as ListDinings and AddOns Availability.

## Gateway Overrides

Supplier-specific overrides are based on measured latency characteristics and are applied per message type.

\---

# Gateway Layer — Supplier Connection Timeout Matrix

## Cruise Search

|Message Type|Default|AMA|Avalon|Carnival|Disney|HAR|MSC|NCL|RCCL|Viking|
|-|-|-|-|-|-|-|-|-|-|-|
|Sail Avail|20s|—|—|—|—|—|25s|—|—|—|
|Fare Avail / Cruise Air Search|30s|—|40s|50s|40s|30s|40s|30s|50s|55s|
|GroupList / GroupRetrieval|30s|—|40s|50s|40s|30s|40s|30s|50s|55s|
|Fare Details / FarePromotionDetails|30s|—|40s|50s|40s|30s|40s|30s|50s|55s|
|Package Avail (Tours)|30s|—|40s|50s|40s|30s|40s|30s|50s|55s|
|Category Avail|30s|—|40s|—|55s|—|40s|40s|—|55s|
|Cabin Avail / Hold / UnHold / Cabin Details|30s|45s|40s|—|—|—|45s|40s|—|—|
|Dining Avail|30s|45s|40s|—|—|—|45s|40s|—|—|
|Itinerary Avail|30s|45s|40s|—|—|—|45s|40s|—|—|
|Price|45s|—|—|—|—|—|—|—|—|—|
|CruiseAddon|30s|—|—|—|—|—|45s|—|—|—|
|SpecialService|30s|—|—|—|—|—|—|—|—|—|

## Booking

|Message Type|Default|AMA|
|-|-|-|
|Book (Create Booking)|58s|—|
|Confirm Booking|58s|—|
|Read|45s|70s|
|ReadPaymentInstallment|45s|70s|
|ManageInstallment|45s|70s|
|BookingHistory|45s|70s|
|Modify|58s|—|
|PaymentExtension|58s|—|
|Cancel Booking|58s|—|
|PriceCancellation|45s|—|
|Release Booking|45s|70s|
|PNRSearch|30s|—|
|Export Booking|58s|—|

## Generic (25s)

The following message types use the generic 25-second timeout and have no supplier-specific overrides:

* CruiseTransferAvail
* CruiseBusAvail
* CruiseTourDescription
* CruisePastPassengerLookup
* CruiseAirGateway
* CruiseAgencyPasswordChange

\---

# Supplier-Specific Notes

## AmaWaterways (AMA)

Extends Read, ReadPaymentInstallment, ManageInstallment, BookingHistory, and Release Booking to 70s due to additional processing in the Amadeus GDS layer.

## Viking

Applies the highest search-phase overrides (55s) across most availability messages.

## RCCL

Uses 50s overrides for core search messages.

## Carnival

Uses 50s overrides for search-phase messages while booking operations use system defaults.

## Disney Cruise Line (DCL)

Applies 40–55s overrides with a 55s ceiling for Category Availability.

## MSC

Extends most search, cabin, dining, itinerary, and addon operations to 45s. Sail Avail uses 25s.

## NCL

Uses 30–40s search overrides. Booking read operations use system defaults.

## HAR

Uses the 30s system default for search messages with no additional overrides.

## Avalon

Uses 40s overrides across most search messages with no booking-phase overrides.

\---

# Summary

* Standard API operations: 45s
* Lightweight lookups: 25s
* Create Reservation: 90s
* Supplier-specific gateway overrides apply where configured
* Application-layer timeouts are what API consumers experience directly

