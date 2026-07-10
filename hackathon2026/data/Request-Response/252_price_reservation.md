# Price Reservation

**Path:** Create Reservation > Create Reservation - Payment Declined Flag > Price Reservation

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
//This request contains only mandatory elements
{
    "cruiseReservation": {
      "pos": {
        "currency": "USD"
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
Date: Wed, 06 Sep 2023 09:40:11 GMT
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
      "requestId": "28c35f07-08a4-4f88-8ba6-9b6e1b5e9470",
      "timeStamp": "06-Sep-2023 05:40:10",
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
        "type": "Any",
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
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "type": 2,
            "amount": 34315.04,
            "dueDate": "06-Sep-2023 05:40:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 34315.04,
            "dueDate": "06-Sep-2023 05:40:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 28961.78,
            "dueDate": "06-Sep-2023 05:40:11"
          }
        ]
      },
      "prices": [
        {
          "id": 128,
          "code": "P1",
          "amount": 10,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 128,
          "code": "P2",
          "amount": 20,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "amount": 51841,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 429,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 5,
          "code": "34",
          "amount": -18135.6,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 33705.4,
          "priority": 10,
          "display": true,
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
          "amount": 25,
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
          "amount": -5,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 46,
          "code": "",
          "amount": 33700.4,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 33271.4,
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
          "amount": 564.64,
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
          "amount": 34315.04,
          "priority": 100,
          "display": true,
          "rph": -1
        },
        {
          "id": 86,
          "code": "",
          "amount": 20,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 20,
          "code": "14",
          "amount": 0,
          "priority": 120,
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
          "amount": 34315.04,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 42,
          "code": "96",
          "amount": 0,
          "priority": 351,
          "display": true,
          "displayType": 9,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 34315.04,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "amount": 34245.04,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "amount": 0,
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
          "amount": 34245.04,
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
          "amount": 5283.26,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 32,
          "code": "32",
          "amount": 28961.78,
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
          "id": 164,
          "code": "31",
          "amount": 5283.26,
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
          "amount": 28961.78,
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
          "amount": 34315.04,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "amount": 5353.260000000002,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 128,
          "code": "P2",
          "amount": 10,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 128,
          "code": "P1",
          "amount": 5,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 1,
          "code": "5",
          "amount": 25920.5,
          "priority": 5,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 214.5,
          "priority": 6,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 5,
          "code": "34",
          "amount": -9067.8,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "amount": 16852.7,
          "priority": 10,
          "display": true,
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
          "amount": -2.5,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 48,
          "code": "",
          "amount": 12.5,
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
          "amount": 16850.2,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "amount": 16635.7,
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
          "amount": 282.32,
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
          "id": 17,
          "code": "",
          "amount": 17157.52,
          "priority": 100,
          "display": true,
          "rph": 1
        },
        {
          "id": 86,
          "code": "",
          "amount": 10,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 20,
          "code": "14",
          "amount": 0,
          "priority": 120,
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
          "amount": 17157.52,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 42,
          "code": "96",
          "amount": 0,
          "priority": 351,
          "display": true,
          "displayType": 9,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "amount": 17157.52,
          "priority": 355,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "amount": 17122.52,
          "priority": 359,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 24,
          "amount": 0,
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
          "amount": 17122.52,
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
          "code": "32",
          "amount": 14480.89,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 32,
          "code": "66",
          "amount": 2641.63,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 164,
          "code": "31",
          "amount": 2641.63,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 510,
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
          "amount": 14480.89,
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
          "amount": 17157.52,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "amount": 2676.630000000001,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 128,
          "code": "P2",
          "amount": 10,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 128,
          "code": "P1",
          "amount": 5,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 1,
          "code": "5",
          "amount": 25920.5,
          "priority": 5,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 214.5,
          "priority": 6,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 5,
          "code": "34",
          "amount": -9067.8,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "amount": 16852.7,
          "priority": 10,
          "display": true,
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
          "amount": -2.5,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 48,
          "code": "",
          "amount": 12.5,
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
          "amount": 16850.2,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "amount": 16635.7,
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
          "amount": 282.32,
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
          "id": 17,
          "code": "",
          "amount": 17157.52,
          "priority": 100,
          "display": true,
          "rph": 2
        },
        {
          "id": 86,
          "code": "",
          "amount": 10,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 20,
          "code": "14",
          "amount": 0,
          "priority": 120,
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
          "amount": 17157.52,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 42,
          "code": "96",
          "amount": 0,
          "priority": 351,
          "display": true,
          "displayType": 9,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "amount": 17157.52,
          "priority": 355,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "amount": 17122.52,
          "priority": 359,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 24,
          "amount": 0,
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
          "amount": 17122.52,
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
          "code": "32",
          "amount": 14480.89,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 32,
          "code": "66",
          "amount": 2641.63,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 164,
          "code": "31",
          "amount": 2641.63,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 510,
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
          "amount": 14480.89,
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
          "amount": 17157.52,
          "priority": 600,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "amount": 2676.630000000001,
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
              "imageUrl": "",
              "calculatedAmount": {
                "0": 5,
                "1": 2.5,
                "2": 2.5
              }
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
              "imageUrl": "",
              "calculatedAmount": {
                "0": 25,
                "1": 12.5,
                "2": 12.5
              }
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
              "imageUrl": "",
              "calculatedAmount": {
                "0": 12,
                "1": 6,
                "2": 6
              }
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
              "imageUrl": "",
              "calculatedAmount": {
                "0": 20,
                "1": 10,
                "2": 10
              }
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
              "imageUrl": "",
              "calculatedAmount": {
                "0": 10,
                "1": 5,
                "2": 5
              }
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
              "imageUrl": "",
              "calculatedAmount": {
                "0": 15,
                "1": 7.5,
                "2": 7.5
              }
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
              "imageUrl": "",
              "calculatedAmount": {
                "0": 25,
                "1": 12.5,
                "2": 12.5
              }
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
              "imageUrl": "",
              "calculatedAmount": {
                "0": 20,
                "1": 10,
                "2": 10
              }
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
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              }
            }
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
