# Price Reservation

**Path:** Create Reservation > Group Reservation > Norwegian Cruiseline > Price Reservation

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
            "packageId": 1313262
        },
        "categories": [
            {
                "code": "IB",
                "fare": {
                    "fareCode": {
                        "code": "A1612559",
                        "groups": [
                            {
                                "code": "A1612559"
                            }
                        ]
                    }
                }
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
Date: Wed, 15 Mar 2023 12:40:23 GMT
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
      "requestId": "02ba2eae-b719-4b5b-b28d-9596f7cdc1a6",
      "timeStamp": "15-Mar-2023 08:40:20",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "16-Dec-2023 00:00:00",
        "arrivalDateTime": "23-Dec-2023 00:00:00",
        "departureCityId": "XPC",
        "arrivalCityId": "XPC",
        "duration": 7
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
            "amount": 500,
            "dueDate": "20-Mar-2023"
          },
          {
            "type": 1,
            "amount": 2452.6000000000004,
            "dueDate": "28-Jul-2023"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 0,
            "amount": 500,
            "dueDate": "20-Mar-2023"
          },
          {
            "type": 1,
            "amount": 2452.6000000000004,
            "dueDate": "28-Jul-2023"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 0,
            "amount": 500,
            "dueDate": "22-Mar-2023"
          },
          {
            "type": 1,
            "amount": 2045.3400000000001,
            "dueDate": "18-Aug-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 3916,
          "rph": -1
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 390,
          "rph": -1
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -1370.6,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 2545.4,
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
          "amount": 2545.4,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 2155.4,
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
          "amount": 407.2,
          "details": {
            "isTax": true,
            "isCommission": false
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
          "amount": 2952.6000000000004,
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
          "amount": 0,
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
          "amount": 2952.6000000000004,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 2952.6000000000004,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 2952.6000000000004,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 500,
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
          "amount": 2952.6,
          "rph": -1
        },
        {
          "id": 98,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
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
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 407.26,
          "details": {
            "isTax": false,
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
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 2545.34,
          "rph": -1
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 2952.6000000000004,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 407.2600000000002,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 1958,
          "rph": 1
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 195,
          "rph": 1
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -685.3,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1272.7,
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
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
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
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 1272.7,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1077.7,
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
          "amount": 203.6,
          "details": {
            "isTax": true,
            "isCommission": false
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
          "amount": 1476.3000000000002,
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
          "amount": 0,
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
          "amount": 1476.3000000000002,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 1476.3000000000002,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 1476.3000000000002,
          "rph": 1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 250,
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
          "amount": 1476.3,
          "rph": 1
        },
        {
          "id": 28,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
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
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 203.63,
          "details": {
            "isTax": false,
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
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1272.67,
          "rph": 1
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1476.3000000000002,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 203.6300000000001,
          "rph": 1
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 1958,
          "rph": 2
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 195,
          "rph": 2
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -685.3,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1272.7,
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
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
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
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 1272.7,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1077.7,
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
          "amount": 203.6,
          "details": {
            "isTax": true,
            "isCommission": false
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
          "amount": 1476.3000000000002,
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
          "amount": 0,
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
          "amount": 1476.3000000000002,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 1476.3000000000002,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 1476.3000000000002,
          "rph": 2
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 250,
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
          "amount": 1476.3,
          "rph": 2
        },
        {
          "id": 28,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
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
            "isTax": false,
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 203.63,
          "details": {
            "isTax": false,
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
            "isTax": false,
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1272.67,
          "rph": 2
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1476.3000000000002,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 203.6300000000001,
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1313262,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13669
            }
          ]
        },
        "itinerary": {
          "id": 363167,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "16-Dec-2023 00:00:00",
          "arrivalDateTime": "23-Dec-2023 00:00:00",
          "departureCityId": "XPC",
          "arrivalCityId": "XPC",
          "code": "18439927"
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
