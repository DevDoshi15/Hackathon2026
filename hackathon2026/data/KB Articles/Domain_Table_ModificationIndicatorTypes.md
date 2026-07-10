URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000050293151/en

ID: 80395000050293151
# Domain Table: ModificationIndicatorTypes (Modification Indicator Types)

## Overview
This is the domain/enum reference table for **`ModificationIndicatorTypes`** — the list of indicators the system can return to signal what aspect of a booking is modifiable (or was modified).

```csharp
public enum ModificationIndicatorTypes
{
    Undefined = 0,
    Cabin = 101,
    Category = 102,
    Dining = 103,
    FareCode = 104,
    Insurance = 105,
    SpecialService = 106,
    Packages = 107,
    Transfer = 108,
    AddOn = 110,
    Bed = 111,
    LinkedBooking = 112,
    FirstName = 121,
    LastName = 122,
    BirthDate = 123,
    Title = 124,
    Citizenship = 125,
    AddPassenger = 126,
    RemovePassenger = 127,
    Address = 128,
    FirstPassengerName = 131,
    OtherPassengerName = 132
}
```

---

## Value Reference Table

| Value | Name | Description |
|---|---|---|
| `0` | `Undefined` | Undefined |
| `101` | `Cabin` | Cabin |
| `102` | `Category` | Category |
| `103` | `Dining` | Dining |
| `104` | `FareCode` | Fare Code |
| `105` | `Insurance` | Cruise line insurance |
| `106` | `SpecialService` | Special service |
| `107` | `Packages` | Packages |
| `108` | `Transfer` | Transfer |
| `110` | `AddOn` | Add-on |
| `111` | `Bed` | Bed |
| `112` | `LinkedBooking` | Linked booking |
| `121` | `FirstName` | Passenger first name — editable |
| `122` | `LastName` | Passenger last name — editable |
| `123` | `BirthDate` | Birth date |
| `124` | `Title` | Title |
| `125` | `Citizenship` | Citizenship |
| `126` | `AddPassenger` | Add passenger |
| `127` | `RemovePassenger` | Remove passenger |
| `128` | `Address` | Address |
| `131` | `FirstPassengerName` | First customer name |
| `132` | `OtherPassengerName` | Other customer name |

---

## Grouping Notes (by value range)

- **0**: Reserved for `Undefined` — no modification type specified.
- **101–112**: Booking-component-level modification indicators (Cabin, Category, Dining, FareCode, Insurance, SpecialService, Packages, Transfer, AddOn, Bed, LinkedBooking). Note: value `109` is **not defined** in this enum (gap between `Transfer = 108` and `AddOn = 110`).
- **121–128**: Passenger-detail-level modification indicators (FirstName, LastName, BirthDate, Title, Citizenship, AddPassenger, RemovePassenger, Address).
- **131–132**: Passenger-name-specific indicators distinguishing the **first/primary customer name** (`131`) from **other customer names** (`132`) on the booking.

---

## Key Takeaways

- This enum is used to indicate **what kind of modification** is being flagged/allowed on a booking (e.g., is the cabin modifiable, is the fare code modifiable, can a passenger's birth date be edited, etc.).
- Values are **not sequential** — there's a deliberate range grouping: booking-component indicators (101–112), passenger-detail indicators (121–128), and passenger-name indicators (131–132).
- Value `109` is intentionally absent/unused between `Transfer (108)` and `AddOn (110)`.
- `FirstPassengerName (131)` and `OtherPassengerName (132)` are distinct from `FirstName (121)` / `LastName (122)` — the former relate to which **customer/passenger** the name belongs to (primary vs. other), while the latter relate to the **name field type** itself (first name vs. last name).
