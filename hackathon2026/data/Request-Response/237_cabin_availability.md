# Cabin Availability

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 4 – All Adults (NCL) > Cabin Availability

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
            "packageId": 1312610,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "H5",
                "fare": {
                    "fareCode": {
                        "code": "BESTFARE"
                    }
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 31,
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
            "age": 30
        },
        {
            "rph": 4,
            "age": 40
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
Date: Fri, 31 Mar 2023 08:49:25 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "65d95636-75f5-44b3-a54d-ac1b6f6857f5",
      "timeStamp": "31-Mar-2023 04:49:22",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "27-Jun-2023 00:00:00",
        "arrivalDateTime": "08-Jul-2023 00:00:00",
        "departureCityId": "SEA",
        "arrivalCityId": "SEA",
        "duration": 11
      },
      "pos": {
        "id": 2250,
        "apiId": "NCL",
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
      "cruise": {
        "packageId": 1312610,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13670
            }
          ]
        },
        "itinerary": {
          "id": 351639,
          "destination": {
            "id": 1
          }
        },
        "tourCode": "18707348",
        "voyage": {
          "departureDateTime": "01-Jul-2023 00:00:00",
          "arrivalDateTime": "08-Jul-2023 00:00:00",
          "departureCityId": "SEA",
          "arrivalCityId": "SEA",
          "code": "18506272"
        },
        "transportationType": 28
      },
      "cabins": [
        {
          "number": "17104",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "17116",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "17118",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "17700",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "17704",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "17708",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "17710",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "17718",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "17724",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9370,
            "name": "Deck 17",
            "description": "Horizon Lounge, Hot Tubs, Sun Deck, The Haven Courtyard, The Haven Lounge, Bar, Aqua Racer, Jogging Track, Le Bistro French Restaurant, American Diner, Spice H2O, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 31,
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
        "age": 30
      },
      {
        "rph": 4,
        "age": 40
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
