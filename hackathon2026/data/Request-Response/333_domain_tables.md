# Domain Tables

**Path:** Domain Tables > Domain Tables

---

## Request Details

**Method:** `GET`

**URL:** `{{BaseUrl}}/v2/DomainTables`

### Headers

```
SiteItemId: {{Nitro.Sandbox.SiteItemId}}
```

### Authentication

**Type:** basic

```
password: {{Nitro.Sandbox.ClientSecret}}
username: {{Nitro.Sandbox.ClientId}}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Mon, 03 Jun 2024 16:00:36 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Served-From: 208.64.67.225
X-Powered-By: ASP.NET
X-Server-Ip: 192.168.214.15
Content-Encoding: gzip
```

### Response Body

```json
{
  "isSucceed": true,
  "data": [
    {
      "entityType": "RuleGroupTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "Discount"
        },
        {
          "value": 2,
          "name": "Markup"
        },
        {
          "value": 3,
          "name": "ValueAddOffer"
        },
        {
          "value": 4,
          "name": "InsuranceIncluded"
        },
        {
          "value": 5,
          "name": "OnBoardCredit"
        },
        {
          "value": 6,
          "name": "RewardPoints"
        },
        {
          "value": 7,
          "name": "BookingFee"
        },
        {
          "value": 8,
          "name": "PaymentDepositDiscount"
        },
        {
          "value": 9,
          "name": "AddOnOptions"
        },
        {
          "value": 10,
          "name": "NonRefundableDeposit"
        },
        {
          "value": 11,
          "name": "AgentCommission"
        },
        {
          "value": 12,
          "name": "BestPriceGuarantee"
        },
        {
          "value": 13,
          "name": "ServiceFee"
        },
        {
          "value": 14,
          "name": "SupplierCommission"
        },
        {
          "value": 15,
          "name": "AddOnHotel"
        },
        {
          "value": 16,
          "name": "AddOnFlights"
        },
        {
          "value": 17,
          "name": "FixedPrice"
        },
        {
          "value": 18,
          "name": "PackageService"
        },
        {
          "value": 19,
          "name": "PaymentInstallmentsOptions"
        },
        {
          "value": 30,
          "name": "ValueAddOfferAffiliate"
        },
        {
          "value": 40,
          "name": "ValueAddOfferConsolidator"
        },
        {
          "value": 50,
          "name": "MasterPromotion"
        },
        {
          "value": 51,
          "name": "RuleDiscount"
        },
        {
          "value": 52,
          "name": "RuleMarkup"
        },
        {
          "value": 100,
          "name": "PaymentProcessingFee"
        },
        {
          "value": 101,
          "name": "ExcludePackage"
        },
        {
          "value": 102,
          "name": "DisplayPriceOnly"
        },
        {
          "value": 103,
          "name": "AirDisplayName"
        },
        {
          "value": 104,
          "name": "AirTicketType"
        },
        {
          "value": 105,
          "name": "BookWithAgent"
        },
        {
          "value": 106,
          "name": "Recommended"
        },
        {
          "value": 107,
          "name": "DisplayPrice"
        },
        {
          "value": 108,
          "name": "ProductExperience"
        },
        {
          "value": 109,
          "name": "FareCodeModify"
        },
        {
          "value": 110,
          "name": "MerchantFlag"
        },
        {
          "value": 111,
          "name": "DynamicNetRateCalculation"
        },
        {
          "value": 112,
          "name": "DynamicRules"
        },
        {
          "value": 201,
          "name": "SupplierPromoCodeInclude"
        },
        {
          "value": 202,
          "name": "BookingOption"
        },
        {
          "value": 401,
          "name": "Advertising"
        }
      ]
    },
    {
      "entityType": "ModificationIndicatorTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 101,
          "name": "Cabin"
        },
        {
          "value": 102,
          "name": "Category"
        },
        {
          "value": 103,
          "name": "Dining"
        },
        {
          "value": 104,
          "name": "FareCode"
        },
        {
          "value": 105,
          "name": "Insurance"
        },
        {
          "value": 106,
          "name": "SpecialService"
        },
        {
          "value": 107,
          "name": "Packages"
        },
        {
          "value": 108,
          "name": "Transfer"
        },
        {
          "value": 110,
          "name": "AddOn"
        },
        {
          "value": 111,
          "name": "Bed"
        },
        {
          "value": 112,
          "name": "LinkedBooking"
        },
        {
          "value": 121,
          "name": "FirstName"
        },
        {
          "value": 122,
          "name": "LastName"
        },
        {
          "value": 123,
          "name": "BirthDate"
        },
        {
          "value": 124,
          "name": "Title"
        },
        {
          "value": 125,
          "name": "Citizenship"
        },
        {
          "value": 126,
          "name": "AddPassenger"
        },
        {
          "value": 127,
          "name": "RemovePassenger"
        },
        {
          "value": 128,
          "name": "Address"
        },
        {
          "value": 131,
          "name": "FirstPassengerName"
        },
        {
          "value": 132,
          "name": "OtherPassengerName"
        }
      ]
    },
    {
      "entityType": "PackageTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "PrePackage"
        },
        {
          "value": 2,
          "name": "PostPackage"
        },
        {
          "value": 3,
          "name": "PreTransfer"
        },
        {
          "value": 4,
          "name": "PostTransfer"
        },
        {
          "value": 5,
          "name": "RoundTransfer"
        },
        {
          "value": 6,
          "name": "PreBus"
        },
        {
          "value": 7,
          "name": "PostBus"
        },
        {
          "value": 8,
          "name": "PreAir"
        },
        {
          "value": 9,
          "name": "PostAir"
        },
        {
          "value": 10,
          "name": "RoundAir"
        },
        {
          "value": 11,
          "name": "ShoreExcursion"
        },
        {
          "value": 12,
          "name": "Activity"
        },
        {
          "value": 13,
          "name": "OnBoardActivity"
        },
        {
          "value": 14,
          "name": "OnBoardService"
        },
        {
          "value": 15,
          "name": "PreCruiseOptions"
        },
        {
          "value": 16,
          "name": "PostCruiseOptions"
        }
      ]
    },
    {
      "entityType": "JourneyTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 30,
          "name": "Pre"
        },
        {
          "value": 31,
          "name": "Post"
        },
        {
          "value": 32,
          "name": "RoundTrip"
        }
      ]
    },
    {
      "entityType": "FareGroupTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "Agency"
        },
        {
          "value": 2,
          "name": "HeadQuater"
        }
      ]
    },
    {
      "entityType": "FarePreferenceTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "Military"
        },
        {
          "value": 2,
          "name": "Police"
        },
        {
          "value": 3,
          "name": "Interline"
        },
        {
          "value": 4,
          "name": "Union"
        },
        {
          "value": 5,
          "name": "Teacher"
        },
        {
          "value": 6,
          "name": "Accessible"
        },
        {
          "value": 7,
          "name": "ConnectingCabins"
        },
        {
          "value": 8,
          "name": "PromoCode"
        },
        {
          "value": 9,
          "name": "SupplierPromoCode"
        },
        {
          "value": 10,
          "name": "ExcludeNonRefundable"
        },
        {
          "value": 11,
          "name": "FireFighter"
        },
        {
          "value": 12,
          "name": "PastPassenger"
        },
        {
          "value": 13,
          "name": "CustomerType"
        }
      ]
    },
    {
      "entityType": "ReadModes",
      "data": [
        {
          "value": 0,
          "name": "View"
        },
        {
          "value": 1,
          "name": "Modify"
        },
        {
          "value": 2,
          "name": "Pay"
        }
      ]
    },
    {
      "entityType": "AutoSyncOptions",
      "data": [
        {
          "value": 0,
          "name": "UNDEFINED"
        },
        {
          "value": 1,
          "name": "NOLOCK"
        },
        {
          "value": 2,
          "name": "LOCK"
        },
        {
          "value": 3,
          "name": "LOCKPRICES"
        }
      ]
    },
    {
      "entityType": "LinkedBookingTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "Booking"
        },
        {
          "value": 2,
          "name": "Dining"
        },
        {
          "value": 3,
          "name": "BookingAndDining"
        }
      ]
    },
    {
      "entityType": "InsuranceTypes",
      "data": [
        {
          "value": 0,
          "name": "Unknown"
        },
        {
          "value": 1,
          "name": "Exteranal"
        },
        {
          "value": 2,
          "name": "Supplier"
        }
      ]
    },
    {
      "entityType": "MandatoryIndicatorTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 6,
          "name": "CitizenShip"
        },
        {
          "value": 8,
          "name": "Residency"
        },
        {
          "value": 9,
          "name": "Insurance"
        },
        {
          "value": 11,
          "name": "Age"
        },
        {
          "value": 12,
          "name": "Title"
        },
        {
          "value": 13,
          "name": "Address"
        },
        {
          "value": 14,
          "name": "Gender"
        },
        {
          "value": 15,
          "name": "PhoneNumber"
        },
        {
          "value": 16,
          "name": "DiningSeating"
        },
        {
          "value": 23,
          "name": "City"
        },
        {
          "value": 38,
          "name": "PassportRequired"
        },
        {
          "value": 41,
          "name": "PassportIssueDate"
        },
        {
          "value": 42,
          "name": "PassportExpirationDate"
        },
        {
          "value": 43,
          "name": "EmergencyPhone"
        },
        {
          "value": 45,
          "name": "TableSize"
        },
        {
          "value": 600,
          "name": "FlightInformation"
        },
        {
          "value": 1001,
          "name": "EMail"
        },
        {
          "value": 1002,
          "name": "Payment"
        }
      ]
    },
    {
      "entityType": "Genders",
      "data": [
        {
          "value": 0,
          "name": "Male"
        },
        {
          "value": 1,
          "name": "Female"
        },
        {
          "value": 2,
          "name": "Unknown"
        }
      ]
    },
    {
      "entityType": "AgeGroupTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "Adult"
        },
        {
          "value": 2,
          "name": "Senior"
        },
        {
          "value": 3,
          "name": "Child"
        },
        {
          "value": 4,
          "name": "Infant"
        },
        {
          "value": 5,
          "name": "SeatedInfant"
        },
        {
          "value": 6,
          "name": "Youth"
        }
      ]
    },
    {
      "entityType": "PayeeTypes",
      "data": [
        {
          "value": 0,
          "name": "Customer"
        },
        {
          "value": 1,
          "name": "Affiliate"
        },
        {
          "value": 2,
          "name": "Supplier"
        }
      ]
    },
    {
      "entityType": "PaymentForms",
      "data": [
        {
          "value": 0,
          "name": "None"
        },
        {
          "value": 1,
          "name": "Card"
        },
        {
          "value": 2,
          "name": "Cash"
        },
        {
          "value": 3,
          "name": "Check"
        },
        {
          "value": 4,
          "name": "AgencyCheck"
        },
        {
          "value": 5,
          "name": "EFT"
        },
        {
          "value": 6,
          "name": "GiftCertificate"
        },
        {
          "value": 7,
          "name": "RewardPoints"
        }
      ]
    },
    {
      "entityType": "PaymentStatuses",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "Failure"
        },
        {
          "value": 2,
          "name": "Success"
        },
        {
          "value": 3,
          "name": "PendingConfirmation"
        }
      ]
    },
    {
      "entityType": "BreakdownTypes",
      "data": [
        {
          "value": 0,
          "name": "None"
        },
        {
          "value": 1,
          "name": "AVGPP"
        },
        {
          "value": 2,
          "name": "AVGPN"
        },
        {
          "value": 3,
          "name": "AVGPPPN"
        },
        {
          "value": 4,
          "name": "SINGLE"
        },
        {
          "value": 5,
          "name": "DOUBLE"
        },
        {
          "value": 6,
          "name": "ADDADT"
        },
        {
          "value": 7,
          "name": "ADDCHD"
        },
        {
          "value": 8,
          "name": "TOTAL"
        },
        {
          "value": 9,
          "name": "ADULT"
        },
        {
          "value": 10,
          "name": "CHILD"
        },
        {
          "value": 11,
          "name": "INFANT"
        },
        {
          "value": 12,
          "name": "INFANTINLAP"
        }
      ]
    },
    {
      "entityType": "FlagStatuses",
      "data": [
        {
          "value": 0,
          "name": "Inactive"
        },
        {
          "value": 1,
          "name": "Active"
        },
        {
          "value": 2,
          "name": "Deleted"
        },
        {
          "value": 3,
          "name": "Completed"
        }
      ]
    },
    {
      "entityType": "FlagTypes",
      "data": [
        {
          "value": 0,
          "name": "NoAction"
        },
        {
          "value": 3,
          "name": "PaymentDeclined"
        },
        {
          "value": 9,
          "name": "GuestCountChanged"
        },
        {
          "value": 15,
          "name": "InstantPayBookingNotConfirmed"
        },
        {
          "value": 25,
          "name": "PriceMismatch"
        },
        {
          "value": 26,
          "name": "PaymentPendingConfirm"
        },
        {
          "value": 32,
          "name": "PaymentScheduleChanged"
        },
        {
          "value": 33,
          "name": "GroupPaymentAllocationFailed"
        },
        {
          "value": 34,
          "name": "PaymentAllocationTimeout"
        },
        {
          "value": 35,
          "name": "Firstnamechanged"
        },
        {
          "value": 36,
          "name": "Lastnamechanged"
        },
        {
          "value": 37,
          "name": "BookingPendingConfirmation"
        }
      ]
    },
    {
      "entityType": "ApplicationTypes",
      "data": [
        {
          "value": 0,
          "name": "Any"
        },
        {
          "value": 1,
          "name": "B2C"
        },
        {
          "value": 2,
          "name": "B2B"
        },
        {
          "value": -1,
          "name": "Undefined"
        }
      ]
    },
    {
      "entityType": "AssociationTypes",
      "data": [
        {
          "value": 0,
          "name": "RES"
        },
        {
          "value": 1,
          "name": "PAX"
        }
      ]
    },
    {
      "entityType": "PenaltyAmountTypes",
      "data": [
        {
          "value": 1,
          "name": "Percentage"
        },
        {
          "value": 2,
          "name": "Fixed"
        }
      ]
    },
    {
      "entityType": "PenaltyAmountApplicableOn",
      "data": [
        {
          "value": 0,
          "name": "FullStay"
        },
        {
          "value": 1,
          "name": "Nights"
        },
        {
          "value": 2,
          "name": "FirstLast"
        },
        {
          "value": 3,
          "name": "Fixed"
        },
        {
          "value": 4,
          "name": "PerPerson"
        },
        {
          "value": 5,
          "name": "PerCabin"
        }
      ]
    },
    {
      "entityType": "AirCategoryTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "Economy"
        },
        {
          "value": 2,
          "name": "PremiumEconomy"
        },
        {
          "value": 3,
          "name": "Business"
        },
        {
          "value": 4,
          "name": "First"
        }
      ]
    },
    {
      "entityType": "CruiseTypes",
      "data": [
        {
          "value": 28,
          "name": "CruiseTour"
        },
        {
          "value": 29,
          "name": "CruiseOnly"
        },
        {
          "value": -1,
          "name": "None"
        }
      ]
    },
    {
      "entityType": "TourTypes",
      "data": [
        {
          "value": 0,
          "name": "Undefined"
        },
        {
          "value": 1,
          "name": "CruiseOnly"
        },
        {
          "value": 2,
          "name": "CruiseLand"
        },
        {
          "value": 3,
          "name": "CruiseLandAir"
        },
        {
          "value": 4,
          "name": "CruiseAir"
        }
      ]
    },
    {
      "entityType": "DestinationTypes",
      "data": [
        {
          "value": 0,
          "name": "All"
        },
        {
          "value": 1,
          "name": "Ocean"
        },
        {
          "value": 2,
          "name": "River"
        }
      ]
    },
    {
      "entityType": "BookingModes",
      "data": [
        {
          "value": 0,
          "name": "None"
        },
        {
          "value": 1,
          "name": "Online"
        },
        {
          "value": 2,
          "name": "Offline"
        },
        {
          "value": 3,
          "name": "RequestQuote"
        }
      ]
    },
    {
      "entityType": "ItineraryNodeTypes",
      "data": [
        {
          "value": 0,
          "name": "Port"
        },
        {
          "value": 1,
          "name": "Sea"
        },
        {
          "value": 2,
          "name": "Hotel"
        },
        {
          "value": 3,
          "name": "Air"
        },
        {
          "value": 4,
          "name": "Transfer"
        },
        {
          "value": 5,
          "name": "Activity"
        },
        {
          "value": 6,
          "name": "Insurance"
        },
        {
          "value": 7,
          "name": "Other"
        },
        {
          "value": 8,
          "name": "Cruise"
        },
        {
          "value": 9,
          "name": "Tour"
        },
        {
          "value": 10,
          "name": "Rail"
        }
      ]
    },
    {
      "entityType": "ItineraryNodePosition",
      "data": [
        {
          "value": 0,
          "name": "CruiseOnly"
        },
        {
          "value": 1,
          "name": "PreCruise"
        },
        {
          "value": 2,
          "name": "PostCruise"
        },
        {
          "value": 3,
          "name": "BetweenCruise"
        }
      ]
    },
    {
      "entityType": "LocationType",
      "data": [
        {
          "value": 0,
          "name": "UnKnown"
        },
        {
          "value": 1,
          "name": "City"
        },
        {
          "value": 2,
          "name": "CruisePort"
        },
        {
          "value": 3,
          "name": "AirPort"
        },
        {
          "value": 4,
          "name": "State"
        },
        {
          "value": 5,
          "name": "Country"
        },
        {
          "value": 6,
          "name": "Destination"
        },
        {
          "value": 7,
          "name": "Hotel"
        },
        {
          "value": 8,
          "name": "Address"
        },
        {
          "value": 9,
          "name": "County"
        },
        {
          "value": 10,
          "name": "Neighbourhood"
        },
        {
          "value": 11,
          "name": "SubLocality"
        },
        {
          "value": 12,
          "name": "HeliPort"
        },
        {
          "value": 13,
          "name": "RailStation"
        },
        {
          "value": 14,
          "name": "BusStation"
        },
        {
          "value": 15,
          "name": "CruiseDestination"
        },
        {
          "value": 16,
          "name": "TravelDestination"
        },
        {
          "value": 17,
          "name": "Landmark"
        }
      ]
    }
  ]
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
