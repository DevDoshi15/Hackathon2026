URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000068264017/en

ID: 80395000068264017

---
# Title: Preset Timeouts When Communicating with Suppliers
category: Infrastructure
endpoint: All Transaction APIs
tags:
  - timeout
  - supplier
  - fto
  - forced-timeout
  - performance
last_updated: 2026-07
---

# Preset Timeouts When Communicating with Suppliers

## Purpose

Odysseus enforces predefined timeout thresholds when communicating with supplier systems to provide a consistent user experience and prevent requests from waiting indefinitely for supplier responses.

When a supplier exceeds the configured timeout threshold, the request is terminated and a **Forced Timeout (FTO)** is returned.

---

# Why Timeouts Exist

Supplier systems can occasionally experience:

- High traffic during peak periods
- Infrastructure issues
- Network latency
- Temporary outages
- Long-running backend processing

Rather than allowing requests to remain open indefinitely, Odysseus applies message-specific timeout limits.

---

# Timeout Strategy

Each API/message may have a different timeout value based on:

- Expected response time
- Supplier capabilities
- Business importance
- User experience considerations

These timeout thresholds are configured by Odysseus and may vary between different booking operations.

---

# Forced Timeout (FTO)

## Definition

A **Forced Timeout (FTO)** indicates that Odysseus stopped waiting for the supplier because the configured timeout threshold was exceeded.

An FTO does **not automatically mean** the supplier is unavailable, but it is treated as an indication that the supplier is experiencing an issue or is responding slower than the acceptable threshold.

---

# Expected Behavior

1. Client sends request to Nitro API.
2. Nitro forwards the request to the supplier.
3. Odysseus waits for the configured timeout period.
4. If the supplier responds within the threshold, the response is returned to the client.
5. If the timeout threshold is exceeded, Nitro returns a **Forced Timeout (FTO)**.

---

# Design Considerations

The configured timeout values are intentionally shorter than allowing requests to wait indefinitely because:

- Users receive faster feedback.
- Application threads are not blocked unnecessarily.
- System resources are protected.
- Slow supplier systems are detected consistently.
- Overall platform responsiveness is improved.

---

# Client Recommendations

Applications integrating with Nitro should:

- Handle FTO responses gracefully.
- Inform users that the supplier did not respond in time.
- Allow retry where appropriate.
- Log timeout occurrences for monitoring.
- Avoid immediately retrying repeatedly, which may increase supplier load.

---

# Troubleshooting

If frequent FTO responses occur:

- Verify supplier system health.
- Check whether the issue affects a specific supplier.
- Compare behavior between Sandbox and Production.
- Review network connectivity.
- Contact Odysseus Support if the issue persists.

---

# Best Practices

- Treat FTO as a supplier availability or performance issue.
- Implement retry logic with exponential backoff when appropriate.
- Monitor timeout frequency by supplier.
- Do not assume all suppliers have identical timeout thresholds.
- Design UI workflows that can recover from temporary supplier delays.

---

# Timeout Threshold Reference

Odysseus maintains predefined timeout values for individual API messages.

Refer to the accompanying timeout matrix/document for the exact timeout (in seconds) configured for each message, as these values may differ by operation.

---

# Related Articles

- HTTP Status Codes, Errors and Advisories
- Troubleshooting Guide
- Booking Flow
- Supplier Integrations
- Performance Best Practices
