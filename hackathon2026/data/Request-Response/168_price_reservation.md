# Price Reservation

**Path:** Create Reservation > Create Reservation With Packages > Auto-Inclusion of Packages > Create Reservation WITHOUT DoNotAutoIncludePackages Preference > Price Reservation

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
            "packageId": 1353443
        },
        "categories": [
            {
                "code": "C",
                "fare": {
                    "fareCode": {
                        "code": "QA1"
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
Date: Fri, 03 Nov 2023 11:07:53 GMT
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
            "requestId": "55e92c3d-6400-428e-bf42-e6d56c4785d6",
            "timeStamp": "03-Nov-2023 07:07:52",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "03-Feb-2024 00:00:00",
                "arrivalDateTime": "10-Feb-2024 00:00:00",
                "departureCityId": "FLL",
                "arrivalCityId": "FLL",
                "duration": 7
            },
            "pos": {
                "id": 2519,
                "officeId": "O100US6797",
                "currency": "USD",
                "type": "Any",
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
                        "type": 2,
                        "amount": 2544,
                        "dueDate": "03-Nov-2023 23:59:00"
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 2544,
                        "dueDate": "03-Nov-2023 23:59:00"
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "type": 2,
                        "amount": 2311.2,
                        "dueDate": "05-Nov-2023 23:59:00"
                    }
                ]
            },
            "prices": [
                {
                    "id": 128,
                    "code": "P1",
                    "amount": 10,
                    "display": true,
                    "displayType": 2,
                    "rph": -1
                },
                {
                    "id": 128,
                    "code": "P2",
                    "amount": 20,
                    "display": true,
                    "displayType": 2,
                    "rph": -1
                },
                {
                    "id": 126,
                    "amount": 350,
                    "display": true,
                    "rph": -1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 2033,
                    "priority": 5,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "amount": 380,
                    "priority": 6,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 2033,
                    "priority": 10,
                    "display": true,
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
                    "amount": 25,
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
                    "amount": -5,
                    "priority": 12,
                    "display": true,
                    "displayType": 2,
                    "rph": -1
                },
                {
                    "id": 46,
                    "code": "",
                    "amount": 2028,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 1648,
                    "priority": 16,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 41, // Here we are getting prices for packages as we have not set the DoNotAutoIncludePackages to true
                    "code": "PKGS",
                    "amount": 76,
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
                    "id": 3,
                    "code": "TXFS",
                    "amount": 390,
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
                    "amount": 2544,
                    "priority": 100,
                    "display": true,
                    "rph": -1
                },
                {
                    "id": 86,
                    "code": "",
                    "amount": 20,
                    "priority": 100,
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
                    "amount": 2544,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": -1
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 2544,
                    "priority": 355,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 2474,
                    "priority": 359,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 370,
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
                    "amount": 162.8,
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
                    "code": "NETD",
                    "amount": 2311.2,
                    "priority": 510,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 65,
                    "code": "",
                    "amount": 2311.2,
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
                    "amount": 2544,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 232.80000000000018,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 126,
                    "amount": 175,
                    "display": true,
                    "rph": 1
                },
                {
                    "id": 128,
                    "code": "P2",
                    "amount": 10,
                    "display": true,
                    "displayType": 2,
                    "rph": 1
                },
                {
                    "id": 128,
                    "code": "P1",
                    "amount": 5,
                    "display": true,
                    "displayType": 2,
                    "rph": 1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 1016.5,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "amount": 190,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 1016.5,
                    "priority": 10,
                    "display": true,
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
                    "amount": 12.5,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 44,
                    "code": "",
                    "amount": -2.5,
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
                    "id": 46,
                    "code": "",
                    "amount": 1014,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 1
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 824,
                    "priority": 16,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 41,
                    "code": "PKGS",
                    "amount": 38,
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
                    "id": 3,
                    "code": "TXFS",
                    "amount": 195,
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
                    "id": 86,
                    "code": "",
                    "amount": 10,
                    "priority": 100,
                    "display": true,
                    "displayType": 2,
                    "rph": 1
                },
                {
                    "id": 17,
                    "code": "",
                    "amount": 1272,
                    "priority": 100,
                    "display": true,
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
                    "id": 84,
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
                    "amount": 1272,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 1
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 1272,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 1237,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 185,
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
                    "id": 32,
                    "code": "COMM",
                    "amount": 81.4,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "priority": 509,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "amount": 1155.6,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 65,
                    "code": "",
                    "amount": 1155.6,
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
                    "amount": 116.40000000000009,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 1272,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1
                },
                {
                    "id": 126,
                    "amount": 175,
                    "display": true,
                    "rph": 2
                },
                {
                    "id": 128,
                    "code": "P2",
                    "amount": 10,
                    "display": true,
                    "displayType": 2,
                    "rph": 2
                },
                {
                    "id": 128,
                    "code": "P1",
                    "amount": 5,
                    "display": true,
                    "displayType": 2,
                    "rph": 2
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 1016.5,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "amount": 190,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 1016.5,
                    "priority": 10,
                    "display": true,
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
                    "amount": 12.5,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 44,
                    "code": "",
                    "amount": -2.5,
                    "priority": 12,
                    "display": true,
                    "displayType": 2,
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
                    "id": 46,
                    "code": "",
                    "amount": 1014,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 2
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 824,
                    "priority": 16,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 41,
                    "code": "PKGS",
                    "amount": 38,
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
                    "id": 3,
                    "code": "TXFS",
                    "amount": 195,
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
                    "amount": 10,
                    "priority": 100,
                    "display": true,
                    "displayType": 2,
                    "rph": 2
                },
                {
                    "id": 17,
                    "code": "",
                    "amount": 1272,
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
                    "amount": 1272,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 2
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 1272,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 1237,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 185,
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
                    "id": 32,
                    "code": "COMM",
                    "amount": 81.4,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "priority": 509,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "amount": 1155.6,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 65,
                    "code": "",
                    "amount": 1155.6,
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
                    "id": 83,
                    "code": "",
                    "amount": 116.40000000000009,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 1272,
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
                "packageId": 1353443,
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
                    "id": 370945,
                    "destination": {
                        "id": 9
                    }
                },
                "voyage": {
                    "departureDateTime": "03-Feb-2024 00:00:00",
                    "arrivalDateTime": "10-Feb-2024 00:00:00",
                    "departureCityId": "FLL",
                    "arrivalCityId": "FLL",
                    "code": "I416"
                },
                "transportationType": 29
            },
            "rulesInfo": {
                "applicableRules": [
                    {
                        "id": 1728537,
                        "name": "OBC CONSOLIDATOR RULE - DEMO PURPOSES ONLY ##PromotionAmount##",
                        "groupName": "nonexcl",
                        "type": 5,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "Customer information for Demo Purposes",
                            "agencyDetails": "Anything this rule promises you is not real.",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "https://sandbox.odysol.com/site/images/promotions/cdor_wine2.png"
                        }
                    },
                    {
                        "id": 1728342,
                        "name": "Cruise Discount (5$)",
                        "groupName": "excl_1728342",
                        "type": 1,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728343,
                        "name": "Cruise Markup (25$)",
                        "groupName": "excl_1728343",
                        "type": 2,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728420,
                        "name": "VAO Exclusive",
                        "groupName": "excl_1728420",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "va_earlysaver.png"
                        }
                    },
                    {
                        "id": 1728421,
                        "name": "VAO One Exclusive",
                        "groupName": "excl_1728421",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "pink-circle.png"
                        }
                    },
                    {
                        "id": 1728422,
                        "name": "VAO Non Exclusive",
                        "groupName": "nonexcl",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "CruiseCategory",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "va_anchor-vODY-635382737153437500.png"
                        }
                    },
                    {
                        "id": 1728423,
                        "name": "VAO Two Non Exclusive",
                        "groupName": "nonexcl",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "CruiseCategory",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "va_sale.png"
                        }
                    },
                    {
                        "id": 1728419,
                        "name": "Cruise Addon",
                        "groupName": "excl_1728419",
                        "type": 9,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728344,
                        "name": "Cruise Service Fee (20$)",
                        "groupName": "excl_1728344",
                        "type": 13,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728415,
                        "name": "Package Service Doc (10)",
                        "groupName": "P1",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728416,
                        "name": "Package Service Doc One (15)",
                        "groupName": "P1",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728417,
                        "name": "Package Service Travel (25) BEST Value YES",
                        "groupName": "P2",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728418,
                        "name": "Package Service Travel (20) BEST Value NO",
                        "groupName": "P2",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    }
                ]
            },
            "categories": [
                {
                    "id": 52916,
                    "code": "C",
                    "fares": [
                        {
                            "rules": [
                                {
                                    "id": 1728537,
                                    "calculatedAmount": {
                                        "0": 50,
                                        "1": 25,
                                        "2": 25
                                    }
                                },
                                {
                                    "id": 1728342,
                                    "calculatedAmount": {
                                        "0": 5,
                                        "1": 2.5,
                                        "2": 2.5
                                    }
                                },
                                {
                                    "id": 1728343,
                                    "calculatedAmount": {
                                        "0": 25,
                                        "1": 12.5,
                                        "2": 12.5
                                    }
                                },
                                {
                                    "id": 1728420
                                },
                                {
                                    "id": 1728421
                                },
                                {
                                    "id": 1728422
                                },
                                {
                                    "id": 1728423
                                },
                                {
                                    "id": 1728419,
                                    "calculatedAmount": {
                                        "0": 12,
                                        "1": 6,
                                        "2": 6
                                    }
                                },
                                {
                                    "id": 1728344,
                                    "calculatedAmount": {
                                        "0": 20,
                                        "1": 10,
                                        "2": 10
                                    }
                                },
                                {
                                    "id": 1728415,
                                    "calculatedAmount": {
                                        "0": 10,
                                        "1": 5,
                                        "2": 5
                                    }
                                },
                                {
                                    "id": 1728416,
                                    "calculatedAmount": {
                                        "0": 15,
                                        "1": 7.5,
                                        "2": 7.5
                                    }
                                },
                                {
                                    "id": 1728417,
                                    "calculatedAmount": {
                                        "0": 25,
                                        "1": 12.5,
                                        "2": 12.5
                                    }
                                },
                                {
                                    "id": 1728418,
                                    "calculatedAmount": {
                                        "0": 20,
                                        "1": 10,
                                        "2": 10
                                    }
                                }
                            ],
                            "fareCode": {
                                "code": "QA1",
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
                "age": 52,
                "address": {
                    "country": {
                        "id": "US"
                    }
                }
            },
            {
                "gender": "Male",
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
