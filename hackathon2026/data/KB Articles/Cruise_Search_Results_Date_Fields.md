URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000050288066/en

ID: 80395000050288066
# Cruise Search Results: What Do the Dates Mean?

## Overview
In the **Nitro API**, the cruise search response can return **three different sets of dates** describing a cruise sailing. This article explains what each set represents and how to interpret them correctly.

---

## Example Response Fields

```json
"startDateTime": "31-Mar-2024",
"endDateTime": "14-Apr-2024",
"departureDateTime": "31-Mar-2024",
"arrivalDateTime": "14-Apr-2024",
"cruisePackageDepartureDateTime": "31-Mar-2024",
"cruisePackageArrivalDateTime": "14-Apr-2024",
```

---

## Field Definitions

### 1. `departureDateTime` & `arrivalDateTime`
- Represents the **cruise sailing's actual departure and arrival dates**.
- This is the **true cruise segment** of the sailing (the actual ship voyage dates), independent of any surrounding package structure.

### 2. `cruisePackageDepartureDateTime` & `cruisePackageArrivalDateTime`
- Represents the departure/arrival dates of the **overall cruise package**.
- **When these differ from `departureDateTime` / `arrivalDateTime`**, it indicates that this is a **cruise line tour** — meaning the package includes a **pre-cruise and/or post-cruise segment** that extends or alters the overall package dates beyond the actual sailing dates.
- **Interpretation rule**: If `cruisePackageDepartureDateTime`/`cruisePackageArrivalDateTime` ≠ `departureDateTime`/`arrivalDateTime`, treat the package as including additional land/tour segments beyond the pure cruise.

### 3. `startDateTime` & `endDateTime`
- Linked to the **Custom Package ("CP") module**.
- For clients who create packages via **CP**, these fields represent the **start and end date of that custom package** — not necessarily the cruise sailing dates or the cruise package tour dates.

---

## Quick Reference Table

| Field(s) | Represents | Notes |
|---|---|---|
| `departureDateTime` / `arrivalDateTime` | True cruise sailing dates | The actual ship voyage — always the "real" cruise segment |
| `cruisePackageDepartureDateTime` / `cruisePackageArrivalDateTime` | Overall cruise package dates | If different from sailing dates → indicates a cruise line tour with pre/post segment(s) |
| `startDateTime` / `endDateTime` | Custom Package (CP) module dates | Only relevant for clients building packages via the CP module |

---

## Key Takeaways

- Do **not** assume all three date pairs represent the same thing — they can diverge depending on package type.
- A mismatch between `departureDateTime`/`arrivalDateTime` and `cruisePackageDepartureDateTime`/`cruisePackageArrivalDateTime` is a **signal**, not an error — it indicates a cruise line tour with additional pre/post segments.
- `startDateTime`/`endDateTime` only applies in the context of the **CP (Custom Package) module** and should not be confused with actual cruise sailing dates.
