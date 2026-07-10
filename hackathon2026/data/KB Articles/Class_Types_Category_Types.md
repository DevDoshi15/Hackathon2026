URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000050153003/en

ID: 80395000050153003
# Class Types / Category Types

## Overview
This article explains the `type` field returned for a **category**, which indicates the **class type** (also referred to as the **meta category**) of that cabin category.

---

## Category `type` Values (Meta Category)

| `type` value | Meta Category |
|---|---|
| `1` | Inside / Interior |
| `2` | Outside / Oceanview |
| `3` | Balcony |
| `4` | Suite |

---

## Key Takeaways

- The `type` field on a category is **not the specific cabin category itself** — it's a higher-level grouping (meta category) that classifies which broad class of cabin the category belongs to.
- Use this field to group or filter categories by broad cabin class (e.g., show all "Balcony" categories) regardless of the specific category codes/names returned by the supplier.
- There are only **4 possible values**: `1`, `2`, `3`, `4` — mapping to Inside, Outside, Balcony, and Suite respectively.
