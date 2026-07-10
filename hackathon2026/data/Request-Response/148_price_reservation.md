# Price Reservation

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with No Transfer Package > Price Reservation

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
            "packageId": 1277420
        },
        "Packages": [ // element to indicate Transfers are not required, if not sent, some cruiselines like Holland America will include that by default
            {
                "Type": "PrePackage",
                "Code": "B0TNOXFR"
            },
            {
                "Type": "PostPackage",
                "Code": "A0TNOXFR"
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
Date: Mon, 06 Mar 2023 08:44:38 GMT
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
            "requestId": "1651af25-12c7-4725-823c-16f33e29f8cb",
            "timeStamp": "06-Mar-2023 03:44:37",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "02-Apr-2023 00:00:00",
                "arrivalDateTime": "09-Apr-2023 00:00:00",
                "departureCityId": "FLL",
                "arrivalCityId": "FLL",
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
                        "amount": 1568,
                        "dueDate": "06-Mar-2023"
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 1568,
                        "dueDate": "06-Mar-2023"
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 1437.12,
                        "dueDate": "07-Mar-2023"
                    }
                ]
            },
            "prices": [
                { // "id": 41 will not be part of the response as we have asked to exlucede that using Packages in the request
                    "id": 1,
                    "code": "AMCT",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 1198,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 380,
                    "rph": -1
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 1198,
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
                    "amount": 1198,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 818,
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
                    "code": "TXFS",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 370,
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
                    "amount": 1568,
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
                    "amount": 1568,
                    "rph": -1
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 1568,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 1568,
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
                    "amount": 1568,
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
                    "amount": 130.88,
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
                    "amount": 1437.12,
                    "rph": -1
                },
                {
                    "id": 65,
                    "code": "",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 1437.12,
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
                    "amount": 1568,
                    "rph": -1
                },
                {
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 130.8800000000001,
                    "rph": -1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 599,
                    "rph": 1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 190,
                    "rph": 1
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 599,
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
                    "amount": 599,
                    "rph": 1
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 409,
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
                    "code": "TXFS",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 185,
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
                    "amount": 784,
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
                    "amount": 784,
                    "rph": 1
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 784,
                    "rph": 1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 784,
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
                    "amount": 784,
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
                    "code": "COMM",
                    "priority": 509,
                    "displayType": 4,
                    "amount": 65.44,
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
                    "amount": 718.56,
                    "rph": 1
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 718.56,
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
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 65.44000000000005,
                    "rph": 1
                },
                {
                    "id": 112,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 784,
                    "rph": 1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "priority": 5,
                    "displayType": 4,
                    "amount": 599,
                    "rph": 2
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "priority": 6,
                    "displayType": 4,
                    "amount": 190,
                    "rph": 2
                },
                {
                    "id": 45,
                    "code": "",
                    "priority": 10,
                    "displayType": 4,
                    "amount": 599,
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
                    "amount": 599,
                    "rph": 2
                },
                {
                    "id": 114,
                    "code": "",
                    "priority": 16,
                    "displayType": 4,
                    "amount": 409,
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
                    "code": "TXFS",
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "amount": 185,
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
                    "amount": 784,
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
                    "amount": 784,
                    "rph": 2
                },
                {
                    "id": 47,
                    "code": "",
                    "priority": 355,
                    "displayType": 4,
                    "amount": 784,
                    "rph": 2
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "priority": 359,
                    "displayType": 4,
                    "amount": 784,
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
                    "amount": 784,
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
                    "code": "COMM",
                    "priority": 509,
                    "displayType": 4,
                    "amount": 65.44,
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
                    "amount": 718.56,
                    "rph": 2
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "priority": 510,
                    "displayType": 4,
                    "amount": 718.56,
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
                    "id": 83,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 65.44000000000005,
                    "rph": 2
                },
                {
                    "id": 112,
                    "code": "",
                    "priority": 600,
                    "displayType": 4,
                    "amount": 784,
                    "rph": 2
                }
            ],
            "cruise": {
                "packageId": 1277420,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 5,
                    "ships": [
                        {
                            "id": 13250
                        }
                    ]
                },
                "itinerary": {
                    "id": 311682,
                    "destination": {
                        "id": 14
                    }
                },
                "voyage": {
                    "departureDateTime": "02-Apr-2023 00:00:00",
                    "arrivalDateTime": "09-Apr-2023 00:00:00",
                    "departureCityId": "FLL",
                    "arrivalCityId": "FLL",
                    "code": "I330"
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
