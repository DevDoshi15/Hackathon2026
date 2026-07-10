# Farecode Availability

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 4 – All Adults (NCL) > Farecode Availability

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
            "packageId": 1312610
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
        },
        {
            "rph": 4,
            "age": 40
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
Date: Fri, 31 Mar 2023 08:48:34 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "cbac7e04-736e-4239-a993-1a073f80c2de",
      "timeStamp": "31-Mar-2023 04:48:32",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "27-Jun-2023 00:00:00",
        "arrivalDateTime": "08-Jul-2023 00:00:00",
        "departureCityId": "SEA",
        "arrivalCityId": "SEA",
        "duration": 11
      },
      "pos": {
        "id": 2250,
        "apiId": "NCL",
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
        },
        {
          "rph": 3,
          "ageGroup": "Adult"
        },
        {
          "rph": 4,
          "ageGroup": "Adult"
        }
      ],
      "cruise": {
        "packageId": 1312610,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13670
            }
          ]
        },
        "itinerary": {
          "id": 351639,
          "destination": {
            "id": 1
          }
        },
        "tourCode": "18707348",
        "voyage": {
          "departureDateTime": "01-Jul-2023 00:00:00",
          "arrivalDateTime": "08-Jul-2023 00:00:00",
          "departureCityId": "SEA",
          "arrivalCityId": "SEA",
          "code": "18506272"
        },
        "transportationType": 28
      },
      "fareCodes": [
        {
          "code": "BESTFARE",
          "name": "BEST_FARE",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "",
            "qualifierCodes": ""
          }
        },
        {
          "code": "EASYFARE",
          "name": "Early Booking Fare",
          "description": "OTH_Early Booking Fare - Upgrades - A/S",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "OTH_Early Booking Fare - Upgrades - A/S",
            "qualifierCodes": ""
          }
        },
        {
          "code": "SAILAWAY",
          "name": "Sail Away Rates",
          "description": "SWY_Sail Away Rates",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "SWY_Sail Away Rates",
            "qualifierCodes": ""
          }
        },
        {
          "code": "PPSRVCHG",
          "name": "Prepaid Service Charges",
          "description": "OTH_Prepaid Service Charges",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 19
            }
          ],
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "OTH_Prepaid Service Charges",
            "qualifierCodes": ""
          }
        },
        {
          "code": "DISC35",
          "name": "NCL Reduce Rate Percentage Off",
          "description": "OTH_NCL Reduce Rate Percentage Off",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 6
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "OTH_NCL Reduce Rate Percentage Off",
            "qualifierCodes": ""
          }
        },
        {
          "code": "FLEXNET",
          "name": "NET RATES",
          "description": "OTH_NET RATES",
          "type": 12,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "OTH_NET RATES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "KOSHER MEAL",
          "name": "Kosher Meal",
          "description": "OTH_Kosher Meal",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "OTH_Kosher Meal"
          }
        },
        {
          "code": "ALL4CHO",
          "name": "Beverage, Dining, Internet, Shorex",
          "description": "FAS_Beverage, Dining, Internet, $50 per port Shore Ex Credit",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 2
            },
            {
              "type": 3
            },
            {
              "type": 4
            },
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Beverage, Dining, Internet, $50 per port Shore Ex Credit",
            "qualifierCodes": ""
          }
        },
        {
          "code": "BVSXIN",
          "name": "Beverage, Internet, $50 Shore Ex credit",
          "description": "FAS_Beverage, Internet, $50 per port Shore Ex Credit",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 3
            },
            {
              "type": 4
            },
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "FAS_Beverage, Internet, $50 per port Shore Ex Credit",
            "qualifierCodes": ""
          }
        },
        {
          "code": "CHOALL4M",
          "name": "Ultimate Beverage, Dining Package, Inter",
          "description": "FAS_Ultimate Beverage, Dining Package, Internet, Shorex Credit",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 2
            },
            {
              "type": 3
            },
            {
              "type": 4
            },
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Ultimate Beverage, Dining Package, Internet, Shorex Credit",
            "qualifierCodes": ""
          }
        },
        {
          "code": "DISXIN",
          "name": "Dining, Internet, $50 Shore Ex credit",
          "description": "FAS_Dining Package, Internet, $50 per port Shore Ex Credit",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 2
            },
            {
              "type": 4
            },
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "FAS_Dining Package, Internet, $50 per port Shore Ex Credit",
            "qualifierCodes": ""
          }
        },
        {
          "code": "HSBVSXIN",
          "name": "Ultimate Beverage, Internet, Shorex Cred",
          "description": "FAS_Ultimate Beverage, Internet, Shorex Credit",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 3
            },
            {
              "type": 4
            },
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Ultimate Beverage, Internet, Shorex Credit",
            "qualifierCodes": ""
          }
        },
        {
          "code": "HSDISXIN",
          "name": "Specialty Dining Package, Internet, Shor",
          "description": "FAS_Specialty Dining Package, Internet, Shorex Credit",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 2
            },
            {
              "type": 4
            },
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Specialty Dining Package, Internet, Shorex Credit",
            "qualifierCodes": ""
          }
        },
        {
          "code": "HSINTSHO",
          "name": "Internet, Shorex Credit",
          "description": "FAS_Internet, Shorex Credit",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 4
            },
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Internet, Shorex Credit",
            "qualifierCodes": ""
          }
        },
        {
          "code": "INTSHO",
          "name": "Internet Package and $50 Shore Ex credit",
          "description": "FAS_Internet Package and $50 per port Shore Ex Credit",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 4
            },
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "FAS_Internet Package and $50 per port Shore Ex Credit",
            "qualifierCodes": ""
          }
        },
        {
          "code": "FITOBC",
          "name": "FIT ONLY- Onboard Credit Offer",
          "description": "OTH_FIT ONLY- Onboard Credit Offer",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 1
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "OTH_FIT ONLY- Onboard Credit Offer",
            "qualifierCodes": ""
          }
        },
        {
          "code": "SAILSHOX",
          "name": "Shorex Discount Program For X Categories",
          "description": "SWY_Shorex Discount Program For X Categories",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 18
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "SWY_Shorex Discount Program For X Categories",
            "qualifierCodes": ""
          }
        }
      ],
      "dinings": [
        {
          "id": 4,
          "code": "FREESTYLE",
          "name": "Freestyle",
          "tableSizeOptions": []
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
      },
      {
        "rph": 4,
        "age": 40
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
