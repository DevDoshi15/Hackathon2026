URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000033205202/en

ID: 80395000033205202

# Domain Table: Dynamic Rule Types

## Overview

`DynamicRuleTypes` is a domain enum used to classify the type of promotional/business rule applied to a booking or fare (e.g. onboard credit, discounts, free perks, cabin experience tiers). Each rule type has a fixed integer value used as its identifier throughout the system.

## Reference Table

| Value | Enum Name | Description | Status |
|---|---|---|---|
| 0 | `Undefined` | Not defined | Active |
| 1 | `OBC` | On Board Credits | Active |
| 2 | `Dining` | Free Dining | Active |
| 3 | `BEV` | Free Alcohol/Beverages | Active |
| 4 | `WiFi` | Free Internet/Wifi | Active |
| 5 | `FreeAir` | Free Air/Flight | Active |
| 6 | `Discount` | Discount | Active |
| 7 | `AddGSTDisc` | Additional Guest Discount | Active |
| 8 | `AddCHDDisc` | Additional Child Discount | **Deprecated** — no longer in use; child discount is now mapped to guest discount (`AddGSTDisc`) instead |
| 9 | `GRATS` | Gratuities | Active |
| 10 | `BOGO` | Buy One Get One Offer | Active |
| 11 | `BOGO50` | Buy One Get One 50% Off | **Deprecated** — no longer in use; mapped to `BOGO` instead |
| 12 | `KidsFree` | KidsFree | Active |
| 13 | `FreeUpg` | Free Upgrades | Active |
| 14 | `VALUE` | Value | Active |
| 15 | `PLUS` | Value Plus | Active |
| 16 | `NR` | Non Refundable | Active |
| 17 | `NRD` | Non Refundable Deposit | Active |
| 18 | `SHOREX` | Shorex Credit | Active |
| 19 | `GRATSI` | Gratuities Included | Active |
| 20 | `FIT` | Fitness Classes | Active |
| 21 | `REDDEP` | Reduced Deposit | Active |
| 22 | `BELLA` | Bella experiences | Active |
| 23 | `FANTASTICA` | Fantastica experiences | Active |
| 24 | `AUREA` | Aurea experiences | Active |
| 25 | `YACHT` | YachtClub experiences | Active |
| 26 | `PIF` | Pay In Full Discount | Active |
| 27 | `ALWAYS` | Always Included | Active |
| 28 | `ELEVATE` | Elevate Package | Active |
| 29 | `INDULGE` | Indulge Package | Active |
| 30 | `RETREAT` | Retreat Package | Active |
| 31 | `HALVV` | View & Verandah for Holland America | Active |
| 32 | `PREMIUM` | Premium all inclusive | Active |
| 33 | `CSTAllInc` | Costa All Inclusive | Active |
| 34 | `EBB` | Early Booking Bonus | Active |
| 35 | `INBOUNDAIR` | Inbound Air | Active |
| 36 | `OUTBOUNDAIR` | Outbound Air | Active |
| 37 | `ROUNDTRIPAIR` | Roundtrip Air | Active |
| 38 | `PHOTO` | Photoshoot package | Active |
| 39 | `SPA` | SPA Package | Active |
| 40 | `OLIFE` | OLIFE for Oceania | Active |
| 41 | `OLIFEU` | OLIFE ULTIMATE for Oceania | Active |
| 42 | `All` | All Included | Active |

## Deprecated Values — Mapping Notes

- **`AddCHDDisc` (8):** Child discount is no longer tracked as a separate rule type; it is mapped into `AddGSTDisc` (Additional Guest Discount, value 7).
- **`BOGO50` (11):** No longer tracked separately; mapped into `BOGO` (Buy One Get One Offer, value 10).

## Notable Supplier/Brand-Specific Rule Types

Some rule types are tied to a specific cruise line's branded experience tier or program rather than being generic across suppliers:
- `BELLA`, `FANTASTICA`, `AUREA` — Costa experience tiers
- `YACHT` — YachtClub experience
- `HALVV` — Holland America's "View & Verandah" program
- `PREMIUM` — Premium all-inclusive
- `CSTAllInc` — Costa's all-inclusive package
- `OLIFE` / `OLIFEU` — Oceania's OLife / OLife Ultimate programs
- `ELEVATE`, `INDULGE`, `RETREAT` — named package tiers
