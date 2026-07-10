# Price Reservation

**Path:** Create Reservation > Create Reservation With Air For NCL > Price Reservation

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
        "CruiselineAir": {
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "MIA"
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
            "packageId": 1330418,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "H6",
                "type": 4,
                "fare": {
                    "farecode": {
                        "code": "DISC50"
                    }
                },
                "cabins": [
                    {
                        "number": "18104"
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
Date: Wed, 08 Feb 2023 09:04:26 GMT
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
            "requestId": "9456e29b-6d43-4a85-be77-f4cc8955ef6b",
            "timeStamp": "08-Feb-2023 04:04:24",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "07-Apr-2024 00:00:00",
                "arrivalDateTime": "28-Apr-2024 00:00:00",
                "departureCityId": "MIA",
                "arrivalCityId": "SEA",
                "duration": 21
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
                        "amount": 29468.32,
                        "dueDate": "08-Feb-2023"
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 29468.32,
                        "dueDate": "08-Feb-2023"
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 25677.76,
                        "dueDate": "09-Feb-2023"
                    }
                ]
            },
            "prices": [
                {
                    "id": 1,
                    "code": "5",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 47382,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "POC",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 650,
                    "rph": -1
                },
                {
                    "id": 5,
                    "code": "34",
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "amount": -23691,
                    "rph": -1
                },
                {
                    "id": 7, // AirFare
                    "code": "1",
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "amount": 4389,
                    "rph": -1 // total airfare for all passengers
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 23691,
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
                    "amount": 23691,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 23041,
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
                    "id": 12,
                    "code": "19",
                    "priority": 25,
                    "display": true,
                    "displayType": 2,
                    "amount": 104,
                    "rph": -1
                },
                {
                    "id": 3,
                    "code": "18",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 1284.32,
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
                    "amount": 29468.32,
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
                    "amount": 29468.32,
                    "rph": -1
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 29468.32,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "8",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 29468.32,
                    "rph": -1
                },
                {
                    "id": 24,
                    "code": "6",
                    "priority": 360,
                    "displayType": 4,
                    "amount": 2369.1000000000004,
                    "rph": -1
                },
                {
                    "id": 126,
                    "priority": 360,
                    "displayType": 4,
                    "amount": 2369.1,
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
                    "amount": 29468.32,
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
                    "amount": 3790.56,
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
                    "amount": 25677.76,
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
                    "amount": 29468.32,
                    "rph": -1
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 3790.5600000000013,
                    "rph": -1
                },
                {
                    "id": 1,
                    "code": "5",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 23691,
                    "rph": 1
                },
                {
                    "id": 2,
                    "code": "POC",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 325,
                    "rph": 1
                },
                {
                    "id": 5,
                    "code": "34",
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "amount": -11845.5,
                    "rph": 1
                },
                {
                    "id": 7, // AirFare
                    "code": "1",
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "amount": 2889,
                    "rph": 1 // for PAX 1
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 11845.5,
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
                    "amount": 11845.5,
                    "rph": 1
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 11520.5,
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
                    "id": 12,
                    "code": "19",
                    "priority": 25,
                    "display": true,
                    "displayType": 2,
                    "amount": 52,
                    "rph": 1
                },
                {
                    "id": 3,
                    "code": "18",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 642.16,
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
                    "amount": 15428.66,
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
                    "amount": 15428.66,
                    "rph": 1
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 15428.66,
                    "rph": 1
                },
                {
                    "id": 50,
                    "code": "8",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 15428.66,
                    "rph": 1
                },
                {
                    "id": 24,
                    "code": "6",
                    "priority": 360,
                    "displayType": 4,
                    "amount": 1240.38,
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
                    "amount": 15428.66,
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
                    "amount": 1895.28,
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
                    "amount": 13533.38,
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
                    "amount": 15428.66,
                    "rph": 1
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 1895.2800000000007,
                    "rph": 1
                },
                {
                    "id": 1,
                    "code": "5",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 23691,
                    "rph": 2
                },
                {
                    "id": 2,
                    "code": "POC",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 325,
                    "rph": 2
                },
                {
                    "id": 5,
                    "code": "34",
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "amount": -11845.5,
                    "rph": 2
                },
                {
                    "id": 7, // AirFare
                    "code": "1",
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "amount": 1500,
                    "rph": 2 // for PAX 2
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 11845.5,
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
                    "amount": 11845.5,
                    "rph": 2
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 11520.5,
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
                    "id": 12,
                    "code": "19",
                    "priority": 25,
                    "display": true,
                    "displayType": 2,
                    "amount": 52,
                    "rph": 2
                },
                {
                    "id": 3,
                    "code": "18",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 642.16,
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
                    "amount": 14039.66,
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
                    "amount": 14039.66,
                    "rph": 2
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 14039.66,
                    "rph": 2
                },
                {
                    "id": 50,
                    "code": "8",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 14039.66,
                    "rph": 2
                },
                {
                    "id": 24,
                    "code": "6",
                    "priority": 360,
                    "displayType": 4,
                    "amount": 1128.72,
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
                    "amount": 14039.66,
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
                    "amount": 1895.28,
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
                    "amount": 12144.38,
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
                    "amount": 14039.66,
                    "rph": 2
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 1895.2800000000007,
                    "rph": 2
                }
            ],
            "cruise": {
                "packageId": 1330418,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 6,
                    "ships": [
                        {
                            "id": 14090
                        }
                    ]
                },
                "itinerary": {
                    "id": 363268,
                    "destination": {
                        "id": 49
                    }
                },
                "voyage": {
                    "departureDateTime": "07-Apr-2024 00:00:00",
                    "arrivalDateTime": "28-Apr-2024 00:00:00",
                    "departureCityId": "MIA",
                    "arrivalCityId": "SEA",
                    "code": "19257773"
                },
                "transportationType": 29
            }
        },
        "customers": [
            {
                "title": "MR",
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
