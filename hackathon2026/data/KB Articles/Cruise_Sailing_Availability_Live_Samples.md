URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=latest#Solutions/dv/80395000080308073/en/Article

ID: 80395000080308073

---
# Title: Cruise Sailing Availability (Live) Samples
category: API Examples
endpoint: /v2/reservation/cruise/SearchPackageWithSupplier
last_updated: 2026-07
---

# Cruise Sailing Availability (Live) Sample Files

This article accompanies the **SearchPackageWithSupplier** API and references the sample request/response files included in the uploaded archive.

## Purpose

The sample payloads demonstrate how to perform a live sailing search against the supplier and understand the structure of the request and response.

## Contents of Uploaded Archive

- `130386_CruiseSailingAvailability(Live)_RQ.json`
- `130386_CruiseSailingAvailability(Live)_RS.json`


## How to Use the Samples

1. Review the request payload and update filter values such as:
   - departureDateTime
   - duration
   - destinationId
   - cruiselineId
   - shipId
   - departurePortCode

2. Submit the request to:

```
POST /v2/reservation/cruise/SearchPackageWithSupplier
```

3. Parse the response and capture the returned **PackageId** for subsequent booking API calls.

## Key Response Fields

- PackageId
- VoyageId
- Cruise Line
- Ship
- Destination
- Cruise Package Departure Date
- Cruise Package Arrival Date
- Cruise Duration
- Itinerary

## Business Rules

- Live availability varies by supplier.
- Returned PackageIds should be treated as the source of truth for downstream reservation APIs.
- Apply filtering to reduce response size and improve performance.

## Best Practices

- Validate required filters before sending requests.
- Cache master data (ships, destinations, ports) using the Master API.
- Handle supplier-specific differences gracefully.
- Log request and response payloads for troubleshooting.

## Related Articles

- Cruise Sailing Availability (Live)
- Package ID Mapping
- Booking Flow
- Master API
