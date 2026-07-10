# Cabin Availability

**Path:** Cabin Availability > Obstructed Cabin Indicator > Cabin Availability

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
            "packageId": 1346847,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "2E",
                "fare": {
                    "fareCode": {
                        "code": "I9604829"
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
Date: Thu, 16 Mar 2023 14:20:01 GMT
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
            "requestId": "2e494cfe-2da3-4375-a57c-62ef06581b28",
            "timeStamp": "16-Mar-2023 10:19:58",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "11-May-2023 00:00:00",
                "arrivalDateTime": "15-May-2023 00:00:00",
                "departureCityId": "SIN",
                "arrivalCityId": "SIN",
                "duration": 4
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
                "packageId": 1346847,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 8,
                    "ships": [
                        {
                            "id": 14118
                        }
                    ]
                },
                "itinerary": {
                    "id": 364263,
                    "destination": {
                        "id": 51
                    }
                },
                "tourCode": "SC04I770",
                "voyage": {
                    "departureDateTime": "11-May-2023 00:00:00",
                    "arrivalDateTime": "15-May-2023 00:00:00",
                    "departureCityId": "SIN",
                    "arrivalCityId": "SIN",
                    "code": "SC04I770"
                },
                "transportationType": 29
            },
            "cabins": [
                {
                    "number": "6260",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true, // Obstructed Cabin Indicator
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "8514",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12133,
                        "name": "Deck 8",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6262",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 40
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6682",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "9514",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12134,
                        "name": "Deck 9",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6670",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6678",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6256",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6258",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "13290",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 30
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6592",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6690",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6206",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "8512",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12133,
                        "name": "Deck 8",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6612",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6684",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 40
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6194",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6198",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6224",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6190",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "8516",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12133,
                        "name": "Deck 8",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6622",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "9254",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12134,
                        "name": "Deck 9",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6290",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "8112",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12133,
                        "name": "Deck 8",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "8114",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12133,
                        "name": "Deck 8",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "7112",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12576,
                        "name": "Deck 7",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6656",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "7114",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12576,
                        "name": "Deck 7",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6658",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "7110",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12576,
                        "name": "Deck 7",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "7116",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12576,
                        "name": "Deck 7",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6660",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "8248",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 30
                    },
                    "deck": {
                        "id": 12133,
                        "name": "Deck 8",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6280",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "7510",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12576,
                        "name": "Deck 7",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6282",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "7512",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12576,
                        "name": "Deck 7",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6284",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6590",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6596",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "8116",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12133,
                        "name": "Deck 8",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "9114",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12134,
                        "name": "Deck 9",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "10516",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12575,
                        "name": "Deck 10",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "7514",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12576,
                        "name": "Deck 7",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "7516",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2C",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2C",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12576,
                        "name": "Deck 7",
                        "description": "Staterooms."
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
                    }
                },
                {
                    "number": "6604",
                    "beds": [
                        {
                            "code": "A",
                            "name": "2K",
                            "description": "Apart",
                            "type": 281
                        },
                        {
                            "code": "T",
                            "name": "2K",
                            "description": "Together",
                            "type": 282
                        }
                    ],
                    "obstruction": {
                        "isObstructed": true,
                        "percent": 50
                    },
                    "deck": {
                        "id": 12573,
                        "name": "Deck 6",
                        "description": "Conference Center, Two70, The Boardroom, Library, Staterooms. "
                    },
                    "occupancy": {
                        "min": 0,
                        "max": 2
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
