# Price Reservation

**Path:** Create Reservation > Create Reservation With AddOns > Price Reservation

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
            "packageId": 1324816
        },
        "categories": [
            {
                "code": "IR1",
                "fare": {
                    "fareCode": {
                        "code": "EZAT35DZE"
                    }
                }
            }
        ],
        "addOns": [
            {
                "code": "MM20PHOT",
                "startDate": "01-Apr-2023"
            },
            {
                "code": "EXP2B",
                "autoInclude": true,
                "additionalCode": "636713325"
            },
            {
                "code": "600",
                "autoInclude": true,
                "additionalCode": "636713572"
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
Date: Thu, 16 Mar 2023 12:44:55 GMT
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
      "requestId": "377f1580-df55-4d25-bbc7-923516db2d80",
      "timeStamp": "16-Mar-2023 08:44:53",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Apr-2023 00:00:00",
        "arrivalDateTime": "08-Apr-2023 00:00:00",
        "departureCityId": "MRS",
        "arrivalCityId": "MRS",
        "duration": 7
      },
      "pos": {
        "id": 2119,
        "apiId": "MSC",
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
            "type": 2,
            "amount": 1852.2,
            "dueDate": "16-Mar-2023"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 1852.2,
            "dueDate": "16-Mar-2023"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 1619.24,
            "dueDate": "16-Mar-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "RAT",
          "priority": 5,
          "displayType": 4,
          "amount": 1436,
          "rph": -1
        },
        {
          "id": 2,
          "code": "",
          "priority": 6,
          "displayType": 4,
          "amount": 318,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1436,
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
          "amount": 1436,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1118,
          "rph": -1
        },
        {
          "id": 54,
          "code": "FUS",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 41,
          "code": "PKG",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 3,
          "code": "TAX",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 130.2,
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
          "amount": 1852.2,
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
          "amount": 1852.2,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 1852.2,
          "rph": -1
        },
        {
          "id": 50,
          "code": "IGT",
          "priority": 359,
          "displayType": 4,
          "amount": 1852.2,
          "rph": -1
        },
        {
          "id": 24,
          "code": "IDA",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 26,
          "code": "IAR",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 63,
          "code": "BAL",
          "priority": 382,
          "displayType": 4,
          "amount": 1852.2,
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
          "code": "CCC",
          "priority": 509,
          "displayType": 4,
          "amount": 232.96,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 66,
          "code": "INT",
          "priority": 510,
          "displayType": 4,
          "amount": 1619.24,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1619.24,
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
          "id": 159,
          "code": "EXP2B",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 159,
          "code": "600",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 159,
          "code": "MM20PHOT",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 286,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1852.2,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 232.96000000000004,
          "rph": -1
        },
        {
          "id": 1,
          "code": "RAT",
          "priority": 5,
          "displayType": 4,
          "amount": 718,
          "rph": 1
        },
        {
          "id": 2,
          "code": "",
          "priority": 6,
          "displayType": 4,
          "amount": 159,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 718,
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
          "amount": 718,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 559,
          "rph": 1
        },
        {
          "id": 54,
          "code": "FUS",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 3,
          "code": "TAX",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 65.1,
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
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 926.1,
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
          "amount": 926.1,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 926.1,
          "rph": 1
        },
        {
          "id": 50,
          "code": "IGT",
          "priority": 359,
          "displayType": 4,
          "amount": 783.1,
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
          "code": "IAR",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 63,
          "code": "BAL",
          "priority": 382,
          "displayType": 4,
          "amount": 783.1,
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
          "code": "CCC",
          "priority": 509,
          "displayType": 4,
          "amount": 95.03,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 66,
          "code": "INT",
          "priority": 510,
          "displayType": 4,
          "amount": 569.91,
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 688.07,
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
          "amount": 926.1,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 238.02999999999997,
          "rph": 1
        },
        {
          "id": 159,
          "code": "MM20PHOT",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 143,
          "rph": 1
        },
        {
          "id": 159,
          "code": "600",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 159,
          "code": "EXP2B",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 1,
          "code": "RAT",
          "priority": 5,
          "displayType": 4,
          "amount": 718,
          "rph": 2
        },
        {
          "id": 2,
          "code": "",
          "priority": 6,
          "displayType": 4,
          "amount": 159,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 718,
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
          "amount": 718,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 559,
          "rph": 2
        },
        {
          "id": 54,
          "code": "FUS",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 3,
          "code": "TAX",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 65.1,
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
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 926.1,
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
          "amount": 926.1,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 926.1,
          "rph": 2
        },
        {
          "id": 50,
          "code": "IGT",
          "priority": 359,
          "displayType": 4,
          "amount": 783.1,
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
          "code": "IAR",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 63,
          "code": "BAL",
          "priority": 382,
          "displayType": 4,
          "amount": 783.1,
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
          "code": "CCC",
          "priority": 509,
          "displayType": 4,
          "amount": 95.03,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 66,
          "code": "INT",
          "priority": 510,
          "displayType": 4,
          "amount": 569.91,
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 688.07,
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
          "amount": 926.1,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 238.02999999999997,
          "rph": 2
        },
        {
          "id": 159,
          "code": "MM20PHOT",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 143,
          "rph": 2
        },
        {
          "id": 159,
          "code": "600",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 159,
          "code": "EXP2B",
          "priority": 600,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1324816,
        "packageTourId": -1,
        "cruiseline": {
          "id": 982,
          "ships": [
            {
              "id": 14091
            }
          ]
        },
        "itinerary": {
          "id": 362627,
          "destination": {
            "id": 18
          }
        },
        "voyage": {
          "departureDateTime": "01-Apr-2023 00:00:00",
          "arrivalDateTime": "08-Apr-2023 00:00:00",
          "departureCityId": "MRS",
          "arrivalCityId": "MRS",
          "code": "GR20230401MRSMRS"
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
