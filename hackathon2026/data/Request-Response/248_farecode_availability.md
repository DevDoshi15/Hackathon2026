# Farecode Availability

**Path:** Create Reservation > Create Reservation - Payment Declined Flag > Farecode Availability

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
        "cruise": {
            "packageId": 1313282
        }
    },
    "customers": [
        {
            "rph": 1,
            "age": 53,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 58
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
Date: Wed, 06 Sep 2023 09:32:47 GMT
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
      "requestId": "dc1f582c-8380-4a6a-96a9-407db287f836",
      "timeStamp": "06-Sep-2023 05:32:44",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Jan-2024 00:00:00",
        "arrivalDateTime": "11-Jan-2024 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 9
      },
      "pos": {
        "id": 2520,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "B2B",
        "system": "Test",
        "apiId": "NCL"
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
        "packageId": 1313282,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 1100
            }
          ]
        },
        "itinerary": {
          "id": 372547,
          "destination": {
            "id": 10
          }
        },
        "voyage": {
          "departureDateTime": "02-Jan-2024 00:00:00",
          "arrivalDateTime": "11-Jan-2024 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "18439803"
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
          "name": "FAS NET RATES",
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
      "rulesInfo": {
        "applicableRules": [
          {
            "id": 1728342,
            "name": "Cruise Discount (5$)",
            "groupName": "excl_1728342",
            "type": 1,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728343,
            "name": "Cruise Markup (25$)",
            "groupName": "excl_1728343",
            "type": 2,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728420,
            "name": "VAO Exclusive",
            "groupName": "excl_1728420",
            "type": 3,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "va_earlysaver.png"
            }
          },
          {
            "id": 1728421,
            "name": "VAO One Exclusive",
            "groupName": "excl_1728421",
            "type": 3,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "pink-circle.png"
            }
          },
          {
            "id": 1728422,
            "name": "VAO Non Exclusive",
            "groupName": "nonexcl",
            "type": 3,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "CruiseCategory",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "va_anchor-vODY-635382737153437500.png"
            }
          },
          {
            "id": 1728423,
            "name": "VAO Two Non Exclusive",
            "groupName": "nonexcl",
            "type": 3,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "CruiseCategory",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "va_sale.png"
            }
          },
          {
            "id": 1728419,
            "name": "Cruise Addon",
            "groupName": "excl_1728419",
            "type": 9,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728344,
            "name": "Cruise Service Fee (20$)",
            "groupName": "excl_1728344",
            "type": 13,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728415,
            "name": "Package Service Doc (10)",
            "groupName": "P1",
            "type": 18,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<strong>Customer Details</strong> added here",
              "agencyDetails": "Agency Details Added Here",
              "redemptionDetails": "Redemption details goes here",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728416,
            "name": "Package Service Doc One (15)",
            "groupName": "P1",
            "type": 18,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<strong>Customer Details</strong> added here",
              "agencyDetails": "Agency Details Added Here",
              "redemptionDetails": "Redemption details goes here",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728417,
            "name": "Package Service Travel (25) BEST Value YES",
            "groupName": "P2",
            "type": 18,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<strong>Customer Details</strong> added here",
              "agencyDetails": "Agency Details Added Here",
              "redemptionDetails": "Redemption details goes here",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728418,
            "name": "Package Service Travel (20) BEST Value NO",
            "groupName": "P2",
            "type": 18,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<strong>Customer Details</strong> added here",
              "agencyDetails": "Agency Details Added Here",
              "redemptionDetails": "Redemption details goes here",
              "customLink": "",
              "imageUrl": ""
            }
          }
        ]
      },
      "dinings": [
        {
          "id": 4,
          "code": "FREESTYLE",
          "name": "Freestyle",
          "status": 7
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 53,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 58
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
