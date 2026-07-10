# Farecode Availability

**Path:** Category Availability > B2B > Farecode Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listfarecodes`

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
            "id": 2231,
            "type": "B2C" // Here Type of Office should be passed
        },
        "cruise": {
            "packageId": 1340642
        }
    },
    "customers": [
        {
            "rph": 1,
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 30
        },
        {
            "rph": 3,
            "age": 32
        },
        {
            "rph": 4,
            "age": 33
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
Date: Mon, 27 Mar 2023 14:32:18 GMT
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
            "requestId": "67a10ce9-38eb-400f-a26e-12eceafafea9",
            "timeStamp": "27-Mar-2023 10:32:10",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "11-Apr-2024 00:00:00",
                "arrivalDateTime": "01-May-2024 00:00:00",
                "departureCityId": "CIV",
                "arrivalCityId": "VCE",
                "duration": 20
            },
            "pos": {
                "id": 2231,
                "apiId": "NVS",
                "officeId": "O100US6797",
                "system": "Test",
                "currency": "USD",
                "type": "B2B" //Only B2B offices are received
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
                },
                {
                    "rph": 3,
                    "ageGroup": "Adult"
                },
                {
                    "rph": 4,
                    "ageGroup": "Adult"
                }
            ],
            "insurances": [
                {
                    "code": "Y"
                }
            ],
            "cruise": {
                "packageId": 1340642,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 14,
                    "ships": [
                        {
                            "id": 15084
                        }
                    ]
                },
                "itinerary": {
                    "id": 357643,
                    "destination": {
                        "id": 51
                    }
                },
                "voyage": {
                    "departureDateTime": "11-Apr-2024 00:00:00",
                    "arrivalDateTime": "01-May-2024 00:00:00",
                    "departureCityId": "CIV",
                    "arrivalCityId": "VCE",
                    "code": "VIS240411A"
                },
                "transportationType": 29
            },
            "fareCodes": [
                {
                    "code": "FIT",
                    "name": "FIT RATE",
                    "description": "Standard FIT Pricing",
                    "type": 0,
                    "refundableType": 1,
                    "bookOnline": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "fareTypeDescription": "",
                        "remarks": "Standard FIT Pricing",
                        "qualifierCodes": ""
                    }
                },
                {
                    "code": "EBS",
                    "name": "EBS RATE",
                    "description": "Early Booking Savings",
                    "type": 0,
                    "refundableType": 1,
                    "dynamicRules": [
                        {
                            "type": 6
                        }
                    ],
                    "bookOnline": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "fareTypeDescription": "",
                        "remarks": "Early Booking Savings",
                        "qualifierCodes": ""
                    }
                },
                {
                    "code": "VISOLCC",
                    "name": "PROMO: Cruise Only Fare/OLife Credit",
                    "description": "NO AIR &amp; NO AMENITIES",
                    "type": 0,
                    "refundableType": 1,
                    "bookOnline": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "remarks": "NO AIR &amp; NO AMENITIES"
                    }
                }
            ]
        },
        "customers": [
            {
                "rph": 1,
                "age": 30,
                "address": {
                    "country": {
                        "id": "US"
                    }
                }
            },
            {
                "rph": 2,
                "age": 30
            },
            {
                "rph": 3,
                "age": 32
            },
            {
                "rph": 4,
                "age": 33
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
