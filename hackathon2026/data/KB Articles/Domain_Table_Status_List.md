URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000033205403/en 

ID: 80395000033205403

---
# Title: Domain Table - Status List
category: Domain Tables
tags:
  - status
  - booking
  - reservation
  - domain-table
last_updated: 2026-07
---

# Domain Table: Status List

## Purpose

The **Status List** defines the standardized status values returned throughout the Nitro Booking API. These statuses represent the lifecycle of sailings, cabins, reservations, payments, ticketing, and other booking operations.

Applications should treat these values as enumerations and use them to drive business logic and user interface behavior.

---

# Status Values

| ID | Status | Description |
|---:|--------|-------------|
| 1 | Available | Resource is available for booking. |
| 2 | Waitlisted | Availability is exhausted; customer may join the waitlist. |
| 3 | Closed | Booking or inventory is closed. |
| 4 | Sold Out | Inventory is fully sold. |
| 5 | Dry Docked | Ship is in dry dock and unavailable. |
| 6 | Held | Reservation or cabin is on hold. |
| 7 | Confirmed | Booking has been confirmed. |
| 8 | Partial Payment Applied | Partial payment has been received. |
| 9 | Paid in Full | Reservation has been fully paid. |
| 10 | On Request | Confirmation is pending supplier approval. |
| 11 | Active | Record is active. |
| 12 | Pending Confirmation | Awaiting confirmation from supplier or system. |
| 13 | Unavailable | Item is unavailable. |
| 14 | Cancelled | Reservation or item has been cancelled. |
| 15 | Not Applicable | Status is not applicable. |
| 16 | Offered | Item has been offered but not accepted. |
| 17 | Expired | Hold, offer, or record has expired. |
| 18 | Test | Test status used in non-production scenarios. |
| 19 | Ticketed | Tickets have been issued. |
| 20 | Fraud | Booking flagged for fraud review. |
| 21 | In Progress | Processing is underway. |
| 22 | Shipping in Progress | Documents or items are being shipped. |
| 23 | Credit Card Denied | Payment authorization failed. |
| 24 | Ticket with Supplier | Ticket issuance is pending or managed by the supplier. |
| 25 | Failed | Operation failed. |
| 26 | ePay/Ticketless | Electronic payment or ticketless processing. |
| 27 | Exchanged | Ticket or reservation has been exchanged. |
| 28 | Refunded | Refund has been processed. |
| 29 | Attention Required | Manual review or intervention is required. |

---

# Integration Guidance

- Treat status IDs as stable enumeration values.
- Store both the numeric ID and display name when possible.
- Drive UI behavior based on status instead of relying on text alone.
- Gracefully handle unknown future status values for forward compatibility.

---

# Common Status Categories

### Availability
- Available
- Waitlisted
- Closed
- Sold Out
- Unavailable

### Reservation
- Held
- Confirmed
- Cancelled
- Pending Confirmation
- In Progress

### Payment
- Partial Payment Applied
- Paid in Full
- Credit Card Denied
- Refunded

### Ticketing
- Ticketed
- Ticket with Supplier
- Exchanged
- ePay/Ticketless

---

# Best Practices

- Compare using the numeric status ID rather than localized text.
- Display user-friendly labels in the UI.
- Handle `Attention Required` by prompting for manual review.
- Avoid hardcoding assumptions about workflow transitions.

---

# Related Articles

- HTTP Status Codes, Errors and Advisories
- Booking Flow
- Reservation Status
- Payment Status
