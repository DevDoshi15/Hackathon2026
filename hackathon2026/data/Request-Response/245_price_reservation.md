# Price Reservation

**Path:** Create Reservation > RCCL switching to CruiseOnly when Cruise + Air is not available > Price Reservation

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
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "Post",
            "GateWayCity": {
                "id": "PTY" // flight departure city
            }
        },
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
            "packageId": 1317656,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "RL",
                "type": 4,
                "fare": {
                    "farecode": {
                        "code": "G0738129"
                    }
                },
                "cabins": [
                    {
                        "number": "8320"
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "title": "MR",
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        },
        {
            "rph": 2,
            "title": "MR",
            "firstName": "Jack",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Mon, 08 May 2023 16:00:01 GMT
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
  "advisories": [
    {
      "code": "CSW0706",
      "message": "W-DEPOSIT IS NON REFUNDABLE 100 USD CHANGE FEE PER GUEST.",
      "description": "RCCL-",
      "type": "Warning"
    }
  ],
  "data": {
    "trackingInfo": {
      "requestId": "7279f4af-bd29-4a6f-9628-6ffde0e3327c",
      "timeStamp": "08-May-2023 11:59:59",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "23-Jun-2023 00:00:00",
        "arrivalDateTime": "30-Jun-2023 00:00:00",
        "departureCityId": "SEA",
        "arrivalCityId": "SEA",
        "duration": 7
      },
      "pos": {
        "id": 2227,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "Any"
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
            "amount": 21859.5,
            "dueDate": "11-May-2023 16:59:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 21859.5,
            "dueDate": "11-May-2023 16:59:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 18511.98,
            "dueDate": "13-May-2023 16:59:00"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "49",
          "amount": 30560,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "60",
          "amount": 470,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 73,
          "code": "NCD",
          "amount": 0,
          "priority": 7,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "amount": -9168,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 7,
          "code": "1",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 74,
          "code": "SER",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 21392,
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
          "amount": 21392,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 20922,
          "priority": 16,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 41,
          "code": "13",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 58,
          "code": "108",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
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
          "id": 9,
          "code": "46",
          "amount": 0,
          "priority": 23,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 10,
          "code": "44",
          "amount": 0,
          "priority": 24,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 12,
          "code": "33",
          "amount": 0,
          "priority": 25,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 3,
          "code": "18",
          "amount": 467.5,
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
          "id": 75,
          "code": "DSC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 76,
          "code": "SOC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 70,
          "code": "70",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 6,
          "code": "52",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 17,
          "code": "",
          "amount": 21859.5,
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
          "id": 14,
          "code": "107",
          "amount": 0,
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
          "amount": 21859.5,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 42,
          "code": "59",
          "amount": 0,
          "priority": 351,
          "display": true,
          "displayType": 9,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 21859.5,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "amount": 21859.5,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "amount": 4278,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 26,
          "code": "IAR",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 63,
          "code": "3",
          "amount": 21859.5,
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
          "code": "80",
          "amount": 3347.52,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 66,
          "code": "42",
          "amount": 18511.98,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "amount": 18511.98,
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
          "amount": 21859.5,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "amount": 3347.5200000000004,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "49",
          "amount": 15280,
          "priority": 5,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 2,
          "code": "60",
          "amount": 235,
          "priority": 6,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 73,
          "code": "NCD",
          "amount": 0,
          "priority": 7,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "amount": 0,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 7,
          "code": "1",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 74,
          "code": "SER",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "amount": 15280,
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
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 46,
          "code": "",
          "amount": 15280,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "amount": 15045,
          "priority": 16,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 58,
          "code": "108",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
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
          "id": 41,
          "code": "13",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 9,
          "code": "46",
          "amount": 0,
          "priority": 23,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 10,
          "code": "44",
          "amount": 0,
          "priority": 24,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 12,
          "code": "33",
          "amount": 0,
          "priority": 25,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 3,
          "code": "18",
          "amount": 233.75,
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
          "id": 76,
          "code": "SOC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 75,
          "code": "DSC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 70,
          "code": "70",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 6,
          "code": "52",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 17,
          "code": "",
          "amount": 15513.75,
          "priority": 100,
          "display": true,
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
          "id": 14,
          "code": "107",
          "amount": 0,
          "priority": 105,
          "display": true,
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
          "id": 60,
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
          "amount": 15513.75,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "amount": 15513.75,
          "priority": 355,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "amount": 15513.75,
          "priority": 359,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 24,
          "code": "6",
          "amount": 3036.11,
          "priority": 360,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 63,
          "code": "3",
          "amount": 10929.75,
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
          "code": "80",
          "amount": 2407.2,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "amount": 13106.55,
          "priority": 510,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 66,
          "code": "42",
          "amount": 13106.55,
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
          "amount": 15513.75,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "amount": 2407.2000000000007,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 1,
          "code": "49",
          "amount": 15280,
          "priority": 5,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 2,
          "code": "60",
          "amount": 235,
          "priority": 6,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 73,
          "code": "NCD",
          "amount": 0,
          "priority": 7,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "amount": -9168,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 7,
          "code": "1",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 74,
          "code": "SER",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "amount": 6112,
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
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 46,
          "code": "",
          "amount": 6112,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "amount": 5877,
          "priority": 16,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 58,
          "code": "108",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
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
          "id": 41,
          "code": "13",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 9,
          "code": "46",
          "amount": 0,
          "priority": 23,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 10,
          "code": "44",
          "amount": 0,
          "priority": 24,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 12,
          "code": "33",
          "amount": 0,
          "priority": 25,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 3,
          "code": "18",
          "amount": 233.75,
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
          "id": 76,
          "code": "SOC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 75,
          "code": "DSC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 70,
          "code": "70",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 6,
          "code": "52",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 17,
          "code": "",
          "amount": 6345.75,
          "priority": 100,
          "display": true,
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
          "id": 14,
          "code": "107",
          "amount": 0,
          "priority": 105,
          "display": true,
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
          "id": 60,
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
          "amount": 6345.75,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "amount": 6345.75,
          "priority": 355,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "amount": 6345.75,
          "priority": 359,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 24,
          "code": "6",
          "amount": 1241.89,
          "priority": 360,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 63,
          "code": "3",
          "amount": 10929.75,
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
          "code": "80",
          "amount": 940.32,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "amount": 5405.43,
          "priority": 510,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 66,
          "code": "42",
          "amount": 5405.43,
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
          "amount": 6345.75,
          "priority": 600,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "amount": 940.3199999999997,
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
        "packageId": 1317656,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 13717
            }
          ]
        },
        "itinerary": {
          "id": 364268,
          "destination": {
            "id": 1
          }
        },
        "tourCode": "OV07A221",
        "voyage": {
          "departureDateTime": "23-Jun-2023 00:00:00",
          "arrivalDateTime": "30-Jun-2023 00:00:00",
          "departureCityId": "SEA",
          "arrivalCityId": "SEA",
          "code": "OV07A221"
        },
        "transportationType": 29
      }
    },
    "customers": [
      {
        "title": "MR",
        "gender": "Male",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      },
      {
        "title": "MR",
        "gender": "Male",
        "rph": 2,
        "firstName": "Jack",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
