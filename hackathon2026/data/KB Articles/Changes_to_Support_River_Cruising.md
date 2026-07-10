URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=latest#Solutions/dv/80395000101370001/en 

ID: 80395000101370001

---
# Title: Changes to Support River Cruising in Data Cache and Itinerary API
category: API Changes
effective_release: February Production Release
tags:
  - river-cruise
  - itinerary
  - data-cache
  - api-change
last_updated: 2026-07
---

# Changes to Support River Cruising

## Purpose

Odysseus has enhanced the Itinerary API and itinerary data cache to properly distinguish **River Cruises** from traditional ocean cruises.

Previously, itinerary nodes representing days away from a port always used the equivalent of **Sea**, causing river cruise itineraries to display **"At Sea"** even when the ship was sailing on a river.

This enhancement introduces a dedicated **River** itinerary type.

---

# Background

Historically:

- Ocean cruises → At Sea ✅
- River cruises → At Sea ❌

After this enhancement:

- Ocean cruises → At Sea
- River cruises → At River

---

# Impacted Components

The change affects:

- Itinerary API responses
- Itinerary Data Cache files
- NormalizedPortsOfCallDetails
- ItineraryJson

---

# Changed Field

Within the itinerary response:

```
root
 └── nodes[]
      └── type
```

## Previous Behavior

```
type = Sea
```

Used for both:

- Ocean cruising
- River cruising

---

## New Behavior

```
type = Sea
```

Ocean cruises

```
type = River
```

River cruises (when supplied by the cruise line)

---

# Business Rules

- The value **River** is returned only when supported by the supplier.
- Ocean cruise behavior is unchanged.
- Existing Sea values continue for ocean itineraries.
- This affects all suppliers offering river cruises.

---

# Data Cache Changes

The enhancement applies to:

## NormalizedPortsOfCallDetails

Before

```
Type = 1 (Sea)
```

After

```
Type = 11 (River)
```

*(Values shown are representative of the updated mapping.)*

---

## ItineraryJson

Before

```
"Type": 1
```

Displayed as:

```
At Sea
```

After

```
"Type": 11
```

Displayed as:

```
At River
```

---

# Integration Impact

Applications consuming itinerary data should:

- Support the new River itinerary type.
- Update UI labels to display **At River** instead of **At Sea**.
- Avoid assuming all non-port days are ocean sea days.
- Handle unknown future itinerary node types gracefully.

---

# Backward Compatibility

Existing integrations supporting **Sea** continue to function.

To fully support river cruising, clients should add handling for the new **River** type.

---

# Best Practices

- Treat itinerary node type as an extensible enumeration.
- Do not hardcode only Sea and Port values.
- Use supplier-provided itinerary types whenever available.
- Test both ocean and river cruise itineraries after deployment.

---

# Related Articles

- Get Cruise Itinerary from Supplier
- Itinerary API
- Data Cache Files
- Transportation Types
