# Cabin Availability

**Path:** Cabin Availability > Guaranteed Cabin Indicator > Cabin Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listcabins`

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
            "packageId": 1275651,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "ZI",
                "fare": {
                    "fareCode": {
                        "code": "G0738129"
                    }
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 57
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
Date: Thu, 16 Mar 2023 14:28:18 GMT
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
            "requestId": "21a0aad2-03d3-44be-9411-6e5d6360e0a5",
            "timeStamp": "16-Mar-2023 10:28:17",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "19-Mar-2023 00:00:00",
                "arrivalDateTime": "24-Mar-2023 00:00:00",
                "departureCityId": "MIA",
                "arrivalCityId": "MIA",
                "duration": 5
            },
            "reservationIndicators": {
                "modifyIndicators": [
                    {
                        "type": 6,
                        "value": false
                    },
                    {
                        "type": 9,
                        "value": false
                    },
                    {
                        "type": 11,
                        "value": false
                    },
                    {
                        "type": 12,
                        "value": false
                    },
                    {
                        "type": 14,
                        "value": false
                    },
                    {
                        "type": 15,
                        "value": false
                    },
                    {
                        "type": 16,
                        "value": false
                    },
                    {
                        "type": 45,
                        "value": false
                    },
                    {
                        "type": 600,
                        "value": false
                    },
                    {
                        "type": 700,
                        "value": false
                    },
                    {
                        "type": 1001,
                        "value": false
                    }
                ],
                "mandatoryIndicators": [
                    {
                        "type": "CitizenShip",
                        "value": true
                    },
                    {
                        "type": "Insurance",
                        "value": true
                    },
                    {
                        "type": "Age",
                        "value": true
                    },
                    {
                        "type": "Title",
                        "value": true
                    },
                    {
                        "type": "Gender",
                        "value": true
                    },
                    {
                        "type": "PhoneNumber",
                        "value": true
                    },
                    {
                        "type": "DiningSeating",
                        "value": true
                    },
                    {
                        "type": "TableSize",
                        "value": true
                    },
                    {
                        "type": "FlightInformation",
                        "value": true
                    },
                    {
                        "type": 700,
                        "value": true
                    },
                    {
                        "type": "EMail",
                        "value": true
                    }
                ]
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
            "cruise": {
                "packageId": 1275651,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 8,
                    "ships": [
                        {
                            "id": 75
                        }
                    ]
                },
                "itinerary": {
                    "id": 364197,
                    "destination": {
                        "id": 14
                    }
                },
                "tourCode": "GR05W392",
                "voyage": {
                    "departureDateTime": "19-Mar-2023 00:00:00",
                    "arrivalDateTime": "24-Mar-2023 00:00:00",
                    "departureCityId": "MIA",
                    "arrivalCityId": "MIA",
                    "code": "GR05W392"
                },
                "transportationType": 29
            },
            "cabins": [
                {
                    "number": "GTY",
                    "isGuarantee": true, // Guaranteed Cabin Indicator
                    "beds": [
                        {
                            "code": "A",
                            "name": "",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "",
                            "description": "Together",
                            "type": 282
                        }
                    ]
                }
            ]
        },
        "customers": [
            {
                "rph": 1,
                "age": 52,
                "address": {
                    "country": {
                        "id": "US"
                    }
                }
            },
            {
                "rph": 2,
                "age": 57
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
