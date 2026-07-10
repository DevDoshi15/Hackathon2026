# Price Reservation

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with Paid Transfer Package > Price Reservation

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
            "packageId": 1298928
        },
        "Packages": [ // packages to be included for the reservation
            {
                "Type": "PrePackage",
                "Code": "B11YVRPAN"
            },
            {
                "Type": "PostPackage",
                "Code": "A22YVRPAN"
            }
        ],
        "categories": [
            {
                "code": "MM",
                "fare": {
                    "fareCode": {
                        "code": "NH1"
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
                },
                "state": {
                    "id": "FL"
                },
                "city": {
                    "id": "MIA"
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
                },
                "state": {
                    "id": "FL"
                },
                "city": {
                    "id": "MIA"
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
Date: Thu, 09 Mar 2023 12:30:32 GMT
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
            "requestId": "a257165f-583c-406f-8f37-9a6c66aa0ff2",
            "timeStamp": "09-Mar-2023 07:30:30",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "07-Jun-2023 00:00:00",
                "arrivalDateTime": "14-Jun-2023 00:00:00",
                "departureCityId": "YVR",
                "arrivalCityId": "YVR",
                "duration": 7
            },
            "pos": {
                "id": 2111,
                "apiId": "Carnival",
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
                        "amount": 3370.42,
                        "dueDate": "09-Mar-2023"
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 3370.42,
                        "dueDate": "09-Mar-2023"
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 3196.2400000000002,
                        "dueDate": "09-Mar-2023"
                    }
                ]
            },
            "prices": [
                {
                    "id": 1,
                    "code": "AMCT",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 1098,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 470,
                    "rph": -1
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 1098,
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
                    "amount": 1098,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 628,
                    "rph": -1
                },
                {
                    "id": 41,
                    "code": "PKGS",
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "amount": 1474,
                    "rph": -1 // -1 Indicates total price of the packages on reservation
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
                    "code": "TXFS",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 798.42,
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
                    "amount": 3370.42,
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
                    "amount": 3370.42,
                    "rph": -1
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 3370.42,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 3370.42,
                    "rph": -1
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "priority": 360,
                    "displayType": 4,
                    "amount": 3196,
                    "rph": -1
                },
                {
                    "id": 26,
                    "code": "PMTS",
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
                    "amount": 3370.42,
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
                    "code": "COMM",
                    "priority": 509,
                    "displayType": 4,
                    "amount": 174.18,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "rph": -1
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 3196.24,
                    "rph": -1
                },
                {
                    "id": 65,
                    "code": "",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 3196.2400000000002,
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
                    "amount": 3370.42,
                    "rph": -1
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 174.17999999999984,
                    "rph": -1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 549,
                    "rph": 1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 235,
                    "rph": 1
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 549,
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
                    "amount": 549,
                    "rph": 1
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 314,
                    "rph": 1
                },
                {
                    "id": 41,
                    "code": "PKGS",
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "amount": 737,
                    "rph": 1 // Indicates prices are for PAX 1
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
                    "code": "TXFS",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 399.21,
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
                    "amount": 1685.21,
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
                    "id": 84,
                    "code": "",
                    "priority": 200,
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
                    "amount": 1685.21,
                    "rph": 1
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 1685.21,
                    "rph": 1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 1685.21,
                    "rph": 1
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "priority": 360,
                    "displayType": 4,
                    "amount": 1598,
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
                    "id": 62,
                    "code": "",
                    "priority": 382,
                    "displayType": 4,
                    "amount": 1685.21,
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
                    "id": 32,
                    "code": "COMM",
                    "priority": 509,
                    "displayType": 4,
                    "amount": 87.09,
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
                    "amount": 1598.1200000000001,
                    "rph": 1
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 1598.12,
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
                    "amount": 1685.21,
                    "rph": 1
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 87.08999999999992,
                    "rph": 1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 549,
                    "rph": 2
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 235,
                    "rph": 2
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 549,
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
                    "amount": 549,
                    "rph": 2
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 314,
                    "rph": 2
                },
                {
                    "id": 41,
                    "code": "PKGS",
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "amount": 737,
                    "rph": 2 // Indicates prices are for PAX 2
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
                    "code": "TXFS",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 399.21,
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
                    "amount": 1685.21,
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
                    "id": 84,
                    "code": "",
                    "priority": 200,
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
                    "amount": 1685.21,
                    "rph": 2
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 1685.21,
                    "rph": 2
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 1685.21,
                    "rph": 2
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "priority": 360,
                    "displayType": 4,
                    "amount": 1598,
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
                    "id": 62,
                    "code": "",
                    "priority": 382,
                    "displayType": 4,
                    "amount": 1685.21,
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
                    "id": 32,
                    "code": "COMM",
                    "priority": 509,
                    "displayType": 4,
                    "amount": 87.09,
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
                    "amount": 1598.1200000000001,
                    "rph": 2
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 1598.12,
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
                    "amount": 1685.21,
                    "rph": 2
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 87.08999999999992,
                    "rph": 2
                }
            ],
            "cruise": {
                "packageId": 1298928,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 5,
                    "ships": [
                        {
                            "id": 43
                        }
                    ]
                },
                "itinerary": {
                    "id": 269387,
                    "destination": {
                        "id": 1
                    }
                },
                "voyage": {
                    "departureDateTime": "07-Jun-2023 00:00:00",
                    "arrivalDateTime": "14-Jun-2023 00:00:00",
                    "departureCityId": "YVR",
                    "arrivalCityId": "YVR",
                    "code": "V329"
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
                    "city": {
                        "id": "MIA"
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
                "firstName": "Maria",
                "lastName": "Doe",
                "dateOfBirth": "01-Jan-1965",
                "age": 57,
                "address": {
                    "city": {
                        "id": "MIA"
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
