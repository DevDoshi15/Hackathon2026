URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000110852508/en

ID: 80395000110852508
# Knowledge Base: Viking Cruises -- Mandatory Residency-Based Currency (Booking API)

## Overview

Viking Cruises (River, Ocean, and Expedition) now mandates that the
booking currency **must match the guest's country of residency**.

Previously, Odysseus allowed: - Canadian (CA) residents to book in
**USD** - United States (US) residents to book in **CAD**

This is **no longer supported** due to a cruise line mandate.

Odysseus has enhanced the **Booking API** and Booking Engine to
automatically switch the booking currency based on the guest's residency
during the **Create Booking** flow.

------------------------------------------------------------------------

## Scope

-   Supplier: Viking Cruises
-   Brands:
    -   River
    -   Ocean
    -   Expedition
-   Applies only to:
    -   United States (US)
    -   Canada (CA)

------------------------------------------------------------------------

## Business Rules

  Guest Residency      Required Currency
  -------------------- -------------------
  Canada (CA)          CAD
  United States (US)   USD

If the office setup currency differs from the required residency
currency, Odysseus automatically changes the booking currency.

------------------------------------------------------------------------

## Currency Switching Logic

### Office Currency = USD

#### Guest Residency = Canada (CA)

-   Request residency: CA
-   Office currency: USD
-   Result:
    -   Currency automatically switches to **CAD**
    -   Warning returned:
        -   `CurrencyChanged`
        -   Prices displayed in CAD based on CA residency

#### Guest Residency = United States (US)

-   Request residency: US
-   Office currency: USD
-   Result:
    -   Currency remains USD
    -   No currency switch

------------------------------------------------------------------------

### Office Currency = CAD

#### Guest Residency = United States (US)

-   Request residency: US
-   Office currency: CAD
-   Result:
    -   Currency automatically switches to **USD**
    -   Warning returned:
        -   `CurrencyChanged`
        -   Prices displayed in USD based on US residency

#### Guest Residency = Canada (CA)

-   Request residency: CA
-   Office currency: CAD
-   Result:
    -   Currency remains CAD
    -   No currency switch

------------------------------------------------------------------------

## Booking API Behavior

When a Create Booking request is received:

1.  Read guest residency from the passenger address.
2.  Determine required booking currency.
3.  Compare with office currency.
4.  If different:
    -   Override request currency.
    -   Send booking using residency currency.
    -   Return `CurrencyChanged` warning.
5.  If same:
    -   Continue without modification.

------------------------------------------------------------------------

## API Response

When currency changes:

-   POS currency reflects the new currency.
-   Warning object is included.

Example:

``` json
{
  "message": "The prices for this booking will be displayed in CAD based on your residency selection of CA",
  "description": "CurrencyChanged",
  "type": "warning"
}
```

The `pos.currency` value will also reflect the updated currency.

------------------------------------------------------------------------

## Important Notes

-   Applies **only** to US and Canadian residents.
-   Odysseus performs the currency switch automatically.
-   Cruise line responses always use the currency actually submitted.
-   This enhancement affects **Create Booking only**.
-   Currency **cannot be changed** during Modify Booking.
-   If residency changes after booking, Viking may update the booking
    currency.

------------------------------------------------------------------------

## FAQ

### Why is currency changing automatically?

Because Viking requires bookings to use the guest's local residency
currency.

### Can clients override the currency?

No.

### Does this affect Modify Booking?

No.

### Is every market affected?

No. Only US and Canada.

------------------------------------------------------------------------

## Summary

-   CA Resident → CAD
-   US Resident → USD
-   Currency mismatch → Automatically corrected
-   Matching currency → No change
-   Currency switching occurs only during Create Booking
-   Modify Booking preserves the original booking currency
