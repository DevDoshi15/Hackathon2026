# Category Availability

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 3 – All Adults (RCCL) > Category Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listCategories`

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
//This request contains only mandatory elements
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1269434
        }
    },
    "customers": [
        {
            "rph": 1,
            "age": 31,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 30
        },
        {
            "rph": 3,
            "age": 30
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
Date: Mon, 27 Mar 2023 09:23:05 GMT
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
      "requestId": "cb928ae9-bd1d-4a3d-9d5a-64791ad91dd5",
      "timeStamp": "27-Mar-2023 05:22:59",
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
        "id": 2227,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2B"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
        },
        {
          "rph": 3,
          "ageGroup": "Adult"
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
          "id": 364180,
          "destination": {
            "id": 7
          }
        },
        "tourCode": "FR4BH098",
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
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Best fare"
          }
        },
        {
          "code": "I1071484_GRP",
          "name": "STANDARD GROUP_GRP",
          "description": "STANDARD GROUP",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD GROUP"
          }
        },
        {
          "code": "I0507001_GRP",
          "name": "BROCHURE_GRP",
          "description": "BROCHURE PRICE",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          }
        },
        {
          "code": "I0507023_GRP",
          "name": "STANDARD_GRP",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD"
          }
        },
        {
          "code": "BVL_GRP",
          "name": "Best Value_GRP",
          "description": "Restrictions May Apply",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "remarks": "Restrictions May Apply"
          }
        },
        {
          "code": "I9614174_GRP",
          "name": "500_GRP",
          "description": "500",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "500"
          }
        },
        {
          "code": "G0738129_GRP",
          "name": "BOGO60 NRD_GRP",
          "description": "GS and above",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9614174",
              "description": "500",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9612916",
              "description": "NRP PROMO H",
              "type": 0,
              "refundableType": 2
            }
          ],
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
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "GS and above"
          }
        },
        {
          "code": "G0737880_GRP",
          "name": "BOGO60 NRD_GRP",
          "description": "JS Below",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9614174",
              "description": "500",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9612916",
              "description": "NRP PROMO H",
              "type": 0,
              "refundableType": 2
            }
          ],
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
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "JS Below"
          }
        },
        {
          "code": "F4169636_GRP",
          "name": "Nets NRD_GRP",
          "description": "Net Rates",
          "type": 12,
          "refundableType": 2,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Net Rates"
          }
        },
        {
          "code": "I9612916_GRP",
          "name": "NRP PROMO H_GRP",
          "description": "NRP",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "NRP"
          }
        },
        {
          "code": "I7996069_GRP",
          "name": "WOW Sale NRD_GRP",
          "description": "5N or Less Inside Oceanview Deluxe",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9614174",
              "description": "500",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9612916",
              "description": "NRP PROMO H",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          }
        },
        {
          "code": "I7997687_GRP",
          "name": "WOW Sale NRD_GRP",
          "description": "5N or Less Balcony",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9614174",
              "description": "500",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9612916",
              "description": "NRP PROMO H",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          }
        },
        {
          "code": "I9610792_GRP",
          "name": "Kids Sail Free_GRP",
          "description": "ksf",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I7515175",
              "description": "WOW Sale",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I7522610",
              "description": "WOW Sale",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ksf"
          }
        },
        {
          "code": "F4348105_GRP",
          "name": "Nets_GRP",
          "description": "Net Rates",
          "type": 12,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Net Rates"
          }
        },
        {
          "code": "I7522610_GRP",
          "name": "WOW Sale_GRP",
          "description": "5N or Less Balcony",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9610792",
              "description": "Kids Sail Free",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          }
        },
        {
          "code": "I7515175_GRP",
          "name": "WOW Sale_GRP",
          "description": "5N or Less Inside Oceanview Deluxe",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9610792",
              "description": "Kids Sail Free",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          }
        },
        {
          "code": "I9602229_GRP",
          "name": "TARGETED NRD 1_GRP",
          "description": "TARGETED NRD 1",
          "type": 0,
          "refundableType": 2,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "TARGETED NRD 1"
          }
        },
        {
          "code": "I9582251_GRP",
          "name": "CC MARKET2 DOM_GRP",
          "description": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)"
          }
        },
        {
          "code": "I9582007_GRP",
          "name": "CC MILITARY_GRP",
          "description": "CC QUALIFIER PROMO - MILITARY ONLY",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CC QUALIFIER PROMO - MILITARY ONLY"
          }
        },
        {
          "code": "I9582012_GRP",
          "name": "CC SENIOR_GRP",
          "description": "AGE SPECIFIC PROMO - SENIOR",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "AGE SPECIFIC PROMO - SENIOR"
          }
        },
        {
          "code": "I9581957_GRP",
          "name": "ES FIRE_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY"
          }
        },
        {
          "code": "I9582003_GRP",
          "name": "ES FIRE2_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI"
          }
        },
        {
          "code": "I9581966_GRP",
          "name": "ES MILITAR_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY"
          }
        },
        {
          "code": "I9582097_GRP",
          "name": "ES Militar2_GRP",
          "description": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE"
          }
        },
        {
          "code": "BESTRATE",
          "name": "Best Rate",
          "description": "Restrictions May Apply",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          }
        },
        {
          "code": "BVL",
          "name": "Best Value",
          "description": "Restrictions May Apply",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          }
        },
        {
          "code": "I0507001",
          "name": "BROCHURE",
          "description": "BROCHURE PRICE",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          }
        },
        {
          "code": "I0507023",
          "name": "STANDARD",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "STANDARD"
          }
        },
        {
          "code": "I9614174",
          "name": "500",
          "description": "500",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "500"
          }
        },
        {
          "code": "G0738129",
          "name": "BOGO60 NRD",
          "description": "GS and above",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9614174",
              "description": "500",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9612916",
              "description": "NRP PROMO H",
              "type": 0,
              "refundableType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "GS and above",
            "qualifierCodes": "2"
          }
        },
        {
          "code": "G0737880",
          "name": "BOGO60 NRD",
          "description": "JS Below",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9614174",
              "description": "500",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9612916",
              "description": "NRP PROMO H",
              "type": 0,
              "refundableType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "JS Below",
            "qualifierCodes": "2"
          }
        },
        {
          "code": "F4169636",
          "name": "Nets NRD",
          "description": "Net Rates",
          "type": 12,
          "refundableType": 2,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Net Rates",
            "remarks": "Net Rates",
            "qualifierCodes": "2"
          }
        },
        {
          "code": "I9612916",
          "name": "NRP PROMO H",
          "description": "NRP",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "NRP"
          }
        },
        {
          "code": "I7996069",
          "name": "WOW Sale NRD",
          "description": "5N or Less Inside Oceanview Deluxe",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9614174",
              "description": "500",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9612916",
              "description": "NRP PROMO H",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          }
        },
        {
          "code": "I7997687",
          "name": "WOW Sale NRD",
          "description": "5N or Less Balcony",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9614174",
              "description": "500",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9612916",
              "description": "NRP PROMO H",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          }
        },
        {
          "code": "I9610792",
          "name": "Kids Sail Free",
          "description": "ksf",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I7515175",
              "description": "WOW Sale",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I7522610",
              "description": "WOW Sale",
              "type": 0,
              "refundableType": 1
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ksf"
          }
        },
        {
          "code": "F4348105",
          "name": "Nets",
          "description": "Net Rates",
          "type": 12,
          "refundableType": 1,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Net Rates",
            "remarks": "Net Rates",
            "qualifierCodes": "1"
          }
        },
        {
          "code": "I7522610",
          "name": "WOW Sale",
          "description": "5N or Less Balcony",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9610792",
              "description": "Kids Sail Free",
              "type": 0,
              "refundableType": 1
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          }
        },
        {
          "code": "I7515175",
          "name": "WOW Sale",
          "description": "5N or Less Inside Oceanview Deluxe",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9610792",
              "description": "Kids Sail Free",
              "type": 0,
              "refundableType": 1
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          }
        },
        {
          "code": "I9602229",
          "name": "TARGETED NRD 1",
          "description": "TARGETED NRD 1",
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "TARGETED NRD 1"
          }
        },
        {
          "code": "I9582251",
          "name": "CC MARKET2 DOM",
          "description": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)"
          }
        },
        {
          "code": "I9582007",
          "name": "CC MILITARY",
          "description": "CC QUALIFIER PROMO - MILITARY ONLY",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CC QUALIFIER PROMO - MILITARY ONLY"
          }
        },
        {
          "code": "I9582012",
          "name": "CC SENIOR",
          "description": "AGE SPECIFIC PROMO - SENIOR",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "AGE SPECIFIC PROMO - SENIOR"
          }
        },
        {
          "code": "I9581957",
          "name": "ES FIRE",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY"
          }
        },
        {
          "code": "I9582003",
          "name": "ES FIRE2",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI"
          }
        },
        {
          "code": "I9581966",
          "name": "ES MILITAR",
          "description": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY"
          }
        },
        {
          "code": "I9582097",
          "name": "ES Militar2",
          "description": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE"
          }
        }
      ],
      "categories": [
        {
          "code": "RS",
          "type": 4,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "RS",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1927,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 499,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 499,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "OS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1305
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1006.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 107.6,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 1305
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1006.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 107.6,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 1305
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1006.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 107.6,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 1305
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1006.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 107.6,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "GT",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1219
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 940,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 99.6,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 1219
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 940,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 99.6,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 1219
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 940,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 99.6,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 1219
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 940,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 99.6,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "GS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1117
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 860,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 90,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 1117
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 860,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 90,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 1117
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 860,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 90,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 1117
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 860,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 90,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VP",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1180
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 705.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 71.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 1180
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 705.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 71.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 1180
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 705.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 71.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 1180
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 705.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 71.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 990
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 769,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 79.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 990
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 769,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 79.08,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "J3",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1022
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 605.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 59.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 1022
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 605.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 59.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 1022
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 605.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 59.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 1022
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 605.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 59.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 852
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 662.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 66.28,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 852
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 662.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 66.28,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "J4",
          "type": 4,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 927,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 499,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 499,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "WS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 757
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 580,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 56.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 757
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 580,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 56.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 757
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 580,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 56.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 757
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 580,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 349,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 56.4,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 913
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 542,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 51.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 913
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 542,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 51.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 913
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 542,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 51.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 913
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 542,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 51.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7522610",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 763
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 592,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 57.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 763
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 592,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 57.84,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "3B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 896
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 528.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 50.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 896
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 528.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 50.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 896
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 528.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 50.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 896
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 528.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 50.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7522610",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 747
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 578,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 56.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 747
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 578,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 56.16,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "2B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 769.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 760.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "CB",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 751,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 823
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 495.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 46.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 823
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 495.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 46.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 823
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 495.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 46.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 823
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 495.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 46.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7522610",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 695
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 538,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 51.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 695
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 538,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 51.36,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "5D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 789
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 468.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 43.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 789
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 468.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 43.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 789
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 468.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 43.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 789
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 468.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 43.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7522610",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 661
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 511.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 48.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 661
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 511.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 48.16,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "2D",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 703,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4D",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 693.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 427,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "XB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 564
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 38.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 564
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 38.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7997687",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 564
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 38.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Balcony"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 564
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 298,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 38.36,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1K",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 975
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 568.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 55.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 975
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 568.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 55.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 975
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 568.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 55.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 975
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 568.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 55.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 805
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 625.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 61.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 805
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 625.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 61.84,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1L",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 773
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 455.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 41.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 773
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 455.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 41.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 773
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 455.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 41.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 773
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 455.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 41.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 643
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 498.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 46.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 643
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 498.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 46.64,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "3M",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 747
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 435.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 39.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 747
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 435.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 39.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 747
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 435.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 39.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 747
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 435.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 39.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 617
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 478.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 44.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 617
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 478.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 44.24,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4M",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 646.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 341,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 341,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 675
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 402,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 35.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 675
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 402,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 35.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 675
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 402,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 35.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 675
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 402,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 35.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 565
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 438.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 39.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 565
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 438.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 39.44,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "3N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 649
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 382,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 32.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 649
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 382,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 32.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 649
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 382,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 32.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 649
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 382,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 32.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 541
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 418,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 36.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 541
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 418,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 36.96,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "2N",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 569.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 341,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 341,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4N",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 560.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 341,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 341,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "YO",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 452
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 343,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 27.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 452
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 343,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 27.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 452
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 343,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 27.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 452
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 343,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 238,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 27.96,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1Q",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 773
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 455,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 41.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 773
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 455,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 41.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 773
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 455,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 41.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 773
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 455,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 41.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 644
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 498,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 46.56,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 644
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 498,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 46.56,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1R",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 739
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 428.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 38.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 739
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 428.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 38.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 739
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 428.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 38.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 739
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 428.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 38.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 608
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 472,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 43.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 608
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 472,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 43.44,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "CP",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 541.3333333333334,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 284,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 284,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "2T",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 512.6666666666666,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 284,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 284,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 625
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 361.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 30.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 625
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 361.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 30.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 625
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 361.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 30.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 625
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 361.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 30.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 514
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 398.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 34.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 514
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 398.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 34.64,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "3V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 561
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 335,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 27,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 561
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 335,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 27,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 561
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 335,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 27,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 561
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 335,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 27,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I9610792",
                "name": "Kids Sail Free",
                "description": "ksf",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I7515175",
                    "description": "WOW Sale",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ksf"
                },
                "supplierRules": [
                  {
                    "description": "Kids Sail Free",
                    "discountType": 2,
                    "amount": 472
                  },
                  {
                    "description": "Kids Sail Free",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 364.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 30.56,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9610792",
                    "description": "Kids Sail Free",
                    "type": 0,
                    "refundableType": 1
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale",
                    "discountType": 2,
                    "amount": 472
                  },
                  {
                    "description": "WOW Sale",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 364.6666666666667,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 30.56,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "2V",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 494,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 284,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 284,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4V",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I0507023",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 484,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 284,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 284,
                  "type": "ADDCHD"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "ZI",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "dynamicRules": [
                  {
                    "type": 10
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 393
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 296.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 22.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "500"
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 393
                  },
                  {
                    "description": "500",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 296.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 22.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "I7996069",
                    "description": "WOW Sale NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "NRP"
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 393
                  },
                  {
                    "description": "NRP PROMO H",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 296.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 22.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "G0738129",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "I9614174",
                    "description": "500",
                    "type": 0,
                    "refundableType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "5N or Less Inside Oceanview Deluxe"
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 393
                  },
                  {
                    "description": "WOW Sale NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 296.3333333333333,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 198,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 22.36,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": true
          }
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 31,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 2,
        "age": 30
      },
      {
        "rph": 3,
        "age": 30
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
