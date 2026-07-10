URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000047677109/en

ID: 80395000047677109
# Cruise Booking API: Error/Advisory Codes

## Overview

The Booking API does **not normalize** Advisory or Error codes. All advisory/error codes are returned **exactly as provided by the cruise line** — unmodified, un-mapped to a common/internal code set.

## Implication

- Advisory/error codes will vary in format and meaning **from supplier to supplier** (e.g. MSC, RCCL, NCL, Carnival), since each cruise line defines its own codes.
- There is **no shared/normalized code table** across suppliers for these codes at the API level — consumers must interpret each code in the context of the specific supplier that returned it.
- Any mapping or normalization of advisory/error codes to a common meaning must happen on the **consuming side**, not within the Booking API itself.

## Integration Notes

- When diagnosing a failure or advisory from the API, always check which **supplier** the response came from before interpreting the code — the same code string can mean different things across different cruise lines.
- Do not assume a given advisory/error code is portable or consistent across suppliers; treat each supplier's codes as its own independent set.
