# Cabin Availability

**Path:** Create Reservation > Create Reservation With Transfer (Pre/Post Airport Transfer) > Cabin Availability

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
Date: Mon, 06 Mar 2023 10:07:36 GMT
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
      "requestId": "93a7f461-73f2-465e-ad93-2b2ec6e20f3d",
      "timeStamp": "06-Mar-2023 05:07:35",
      "token": "EQTEMPKEN"
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
      "cabins": [
        {
          "number": "6447",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7669",
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
          "deck": {
            "id": 12154,
            "name": "Deck 7",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6645",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8677",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6649",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6683",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7471",
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
          "deck": {
            "id": 12154,
            "name": "Deck 7",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9477",
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
          "deck": {
            "id": 12156,
            "name": "Deck 9",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7477",
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
          "deck": {
            "id": 12154,
            "name": "Deck 7",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7479",
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
          "deck": {
            "id": 12154,
            "name": "Deck 7",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2641",
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
          "deck": {
            "id": 12151,
            "name": "Deck 2",
            "description": "Conference Center, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7351",
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
          "deck": {
            "id": 12154,
            "name": "Deck 7",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3021",
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
          "deck": {
            "id": 12152,
            "name": "Deck 3",
            "description": "The Lyric Theater, Studio B, Photo & Art Gallery, Main Dining Room, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3023",
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
          "deck": {
            "id": 12152,
            "name": "Deck 3",
            "description": "The Lyric Theater, Studio B, Photo & Art Gallery, Main Dining Room, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9335",
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
          "deck": {
            "id": 12156,
            "name": "Deck 9",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3027",
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
          "deck": {
            "id": 12152,
            "name": "Deck 3",
            "description": "The Lyric Theater, Studio B, Photo & Art Gallery, Main Dining Room, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3029",
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
          "deck": {
            "id": 12152,
            "name": "Deck 3",
            "description": "The Lyric Theater, Studio B, Photo & Art Gallery, Main Dining Room, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6217",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6219",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6471",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6477",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6651",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8681",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6657",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8685",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6237",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8381",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8383",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8387",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8365",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6365",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8369",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6369",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8451",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6123",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8121",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6125",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6129",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6371",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8357",
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
          "deck": {
            "id": 12155,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6451",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6453",
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
          "deck": {
            "id": 12153,
            "name": "Deck 6",
            "description": "Next Cruise, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9367",
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
          "deck": {
            "id": 12156,
            "name": "Deck 9",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7383",
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
          "deck": {
            "id": 12154,
            "name": "Deck 7",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9369",
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
          "deck": {
            "id": 12156,
            "name": "Deck 9",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7387",
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
          "deck": {
            "id": 12154,
            "name": "Deck 7",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7451",
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
          "deck": {
            "id": 12154,
            "name": "Deck 7",
            "description": "Staterooms."
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
