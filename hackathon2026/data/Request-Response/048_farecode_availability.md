# Farecode Availability

**Path:** Cabin Details > Cabin Position & Remarks > Farecode Availability

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
        "pos": {
            "currency": "USD"
        },
        "cruise": {
            "packageId": 1282255
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
Date: Thu, 16 Mar 2023 14:41:28 GMT
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
      "requestId": "6e4c33ef-046b-4319-959e-1edc7ebc488b",
      "timeStamp": "16-Mar-2023 10:41:22",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "09-Apr-2023 00:00:00",
        "arrivalDateTime": "16-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 7
      },
      "pos": {
        "id": 2109,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2C"
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
      "cruise": {
        "packageId": 1282255,
        "packageTourId": -1,
        "cruiseline": {
          "id": 2,
          "ships": [
            {
              "id": 14948
            }
          ]
        },
        "itinerary": {
          "id": 364303,
          "destination": {
            "id": 14
          }
        },
        "tourCode": "BY07W480",
        "voyage": {
          "departureDateTime": "09-Apr-2023 00:00:00",
          "arrivalDateTime": "16-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "BY07W480"
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
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
          "code": "I3404962_GRP",
          "name": "GROUPX_GRP",
          "description": "GROUPX",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "GROUPX"
          }
        },
        {
          "code": "I3403852_GRP",
          "name": "STANDARD_GRP",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
          "code": "I3392231_GRP",
          "name": "BROCHURE_GRP",
          "description": "BROCHURE PRICE",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
          "code": "I3406581_GRP",
          "name": "STANDARD CREW_GRP",
          "description": "STANDARD CREW",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD CREW"
          }
        },
        {
          "code": "I3395524_GRP",
          "name": "ES STANDARD_GRP",
          "description": "ES STANDARD",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "ES STANDARD"
          }
        },
        {
          "code": "H8212136_GRP",
          "name": "ALWAYS INC NRD_GRP",
          "description": "Surf Wifi Classic Bev tips or svc fees NRD",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 27
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Surf Wifi Classic Bev tips or svc fees NRD"
          }
        },
        {
          "code": "H8498689_GRP",
          "name": "ELEVATE NRD_GRP",
          "description": "Surf Wifi Prem Bev OBC tips or svc fees NRD",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 28
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Surf Wifi Prem Bev OBC tips or svc fees NRD"
          }
        },
        {
          "code": "H8212138_GRP",
          "name": "INDULGE NRD_GRP",
          "description": "Stream Wifi Prem Bev OBC tips or svc fees NRD",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 29
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Stream Wifi Prem Bev OBC tips or svc fees NRD"
          }
        },
        {
          "code": "I9565249_GRP",
          "name": "NRP Promo 4_GRP",
          "description": "NRP",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "H8212139",
              "description": "RETREAT NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212136",
              "description": "ALWAYS INC NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212138",
              "description": "INDULGE NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8498689",
              "description": "ELEVATE NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
          "code": "I9565670_GRP",
          "name": "PROMOCODE G NRD_GRP",
          "description": "promo code g",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212139",
              "description": "RETREAT NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212136",
              "description": "ALWAYS INC NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212138",
              "description": "INDULGE NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8498689",
              "description": "ELEVATE NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "promo code g"
          }
        },
        {
          "code": "H8212139_GRP",
          "name": "RETREAT NRD_GRP",
          "description": "Stream Wifi Prem Bev OBC tips or svc fees NRD",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 30
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Stream Wifi Prem Bev OBC tips or svc fees NRD"
          }
        },
        {
          "code": "I5942158_GRP",
          "name": "SIMPLY SAIL NRD_GRP",
          "description": "Non Refundable Rate only no perks",
          "type": 0,
          "refundableType": 2,
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "Non Refundable Rate only no perks"
          }
        },
        {
          "code": "I9575200_GRP",
          "name": "Air Test2_GRP",
          "description": "Air Test 2",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8498688",
              "description": "ELEVATE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212135",
              "description": "RETREAT",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "Air Test 2"
          }
        },
        {
          "code": "H8212132_GRP",
          "name": "ALWAYS INC_GRP",
          "description": "Surf Wifi Classic Bev tips or svc fees",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 27
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Surf Wifi Classic Bev tips or svc fees"
          }
        },
        {
          "code": "H8498688_GRP",
          "name": "ELEVATE_GRP",
          "description": "Surf Wifi Prem Bev OBC tips or svc fees",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 28
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Surf Wifi Prem Bev OBC tips or svc fees"
          }
        },
        {
          "code": "H8212134_GRP",
          "name": "INDULGE_GRP",
          "description": "Stream Wifi Prem Bev OBC tips or svc fees",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 29
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Stream Wifi Prem Bev OBC tips or svc fees"
          }
        },
        {
          "code": "I9573782_GRP",
          "name": "MIguel Air_GRP",
          "description": "Miguel Air",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8498688",
              "description": "ELEVATE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212135",
              "description": "RETREAT",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "Miguel Air"
          }
        },
        {
          "code": "I9573527_GRP",
          "name": "PC 7_GRP",
          "description": "PC 7",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "PC 7"
          }
        },
        {
          "code": "I9573528_GRP",
          "name": "PC5_GRP",
          "description": "PC5",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "PC5"
          }
        },
        {
          "code": "I9573529_GRP",
          "name": "PC8_GRP",
          "description": "PC8",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "PC8"
          }
        },
        {
          "code": "I9565245_GRP",
          "name": "Promo 4_GRP",
          "description": "Promo 4",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "Promo 4"
          }
        },
        {
          "code": "I9565726_GRP",
          "name": "Promo H_GRP",
          "description": "Promo H",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "Promo H"
          }
        },
        {
          "code": "I9565671_GRP",
          "name": "PROMOCODE G_GRP",
          "description": "PROMO CODE G",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8498688",
              "description": "ELEVATE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212135",
              "description": "RETREAT",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "PROMO CODE G"
          }
        },
        {
          "code": "H8212135_GRP",
          "name": "RETREAT_GRP",
          "description": "Stream Wifi Prem Bev OBC tips or svc fees",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 30
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Stream Wifi Prem Bev OBC tips or svc fees"
          }
        },
        {
          "code": "I9562268_GRP",
          "name": "RLG Air Test_GRP",
          "description": "RLG Air Test",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8498688",
              "description": "ELEVATE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212135",
              "description": "RETREAT",
              "type": 0,
              "refundableType": 1
            }
          ],
          "groups": [
            {
              "code": "4476810",
              "name": "DIRECT LINE",
              "type": 1,
              "subType": 2
            },
            {
              "code": "3437439",
              "name": "TLN HEADQUARTER",
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
            "remarks": "RLG Air Test"
          }
        },
        {
          "code": "BESTRATE",
          "name": "Best Rate",
          "description": "Restrictions May Apply",
          "type": 0,
          "refundableType": 1,
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
          "code": "I3392231",
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
          "code": "I3406581",
          "name": "STANDARD CREW",
          "description": "STANDARD CREW",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD CREW"
          }
        },
        {
          "code": "I3395524",
          "name": "ES STANDARD",
          "description": "ES STANDARD",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "ES STANDARD"
          }
        },
        {
          "code": "I3403852",
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
          "code": "H8212136",
          "name": "ALWAYS INC NRD",
          "description": "Surf Wifi Classic Bev tips or svc fees NRD",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 27
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Surf Wifi Classic Bev tips or svc fees NRD",
            "qualifierCodes": ""
          }
        },
        {
          "code": "H8498689",
          "name": "ELEVATE NRD",
          "description": "Surf Wifi Prem Bev OBC tips or svc fees NRD",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 28
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Surf Wifi Prem Bev OBC tips or svc fees NRD",
            "qualifierCodes": ""
          }
        },
        {
          "code": "H8212138",
          "name": "INDULGE NRD",
          "description": "Stream Wifi Prem Bev OBC tips or svc fees NRD",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 29
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Stream Wifi Prem Bev OBC tips or svc fees NRD",
            "qualifierCodes": ""
          }
        },
        {
          "code": "I9565249",
          "name": "NRP Promo 4",
          "description": "NRP",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "H8212139",
              "description": "RETREAT NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212136",
              "description": "ALWAYS INC NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212138",
              "description": "INDULGE NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8498689",
              "description": "ELEVATE NRD",
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
          "code": "I9565670",
          "name": "PROMOCODE G NRD",
          "description": "promo code g",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212139",
              "description": "RETREAT NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212136",
              "description": "ALWAYS INC NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8212138",
              "description": "INDULGE NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "H8498689",
              "description": "ELEVATE NRD",
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
            "remarks": "promo code g"
          }
        },
        {
          "code": "H8212139",
          "name": "RETREAT NRD",
          "description": "Stream Wifi Prem Bev OBC tips or svc fees NRD",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I9565670",
              "description": "PROMOCODE G NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I9565250",
              "description": "NRP Loyalty",
              "type": 10,
              "refundableType": 2
            },
            {
              "code": "I9565249",
              "description": "NRP Promo 4",
              "type": 0,
              "refundableType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 30
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Stream Wifi Prem Bev OBC tips or svc fees NRD",
            "qualifierCodes": ""
          }
        },
        {
          "code": "I5942158",
          "name": "SIMPLY SAIL NRD",
          "description": "Non Refundable Rate only no perks",
          "type": 0,
          "refundableType": 2,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Non Refundable Rate only no perks",
            "qualifierCodes": ""
          }
        },
        {
          "code": "I9575200",
          "name": "Air Test2",
          "description": "Air Test 2",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8498688",
              "description": "ELEVATE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212135",
              "description": "RETREAT",
              "type": 0,
              "refundableType": 1
            }
          ],
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Air Test 2"
          }
        },
        {
          "code": "H8212132",
          "name": "ALWAYS INC",
          "description": "Surf Wifi Classic Bev tips or svc fees",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "dynamicRules": [
            {
              "type": 27
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Surf Wifi Classic Bev tips or svc fees",
            "qualifierCodes": ""
          }
        },
        {
          "code": "H8498688",
          "name": "ELEVATE",
          "description": "Surf Wifi Prem Bev OBC tips or svc fees",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "dynamicRules": [
            {
              "type": 28
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Surf Wifi Prem Bev OBC tips or svc fees",
            "qualifierCodes": ""
          }
        },
        {
          "code": "H8212134",
          "name": "INDULGE",
          "description": "Stream Wifi Prem Bev OBC tips or svc fees",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "dynamicRules": [
            {
              "type": 29
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Stream Wifi Prem Bev OBC tips or svc fees",
            "qualifierCodes": ""
          }
        },
        {
          "code": "I9573782",
          "name": "MIguel Air",
          "description": "Miguel Air",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8498688",
              "description": "ELEVATE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212135",
              "description": "RETREAT",
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
            "remarks": "Miguel Air"
          }
        },
        {
          "code": "I9573527",
          "name": "PC 7",
          "description": "PC 7",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
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
            "remarks": "PC 7"
          }
        },
        {
          "code": "I9573528",
          "name": "PC5",
          "description": "PC5",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
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
            "remarks": "PC5"
          }
        },
        {
          "code": "I9573529",
          "name": "PC8",
          "description": "PC8",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
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
            "remarks": "PC8"
          }
        },
        {
          "code": "I9565245",
          "name": "Promo 4",
          "description": "Promo 4",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Promo 4"
          }
        },
        {
          "code": "I9565726",
          "name": "Promo H",
          "description": "Promo H",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Promo H"
          }
        },
        {
          "code": "I9565671",
          "name": "PROMOCODE G",
          "description": "PROMO CODE G",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8498688",
              "description": "ELEVATE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212135",
              "description": "RETREAT",
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
            "remarks": "PROMO CODE G"
          }
        },
        {
          "code": "H8212135",
          "name": "RETREAT",
          "description": "Stream Wifi Prem Bev OBC tips or svc fees",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9575200",
              "description": "Air Test2",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "I9565671",
              "description": "PROMOCODE G",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573782",
              "description": "MIguel Air",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9562268",
              "description": "RLG Air Test",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            }
          ],
          "dynamicRules": [
            {
              "type": 30
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "Stream Wifi Prem Bev OBC tips or svc fees",
            "qualifierCodes": ""
          }
        },
        {
          "code": "I9562268",
          "name": "RLG Air Test",
          "description": "RLG Air Test",
          "type": 0,
          "refundableType": 1,
          "combinableFares": [
            {
              "code": "I9573527",
              "description": "PC 7",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573529",
              "description": "PC8",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565726",
              "description": "Promo H",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565245",
              "description": "Promo 4",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9565247",
              "description": "Loyalty",
              "type": 10,
              "refundableType": 1
            },
            {
              "code": "H8212132",
              "description": "ALWAYS INC",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I9573528",
              "description": "PC5",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212134",
              "description": "INDULGE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8498688",
              "description": "ELEVATE",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "H8212135",
              "description": "RETREAT",
              "type": 0,
              "refundableType": 1
            }
          ],
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "RLG Air Test"
          }
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
