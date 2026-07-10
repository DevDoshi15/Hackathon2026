# Transfer Availability

**Path:** Create Reservation > Create Reservation With Transfer (Pre/Post Airport Transfer) > Transfer Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listTransfers`

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
        "cruise": {
            "packageId": 1269292
        },
        "categories": [
            {
                "code": "4V",
                "fare": {
                    "fareCode": {
                        "code": "I0452040"
                    }
                }
            }
        ],
        "customerReferences": [
            {
                "RPH": "1",
                "isPrimaryContact": true
            },
            {
                "RPH": "2"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970"
        },
        {
            "rph": 2,
            "age": 57,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965"
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Mon, 06 Mar 2023 10:07:21 GMT
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
            "requestId": "676aee49-a383-4ce6-91d4-2d9f4d59e032",
            "timeStamp": "06-Mar-2023 05:07:20"
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
            },
            "packages": [ // list of transfers available for the package
                {
                    "code": "TIAHPU",
                    "description": "ARRIVAL - GEORGE BUSH INT'L AIRPORT PICK",
                    "prices": [
                        {
                            "id": 41,
                            "amount": 39.95,
                            "type": "AVGPP"
                        }
                    ],
                    "additionalCode": "7",
                    "packageType": "PreCruiseOptions"
                },
                {
                    "code": "THOUPU",
                    "description": "ARRIVAL-WILLIAM P. HOBBY AIRPORT PICK UP",
                    "prices": [
                        {
                            "id": 41,
                            "amount": 31.95,
                            "type": "AVGPP"
                        }
                    ],
                    "additionalCode": "7",
                    "packageType": "PreCruiseOptions"
                },
                {
                    "code": "TIAHDO",
                    "description": "DEPARTURE - GEORGE BUSH INT'L- DROP OFF",
                    "prices": [
                        {
                            "id": 41,
                            "amount": 39.95,
                            "type": "AVGPP"
                        }
                    ],
                    "additionalCode": "8",
                    "packageType": "PostCruiseOptions"
                },
                {
                    "code": "THOUDO",
                    "description": "DEPARTURE-HOBBY INTERNATIONAL - DROP OFF",
                    "prices": [
                        {
                            "id": 41,
                            "amount": 31.95,
                            "type": "AVGPP"
                        }
                    ],
                    "additionalCode": "8",
                    "packageType": "PostCruiseOptions"
                },
                {
                    "code": "THOUPD",
                    "description": "R/T - HOU A/P PICK UP / HOU A/P DROP OFF",
                    "prices": [
                        {
                            "id": 41,
                            "amount": 63.9,
                            "type": "AVGPP"
                        }
                    ],
                    "additionalCode": "9",
                    "packageType": "RoundTransfer"
                },
                {
                    "code": "TIAHPD",
                    "description": "R/T - IAH A/P PICK UP / IAH A/P DROP OFF",
                    "prices": [
                        {
                            "id": 41,
                            "amount": 79.9,
                            "type": "AVGPP"
                        }
                    ],
                    "additionalCode": "9",
                    "packageType": "RoundTransfer"
                }
            ]
        },
        "customers": [
            {
                "rph": 1,
                "firstName": "John",
                "lastName": "Doe",
                "dateOfBirth": "02-Jan-1970",
                "age": 52
            },
            {
                "rph": 2,
                "firstName": "Maria",
                "lastName": "Doe",
                "dateOfBirth": "01-Jan-1965",
                "age": 57
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
