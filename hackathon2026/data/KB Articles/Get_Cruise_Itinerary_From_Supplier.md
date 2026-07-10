URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000080308005/en

ID: 80395000080308005

---
# Title: Get Cruise Itinerary from Supplier
category: Transaction API
endpoint: /v2/reservation/cruise/getitineraryfromsupplier
method: POST
tags:
  - itinerary
  - supplier
  - live
  - packageid
last_updated: 2026-07
---

# Get Cruise Itinerary from Supplier

## Purpose

The **Get Cruise Itinerary from Supplier** API retrieves the **live, detailed itinerary** for a cruise package directly from the cruise line using a **PackageId**.

Unlike cached itinerary information, this endpoint requests the latest itinerary from the supplier.

---

# Endpoint

```http
POST /v2/reservation/cruise/getitineraryfromsupplier
```

---

# When to Use

Use this API when you need:

- The latest itinerary directly from the supplier
- Detailed day-by-day itinerary information
- Live itinerary validation before booking
- Updated itinerary after obtaining a PackageId

---

# Prerequisites

A valid **PackageId** is required.

PackageId can be obtained from:

- Search Package With Supplier API
- Cruise Data Cache (`cruises.zip`)

---

# Required Parameters

| Field | Required | Description |
|------|:--------:|-------------|
| packageId | ✅ | Odysseus Package ID identifying the sailing |

---

# Request Structure

```json
{
  "cruiseReservation": {
    "cruise": {
      "packageId": 1330761
    }
  },
  "trackingInfo": {
    "token": "EQTEMPKEN"
  }
}
```

---

# Request Field Details

## cruiseReservation.cruise.packageId

Unique Odysseus Package ID for the sailing.

This is the only business parameter required by this API.

## trackingInfo.token

Correlation token used for request tracking and diagnostics.

---

# Response Overview

When successful, the response contains:

- Itinerary ID
- Ordered itinerary nodes
- Departure and arrival times
- Day offsets
- Port information
- Port type
- Descriptions (hotel stay, embarkation, ports, disembarkation, etc.)

---

# Itinerary Node Structure

Each itinerary node may contain:

| Field | Description |
|------|-------------|
| departureTime | Departure time from the location |
| arrivalTime | Arrival time at the location |
| dayOffset | Relative day within the itinerary |
| description | Human-readable itinerary event |
| port.code | Port or city code |
| port.type | City or CruisePort |
| port.internalCode | Internal Odysseus code |

---

# Example Response Events

Typical itinerary events include:

- Hotel Check-In
- Hotel Check-Out
- Embarkation Port
- Cruise Ports of Call
- Sea Days (supplier dependent)
- Final Disembarkation

---

# Business Rules

- Live itinerary support varies by cruise line.
- The itinerary returned reflects the supplier's current information.
- A valid PackageId is mandatory.
- PackageIds should be obtained from supported search APIs or the data cache.

---

# Common Errors

| Scenario | Result |
|----------|--------|
| Missing packageId | Validation error |
| Invalid PackageId | Package not found |
| Unsupported supplier | Supplier error |
| Supplier unavailable | Timeout or supplier error |

---

# Best Practices

- Always validate PackageId before calling this API.
- Fetch PackageId using the latest live search when itinerary accuracy is critical.
- Do not assume cached itineraries match the supplier's latest itinerary.
- Log tracking tokens to simplify troubleshooting.

---

# Integration Flow

```text
Cruise Search / SearchPackageWithSupplier
            │
            ▼
      Obtain PackageId
            │
            ▼
Get Cruise Itinerary from Supplier
            │
            ▼
Use itinerary for booking flow or customer display
```

---

# Related Articles

- Search Package With Supplier
- Package ID Mapping
- Booking Flow
- Cruise Search
- Data Cache Files
