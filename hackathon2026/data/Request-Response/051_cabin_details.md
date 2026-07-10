# Cabin Details

**Path:** Cabin Details > Cabin Position & Remarks > Cabin Details

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/getcabindetails`

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
            "packageId": 1282255,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "08",
                "fare": {
                    "fareCode": {
                        "code": "H8212136"
                    }
                },
                "cabins": [
                    {
                        "number": "3119"
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52
        },
        {
            "rph": 2,
            "age": 57
        }
    ],
    "trackingInfo": {}
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Thu, 16 Mar 2023 15:00:42 GMT
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
            "requestId": "9a998f0c-135d-4111-bfcf-ec76cc28938d",
            "timeStamp": "16-Mar-2023 11:00:41"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "09-Apr-2023 00:00:00",
                "arrivalDateTime": "16-Apr-2023 00:00:00",
                "departureCityId": "FLL",
                "arrivalCityId": "FLL",
                "duration": 7
            },
            "pos": {
                "id": 2109,
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
                "packageId": 1282255,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 2,
                    "ships": [
                        {
                            "id": 14948
                        }
                    ]
                },
                "itinerary": {
                    "id": 364303,
                    "destination": {
                        "id": 14
                    }
                },
                "tourCode": "BY07W480",
                "voyage": {
                    "departureDateTime": "09-Apr-2023 00:00:00",
                    "arrivalDateTime": "16-Apr-2023 00:00:00",
                    "departureCityId": "FLL",
                    "arrivalCityId": "FLL",
                    "code": "BY07W480"
                },
                "transportationType": 29
            },
            "cabins": [
                {
                    "number": "3119",
                    "position": "Forward", // Position of Cabin
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    },
                    "remarks": "The color scheme for the cabin is: NUTRL. The cabin contains following furniture items: CONVERTIBLE KING BED, SITTING AREA WITH SOFA, FLAT SCREEN INTERACTIVE TV, LIGHTING CONTROL PANEL, WALK IN SHOWER, MINI BAR, VANITY & CLOSET WITH DRAWERS, HAIR DRYER, SAFE, TELEPHONE" // Description of Cabin
                }
            ]
        },
        "customers": [
            {
                "rph": 1,
                "age": 52
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
