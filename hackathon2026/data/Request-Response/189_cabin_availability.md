# Cabin Availability

**Path:** Create Reservation > Group Reservation > Royal Carribean Cruiseline > Cabin Availability

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
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1269434
        },
        "categories": [
            {
                "code": "2N",
                "externalSessionInfo": { // external session info received in the category avail API response
                    "externalId": "5"
                },
                "fare": {
                    "fareCode": {
                        "code": "I1071484_GRP",
                        "groups": [
                            {
                                "code": "1179594"
                            }
                        ]
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
Date: Tue, 14 Mar 2023 09:40:21 GMT
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
      "requestId": "b9db534c-a239-4622-9405-2ac1a0525cbf",
      "timeStamp": "14-Mar-2023 05:40:20",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
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
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 364180,
          "destination": {
            "id": 7
          }
        },
        "tourCode": "FR4BH098",
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "2616",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2618",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2610",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2278",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2320",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2328",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2326",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2300",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2306",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2308",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2562",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3610",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2600",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2606",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2608",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3310",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2318",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2316",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2310",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2244",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2246",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3608",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2634",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2550",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2620",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2628",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2626",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3304",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3306",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3308",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2290",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2294",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2296",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2298",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2332",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2334",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2302",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2312",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2554",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2556",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2558",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2630",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2632",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3300",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2286",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2612",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12553,
            "name": "Deck 2",
            "description": "Center Ice Rink, Studio B, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3252",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3614",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3616",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3314",
          "beds": [
            {
              "code": "A",
              "name": "86",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "86",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12554,
            "name": "Deck 3",
            "description": "Royal Theatre, Studio B, Photo Studio, Art Gallery, Main Dining Room, Staterooms."
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
