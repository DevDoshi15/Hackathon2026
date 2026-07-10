# Farecode Availability

**Path:** Create Reservation > Occupancy Based Samples > Single Occupancy (RCCL) > Farecode Availability

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
Date: Mon, 27 Mar 2023 10:18:05 GMT
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
      "requestId": "3cf429c5-75bd-4cc1-a12a-03ac55f1b663",
      "timeStamp": "27-Mar-2023 06:18:00",
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
