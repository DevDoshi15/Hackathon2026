URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000110852542/en

ID: 80395000110852542
# Atlas Ocean Voyages (AOV) -- Mandatory Unique Guest Emails

## Overview

Atlas Ocean Voyages (AOV) requires **every guest** in a booking to have
a **unique email address**.

To support this supplier requirement, the **Odysseus Booking API
enforces guest-level unique email validation** for all AOV bookings.

Failure to provide unique guest email addresses may cause the booking
request to be rejected or fail during supplier processing.

------------------------------------------------------------------------

# Business Rule

For **Atlas Ocean Voyages (AOV)** bookings:

-   Every guest **must have a valid email address**.
-   Every guest **must have a unique email address**.
-   The same email address **must not be reused** for multiple guests
    within a booking.
-   Email addresses should be validated before submitting the Booking
    API request.

------------------------------------------------------------------------

# Why This Is Important

Atlas uses guest email addresses as the primary identifier for creating
and maintaining guest profiles.

Reusing an email address for multiple guests can result in:

-   Guest profile corruption
-   Profile overwrites
-   Duplicate guest profiles
-   Loyalty status loss
-   Incorrect booking history
-   Incorrect guest management

------------------------------------------------------------------------

# Real-World Scenarios

## Profile Overwrite

Emma and Liam travel together using **liam@example.com**.

A year later Emma books another cruise but again uses
**liam@example.com**.

Result:

-   Emma's profile may be overwritten with Liam's details.
-   Guest information becomes inconsistent.

------------------------------------------------------------------------

## Loss of Loyalty Benefits

Emma books one cruise using:

-   emma@example.com

Later she books using:

-   liam@example.com

Result:

-   Atlas creates two different guest profiles.
-   Loyalty history and benefits may not carry over.

------------------------------------------------------------------------

## Multiple Cabins

Cabin 1

-   Emma
-   Liam

Cabin 2

-   Noah

If **liam@example.com** is assigned to every guest:

-   Noah's profile may overwrite Liam's profile.
-   Guest records become corrupted.

------------------------------------------------------------------------

# Developer Requirements

Applications integrating with the Booking API should:

-   Ensure every guest has a valid email address.
-   Ensure every guest email is unique.
-   Prevent duplicate emails within the same booking.
-   Perform client-side email validation.
-   Update booking forms to require guest-specific email addresses.

------------------------------------------------------------------------

# Booking Request Location

Guest email is supplied under each customer object.

``` json
{
  "customers": [
    {
      "contactInfo": {
        "email": "liam@example.com"
      }
    }
  ]
}
```

The email must be unique for each guest in the `customers` array.

------------------------------------------------------------------------

# Validation Rules

  Validation         Requirement
  ------------------ ---------------------
  Email Required     Yes
  Email Format       Valid email address
  Unique Per Guest   Required
  Duplicate Emails   Not Allowed

------------------------------------------------------------------------

# Expected Behavior

## Valid

Guest 1

    emma@example.com

Guest 2

    liam@example.com

Booking proceeds.

## Invalid

Guest 1

    liam@example.com

Guest 2

    liam@example.com

Booking request is rejected or fails during supplier processing.

------------------------------------------------------------------------

# Common Questions

## Does every guest require an email?

Yes, for Atlas Ocean Voyages bookings.

## Can family members share the same email?

No.

Each guest must have their own unique email address.

## Should validation happen before calling the Booking API?

Yes. Client-side validation is strongly recommended.

------------------------------------------------------------------------

# Related Knowledge

-   Booking Request Schema
-   Customer Object
-   Contact Information
-   Supplier Validation Rules
-   Atlas Ocean Voyages (AOV) Integration
