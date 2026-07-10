# Price Reservation

**Path:** Modify Reservation > Create Reservation With Gratuities then Modify By Adding Insurance > Price Reservation

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listprices`

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
            "packageId": 1307173,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "SL",
                "fare": {
                    "fareCode": {
                        "code": "BESTFARE"
                    }
                }
            }
        ],
        "addOns": [
            {
                "code": "PPSRVCHG"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970",
            "age": 52,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "age": 57,
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
Date: Thu, 04 May 2023 08:41:53 GMT
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
      "requestId": "c762e2b1-1570-4d6b-a18d-dee3a6e8cf3b",
      "timeStamp": "04-May-2023 04:41:50",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "15-Mar-2024 00:00:00",
        "arrivalDateTime": "22-Mar-2024 00:00:00",
        "departureCityId": "GLS",
        "arrivalCityId": "GLS",
        "duration": 7
      },
      "pos": {
        "id": 2250,
        "apiId": "NCL",
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
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "type": 0,
            "amount": 972.14,
            "dueDate": "04-May-2023 04:41:00"
          },
          {
            "type": 1,
            "amount": 9467.8,
            "dueDate": "26-Oct-2023 00:00:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 0,
            "amount": 972.14,
            "dueDate": "04-May-2023 04:41:00"
          },
          {
            "type": 1,
            "amount": 9467.8,
            "dueDate": "26-Oct-2023 00:00:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 0,
            "amount": 972.14,
            "dueDate": "05-May-2023 04:41:52"
          },
          {
            "type": 1,
            "amount": 7912.38,
            "dueDate": "16-Nov-2023 00:00:00"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "5",
          "amount": 14956,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 390,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 5,
          "code": "34",
          "amount": -5234.6,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 9721.4,
          "priority": 10,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 48,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 46,
          "code": "",
          "amount": 9721.4,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 9331.4,
          "priority": 16,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 3,
          "code": "18",
          "amount": 368.54,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": -1
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 17,
          "code": "",
          "amount": 10439.939999999999,
          "priority": 100,
          "display": true,
          "rph": -1
        },
        {
          "id": 86,
          "code": "",
          "amount": 0,
          "priority": 100,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 16,
          "code": "15",
          "amount": 350,
          "priority": 105,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 23,
          "code": "",
          "amount": 10439.939999999999,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 10439.939999999999,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "amount": 10439.94,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "amount": 972.14,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 26,
          "code": "2",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 62,
          "code": "",
          "amount": 10439.94,
          "priority": 382,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 32,
          "code": "66",
          "amount": 1555.42,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 36,
          "code": "85",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 510,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "amount": 8884.52,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "amount": 10439.939999999999,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "amount": 1555.4199999999983,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "amount": 7478,
          "priority": 5,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 195,
          "priority": 6,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 5,
          "code": "34",
          "amount": -2617.3,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "amount": 4860.7,
          "priority": 10,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 48,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 46,
          "code": "",
          "amount": 4860.7,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "amount": 4665.7,
          "priority": 16,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 3,
          "code": "18",
          "amount": 184.27,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 1
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 86,
          "code": "",
          "amount": 0,
          "priority": 100,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 17,
          "code": "",
          "amount": 5219.969999999999,
          "priority": 100,
          "display": true,
          "rph": 1
        },
        {
          "id": 16,
          "code": "15",
          "amount": 175,
          "priority": 105,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 23,
          "code": "",
          "amount": 5219.969999999999,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "amount": 5219.969999999999,
          "priority": 355,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "amount": 5219.97,
          "priority": 359,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 24,
          "code": "6",
          "amount": 486.07,
          "priority": 360,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 26,
          "code": "2",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 62,
          "code": "",
          "amount": 5219.97,
          "priority": 382,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 32,
          "code": "66",
          "amount": 777.71,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 36,
          "code": "85",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 510,
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "amount": 4442.26,
          "priority": 510,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 112,
          "code": "",
          "amount": 5219.969999999999,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "amount": 777.7099999999991,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 1,
          "code": "5",
          "amount": 7478,
          "priority": 5,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 195,
          "priority": 6,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 5,
          "code": "34",
          "amount": -2617.3,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "amount": 4860.7,
          "priority": 10,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 48,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 46,
          "code": "",
          "amount": 4860.7,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "amount": 4665.7,
          "priority": 16,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 3,
          "code": "18",
          "amount": 184.27,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 2
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 86,
          "code": "",
          "amount": 0,
          "priority": 100,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 17,
          "code": "",
          "amount": 5219.969999999999,
          "priority": 100,
          "display": true,
          "rph": 2
        },
        {
          "id": 16,
          "code": "15",
          "amount": 175,
          "priority": 105,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 23,
          "code": "",
          "amount": 5219.969999999999,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "amount": 5219.969999999999,
          "priority": 355,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "amount": 5219.97,
          "priority": 359,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 24,
          "code": "6",
          "amount": 486.07,
          "priority": 360,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 26,
          "code": "2",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 62,
          "code": "",
          "amount": 5219.97,
          "priority": 382,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 32,
          "code": "66",
          "amount": 777.71,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 36,
          "code": "85",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 510,
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "amount": 4442.26,
          "priority": 510,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 112,
          "code": "",
          "amount": 5219.969999999999,
          "priority": 600,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "amount": 777.7099999999991,
          "priority": 600,
          "displayType": 4,
          "rph": 2
        }
      ],
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1307173,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 15089
            }
          ]
        },
        "itinerary": {
          "id": 363332,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "15-Mar-2024 00:00:00",
          "arrivalDateTime": "22-Mar-2024 00:00:00",
          "departureCityId": "GLS",
          "arrivalCityId": "GLS",
          "code": "18440175"
        },
        "transportationType": 29
      },
      "addOns": [
        {
          "code": "CHOALL4M",
          "name": "FAS_Ultimate Beverage, Dining Package, Internet, Shorex Credit",
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
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ],
          "externalSessionInfo": {}
        },
        {
          "code": "EASYFARE",
          "name": "OTH_Early Booking Fare - Upgrades - A/S",
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
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ],
          "externalSessionInfo": {}
        },
        {
          "code": "FLEXNET",
          "name": "OTH_FAS NET RATES",
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
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ],
          "externalSessionInfo": {}
        },
        {
          "code": "HSBVSXIN",
          "name": "FAS_Ultimate Beverage, Internet, Shorex Credit",
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
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ],
          "externalSessionInfo": {}
        },
        {
          "code": "HSDISXIN",
          "name": "FAS_Specialty Dining Package, Internet, Shorex Credit",
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
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ],
          "externalSessionInfo": {}
        },
        {
          "code": "HSINTSHO",
          "name": "FAS_Internet, Shorex Credit",
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
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ],
          "externalSessionInfo": {}
        },
        {
          "code": "KOSHER MEAL",
          "name": "OTH_Kosher Meal",
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
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "PPSRVCHG"
          ],
          "externalSessionInfo": {}
        },
        {
          "code": "PPSRVCHG",
          "name": "OTH_Prepaid Service Charges",
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
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL"
          ],
          "externalSessionInfo": {}
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
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
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "age": 57,
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
