URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000065128001/en

ID: 80395000065128001

---
# Title: Mapping Correct Package IDs for Cruise Only and Cruise Tour Sailings
category: Business Rules
endpoint: Cruise Search / Booking Flow
tags:
  - packageid
  - cruise-tour
  - cruise-only
  - mapping
  - voyage
last_updated: 2026-07
---

# Mapping Correct Package IDs for Cruise Only and Cruise Tour Sailings

## Purpose

This article explains the recommended approach for mapping an external cruise supplier's sailing data to the correct **Odysseus PackageId** when integrating with the Nitro Booking API.

Accurate PackageId mapping is critical because an incorrect mapping can result in creating a booking for the wrong sailing.

---

# Why This Matters

The Nitro Booking API uses **PackageId** as the primary identifier for shopping and booking operations.

If your application maintains its own cruise inventory or consumes data directly from a cruise line, you must correctly map your sailing records to the corresponding Odysseus PackageId before making booking API calls.

---

# Important Fields

## VoyageId

- Also known as **VoyageCode** or **SailId**
- Value supplied by the cruise line
- Primary identifier for a sailing

---

## CruiseTourCode

- TourCode supplied by the cruise line
- Applicable only to Cruise Tour sailings
- Helps distinguish cruise tours from cruise-only sailings

---

## Duration

Total sailing duration.

For Cruise Tours, duration includes both:

- Land tour
- Cruise

---

## Departure Port

Field:

```
itinerary.departure.code
```

Represents the Odysseus internal seaport code.

Reference data:

- PortMasters
- CityMasters (`isSeaPort = true`)

---

## Arrival Port

Field:

```
itinerary.arrival.code
```

Represents the Odysseus internal seaport code.

Reference data:

- PortMasters
- CityMasters (`isSeaPort = true`)

---

## DepartureDateTime

The date on which the cruise portion begins.

---

## CruisePackageDepartureDateTime

The date the complete cruise package begins.

For Cruise Only sailings:

```
CruisePackageDepartureDateTime == DepartureDateTime
```

---

## ArrivalDateTime

The date on which the cruise portion ends.

---

## CruisePackageArrivalDateTime

The date the complete cruise package ends.

For Cruise Only sailings:

```
CruisePackageArrivalDateTime == ArrivalDateTime
```

---

## TransportationType

Used to distinguish sailing types.

| Value | Meaning |
|-------:|---------|
|29|Cruise Only|
|28|Cruise Tour|

---

# Recommended Mapping Process

## Step 1 – Primary Matching

Match sailings using:

- Cruise Line
- Ship
- Cruise Package Departure Date
- Duration
- VoyageId
- CruiseTourCode

---

## Step 2 – Secondary Validation

If multiple records are returned, refine the match using:

- Cruise Package Arrival Date
- Departure Port
- Arrival Port

This helps uniquely identify the correct sailing.

---

## Step 3 – Validate Sailing Type

Always verify whether the sailing is:

- Cruise Only
- Cruise Tour

If known in advance, include **TransportationType** in the initial filter to reduce ambiguity.

---

# Recommended Matching Priority

1. Cruise Line
2. Ship
3. CruisePackageDepartureDateTime
4. Duration
5. VoyageId
6. CruiseTourCode
7. CruisePackageArrivalDateTime
8. Departure Port
9. Arrival Port
10. TransportationType

---

# Prerequisites

This mapping strategy assumes your external cruise source provides:

- Ship
- Departure Date
- Duration
- VoyageId / SailId
- CruiseTourCode (for tours)
- Departure Port
- Arrival Port

---

# Risks of Incorrect Mapping

Incorrect PackageId mapping may result in:

- Booking the wrong sailing
- Booking the wrong cruise tour
- Pricing mismatches
- Incorrect itinerary
- Customer booking errors
- Supplier booking failures

---

# Best Practices

- Treat VoyageId as a primary matching field.
- Validate TransportationType whenever possible.
- Use Departure and Arrival ports as tie-breakers.
- Verify both package departure and arrival dates before persisting a mapping.
- Revalidate mappings whenever supplier sailing data changes.

---

# Related Articles

- PackageId
- Cruise Search
- Booking Flow
- Cruise Tour Concepts
- PortMasters
- CityMasters
