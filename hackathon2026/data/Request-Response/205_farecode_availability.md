# Farecode Availability

**Path:** Create Reservation > Occupancy Based Samples > Single Occupancy (NCL) > Farecode Availability

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
            "packageId": 1238898,
            "packageTourId": -1
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
Date: Thu, 23 Mar 2023 12:01:39 GMT
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
      "requestId": "f2b23636-f56e-49ce-bf30-9ab2e83295fa",
      "timeStamp": "23-Mar-2023 08:01:37",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "05-May-2023 00:00:00",
        "arrivalDateTime": "08-May-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 3
      },
      "pos": {
        "id": 2112,
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
        }
      ],
      "cruise": {
        "packageId": 1238898,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 1179
            }
          ]
        },
        "itinerary": {
          "id": 363194,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "05-May-2023 00:00:00",
          "arrivalDateTime": "08-May-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "17183730"
        },
        "transportationType": 29
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
          "code": "34CHO",
          "name": "Taxes Only 3-4",
          "description": "FAS_Taxes Only 3-4",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 12
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "FAS_Taxes Only 3-4",
            "qualifierCodes": ""
          }
        },
        {
          "code": "CHO34",
          "name": "Taxes Only 3-4",
          "description": "FAS_Taxes Only 3-4",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 12
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Taxes Only 3-4",
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
        "age": 52,
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
