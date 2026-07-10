URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000041641001/en 

ID: 80395000041641001

---
# Title: Read/Retrieve Booking Message(s)
category: Booking API
tags:
  - booking
  - read reservation
  - supplier sync
---

# Read/Retrieve Booking Message(s)

## Overview

The Booking API provides two ways to retrieve reservation information depending on the desired source.

| Message | Source | Description |
|---------|--------|-------------|
| **Read** | Odysseus Database | Returns the booking as stored within the Odysseus platform. |
| **ReadFromSupplier** | Cruise Line / Supplier | Retrieves the latest booking directly from the supplier in real time. |

---

# 1. Read

Reads the booking from the **Odysseus database**.

Use this when:
- Retrieving the locally stored reservation.
- Live supplier synchronization is not required.
- Fast response time is preferred.

---

# 2. ReadFromSupplier

Reads the booking directly from the cruise line.

This call retrieves the latest reservation information and can also synchronize supplier changes back into the Odysseus database.

## Read Modes

The `Mode` parameter controls how the booking is accessed.

| Mode | Description |
|------|-------------|
| **View** | Booking is not locked. Intended for viewing or reviewing reservation details. |
| **Modify** | Locks the booking at the supplier before modification. Recommended immediately before calling Modify Booking. |
| **Pay** | Similar to Modify mode, but indicates the intention is payment only. |

> **Note**
>
> Some cruise lines lock reservations during modification. Using the appropriate mode helps prevent conflicting updates.

---

## AutoSyncOption

`AutoSyncOption` controls how supplier data updates the Odysseus database.

| Value | Behavior |
|--------|----------|
| **UNDEFINED** | Uses the Site Preference configuration. |
| **NOLOCK** | Synchronizes all booking information, including prices and package details. |
| **LOCK** | Does not update any local booking information. |
| **LOCKPRICES** | Updates package information but does **not** update prices. |

---

# Recommended Usage

### View Reservation

- ReadFromSupplier
- Mode = View
- AutoSyncOption = UNDEFINED (or Site Preference)

### Modify Reservation

1. ReadFromSupplier
2. Mode = Modify
3. Perform Modify Booking

### Payment

1. ReadFromSupplier
2. Mode = Pay
3. Submit Payment

---

# Important Behavior

> **Alert**
>
> If an agent manually performs **Cross Check with Supplier**, or edits/modifies the booking through the Odysseus Booking Engine, those actions override the `LOCK` AutoSyncOption settings.

---

# Best Practices

- Use **Read** when live supplier data is unnecessary.
- Use **ReadFromSupplier** before Modify or Pay operations.
- Select the appropriate `Mode` to prevent conflicting updates.
- Use `LOCK` or `LOCKPRICES` only when synchronization should be restricted.
- Allow `UNDEFINED` when Site Preferences should determine synchronization behavior.

---

# Related Articles

- Read Reservation
- Modify Reservation
- Payment Processing
- Booking Flags
- HTTP Status Codes, Errors and Advisories
