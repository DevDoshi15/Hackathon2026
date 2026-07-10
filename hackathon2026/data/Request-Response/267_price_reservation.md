# Price Reservation

**Path:** Create Reservation > Create Reservation With Air For P&O Cruise line > Price Reservation

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
            "requestId": "dae451b7-a476-42f8-9446-74faa39a8037",
            "timeStamp": "23-Jun-2026 07:35:00",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "03-Jun-2027 00:00:00",
                "arrivalDateTime": "10-Jun-2027 00:00:00",
                "departureCityId": "VLT",
                "arrivalCityId": "VLT",
                "duration": 7
            },
            "reservationIndicators": {
                "mandatoryIndicators": [
                    {
                        "type": "PhoneNumber",
                        "value": true
                    }
                ]
            },
            "pos": {
                "id": 3487,
                "officeId": "O212GBTP17",
                "currency": "GBP",
                "type": "B2B",
                "system": "Test",
                "apiId": "Carnival"
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
                        "amount": 873,
                        "dueDate": "23-Jun-2026 04:59:00"
                    },
                    {
                        "type": 1,
                        "amount": 5048.36,
                        "dueDate": "14-Jan-2027 04:59:00"
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "type": 0,
                        "amount": 873,
                        "dueDate": "24-Jun-2026 04:59:00"
                    },
                    {
                        "type": 1,
                        "amount": 5048.36,
                        "dueDate": "14-Jan-2027 04:59:00"
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "type": 0,
                        "amount": 873,
                        "dueDate": "24-Jun-2026 04:59:00"
                    },
                    {
                        "type": 1,
                        "amount": 4324.84,
                        "dueDate": "04-Feb-2027 04:59:00"
                    }
                ]
            },
            "prices": [
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 5658,
                    "priority": 5,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "description": "Non-commissionable Fare",
                    "amount": 218,
                    "priority": 6,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 7, // Air Fare PriceItem
                    "code": "AADD",
                    "amount": 160,
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "rph": -1 
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 5658,
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
                    "amount": 5658,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 5440,
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
                    "code": "VAMT",
                    "amount": 103.36,
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
                    "amount": 5921.36,
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
                    "amount": 5921.36,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": -1
                },
                {
                    "id": 42,
                    "code": "OBCR",
                    "amount": 170,
                    "priority": 351,
                    "display": true,
                    "displayType": 9,
                    "rph": -1
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 5921.36,
                    "priority": 355,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 5818,
                    "priority": 359,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 873,
                    "priority": 360,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 26,
                    "code": "",
                    "amount": 0,
                    "priority": 380,
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
                    "code": "COMM",
                    "amount": 620.16,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "priority": 509,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 65,
                    "code": "NAMT",
                    "amount": 5197.84,
                    "priority": 510,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "amount": 5197.84,
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
                    "amount": 5921.36,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 723.5199999999995,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 33,
                    "code": "ADMN",
                    "amount": 108.8,
                    "priority": 610,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 2829,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "description": "Non-commissionable Fare",
                    "amount": 109,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 7,
                    "code": "AADD",
                    "amount": 80,
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "rph": 1
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 2829,
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
                    "id": 49,
                    "code": "",
                    "amount": 0,
                    "priority": 12,
                    "displayType": 4,
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
                    "id": 46,
                    "code": "",
                    "amount": 2829,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 1
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 2720,
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
                    "code": "VAMT",
                    "amount": 0,
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
                    "amount": 2909,
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
                    "amount": 2909,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 1
                },
                {
                    "id": 42,
                    "code": "OBCR",
                    "amount": 85,
                    "priority": 351,
                    "display": true,
                    "displayType": 9,
                    "rph": 1
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 2909,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 2909,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 436.5,
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
                    "code": "COMM",
                    "amount": 310.08,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "priority": 509,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 166,
                    "code": "AGFT",
                    "amount": 0,
                    "priority": 509,
                    "display": true,
                    "displayType": 9,
                    "rph": 1
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "amount": 2598.92,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 65,
                    "code": "NAMT",
                    "amount": 2598.92,
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
                    "id": 83,
                    "code": "",
                    "amount": 310.0799999999999,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 2909,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 33,
                    "code": "ADMN",
                    "amount": 54.4,
                    "priority": 610,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 2829,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "description": "Non-commissionable Fare",
                    "amount": 109,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 7,
                    "code": "AADD",
                    "amount": 80,
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "rph": 2
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 2829,
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
                    "id": 48,
                    "code": "",
                    "amount": 0,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 46,
                    "code": "",
                    "amount": 2829,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 2
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 2720,
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
                    "code": "VAMT",
                    "amount": 0,
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
                    "amount": 2909,
                    "priority": 100,
                    "display": true,
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
                    "amount": 2909,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 2
                },
                {
                    "id": 42,
                    "code": "OBCR",
                    "amount": 85,
                    "priority": 351,
                    "display": true,
                    "displayType": 9,
                    "rph": 2
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 2909,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 2909,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 436.5,
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
                    "id": 166,
                    "code": "AGFT",
                    "amount": 0,
                    "priority": 509,
                    "display": true,
                    "displayType": 9,
                    "rph": 2
                },
                {
                    "id": 32,
                    "code": "COMM",
                    "amount": 310.08,
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
                    "code": "NAMT",
                    "amount": 2598.92,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "amount": 2598.92,
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
                    "amount": 2909,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 310.0799999999999,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 33,
                    "code": "ADMN",
                    "amount": 54.4,
                    "priority": 610,
                    "displayType": 4,
                    "rph": 2
                }
            ],
            "currencyInfo": {
                "currencyId": "GBP",
                "countryId": "GB"
            },
            "externalSessionInfo": {
                "externalId": "a@#$A721"
            },
            "type": "Cruise",
            "cruise": {
                "packageId": 1501519,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 16,
                    "ships": [
                        {
                            "id": 13257,
                            "code": "AZ"
                        }
                    ]
                },
                "voyage": {
                    "departureDateTime": "03-Jun-2027 00:00:00",
                    "arrivalDateTime": "10-Jun-2027 00:00:00",
                    "departureCityId": "VLT",
                    "arrivalCityId": "VLT",
                    "code": "A721"
                },
                "itinerary": {
                    "id": 433252,
                    "destination": {
                        "id": 51
                    }
                },
                "transportationType": 29
            },
            "categories": [
                {
                    "id": 60438,
                    "code": "B2",
                    "fares": [
                        {
                            "fareCode": {
                                "code": "KD1",
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
                "firstName": "John",
                "lastName": "Doe",
                "dateOfBirth": "02-Jan-1970",
                "age": 53,
                "address": {
                    "country": {
                        "id": "GB"
                    }
                }
            },
            {
                "gender": "Male",
                "rph": 2,
                "firstName": "Maria",
                "lastName": "Doe",
                "dateOfBirth": "01-Jan-1965",
                "age": 58,
                "address": {
                    "country": {
                        "id": "GB"
                    }
                }
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
