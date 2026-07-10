# Cabin Availability

**Path:** Create Reservation > Create Reservation With Air For SilverSea > Cabin Availability

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
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "BHM" // flight departure city
            }
        },
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
            "packageId": 1252535,
            "packageTourId": -1
        },
        "categories": [
            {
                "Fare": {
                    "fareCode": {
                        "Code": "03",
                        "externalSessionInfo": {
                            "externalId": "03"
                        }
                    }
                },
                "Code": "SV"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "title": "MR",
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        },
        {
            "rph": 2,
            "title": "MR",
            "firstName": "Jack",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Fri, 10 Feb 2023 13:27:18 GMT
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
      "requestId": "130ef1e0-557e-48d6-9ed3-edd2fb4279b8",
      "timeStamp": "10-Feb-2023 08:27:12",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "06-Mar-2023 00:00:00",
        "arrivalDateTime": "13-Mar-2023 00:00:00",
        "departureCityId": "SJU",
        "arrivalCityId": "BGI",
        "duration": 7
      },
      "pos": {
        "id": 2122,
        "apiId": "SSC",
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
        "packageId": 1252535,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8115,
          "ships": [
            {
              "id": 14717
            }
          ]
        },
        "itinerary": {
          "id": 291413,
          "destination": {
            "id": 9
          }
        },
        "voyage": {
          "departureDateTime": "06-Mar-2023 00:00:00",
          "arrivalDateTime": "13-Mar-2023 00:00:00",
          "departureCityId": "SJU",
          "arrivalCityId": "BGI",
          "code": "DA230306007"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "705",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "706",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "707",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "708",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "709",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "710",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "712",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "714",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "715",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "716",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "718",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "719",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "720",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "721",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "722",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "724",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "726",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "727",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "728",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "731",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "734",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "735",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "736",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "737",
          "deck": {
            "id": 10630,
            "name": "Deck 7",
            "description": "La Terrazza, Silver Note, Casino, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "803",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "804",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "805",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "806",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "807",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "808",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "809",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "810",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "811",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "812",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "814",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "815",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "816",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "817",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "818",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "819",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "828",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "832",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "833",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "834",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "835",
          "deck": {
            "id": 10629,
            "name": "Deck 8",
            "description": "Arts Café, Boutique, La Dame, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "903",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "904",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "905",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "906",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "907",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "908",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "909",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "910",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "911",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "912",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "914",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "915",
          "deck": {
            "id": 10628,
            "name": "Deck 9",
            "description": "Panorama Lounge, Connoisseur’s Corner, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        }
      ],
      "addOns": [
        {
          "code": "1",
          "name": "Economy Class Promotion Air",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "type": 2,
          "combinableCodes": []
        },
        {
          "code": "16",
          "name": "Free Shorex Included",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "autoInclude": true,
          "combinableCodes": []
        }
      ]
    },
    "customers": [
      {
        "title": "MR",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      },
      {
        "title": "MR",
        "rph": 2,
        "firstName": "Jack",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
