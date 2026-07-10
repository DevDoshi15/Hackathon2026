URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000101725049/en 

ID: 80395000101725049

---
# Title: NCL Past Passenger Number - TrustPastPassengerNumber Enhancement
category: Supplier Enhancements
supplier: Norwegian Cruise Line (NCL)
endpoint:
  - Create Reservation
  - Modify Reservation
tags:
  - ncl
  - past-passenger
  - trustpastpassengernumber
  - loyalty
last_updated: 2026-07
---

# NCL Past Passenger Number - TrustPastPassengerNumber Enhancement

## Purpose

This enhancement introduces the **TrustPastPassengerNumber** reservation preference for Norwegian Cruise Line (NCL).

When enabled, Odysseus sends **only the Past Passenger Number** to NCL during Create/Modify Reservation requests instead of the full guest profile.

This helps prevent duplicate customer profiles and preserves past passenger promotional fares.

---

# Background

NCL updated its profile matching logic.

Previously, slight mismatches (for example, middle name or date of birth) could update an existing customer profile incorrectly.

NCL's new matching process instead creates a **new customer profile** when passenger details do not match exactly.

While this avoids incorrect profile updates, it can introduce new issues:

- Duplicate customer profiles
- Past passenger promotional fares being removed
- Incorrect loyalty recognition

---

# Solution

NCL introduced support for identifying guests using only their **Past Passenger Number**.

Odysseus exposes this capability through a new reservation preference:

```json
{
  "Type": "TrustPastPassengerNumber",
  "Value": true
}
```

When enabled:

- Odysseus sends only the `pastPaxNumber`.
- Guest details (name, DOB, email, etc.) are not sent to NCL.
- NCL retrieves the guest profile directly from the supplied Past Passenger Number.

---

# Example Request

```json
"ReservationPreferences": [
  {
    "Type": "TrustPastPassengerNumber",
    "Value": true
  }
]
```

Customer:

```json
{
  "rph": 1,
  "pastPaxNumber": "272413791"
}
```

---

# Business Rules

- Applies **only to NCL**.
- Supported for Create Reservation and Modify Reservation.
- Client is responsible for validating that the Past Passenger Number belongs to the correct traveler.
- Guest information is intentionally omitted when the option is enabled.

---

# Backward Compatibility

If `TrustPastPassengerNumber` is **not** supplied:

- Existing behavior continues.
- Odysseus sends both guest information and the Past Passenger Number.

No changes are required for existing integrations unless this new feature is desired.

---

# Recommended Workflow

1. Retrieve passenger information using the **GetPastPaxDetails** API.
2. Validate that the returned profile matches the traveler.
3. Submit Create/Modify Reservation with:
   - `TrustPastPassengerNumber = true`
   - `pastPaxNumber`
4. Allow NCL to populate the guest profile from its loyalty database.

---

# Benefits

- Reduces duplicate NCL customer profiles.
- Preserves past passenger promotional fares.
- Improves loyalty profile matching.
- Reduces profile update errors.

---

# Common Mistakes

## Trusting an Incorrect Past Passenger Number

The API assumes the supplied number has already been validated.

## Enabling the Option Without Validation

Always verify passenger details using GetPastPaxDetails before booking.

## Expecting Guest Details to be Sent

When enabled, Odysseus intentionally suppresses guest profile fields.

---

# Related Articles

- Booking API: Past Passenger Details via Past Passenger Number
- Create Reservation
- Modify Reservation
- NCL Supplier Integration
