# Category Availabililty

**Path:** Modify Reservation > Category, Fare code and Cabin - Royal Caribbean > Category Availabililty

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
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1336123
        }
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "address": {
                "country": {
                    "id": "US"
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
Date: Thu, 04 May 2023 10:38:31 GMT
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
  "advisories": [
    {
      "code": "WRN0605",
      "message": "THE DEPOSIT AMOUNT MAY CHANGE. PLEASE REVIEW FINAL CONFIRMATION.",
      "description": "RCCL-",
      "type": "Warning"
    }
  ],
  "data": {
    "trackingInfo": {
      "requestId": "ba30a096-5ee7-43ec-8cef-4925c499259a",
      "timeStamp": "04-May-2023 06:38:27",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Dec-2023 00:00:00",
        "arrivalDateTime": "09-Dec-2023 00:00:00",
        "departureCityId": "ONX",
        "arrivalCityId": "ONX",
        "duration": 7
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
        }
      ],
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1336123,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 84
            }
          ]
        },
        "itinerary": {
          "id": 364276,
          "destination": {
            "id": 9
          }
        },
        "tourCode": "RH07D356",
        "voyage": {
          "departureDateTime": "02-Dec-2023 00:00:00",
          "arrivalDateTime": "09-Dec-2023 00:00:00",
          "departureCityId": "ONX",
          "arrivalCityId": "ONX",
          "code": "RH07D356"
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
              "code": "376364",
              "name": "TCC",
              "type": 1,
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
          "code": "I9581063_GRP",
          "name": "STANDARD_GRP",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD"
          }
        },
        {
          "code": "I9614245_GRP",
          "name": "STANDARD_GRP",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
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
          "code": "G0738129_GRP",
          "name": "BOGO60 NRD_GRP",
          "description": "GS and above",
          "type": 0,
          "refundableType": 2,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
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
          "code": "G0684253_GRP",
          "name": "BOGO60_GRP",
          "description": "4n or less",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
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
            "remarks": "4n or less"
          }
        },
        {
          "code": "G0684447_GRP",
          "name": "BOGO60_GRP",
          "description": "5n and longer",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
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
            "remarks": "5n and longer"
          }
        },
        {
          "code": "I9624697_GRP",
          "name": "CAT-TEST_GRP",
          "description": "CAT-TEST",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CAT-TEST"
          }
        },
        {
          "code": "I9605316_GRP",
          "name": "CATEGORYSPECIAL_GRP",
          "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
          }
        },
        {
          "code": "I9614314_GRP",
          "name": "CONVERT NO_GRP",
          "description": "ALLOWED TO CONVERT IS NO",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ALLOWED TO CONVERT IS NO"
          }
        },
        {
          "code": "I9610946_GRP",
          "name": "CATEGORYMIL_GRP",
          "description": "CATEGORY BALCONY, INSIDE + MILITARY COMBINABI",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CATEGORY BALCONY, INSIDE + MILITARY COMBINABI"
          }
        },
        {
          "code": "I9582259_GRP",
          "name": "ES CATEGORY NOT_GRP",
          "description": "ESPRESSO SUPERCATEGORY - BALCONY QUALIFIER -",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO SUPERCATEGORY - BALCONY QUALIFIER -"
          }
        },
        {
          "code": "I9582069_GRP",
          "name": "ES COMBORESLOY3_GRP",
          "description": "ESPRESSO QUALIFIER FLORIDA RESIDENT AND GOLD",
          "type": 8,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER FLORIDA RESIDENT AND GOLD"
          }
        },
        {
          "code": "I9582064_GRP",
          "name": "ES COMBOSENLOY2_GRP",
          "description": "ESPRESSO QUALFIER COMBINATION OF SENIOR AND G",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALFIER COMBINATION OF SENIOR AND G"
          }
        },
        {
          "code": "I9582065_GRP",
          "name": "ES COMBOSENLOY3_GRP",
          "description": "ESPRESSO QUALIFIER COMBINATION OF SENIOR AND",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER COMBINATION OF SENIOR AND"
          }
        },
        {
          "code": "I9610944_GRP",
          "name": "ES COMBOSENMIL2_GRP",
          "description": "SENIOR AND MILITARY - UNIQUE RESTRICTED LIMIT",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "SENIOR AND MILITARY - UNIQUE RESTRICTED LIMIT"
          }
        },
        {
          "code": "I9601078_GRP",
          "name": "ES COPYRESLOY4_GRP",
          "description": "Espresso Unique Unlimited Unrestricted - Flor",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Espresso Unique Unlimited Unrestricted - Flor"
          }
        },
        {
          "code": "I9614297_GRP",
          "name": "ES HUNDRED 2/4_GRP",
          "description": "ESPRESSO HUNDRED PROMOTION FOR 2ND ONLY",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO HUNDRED PROMOTION FOR 2ND ONLY"
          }
        },
        {
          "code": "I9614295_GRP",
          "name": "ES HUNDRED 3/4_GRP",
          "description": "ESPRESSO HUNDRED PROMOTION FOR 3RD AND 4TH ON",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO HUNDRED PROMOTION FOR 3RD AND 4TH ON"
          }
        },
        {
          "code": "I9614166_GRP",
          "name": "ES HUNDRED ALL_GRP",
          "description": "HUNDRED PERCENT FOR ALL THE GUEST",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "HUNDRED PERCENT FOR ALL THE GUEST"
          }
        },
        {
          "code": "I9602056_GRP",
          "name": "ES HUNDRED PERC_GRP",
          "description": "ESPRESSO UNIQUE - 100% PROMOTION NO QUALIFIER",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO UNIQUE - 100% PROMOTION NO QUALIFIER"
          }
        },
        {
          "code": "I9610006_GRP",
          "name": "ES HUNDRED SEN_GRP",
          "description": "CASINO PROMOTION WITH SENIOR QUALIFIER FOR ES",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CASINO PROMOTION WITH SENIOR QUALIFIER FOR ES"
          }
        },
        {
          "code": "I9614173_GRP",
          "name": "ES HUNDRED UL_GRP",
          "description": "HUNDRED PERCENT PROMOTION - UNRESTRICTED LIMI",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "HUNDRED PERCENT PROMOTION - UNRESTRICTED LIMI"
          }
        },
        {
          "code": "I9614172_GRP",
          "name": "ES HUNDREDPERC2_GRP",
          "description": "HUNDRED PERCENT PROMOTION",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "HUNDRED PERCENT PROMOTION"
          }
        },
        {
          "code": "I9610005_GRP",
          "name": "ES HUNDREDPERC2_GRP",
          "description": "100 PERCENT PROMOTION FOR CASINO NO QUALIFIER",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "100 PERCENT PROMOTION FOR CASINO NO QUALIFIER"
          }
        },
        {
          "code": "I9582245_GRP",
          "name": "ES PLAIN_GRP",
          "description": "ESPRESSO NO QUALIFIER BEST RATE - UNIQUE REST",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO NO QUALIFIER BEST RATE - UNIQUE REST"
          }
        },
        {
          "code": "I9582076_GRP",
          "name": "ES ResidentNRD2_GRP",
          "description": "ESPRESSO QUALIFIER FLORIDA RESIDENT PROMOTION",
          "type": 8,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER FLORIDA RESIDENT PROMOTION"
          }
        },
        {
          "code": "I9594761_GRP",
          "name": "ES SENIOR COPY_GRP",
          "description": "ESPRESSO SENIOR QUALIFIER - UNIQUE RESTRICTED",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO SENIOR QUALIFIER - UNIQUE RESTRICTED"
          }
        },
        {
          "code": "I9582000_GRP",
          "name": "ES SENIOR2_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - SENIOR AGE ONL",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - SENIOR AGE ONL"
          }
        },
        {
          "code": "I9610801_GRP",
          "name": "RESIDENT_GRP",
          "description": "RESIDENT FLORIDA ONLY",
          "type": 8,
          "refundableType": 1,
          "groups": [
            {
              "code": "376364",
              "name": "TCC",
              "type": 1,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "RESIDENT FLORIDA ONLY"
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
          "code": "I9614245",
          "name": "STANDARD",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD"
          }
        },
        {
          "code": "G0738129",
          "name": "BOGO60 NRD",
          "description": "GS and above",
          "type": 0,
          "refundableType": 2,
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
          "code": "G0684253",
          "name": "BOGO60",
          "description": "4n or less",
          "type": 0,
          "refundableType": 1,
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
            "agencyDescription": "Buy One and Get One Free - Special Offer",
            "fareTypeDescription": "Discount",
            "remarks": "4n or less",
            "qualifierCodes": "1"
          }
        },
        {
          "code": "G0684447",
          "name": "BOGO60",
          "description": "5n and longer",
          "type": 0,
          "refundableType": 1,
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
            "remarks": "5n and longer",
            "qualifierCodes": "1"
          }
        },
        {
          "code": "I9624697",
          "name": "CAT-TEST",
          "description": "CAT-TEST",
          "type": 0,
          "refundableType": 1,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CAT-TEST"
          }
        },
        {
          "code": "I9605316",
          "name": "CATEGORYSPECIAL",
          "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
          "type": 0,
          "refundableType": 1,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
          }
        },
        {
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
          }
        },
        {
          "code": "I9610946",
          "name": "CATEGORYMIL",
          "description": "CATEGORY BALCONY, INSIDE + MILITARY COMBINABI",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CATEGORY BALCONY, INSIDE + MILITARY COMBINABI"
          }
        },
        {
          "code": "I9582259",
          "name": "ES CATEGORY NOT",
          "description": "ESPRESSO SUPERCATEGORY - BALCONY QUALIFIER -",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO SUPERCATEGORY - BALCONY QUALIFIER -"
          }
        },
        {
          "code": "I9582069",
          "name": "ES COMBORESLOY3",
          "description": "ESPRESSO QUALIFIER FLORIDA RESIDENT AND GOLD",
          "type": 8,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER FLORIDA RESIDENT AND GOLD"
          }
        },
        {
          "code": "I9582064",
          "name": "ES COMBOSENLOY2",
          "description": "ESPRESSO QUALFIER COMBINATION OF SENIOR AND G",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALFIER COMBINATION OF SENIOR AND G"
          }
        },
        {
          "code": "I9582065",
          "name": "ES COMBOSENLOY3",
          "description": "ESPRESSO QUALIFIER COMBINATION OF SENIOR AND",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER COMBINATION OF SENIOR AND"
          }
        },
        {
          "code": "I9610944",
          "name": "ES COMBOSENMIL2",
          "description": "SENIOR AND MILITARY - UNIQUE RESTRICTED LIMIT",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "SENIOR AND MILITARY - UNIQUE RESTRICTED LIMIT"
          }
        },
        {
          "code": "I9601078",
          "name": "ES COPYRESLOY4",
          "description": "Espresso Unique Unlimited Unrestricted - Flor",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Espresso Unique Unlimited Unrestricted - Flor"
          }
        },
        {
          "code": "I9614297",
          "name": "ES HUNDRED 2/4",
          "description": "ESPRESSO HUNDRED PROMOTION FOR 2ND ONLY",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO HUNDRED PROMOTION FOR 2ND ONLY"
          }
        },
        {
          "code": "I9614295",
          "name": "ES HUNDRED 3/4",
          "description": "ESPRESSO HUNDRED PROMOTION FOR 3RD AND 4TH ON",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO HUNDRED PROMOTION FOR 3RD AND 4TH ON"
          }
        },
        {
          "code": "I9614166",
          "name": "ES HUNDRED ALL",
          "description": "HUNDRED PERCENT FOR ALL THE GUEST",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "HUNDRED PERCENT FOR ALL THE GUEST"
          }
        },
        {
          "code": "I9602056",
          "name": "ES HUNDRED PERC",
          "description": "ESPRESSO UNIQUE - 100% PROMOTION NO QUALIFIER",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO UNIQUE - 100% PROMOTION NO QUALIFIER"
          }
        },
        {
          "code": "I9610006",
          "name": "ES HUNDRED SEN",
          "description": "CASINO PROMOTION WITH SENIOR QUALIFIER FOR ES",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CASINO PROMOTION WITH SENIOR QUALIFIER FOR ES"
          }
        },
        {
          "code": "I9614173",
          "name": "ES HUNDRED UL",
          "description": "HUNDRED PERCENT PROMOTION - UNRESTRICTED LIMI",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "HUNDRED PERCENT PROMOTION - UNRESTRICTED LIMI"
          }
        },
        {
          "code": "I9614172",
          "name": "ES HUNDREDPERC2",
          "description": "HUNDRED PERCENT PROMOTION",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "HUNDRED PERCENT PROMOTION"
          }
        },
        {
          "code": "I9610005",
          "name": "ES HUNDREDPERC2",
          "description": "100 PERCENT PROMOTION FOR CASINO NO QUALIFIER",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "100 PERCENT PROMOTION FOR CASINO NO QUALIFIER"
          }
        },
        {
          "code": "I9582245",
          "name": "ES PLAIN",
          "description": "ESPRESSO NO QUALIFIER BEST RATE - UNIQUE REST",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO NO QUALIFIER BEST RATE - UNIQUE REST"
          }
        },
        {
          "code": "I9582076",
          "name": "ES ResidentNRD2",
          "description": "ESPRESSO QUALIFIER FLORIDA RESIDENT PROMOTION",
          "type": 8,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER FLORIDA RESIDENT PROMOTION"
          }
        },
        {
          "code": "I9594761",
          "name": "ES SENIOR COPY",
          "description": "ESPRESSO SENIOR QUALIFIER - UNIQUE RESTRICTED",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO SENIOR QUALIFIER - UNIQUE RESTRICTED"
          }
        },
        {
          "code": "I9582000",
          "name": "ES SENIOR2",
          "description": "ESPRESSO QUALIFIER PROMOTION - SENIOR AGE ONL",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - SENIOR AGE ONL"
          }
        },
        {
          "code": "I9610801",
          "name": "RESIDENT",
          "description": "RESIDENT FLORIDA ONLY",
          "type": 8,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "RESIDENT FLORIDA ONLY"
          }
        }
      ],
      "categories": [
        {
          "id": 353805213,
          "code": "1N",
          "type": 2,
          "externalSessionInfo": {
            "externalId": "1"
          },
          "fares": [
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "I9581063_GRP",
                "name": "STANDARD_GRP",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "376364",
                    "name": "TCC",
                    "type": 1,
                    "subType": 2
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1334,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 148.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "G0684253_GRP",
                "name": "BOGO60_GRP",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "376364",
                    "name": "TCC",
                    "type": 1,
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
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 933.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 100.02,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "G0684447_GRP",
                "name": "BOGO60_GRP",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "376364",
                    "name": "TCC",
                    "type": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 933.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 100.02,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "I9624697_GRP",
                "name": "CAT-TEST_GRP",
                "description": "CAT-TEST",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "376364",
                    "name": "TCC",
                    "type": 1,
                    "subType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CAT-TEST"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1309,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 145.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "I9605316_GRP",
                "name": "CATEGORYSPECIAL_GRP",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "376364",
                    "name": "TCC",
                    "type": 1,
                    "subType": 2
                  }
                ],
                "specialFare": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 933,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 70,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 103.56,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "I9614314_GRP",
                "name": "CONVERT NO_GRP",
                "description": "ALLOWED TO CONVERT IS NO",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "376364",
                    "name": "TCC",
                    "type": 1,
                    "subType": 2
                  }
                ],
                "bookOnline": true,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "ALLOWED TO CONVERT IS NO"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 834,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 88.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "I9614245_GRP",
                "name": "STANDARD_GRP",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "376364",
                    "name": "TCC",
                    "type": 1,
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
              "prices": [
                {
                  "id": 1,
                  "amount": 1334,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 148.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 933.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 100.02,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 933.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 100.02,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 834,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 88.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1N",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 933,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 99.96,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 8,
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 354225749,
          "code": "RS",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "RS",
              "status": 2,
              "fareCode": {
                "code": "I9614245",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7956,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Deluxe"
          }
        },
        {
          "id": 354271756,
          "code": "OS",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "OS",
              "status": 1,
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4419,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 518.28,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "OS",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4419,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 518.28,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "OS",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 5813,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 685.56,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Deluxe"
          }
        },
        {
          "id": 354127850,
          "code": "GT",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "GT",
              "status": 2,
              "fareCode": {
                "code": "I9614245",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 5356,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Deluxe"
          }
        },
        {
          "id": 354206726,
          "code": "GS",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "GS",
              "status": 1,
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3168.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 368.22,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "GS",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3168,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 368.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "GS",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4027,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 471.24,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Deluxe"
          }
        },
        {
          "id": 354175974,
          "code": "VO",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "VO",
              "status": 2,
              "fareCode": {
                "code": "I9614245",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3841,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Deluxe"
          }
        },
        {
          "id": 354156352,
          "code": "J3",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "J3",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2429.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 279.54,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "J3",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2429.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 279.54,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "J3",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2429,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 279.48,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "J3",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2971,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 344.52,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Deluxe"
          }
        },
        {
          "id": 63907,
          "code": "J4",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "J4",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2111,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
              "upgradeFrom": "J4",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2111,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
              "upgradeFrom": "J4",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2111,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
              "upgradeFrom": "J4",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2516,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 289.92,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Deluxe"
          }
        },
        {
          "id": 63942,
          "code": "WS",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "WS",
              "status": 2,
              "fareCode": {
                "code": "I9614245",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2741,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Deluxe"
          }
        },
        {
          "id": 354088608,
          "code": "1B",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "1B",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1813.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 205.62,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1B",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1813.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 205.62,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1B",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1813,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 205.56,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1B",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2091,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 238.92,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Balcony"
          }
        },
        {
          "id": 354089063,
          "code": "2B",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "2B",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1659.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 187.14,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2B",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1659.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 187.14,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2B",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1659,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 187.08,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2B",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1871,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 212.52,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Balcony"
          }
        },
        {
          "id": 354088073,
          "code": "4B",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "4B",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1572,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 176.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4B",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1572,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 176.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4B",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1572,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 176.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4B",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1746,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 197.52,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Balcony"
          }
        },
        {
          "id": 63943,
          "code": "XB",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "XB",
              "status": 2,
              "fareCode": {
                "code": "I9614245",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2041,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Balcony"
          }
        },
        {
          "id": 63944,
          "code": "1K",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "1K",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1143,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 125.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1K",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1143,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 125.16,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1K",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1133,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 123.96,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1K",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1143,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 125.16,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 353805215,
          "code": "1M",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "1M",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1022,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 110.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1M",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1022,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 110.64,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1M",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 960,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 103.2,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1M",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1022,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 110.64,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 60058,
          "code": "CO",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "CO",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 856.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 90.78,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "CO",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 856.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 90.78,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "CO",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 74.88,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "CO",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 856,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 90.72,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 353805212,
          "code": "3N",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "3N",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 900.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 96.06,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "3N",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 900.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 96.06,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "3N",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 787,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 82.44,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "3N",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 900,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 96,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 353805214,
          "code": "2N",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "2N",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 856.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 90.78,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2N",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 856.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 90.78,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2N",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 74.88,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2N",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 856,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 90.72,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 68079,
          "code": "4N",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "4N",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 812.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4N",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 812.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4N",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 661,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 67.32,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4N",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 812,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.44,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 63945,
          "code": "YO",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "YO",
              "status": 2,
              "fareCode": {
                "code": "I9614245",
                "name": "STANDARD",
                "description": "STANDARD",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "isEligible": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "STANDARD"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1056,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 353805216,
          "code": "1V",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "1V",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 845.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 89.46,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1V",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 845.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 89.46,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "1V",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 708,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
              "upgradeFrom": "1V",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 845,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 89.4,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Inside"
          }
        },
        {
          "id": 354004885,
          "code": "3V",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "3V",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 812.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "3V",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 812.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "3V",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 661,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 67.32,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "3V",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 812,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.44,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Inside"
          }
        },
        {
          "id": 354004596,
          "code": "2V",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "2V",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 779.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 81.54,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2V",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 779.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 81.54,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2V",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 614,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 61.68,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "2V",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 779,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 81.48,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Inside"
          }
        },
        {
          "id": 354005163,
          "code": "4V",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "4V",
              "status": 1,
              "fareCode": {
                "code": "G0684253",
                "name": "BOGO60",
                "description": "4n or less",
                "type": 0,
                "refundableType": 1,
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
                  "agencyDescription": "Buy One and Get One Free - Special Offer",
                  "fareTypeDescription": "Discount",
                  "remarks": "4n or less"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 735.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 76.26,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4V",
              "status": 1,
              "fareCode": {
                "code": "G0684447",
                "name": "BOGO60",
                "description": "5n and longer",
                "type": 0,
                "refundableType": 1,
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
                  "remarks": "5n and longer"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 735.5,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 76.26,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4V",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 551,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 54.12,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "4V",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 735,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 76.2,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Inside"
          }
        },
        {
          "id": 63946,
          "code": "ZI",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "ZI",
              "status": 1,
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "description": "GS and above",
                "type": 0,
                "refundableType": 2,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 669,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.28,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "ZI",
              "status": 1,
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
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 456,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 42.72,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "ZI",
              "status": 1,
              "fareCode": {
                "code": "I9605316",
                "name": "CATEGORYSPECIAL",
                "description": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE",
                "type": 0,
                "refundableType": 1,
                "isEligible": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Discount",
                  "remarks": "CATEGORY SPECIAL SUB TYPE - NO QUALIFIERS NEE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 669,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 79.45,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.28,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": true
          },
          "location": {
            "code": "Inside"
          }
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 52,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
