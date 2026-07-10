# Price Reservation

**Path:** Create Reservation > Create Reservation With Grats For RCCL > Price Reservation

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
            "packageId": 1269329,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "2N",
                "fare": {
                    "fareCode": {
                        "code": "G0737880" // We will pass the farecode along with category to fetch the list of cabins & addons
                    }
                }
            }
        ],       
        "services": [
            {
                "code": "PPGR",
                "name": "GRATUITIES"
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
Date: Mon, 20 Feb 2023 08:53:14 GMT
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
      "requestId": "4956f4b6-3574-43b6-823f-e079b201e44b",
      "timeStamp": "20-Feb-2023 03:53:12",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "15-Apr-2023 00:00:00",
        "arrivalDateTime": "20-Apr-2023 00:00:00",
        "departureCityId": "TPA",
        "arrivalCityId": "TPA",
        "duration": 5
      },
      "pos": {
        "id": 2114,
        "apiId": "RCCL",
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
            "amount": 1460.7,
            "dueDate": "25-Feb-2023"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 1460.7,
            "dueDate": "25-Feb-2023"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 1318.46,
            "dueDate": "27-Feb-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 1573,
          "rph": -1
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 189,
          "rph": -1
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": -81,
          "rph": -1
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -495,
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
          "amount": 1078,
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
          "amount": 1078,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 889,
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
          "amount": 222.7,
          "details": {
            "isTax": true
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
          "amount": 1460.7,
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
          "amount": 160,
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
          "amount": 1460.7,
          "rph": -1
        },
        {
          "id": 42,
          "code": "59",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 50,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 1460.7,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 1460.7,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 200,
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
          "amount": 1460.7,
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
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 142.24,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 1318.46,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1318.46,
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
          "amount": 1460.7,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 142.24,
          "rph": -1
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 827,
          "rph": 1
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 135,
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
          "id": 5,
          "code": "BOGO60NRD",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -57,
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
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 770,
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
          "amount": 770,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 635,
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
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
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
          "amount": 111.35,
          "details": {
            "isTax": true
          },
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
          "amount": 961.35,
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
          "amount": 80,
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
          "amount": 961.35,
          "rph": 1
        },
        {
          "id": 42,
          "code": "59",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 25,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 961.35,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 961.35,
          "rph": 1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 131.63,
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
          "amount": 730.35,
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
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 101.6,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 859.75,
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 859.75,
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
          "amount": 961.35,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 101.60000000000002,
          "rph": 1
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 746,
          "rph": 2
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 54,
          "rph": 2
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": -81,
          "rph": 2
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -438,
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
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 308,
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
          "amount": 308,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 254,
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
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
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
          "amount": 111.35,
          "details": {
            "isTax": true
          },
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
          "amount": 499.35,
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
          "amount": 80,
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
          "amount": 499.35,
          "rph": 2
        },
        {
          "id": 42,
          "code": "59",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 25,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 499.35,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 499.35,
          "rph": 2
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 68.37,
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
          "amount": 730.35,
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
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 40.64,
          "details": {
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 458.71,
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 458.71000000000004,
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
          "amount": 499.35,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 40.639999999999986,
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269329,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 72
            }
          ]
        },
        "itinerary": {
          "id": 311000,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "15-Apr-2023 00:00:00",
          "arrivalDateTime": "20-Apr-2023 00:00:00",
          "departureCityId": "TPA",
          "arrivalCityId": "TPA",
          "code": "BR05W366"
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
