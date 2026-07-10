# Category Availability

**Path:** Create Reservation > Occupancy Based Samples > Single Occupancy (RCCL) > Category Availability

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
Date: Mon, 27 Mar 2023 10:18:24 GMT
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
  "data": {
    "trackingInfo": {
      "requestId": "b0b6dbf7-3c89-4bfe-81ac-8075145d4f58",
      "timeStamp": "27-Mar-2023 06:18:18",
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
              "code": "E9619599",
              "description": "Singles",
              "type": 0,
              "refundableType": 2
            },
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
              "code": "E5822874",
              "description": "Single NRD",
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
              "code": "E9619599",
              "description": "Singles",
              "type": 0,
              "refundableType": 2
            },
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
              "code": "E5822874",
              "description": "Single NRD",
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
              "code": "E9619599",
              "description": "Singles",
              "type": 0,
              "refundableType": 2
            },
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
              "code": "E5822874",
              "description": "Single NRD",
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
              "code": "E9619599",
              "description": "Singles",
              "type": 0,
              "refundableType": 2
            },
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
              "code": "E5822874",
              "description": "Single NRD",
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
          "code": "E5822874_GRP",
          "name": "Single NRD_GRP",
          "description": "Single Promotion",
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
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Single Promotion"
          }
        },
        {
          "code": "E9619599_GRP",
          "name": "Singles_GRP",
          "description": "Singles",
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
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Singles"
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
              "code": "E9619599",
              "description": "Singles",
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
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "E5822874",
              "description": "Single NRD",
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
              "code": "E9619599",
              "description": "Singles",
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
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "E5822874",
              "description": "Single NRD",
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
          "code": "I9614314_GRP",
          "name": "CONVERT NO_GRP",
          "description": "ALLOWED TO CONVERT IS NO",
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
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ALLOWED TO CONVERT IS NO"
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
              "code": "I9614314",
              "description": "CONVERT NO",
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
              "code": "I9614314",
              "description": "CONVERT NO",
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
              "code": "E9619599",
              "description": "Singles",
              "type": 0,
              "refundableType": 2
            },
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
              "code": "E5822874",
              "description": "Single NRD",
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
              "code": "E9619599",
              "description": "Singles",
              "type": 0,
              "refundableType": 2
            },
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
              "code": "E5822874",
              "description": "Single NRD",
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
              "code": "E9619599",
              "description": "Singles",
              "type": 0,
              "refundableType": 2
            },
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
              "code": "E5822874",
              "description": "Single NRD",
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
              "code": "E9619599",
              "description": "Singles",
              "type": 0,
              "refundableType": 2
            },
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
              "code": "E5822874",
              "description": "Single NRD",
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
          "code": "E5822874",
          "name": "Single NRD",
          "description": "Single Promotion",
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
            "remarks": "Single Promotion",
            "qualifierCodes": "2"
          }
        },
        {
          "code": "E9619599",
          "name": "Singles",
          "description": "Singles",
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
            "remarks": "Singles",
            "qualifierCodes": "2"
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
              "code": "E9619599",
              "description": "Singles",
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
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "E5822874",
              "description": "Single NRD",
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
              "code": "E9619599",
              "description": "Singles",
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
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "E5822874",
              "description": "Single NRD",
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
          "code": "I9614314",
          "name": "CONVERT NO",
          "description": "ALLOWED TO CONVERT IS NO",
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
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ALLOWED TO CONVERT IS NO"
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
              "code": "I9614314",
              "description": "CONVERT NO",
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
              "code": "I9614314",
              "description": "CONVERT NO",
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
                  "amount": 5282,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "RS",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7924,
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
                  "amount": 220,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1155
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
                  "amount": 2671,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 294.12,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 1155
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
                  "amount": 2671,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 294.12,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 1155
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
                  "amount": 2671,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 294.12,
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
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 1155
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
                  "amount": 2671,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 294.12,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2826,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 312.72,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
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
              "prices": [
                {
                  "id": 1,
                  "amount": 3826,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 432.72,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1069
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
                  "amount": 2471,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 270.12,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 1069
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
                  "amount": 2471,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 270.12,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 1069
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
                  "amount": 2471,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 270.12,
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
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 1069
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
                  "amount": 2471,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 270.12,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2540,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 278.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
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
              "prices": [
                {
                  "id": 1,
                  "amount": 3540,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 398.4,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "GS and above"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 967
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
                  "amount": 2231,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 241.32,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 967
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
                  "amount": 2231,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 241.32,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 967
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
                  "amount": 2231,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 241.32,
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
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 967
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
                  "amount": 2231,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 241.32,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2198,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 237.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
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
              "prices": [
                {
                  "id": 1,
                  "amount": 3198,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 357.36,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1030
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
                  "amount": 1768,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 185.76,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 1030
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
                  "amount": 1768,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 185.76,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 1030
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
                  "amount": 1768,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 185.76,
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
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 1030
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
                  "amount": 1768,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 185.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 1798,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 189.36,
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
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 1798,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 189.36,
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
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 872
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
                  "amount": 1468,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 149.76,
                  "type": "AVGPP"
                }
              ]
            },
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 872
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
                  "amount": 1468,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 149.76,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 872
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
                  "amount": 1468,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 149.76,
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
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 872
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
                  "amount": 1468,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 149.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 1340,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 134.4,
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
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 1340,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 134.4,
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
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 855
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
                  "amount": 1427,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 144.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 855
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
                  "amount": 1427,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 144.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 855
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
                  "amount": 1427,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 144.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 855
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
                  "amount": 1427,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 144.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 1282,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 127.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 1282,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 127.44,
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
          "code": "WS",
          "type": 4,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "WS",
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
                  "amount": 1998,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2998,
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
                  "amount": 220,
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
          "code": "1B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1B",
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
                  "amount": 2112,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3168,
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
                  "amount": 220,
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
              "status": 2,
              "upgradeFrom": "3B",
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
                  "amount": 2054,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3082,
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
                  "amount": 220,
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
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 694
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
                  "amount": 1188,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 116.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 694
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
                  "amount": 1188,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 116.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 694
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
                  "amount": 1188,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 116.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 694
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
                  "amount": 1188,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 116.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 882,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 79.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 882,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 79.44,
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
          "code": "4B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 687
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
                  "amount": 1167,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 113.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 687
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
                  "amount": 1167,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 113.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 687
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
                  "amount": 1167,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 113.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 687
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
                  "amount": 1167,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 113.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 854,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 76.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 854,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 76.08,
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
          "code": "CB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 679
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
                  "amount": 1147,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 111.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 679
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
                  "amount": 1147,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 111.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 679
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
                  "amount": 1147,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 111.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 679
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
                  "amount": 1147,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 111.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 826,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.72,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 826,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.72,
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
          "code": "1D",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1D",
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
                  "amount": 1882,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2824,
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
                  "amount": 220,
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
              "status": 2,
              "upgradeFrom": "5D",
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
                  "amount": 1768,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2652,
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
                  "amount": 220,
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
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 634
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
                  "amount": 1048,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 99.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 634
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
                  "amount": 1048,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 99.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 634
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
                  "amount": 1048,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 99.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 634
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
                  "amount": 1048,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 99.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 682,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 55.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 682,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 55.44,
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
          "code": "4D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 627
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
                  "amount": 1027,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 96.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 627
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
                  "amount": 1027,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 96.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 627
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
                  "amount": 1027,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 96.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I7997687",
                "name": "WOW Sale NRD",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 627
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
                  "amount": 1027,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 96.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 654,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I7522610",
                "name": "WOW Sale",
                "description": "5N or Less Balcony",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 654,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.08,
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
          "code": "XB",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "XB",
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
                  "amount": 1426,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2140,
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
                  "amount": 220,
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
          "code": "1K",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1K",
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
                  "amount": 2340,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3510,
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
                  "amount": 220,
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
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 670
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
                  "amount": 1128,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 108.96,
                  "type": "AVGPP"
                }
              ]
            },
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 670
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
                  "amount": 1128,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 108.96,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 670
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
                  "amount": 1128,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 108.96,
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
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 670
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
                  "amount": 1128,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 108.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 798,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 69.36,
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
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 798,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 69.36,
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
              "status": 2,
              "upgradeFrom": "3M",
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
                  "amount": 1712,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2568,
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
                  "amount": 220,
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
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 591
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
                  "amount": 1007,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 94.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 591
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
                  "amount": 1007,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 94.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 591
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
                  "amount": 1007,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 94.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 591
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
                  "amount": 1007,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 94.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 598,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 45.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 598,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 45.36,
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
          "code": "1N",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1N",
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
                  "amount": 1540,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2310,
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
                  "amount": 220,
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
              "status": 2,
              "upgradeFrom": "3N",
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
                  "amount": 1454,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2182,
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
                  "amount": 220,
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
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 520
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
                  "amount": 848,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 75.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 520
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
                  "amount": 848,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 75.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 520
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
                  "amount": 848,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 75.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 520
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
                  "amount": 848,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 75.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 368,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 17.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 368,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 17.76,
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
          "code": "4N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 512
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
                  "amount": 828,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 512
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
                  "amount": 828,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 512
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
                  "amount": 828,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 512
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
                  "amount": 828,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 340,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 14.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 340,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 14.4,
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
          "code": "YO",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "YO",
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
                  "amount": 1140,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1710,
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
                  "amount": 220,
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
          "code": "1Q",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1Q",
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
                  "amount": 1854,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2782,
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
                  "amount": 220,
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
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 653
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
                  "amount": 1087,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 104.04,
                  "type": "AVGPP"
                }
              ]
            },
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 653
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
                  "amount": 1087,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 104.04,
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
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 653
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
                  "amount": 1087,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 104.04,
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
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 653
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
                  "amount": 1087,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 104.04,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 740,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 62.4,
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
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 740,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 62.4,
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
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 512
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
                  "amount": 828,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 512
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
                  "amount": 828,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 512
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
                  "amount": 828,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 512
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
                  "amount": 828,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 340,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 14.4,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 340,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 14.4,
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
          "code": "2T",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 466
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
                  "amount": 788,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 466
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
                  "amount": 788,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 466
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
                  "amount": 788,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 466
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
                  "amount": 788,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I9614314",
                "name": "CONVERT NO",
                "description": "ALLOWED TO CONVERT IS NO",
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
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                },
                "supplierRules": [
                  {
                    "description": "CONVERT NO",
                    "discountType": 2,
                    "amount": 1000
                  },
                  {
                    "description": "CONVERT NO",
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
                  "amount": 254,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 4.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I7515175",
                "name": "WOW Sale",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 1,
                "combinableFares": [
                  {
                    "code": "I9614314",
                    "description": "CONVERT NO",
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
                    "amount": 1000
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
                  "amount": 254,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 4.08,
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
          "code": "1V",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1V",
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
                  "amount": 1426,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2140,
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
                  "amount": 220,
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
              "status": 2,
              "upgradeFrom": "3V",
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
                  "amount": 1282,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1924,
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
                  "amount": 220,
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
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 451
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
                  "amount": 747,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 63.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 451
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
                  "amount": 747,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 63.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 451
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
                  "amount": 747,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 63.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 451
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
                  "amount": 747,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 63.24,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
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
              "prices": [
                {
                  "id": 1,
                  "amount": 1198,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 117.36,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
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
              "prices": [
                {
                  "id": 1,
                  "amount": 1798,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 189.36,
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
          "code": "4V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "G0737880",
                "name": "BOGO60 NRD",
                "description": "JS Below",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                  "remarks": "JS Below"
                },
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 441
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
                  "amount": 727,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 60.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I9614174",
                "name": "500",
                "description": "500",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "500",
                    "discountType": 2,
                    "amount": 441
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
                  "amount": 727,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 60.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I9612916",
                "name": "NRP PROMO H",
                "description": "NRP",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
                    "type": 0,
                    "refundableType": 2
                  },
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
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "NRP PROMO H",
                    "discountType": 2,
                    "amount": 441
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
                  "amount": 727,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 60.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I7996069",
                "name": "WOW Sale NRD",
                "description": "5N or Less Inside Oceanview Deluxe",
                "type": 0,
                "refundableType": 2,
                "combinableFares": [
                  {
                    "code": "E9619599",
                    "description": "Singles",
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
                    "code": "G0737880",
                    "description": "BOGO60 NRD",
                    "type": 0,
                    "refundableType": 2
                  },
                  {
                    "code": "E5822874",
                    "description": "Single NRD",
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
                },
                "supplierRules": [
                  {
                    "description": "WOW Sale NRD",
                    "discountType": 2,
                    "amount": 441
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
                  "amount": 727,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 60.84,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
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
              "prices": [
                {
                  "id": 1,
                  "amount": 1168,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 113.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
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
              "prices": [
                {
                  "id": 1,
                  "amount": 1752,
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 183.84,
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
          "code": "ZI",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "ZI",
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
                  "amount": 998,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I0507001",
                "name": "BROCHURE",
                "description": "BROCHURE PRICE",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "BROCHURE PRICE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1498,
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
                  "amount": 220,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
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
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
