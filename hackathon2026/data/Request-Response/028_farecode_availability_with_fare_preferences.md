# Farecode Availability With Fare Preferences

**Path:** Farecode Availability > Farecode Availability With Fare Preferences

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listfarecodes`

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

### Request Body

```json
{
    "cruiseReservation": {
        "pos": { //Either id or currency is mandatory
            //"id": 1, //Id received in the ListPOS
            "currency": "USD"
        },
        "customerReferences": [
            {
                "rph": 1,
                "isPrimaryContact": true // customer address is required for the customer whose isPrimaryContact is true
            },
            {
                "rph": 2
            }
        ],
        "cruise": {
            "packageId": 1269434
        },
        "farePreferences": [
            {
                "Type": "Military"
            } //,
            // {
            //     "Type": "Police"
            // },
            // {
            //     "Type": "Interline"
            // },
            // {
            //     "Type": "Union"
            // },
            // {
            //     "Type": "Teacher"
            // },
            // {
            //     "Type": "Accessible"
            // },
            // {
            //     "Type": "ConnectingCabins"
            // },
            // {
            //     "Type": "PromoCode"
            //     "value": ""
            // },
            // {
            //     "Type": "SupplierPromoCode"
            //     "value": ""
            // },
            // {
            //     "Type": "ExcludeNonRefundable"
            // }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        },
        {
            "rph": 2,
            "age": 57
        }
    ],
    "trackingInfo": {
        "token": "EQTEMPKEN"
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 01 Feb 2023 09:50:33 GMT
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Served-From: 208.64.67.223
X-Powered-By: ASP.NET
X-Server-Ip: 192.168.214.13
Content-Encoding: gzip
```

### Response Body

```json
{
  "isSucceed": true,
  "data": {
    "trackingInfo": {
      "requestId": "56e54865-0be4-4111-9f0b-ff6c7bc73ebe",
      "timeStamp": "01-Feb-2023 04:50:31",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 4
      },
      "pos": {
        "id": 2114,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2C"
      },
      "customerReferences": [
        {
          "rph": 1,
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 311051,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "BESTRATE_GRP",
          "name": "Best Rate_GRP",
          "description": "Best fare",
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Best fare"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I1071484_GRP",
          "name": "STANDARD GROUP_GRP",
          "description": "STANDARD GROUP",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD GROUP"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I0507001_GRP",
          "name": "BROCHURE_GRP",
          "description": "BROCHURE PRICE",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I0507023_GRP",
          "name": "STANDARD_GRP",
          "description": "STANDARD",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "BVL_GRP",
          "name": "Best Value_GRP",
          "description": "Restrictions May Apply",
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "remarks": "Restrictions May Apply"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "G0684253_GRP",
          "name": "BOGO60_GRP",
          "description": "4n or less",
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "4n or less"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "combinableFares": [
            {
              "code": "I7515175",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I6927341",
              "type": 2,
              "refundableType": 1
            },
            {
              "code": "I7522610",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I6927341_GRP",
          "name": "Military Disc_GRP",
          "description": "Military Disc",
          "bookOnline": true,
          "isEligible": true,
          "type": 2,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Military Disc"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "combinableFares": [
            {
              "code": "I7515175",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I7522610",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I7522610_GRP",
          "name": "WOW Sale_GRP",
          "description": "5N or Less Balcony",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "combinableFares": [
            {
              "code": "I6927341",
              "type": 2,
              "refundableType": 1
            },
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I7515175_GRP",
          "name": "WOW Sale_GRP",
          "description": "5N or Less Inside Oceanview Deluxe",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "combinableFares": [
            {
              "code": "I6927341",
              "type": 2,
              "refundableType": 1
            },
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I9582251_GRP",
          "name": "CC MARKET2 DOM_GRP",
          "description": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9582007_GRP",
          "name": "CC MILITARY_GRP",
          "description": "CC QUALIFIER PROMO - MILITARY ONLY",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CC QUALIFIER PROMO - MILITARY ONLY"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9582012_GRP",
          "name": "CC SENIOR_GRP",
          "description": "AGE SPECIFIC PROMO - SENIOR",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "AGE SPECIFIC PROMO - SENIOR"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9581957_GRP",
          "name": "ES FIRE_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9582003_GRP",
          "name": "ES FIRE2_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9581966_GRP",
          "name": "ES MILITAR_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9582097_GRP",
          "name": "ES Militar2_GRP",
          "description": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "BESTRATE",
          "name": "Best Rate",
          "description": "Restrictions May Apply",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "BVL",
          "name": "Best Value",
          "description": "Restrictions May Apply",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "I0507001",
          "name": "BROCHURE",
          "description": "BROCHURE PRICE",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "I0507023",
          "name": "STANDARD",
          "description": "STANDARD",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "STANDARD"
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "G0684253",
          "name": "BOGO60",
          "description": "4n or less",
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "Buy One and Get One Free - Special Offer",
            "fareTypeDescription": "Discount",
            "remarks": "4n or less",
            "qualifierCodes": "1"
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "combinableFares": [
            {
              "code": "I7515175",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I6927341",
              "type": 2,
              "refundableType": 1
            },
            {
              "code": "I7522610",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I6927341",
          "name": "Military Disc",
          "description": "Military Disc",
          "bookOnline": true,
          "isEligible": true,
          "type": 2,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Military Disc"
          },
          "groups": [
            {}
          ],
          "combinableFares": [
            {
              "code": "I7515175",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I7522610",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I7522610",
          "name": "WOW Sale",
          "description": "5N or Less Balcony",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          },
          "groups": [
            {}
          ],
          "combinableFares": [
            {
              "code": "I6927341",
              "type": 2,
              "refundableType": 1
            },
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I7515175",
          "name": "WOW Sale",
          "description": "5N or Less Inside Oceanview Deluxe",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          },
          "groups": [
            {}
          ],
          "combinableFares": [
            {
              "code": "I6927341",
              "type": 2,
              "refundableType": 1
            },
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            }
          ]
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 52,
        "address": {
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      },
      {
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
