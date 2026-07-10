# Price Reservation

**Path:** Create Reservation > Create Reservation With Transfer (Pre/Post Airport Transfer) > Price Reservation

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
            "packageId": 1269292
        },
        "packages": [ // transfers for which prices are to be included in the response
            {
                "Type": "RoundTransfer",
                "Code": "THOUPD",
                "AdditionalCode": "7"
            }
        ],
        "categories": [
            {
                "code": "4V",
                "fare": {
                    "fareCode": {
                        "code": "I0452040"
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
Date: Thu, 16 Mar 2023 09:01:44 GMT
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
            "requestId": "e8c0c1a3-9240-4170-87e2-9ea92f95b117",
            "timeStamp": "16-Mar-2023 05:01:42",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "30-Mar-2023 00:00:00",
                "arrivalDateTime": "03-Apr-2023 00:00:00",
                "departureCityId": "GLS",
                "arrivalCityId": "GLS",
                "duration": 4
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
                        "amount": 934.5999999999999,
                        "dueDate": "21-Mar-2023"
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 934.5999999999999,
                        "dueDate": "21-Mar-2023"
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 857.1600000000001,
                        "dueDate": "23-Mar-2023"
                    }
                ]
            },
            "prices": [
                {
                    "id": 1,
                    "code": "49",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 932,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "60",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 154,
                    "rph": -1
                },
                {
                    "id": 73,
                    "code": "NCD",
                    "priority": 7,
                    "displayType": 4,
                    "amount": -66,
                    "rph": -1
                },
                {
                    "id": 5,
                    "code": "BOGO60NRD",
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "amount": -294,
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
                    "amount": 638,
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
                    "amount": 638,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 484,
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
                    "id": 12, // transfer price item
                    "code": "33",
                    "priority": 25,
                    "display": true,
                    "displayType": 2,
                    "amount": 127.8,
                    "rph": -1 // Price item with RPH -1 indicates total for transfers for all PAX
                },
                {
                    "id": 3,
                    "code": "18",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 168.8,
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
                    "amount": 934.5999999999999,
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
                    "amount": 934.5999999999999,
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
                    "amount": 934.5999999999999,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "8",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 934.6000000000001,
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
                    "amount": 934.6,
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
                    "amount": 77.44,
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
                    "amount": 857.16,
                    "rph": -1
                },
                {
                    "id": 65,
                    "code": "",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 857.1600000000001,
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
                    "amount": 934.5999999999999,
                    "rph": -1
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 77.43999999999983,
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
                    "id": 5,
                    "code": "BOGO60NRD",
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "amount": -43,
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
                    "amount": 456,
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
                    "amount": 456,
                    "rph": 1
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 346,
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
                    "amount": 63.9,
                    "rph": 1 // amount for PAX 1
                },
                {
                    "id": 3,
                    "code": "18",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 84.4,
                    "details": {
                        "isTax": true,
                        "isCommission": false
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
                    "amount": 604.3,
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
                    "amount": 604.3,
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
                    "amount": 604.3,
                    "rph": 1
                },
                {
                    "id": 50,
                    "code": "8",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 604.3,
                    "rph": 1
                },
                {
                    "id": 24,
                    "code": "6",
                    "priority": 360,
                    "displayType": 4,
                    "amount": 129.32,
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
                    "amount": 467.3,
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
                    "amount": 55.36,
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
                    "amount": 548.94,
                    "rph": 1
                },
                {
                    "id": 65,
                    "code": "",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 548.9399999999999,
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
                    "amount": 604.3,
                    "rph": 1
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 55.360000000000014,
                    "rph": 1
                },
                {
                    "id": 1,
                    "code": "49",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 433,
                    "rph": 2
                },
                {
                    "id": 2,
                    "code": "60",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 44,
                    "rph": 2
                },
                {
                    "id": 73,
                    "code": "NCD",
                    "priority": 7,
                    "displayType": 4,
                    "amount": -66,
                    "rph": 2
                },
                {
                    "id": 5,
                    "code": "BOGO60NRD",
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "amount": -251,
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
                    "amount": 182,
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
                    "amount": 182,
                    "rph": 2
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 138,
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
                    "amount": 63.9,
                    "rph": 2 // amount for PAX 2
                },
                {
                    "id": 3,
                    "code": "18",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 84.4,
                    "details": {
                        "isTax": true,
                        "isCommission": false
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
                    "amount": 330.29999999999995,
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
                    "amount": 330.29999999999995,
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
                    "amount": 330.29999999999995,
                    "rph": 2
                },
                {
                    "id": 50,
                    "code": "8",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 330.3,
                    "rph": 2
                },
                {
                    "id": 24,
                    "code": "6",
                    "priority": 360,
                    "displayType": 4,
                    "amount": 70.68,
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
                    "amount": 467.3,
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
                    "amount": 22.08,
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
                    "amount": 308.22,
                    "rph": 2
                },
                {
                    "id": 65,
                    "code": "",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 308.22,
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
                    "amount": 330.29999999999995,
                    "rph": 2
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 22.079999999999927,
                    "rph": 2
                }
            ],
            "cruise": {
                "packageId": 1269292,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 8,
                    "ships": [
                        {
                            "id": 71
                        }
                    ]
                },
                "itinerary": {
                    "id": 355501,
                    "destination": {
                        "id": 14
                    }
                },
                "tourCode": "AD04W115",
                "voyage": {
                    "departureDateTime": "30-Mar-2023 00:00:00",
                    "arrivalDateTime": "03-Apr-2023 00:00:00",
                    "departureCityId": "GLS",
                    "arrivalCityId": "GLS",
                    "code": "AD04W115"
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
