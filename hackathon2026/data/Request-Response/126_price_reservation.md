# Price Reservation

**Path:** Create Reservation > Create Reservation With Grats/AddOns For NCL > Price Reservation

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
            "packageId": 1238898,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "OC",
                "fare": {
                    "fareCode": {
                        "code": "DISC50"
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
Date: Fri, 17 Feb 2023 15:32:51 GMT
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
      "requestId": "23293105-6682-4d5b-909b-03a8ffe1e860",
      "timeStamp": "17-Feb-2023 10:32:49",
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
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "type": 2,
            "amount": 1737.72,
            "dueDate": "17-Feb-2023"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 1737.72,
            "dueDate": "17-Feb-2023"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 1578.04,
            "dueDate": "17-Feb-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 2436,
          "rph": -1
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 110,
          "rph": -1
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -1218,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1218,
          "rph": -1
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 1218,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1108,
          "rph": -1
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 399.72,
          "details": {
            "isTax": true
          },
          "rph": -1
        },
        {
          "id": 6,
          "code": "",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 1737.72,
          "rph": -1
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 16,
          "code": "15",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 120,
          "rph": -1
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 1737.72,
          "rph": -1
        },
        {
          "id": 42,
          "code": "96",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 1737.72,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 1737.72,
          "rph": -1
        },
        {
          "id": 24,
          "code": "",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 26,
          "code": "2",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 62,
          "code": "",
          "priority": 382,
          "displayType": 4,
          "amount": 1737.72,
          "rph": -1
        },
        {
          "id": 98,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 28,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 159.68,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 36,
          "code": "85",
          "priority": 510,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1578.04,
          "rph": -1
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1737.72,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 159.68000000000006,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 1218,
          "rph": 1
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 55,
          "rph": 1
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -609,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 609,
          "rph": 1
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 609,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 554,
          "rph": 1
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 199.86,
          "details": {
            "isTax": true
          },
          "rph": 1
        },
        {
          "id": 6,
          "code": "",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 868.86,
          "rph": 1
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 16,
          "code": "15",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 60,
          "rph": 1
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 868.86,
          "rph": 1
        },
        {
          "id": 42,
          "code": "96",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 868.86,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 868.86,
          "rph": 1
        },
        {
          "id": 24,
          "code": "",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 26,
          "code": "2",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 62,
          "code": "",
          "priority": 382,
          "displayType": 4,
          "amount": 868.86,
          "rph": 1
        },
        {
          "id": 28,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 98,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 79.84,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 36,
          "code": "85",
          "priority": 510,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 789.02,
          "rph": 1
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 868.86,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 79.84000000000003,
          "rph": 1
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 1218,
          "rph": 2
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 55,
          "rph": 2
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -609,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 609,
          "rph": 2
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 609,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 554,
          "rph": 2
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 199.86,
          "details": {
            "isTax": true
          },
          "rph": 2
        },
        {
          "id": 6,
          "code": "",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 868.86,
          "rph": 2
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 16,
          "code": "15",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 60,
          "rph": 2
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 868.86,
          "rph": 2
        },
        {
          "id": 42,
          "code": "96",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 868.86,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 868.86,
          "rph": 2
        },
        {
          "id": 24,
          "code": "",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 26,
          "code": "2",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 62,
          "code": "",
          "priority": 382,
          "displayType": 4,
          "amount": 868.86,
          "rph": 2
        },
        {
          "id": 28,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 98,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 79.84,
          "details": {
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 36,
          "code": "85",
          "priority": 510,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 789.02,
          "rph": 2
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 868.86,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 79.84000000000003,
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
      }
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
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
