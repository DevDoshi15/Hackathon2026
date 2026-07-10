URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000117981332/en

ID: 80395000117981332
# Knowledge Base: Norwegian Cruise Line (NCL) Pricing Update -- Inclusion of More At Sea (MAS) Program Costs (US & Canada Only)

## Overview

Norwegian Cruise Line (NCL) has enhanced pricing for the **More At Sea
(MAS)** program by including MAS-related service charges in the
**Category (ListCategories)** step of the booking flow.

Previously, these costs were not reflected until later in the booking
process. Odysseus now calculates and includes these charges in category
pricing to provide a more accurate upfront price.

------------------------------------------------------------------------

# Scope

-   **Supplier:** Norwegian Cruise Line (NCL)
-   **Markets:** United States (US) and Canada (CA) only
-   **Impacted API:** `ListCategories`
-   **Environment:** Implemented in TEST by NCL and enabled by Odysseus
    in Sandbox/CDN/UAT. Production will be enabled after NCL's
    production rollout.

------------------------------------------------------------------------

# Background

### Previous Behavior

-   MAS service charges were **not included** in the Category response.
-   Initial category pricing understated the final cost.
-   MAS costs became visible later in the booking flow.

### New Behavior

-   Category pricing now **includes MAS program costs**.
-   The booking flow displays a more accurate upfront total.
-   No request or response schema changes are required.

------------------------------------------------------------------------

# API Impact

## Request Structure

**No changes.**

Existing `ListCategories` requests continue to work unchanged.

## Response Structure

**No structural changes.**

Odysseus updates pricing values internally while keeping the response
schema identical.

------------------------------------------------------------------------

# Pricing Logic

Odysseus---not the supplier---calculates MAS pricing by comparing
**EASYFARE** with applicable **MAS fares**.

The Category response is updated before it is returned to clients.

### Before

-   Base amount excluded MAS charges.
-   Example:
    -   `amount = 1260.00`
-   MAS promotion cost not included.

### After

-   Base amount includes MAS charges.
-   Example:
    -   `amount = 1420.00`
    -   `includedFees = 160.00`

`includedFees` represents the MAS promotion cost incorporated into the
displayed category price.

------------------------------------------------------------------------

# Business Rules

1.  Applies only to US and Canadian markets.
2.  No request modifications are required.
3.  No response schema changes are introduced.
4.  Category pricing now reflects MAS-related charges.
5.  Odysseus performs the pricing calculation.
6.  Supplier does not return the MAS fee directly.
7.  Pricing responses remain structurally unchanged.

------------------------------------------------------------------------

# Client Impact

Clients do **not** need to modify their integrations.

Expected changes:

-   Higher category totals where MAS applies.
-   More accurate upfront pricing.
-   Existing parsing logic continues to work.

------------------------------------------------------------------------

# Environment Rollout

  Environment        Status
  ------------------ --------------------------------
  NCL TEST           Enabled
  Odysseus Sandbox   Enabled
  CDN                Enabled
  UAT                Enabled
  Production         Pending NCL production release

------------------------------------------------------------------------

# Troubleshooting

### Category price increased

Expected behavior when MAS applies. The increase includes MAS program
charges.

### No `includedFees` returned

Verify: - Booking is for the US or Canada market. - Selected fare
qualifies for MAS. - Environment has the feature enabled.

### Response format changed?

No. Only pricing values change; the API schema remains the same.

------------------------------------------------------------------------

# Agent Knowledge

The AI agent should know:

-   MAS pricing enhancement applies only to US/CA.
-   No API request or response changes are required.
-   Odysseus calculates MAS charges by comparing EASYFARE and MAS fares.
-   Category totals now include MAS costs.
-   `includedFees` represents the MAS promotion amount when applicable.
-   Pricing responses remain backward compatible.

------------------------------------------------------------------------

# Search Keywords

NCL, Norwegian Cruise Line, More At Sea, MAS, ListCategories, Category
Pricing, includedFees, EASYFARE, Pricing Update, US Market, Canada
Market, Booking API
