# Price Reservation

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 4 – All Adults (RCCL) > Price Reservation

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
        "cruise": {
            "packageId": 1269434,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "ZI",
                "fare": {
                    "fareCode": {
                        "code": "I0507023"
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
            "dateOfBirth": "02-Jan-1992",
            "age": 31,
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
            "dateOfBirth": "02-Jan-1993",
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 3,
            "firstName": "Johny",
            "lastName": "Doe",
            "dateOfBirth": "12-Jan-1993",
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 4,
            "firstName": "Martina",
            "lastName": "Doe",
            "dateOfBirth": "12-Jan-1993",
            "age": 30,
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
Date: Mon, 27 Mar 2023 10:10:31 GMT
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
      "requestId": "a5e217d7-0a86-4f7f-a7ca-0c4fada10b55",
      "timeStamp": "27-Mar-2023 06:10:30",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 4
      },
      "pos": {
        "id": 2227,
        "apiId": "RCCL",
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
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "type": 2,
            "amount": 2019,
            "dueDate": "01-Apr-2023"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 2019,
            "dueDate": "01-Apr-2023"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 1838.84,
            "dueDate": "03-Apr-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 1566,
          "rph": -1
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 440,
          "rph": -1
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 7,
          "code": "1",
          "priority": 10,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1566,
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
          "amount": 1566,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1126,
          "rph": -1
        },
        {
          "id": 41,
          "code": "13",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
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
          "id": 9,
          "code": "46",
          "priority": 23,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 10,
          "code": "44",
          "priority": 24,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 12,
          "code": "33",
          "priority": 25,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 453,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": -1
        },
        {
          "id": 75,
          "code": "DSC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 76,
          "code": "SOC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 70,
          "code": "70",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 6,
          "code": "52",
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
          "amount": 2019,
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
          "id": 14,
          "code": "107",
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
          "amount": 2019,
          "rph": -1
        },
        {
          "id": 42,
          "code": "59",
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
          "amount": 2019,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 2019,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 400,
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
          "code": "3",
          "priority": 382,
          "displayType": 4,
          "amount": 2019,
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
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 180.16,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 1838.84,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1838.84,
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
          "amount": 2019,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 180.16000000000008,
          "rph": -1
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 499,
          "rph": 1
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 110,
          "rph": 1
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 7,
          "code": "1",
          "priority": 10,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 499,
          "rph": 1
        },
        {
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
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
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 499,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 389,
          "rph": 1
        },
        {
          "id": 41,
          "code": "13",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
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
          "id": 9,
          "code": "46",
          "priority": 23,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 10,
          "code": "44",
          "priority": 24,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 12,
          "code": "33",
          "priority": 25,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 113.25,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": 1
        },
        {
          "id": 75,
          "code": "DSC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 76,
          "code": "SOC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 70,
          "code": "70",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 6,
          "code": "52",
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
          "amount": 612.25,
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
          "id": 14,
          "code": "107",
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
          "amount": 612.25,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 612.25,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 612.25,
          "rph": 1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 121.3,
          "rph": 1
        },
        {
          "id": 26,
          "code": "",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 63,
          "code": "3",
          "priority": 382,
          "displayType": 4,
          "amount": 504.75,
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
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 62.24,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 550.01,
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 550.01,
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
          "amount": 612.25,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 62.24000000000001,
          "rph": 1
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 499,
          "rph": 2
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 110,
          "rph": 2
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 7,
          "code": "1",
          "priority": 10,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 499,
          "rph": 2
        },
        {
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
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
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 499,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 389,
          "rph": 2
        },
        {
          "id": 41,
          "code": "13",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
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
          "id": 9,
          "code": "46",
          "priority": 23,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 10,
          "code": "44",
          "priority": 24,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 12,
          "code": "33",
          "priority": 25,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 113.25,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": 2
        },
        {
          "id": 75,
          "code": "DSC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 76,
          "code": "SOC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 70,
          "code": "70",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 6,
          "code": "52",
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
          "amount": 612.25,
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
          "id": 14,
          "code": "107",
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
          "amount": 612.25,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 612.25,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 612.25,
          "rph": 2
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 121.3,
          "rph": 2
        },
        {
          "id": 26,
          "code": "",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 63,
          "code": "3",
          "priority": 382,
          "displayType": 4,
          "amount": 504.75,
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
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 62.24,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 550.01,
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 550.01,
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
          "amount": 612.25,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 62.24000000000001,
          "rph": 2
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 284,
          "rph": 3
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 110,
          "rph": 3
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 7,
          "code": "1",
          "priority": 10,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 284,
          "rph": 3
        },
        {
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 284,
          "rph": 3
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 174,
          "rph": 3
        },
        {
          "id": 41,
          "code": "13",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 9,
          "code": "46",
          "priority": 23,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 10,
          "code": "44",
          "priority": 24,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 12,
          "code": "33",
          "priority": 25,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 113.25,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": 3
        },
        {
          "id": 75,
          "code": "DSC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 76,
          "code": "SOC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 70,
          "code": "70",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 6,
          "code": "52",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 397.25,
          "rph": 3
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 14,
          "code": "107",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 397.25,
          "rph": 3
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 397.25,
          "rph": 3
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 397.25,
          "rph": 3
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 78.7,
          "rph": 3
        },
        {
          "id": 26,
          "code": "",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 63,
          "code": "3",
          "priority": 382,
          "displayType": 4,
          "amount": 504.75,
          "rph": 3
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
          "rph": 3
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
          "rph": 3
        },
        {
          "id": 32,
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 27.84,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 3
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 369.41,
          "rph": 3
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 369.41,
          "rph": 3
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
          "rph": 3
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 397.25,
          "rph": 3
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 27.839999999999975,
          "rph": 3
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 284,
          "rph": 4
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 110,
          "rph": 4
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 7,
          "code": "1",
          "priority": 10,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 284,
          "rph": 4
        },
        {
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 284,
          "rph": 4
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 174,
          "rph": 4
        },
        {
          "id": 41,
          "code": "13",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 9,
          "code": "46",
          "priority": 23,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 10,
          "code": "44",
          "priority": 24,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 12,
          "code": "33",
          "priority": 25,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 113.25,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": 4
        },
        {
          "id": 75,
          "code": "DSC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 76,
          "code": "SOC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 70,
          "code": "70",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 6,
          "code": "52",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 397.25,
          "rph": 4
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 14,
          "code": "107",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 397.25,
          "rph": 4
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 397.25,
          "rph": 4
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 397.25,
          "rph": 4
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 78.7,
          "rph": 4
        },
        {
          "id": 26,
          "code": "",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 63,
          "code": "3",
          "priority": 382,
          "displayType": 4,
          "amount": 504.75,
          "rph": 4
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
          "rph": 4
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
          "rph": 4
        },
        {
          "id": 32,
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 27.84,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 4
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 369.41,
          "rph": 4
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 369.41,
          "rph": 4
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
          "rph": 4
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 397.25,
          "rph": 4
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 27.839999999999975,
          "rph": 4
        }
      ],
      "cruise": {
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 364180,
          "destination": {
            "id": 7
          }
        },
        "tourCode": "FR4BH098",
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
        },
        "transportationType": 29
      }
    },
    "customers": [
      {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1992",
        "age": 31,
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
        "dateOfBirth": "02-Jan-1993",
        "age": 30,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 3,
        "firstName": "Johny",
        "lastName": "Doe",
        "dateOfBirth": "12-Jan-1993",
        "age": 30,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 4,
        "firstName": "Martina",
        "lastName": "Doe",
        "dateOfBirth": "12-Jan-1993",
        "age": 30,
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
