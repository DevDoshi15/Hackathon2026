# Farecode Availability

**Path:** Create Reservation > Create Reservation With Grats/AddOns For NCL > Farecode Availability

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
            "currency":"USD"
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
            "packageId": 1238898
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
Date: Fri, 17 Feb 2023 15:27:16 GMT
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
      "requestId": "b0c2b914-6e64-4698-a9c1-1af168171ccd",
      "timeStamp": "17-Feb-2023 10:27:12",
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
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
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "EASYFARE",
          "name": "Early Booking Fare",
          "description": "OTH_Early Booking Fare - Upgrades - A/S",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "OTH_Early Booking Fare - Upgrades - A/S",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "SAILAWAY",
          "name": "Sail Away Rates",
          "description": "SWY_Sail Away Rates",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "SWY_Sail Away Rates",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "DISC50",
          "name": "NCL Reduce Rate Percentage Off",
          "description": "OTH_NCL Reduce Rate Percentage Off",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "OTH_NCL Reduce Rate Percentage Off"
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "ALL4CHO",
          "name": "Beverage, Dining, Internet, Shorex",
          "description": "FAS_Beverage, Dining, Internet, $50 per port Shore Ex Credit",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Beverage, Dining, Internet, $50 per port Shore Ex Credit",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
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
          ]
        },
        {
          "code": "BVSXIN",
          "name": "Beverage, Internet, $50 Shore Ex credit",
          "description": "FAS_Beverage, Internet, $50 per port Shore Ex Credit",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "FAS_Beverage, Internet, $50 per port Shore Ex Credit",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
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
          ]
        },
        {
          "code": "CHOALL4M",
          "name": "Ultimate Beverage, Dining Package, Inter",
          "description": "FAS_Ultimate Beverage, Dining Package, Internet, Shorex Credit",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Ultimate Beverage, Dining Package, Internet, Shorex Credit",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
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
          ]
        },
        {
          "code": "DISXIN",
          "name": "Dining, Internet, $50 Shore Ex credit",
          "description": "FAS_Dining Package, Internet, $50 per port Shore Ex Credit",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "FAS_Dining Package, Internet, $50 per port Shore Ex Credit",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
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
          ]
        },
        {
          "code": "HSBVSXIN",
          "name": "Ultimate Beverage, Internet, Shorex Cred",
          "description": "FAS_Ultimate Beverage, Internet, Shorex Credit",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Ultimate Beverage, Internet, Shorex Credit",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
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
          ]
        },
        {
          "code": "HSDISXIN",
          "name": "Specialty Dining Package, Internet, Shor",
          "description": "FAS_Specialty Dining Package, Internet, Shorex Credit",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Specialty Dining Package, Internet, Shorex Credit",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
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
          ]
        },
        {
          "code": "HSINTSHO",
          "name": "Internet, Shorex Credit",
          "description": "FAS_Internet, Shorex Credit",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Internet, Shorex Credit",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 4
            },
            {
              "type": 18
            }
          ]
        },
        {
          "code": "INTSHO",
          "name": "Internet Package and $50 Shore Ex credit",
          "description": "FAS_Internet Package and $50 per port Shore Ex Credit",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "FAS_Internet Package and $50 per port Shore Ex Credit",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 4
            },
            {
              "type": 18
            }
          ]
        },
        {
          "code": "34CHO",
          "name": "Taxes Only 3-4",
          "description": "FAS_Taxes Only 3-4",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "FAS_Taxes Only 3-4",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 12
            }
          ]
        },
        {
          "code": "CHO34",
          "name": "Taxes Only 3-4",
          "description": "FAS_Taxes Only 3-4",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "FAS_Taxes Only 3-4",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 12
            }
          ]
        },
        {
          "code": "FITOBC",
          "name": "FIT ONLY- Onboard Credit Offer",
          "description": "OTH_FIT ONLY- Onboard Credit Offer",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "OTH_FIT ONLY- Onboard Credit Offer",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 1
            }
          ]
        },
        {
          "code": "SAILSHOX",
          "name": "Shorex Discount Program For X Categories",
          "description": "SWY_Shorex Discount Program For X Categories",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "SWY_Shorex Discount Program For X Categories",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 18
            }
          ]
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
