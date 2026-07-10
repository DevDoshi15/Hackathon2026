# Cabin Availability

**Path:** Create Reservation > Create Reservation - Payment Declined Flag > Cabin Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listcabins`

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
            "packageId": 1313282,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "H1",
                "fare": {
                    "fareCode": {
                        "code": "DISC35"
                    }
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
Date: Wed, 06 Sep 2023 09:38:48 GMT
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
      "requestId": "21c4ff74-7234-49a4-b476-6f2f36981083",
      "timeStamp": "06-Sep-2023 05:38:46",
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
      "categories": [
        {
          "id": 60316,
          "code": "H1",
          "fares": [
            {
              "fareCode": {
                "code": "DISC35",
                "type": 0
              }
            }
          ]
        }
      ],
      "cabins": [
        {
          "number": "14000",
          "beds": [
            {
              "code": "28",
              "description": "Single Sofa ",
              "type": 254,
              "count": 2
            },
            {
              "code": "15",
              "description": "Queen Bed ",
              "type": 243,
              "count": 2
            },
            {
              "code": "30",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            }
          ],
          "deck": {
            "id": 9444,
            "name": "Deck 14",
            "description": "Sun Deck, Private Hot Tub, The Haven Courtyard, Climbing Wall, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 8
          }
        }
      ],
      "addOns": [
        {
          "code": "CHO34",
          "name": "FAS_Taxes Only 3-4",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "CHOALL4M",
          "name": "FAS_Ultimate Beverage, Dining Package, Internet, Shorex Credit",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "DISC35",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "EASYFARE",
          "name": "OTH_Early Booking Fare - Upgrades - A/S",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "CHOALL4M",
            "DISC35",
            "FITOBC",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "FITOBC",
          "name": "OTH_FIT ONLY- Onboard Credit Offer",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "FLEXNET",
          "name": "OTH_FAS NET RATES",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "HSBVSXIN",
          "name": "FAS_Ultimate Beverage, Internet, Shorex Credit",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "DISC35",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "HSDISXIN",
          "name": "FAS_Specialty Dining Package, Internet, Shorex Credit",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "DISC35",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "HSINTSHO",
          "name": "FAS_Internet, Shorex Credit",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "DISC35",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "KOSHER MEAL",
          "name": "OTH_Kosher Meal",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "PPSRVCHG"
          ]
        },
        {
          "code": "PPSRVCHG",
          "name": "OTH_Prepaid Service Charges",
          "externalSessionInfo": {},
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHO34",
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL"
          ]
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
