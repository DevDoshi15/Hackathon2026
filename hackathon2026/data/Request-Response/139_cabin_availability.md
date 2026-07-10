# Cabin Availability

**Path:** Create Reservation > Create Reservation With Combinable FareCodes > Cabin Availability

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
            "packageId": 1269619,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "2N",
                "fare": {
                    "fareCode": {
                        "code": "G0738129",
                        "combinableFares": [
                            {
                                "code": "I7996069",
                                "type": 0
                            },
                            {
                                "code": "I7997687",
                                "type": 0
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
Date: Fri, 17 Feb 2023 16:28:56 GMT
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
      "requestId": "3d303998-6bcd-49cb-9400-7929d77848c7",
      "timeStamp": "17-Feb-2023 11:28:54",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Apr-2023 00:00:00",
        "arrivalDateTime": "10-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 3
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269619,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 1093
            }
          ]
        },
        "itinerary": {
          "id": 349022,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "07-Apr-2023 00:00:00",
          "arrivalDateTime": "10-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "LB3BH045"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "2616",
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2254",
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2256",
          "connectingCabinNumber": "2258",
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2258",
          "connectingCabinNumber": "2256",
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2630",
          "connectingCabinNumber": "2632",
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2632",
          "connectingCabinNumber": "2630",
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3552",
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3604",
          "connectingCabinNumber": "3606",
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3606",
          "connectingCabinNumber": "3604",
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "3600",
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
            "id": 10788,
            "name": "Deck 3",
            "description": "Platinum Theater, Studio B, On Air Club, Art Gallery, Main Dining Room, Staterooms."
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2602",
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
            "id": 12074,
            "name": "Deck 2",
            "description": "Platinum Theater, Conference Room, Center Ice Rink, Studio B, Staterooms.\n"
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
