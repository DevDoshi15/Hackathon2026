# Cabin Availability

**Path:** Cabin Availability > Location > Cabin Availability

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
        "cruise": {
            "packageId": 1310045,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "XBO",
                "fare": {
                    "fareCode": {
                        "code": "BESTPRICE"
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
Date: Thu, 16 Mar 2023 14:35:27 GMT
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
            "requestId": "6fcc1282-d2bd-4a30-9908-0d24cc1e9537",
            "timeStamp": "16-Mar-2023 10:35:24",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "01-Apr-2023 00:00:00",
                "arrivalDateTime": "08-Apr-2023 00:00:00",
                "departureCityId": "PIRA",
                "arrivalCityId": "PIRA",
                "duration": 7
            },
            "pos": {
                "id": 2131,
                "apiId": "Seaware",
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
                "packageId": 1310045,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 8224,
                    "ships": [
                        {
                            "id": 14065
                        }
                    ]
                },
                "itinerary": {
                    "id": 364154,
                    "destination": {
                        "id": 16
                    }
                },
                "voyage": {
                    "departureDateTime": "01-Apr-2023 00:00:00",
                    "arrivalDateTime": "08-Apr-2023 00:00:00",
                    "departureCityId": "PIRA",
                    "arrivalCityId": "PIRA",
                    "code": "CC07230401-NP"
                },
                "transportationType": 29
            },
            "cabins": [
                {
                    "number": "6018",
                    "location": "Port", // Indicates the location of cabin
                    "occupancy": {
                        "min": 0,
                        "max": 3
                    }
                },
                {
                    "number": "6019",
                    "location": "Port",
                    "occupancy": {
                        "min": 0,
                        "max": 3
                    }
                },
                {
                    "number": "6020",
                    "location": "Port",
                    "occupancy": {
                        "min": 0,
                        "max": 3
                    }
                },
                {
                    "number": "6021",
                    "location": "Port",
                    "occupancy": {
                        "min": 0,
                        "max": 3
                    }
                },
                {
                    "number": "6022",
                    "location": "Port",
                    "occupancy": {
                        "min": 0,
                        "max": 3
                    }
                },
                {
                    "number": "6023",
                    "location": "Port",
                    "occupancy": {
                        "min": 0,
                        "max": 3
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
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
