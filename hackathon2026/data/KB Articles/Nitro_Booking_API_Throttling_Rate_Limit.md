URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000033357071/en

ID: 80395000033357071
# Odysseus Nitro Booking API: Throttling / Rate Limit

## Overview
This article explains whether the **Odysseus Nitro Booking API** enforces throttling/rate limiting, what the current **sandbox** limits are, how the limit windows work, and what response to expect when throttled.

---

## Does Odysseus Throttle / Rate Limit?

**Yes** — throttling / rate limiting is enforced on the Odysseus Nitro Booking API.

---

## Sandbox Environment Limits

| Window | Limit |
|---|---|
| Per Minute | **25** requests |
| Per Hour | **1,000** requests |
| Per Day | **15,000** requests |

> **Note**: Production limits are **different and higher**, and will be documented separately later. The limits above apply **only to the sandbox environment**.

---

## How the Limit Windows Work

### Per-Minute Limit (25/min)
- If you exceed **25 requests within 1 minute**, you are **blocked for that minute only**.
- The block clears at the **start of the next minute** relative to when the window began.
- **Example**: First request received at `10:01:01`. You cross 25 requests at `10:01:42`. All subsequent requests are **rejected/blocked until `10:02:01`**.

### Per-Hour Limit (1,000/hour)
- If you exceed **1,000 requests within 1 hour**, you are **blocked for the remainder of that hour**, measured from the **1st request** in that window.
- **Example**: First request received at `10:01:01`. You cross 1,000 requests before `11:01:01`. All subsequent requests are **rejected/blocked until `11:01:01`**.

### Per-Day Limit (15,000/day)
- If you exceed **15,000 requests within a 24-hour period**, you are **blocked**.
- **Example**: First request received on **Jan 10, 10:01:01**. You cross 15,000 requests before **Jan 11, 10:01:01**. You are **blocked until Jan 11, 10:01:01**.

---

## Response When Throttled / Blocked

| Field | Value |
|---|---|
| HTTP Status Code | **`429`** (Too Many Requests) |

---

## Important Notes

1. **Rate limits are enforced at the customer level, not the IP address level.**
   - Whether you send requests from **1 IP** or **40 IPs**, the same limits above apply in aggregate to that customer.
2. **Time zones do not matter for rate limit calculations.**
   - The rate limit window is triggered based on **when the 1st request in that window was received** — not tied to any specific time zone.

---

## Quick Reference Table

| Limit Type | Threshold | Block Duration | Block Trigger Reference Point |
|---|---|---|---|
| Per Minute | 25 requests | Remainder of that minute | Start of the current minute window |
| Per Hour | 1,000 requests | Remainder of that hour | Time of the 1st request in that hour window |
| Per Day | 15,000 requests | Remainder of that 24-hour period | Time of the 1st request in that 24-hour window |

---

## Key Takeaways

- All three limit windows (**minute, hour, day**) are **independent and can trigger separately** — crossing the per-minute limit doesn't necessarily mean you've crossed the per-hour or per-day limit, but repeated per-minute violations will contribute toward the hour/day totals.
- Blocking is **temporary and window-based** — once the relevant window resets (per the reference point above), requests will succeed again, assuming no other limit is currently active.
- Throttling is identified by an **HTTP 429** response — client/integration logic should detect this status code and implement backoff/retry logic accordingly.
- Limits apply to the **customer as a whole**, so distributing requests across multiple IPs does **not** increase the effective limit.
- These limits are **sandbox-only** — do not assume production behaves the same; production limits are higher and will be published separately.
