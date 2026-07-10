# Cabin Availability

**Path:** Create Reservation > Create Reservation For Resident Farecodes Disney > Cabin Availability

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
            "packageId": 1310995
        },
        "categories": [
            {
                "code": "07A",
                "fare": {
                    "fareCode": {
                        "code": "FLR"
                    }
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 32,
            "address": {
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
            "age": 32,
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
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
Date: Mon, 20 Feb 2023 07:52:40 GMT
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
      "requestId": "c69a8a86-c08d-4f06-89af-febebe02a595",
      "timeStamp": "20-Feb-2023 02:52:38",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Apr-2023 00:00:00",
        "arrivalDateTime": "12-Apr-2023 00:00:00",
        "departureCityId": "SAN",
        "arrivalCityId": "SAN",
        "duration": 5
      },
      "pos": {
        "id": 2110,
        "apiId": "Seaware",
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
        "packageId": 1310995,
        "packageTourId": -1,
        "cruiseline": {
          "id": 4,
          "ships": [
            {
              "id": 33
            }
          ]
        },
        "itinerary": {
          "id": 349515,
          "destination": {
            "id": 56
          }
        },
        "voyage": {
          "departureDateTime": "07-Apr-2023 00:00:00",
          "arrivalDateTime": "12-Apr-2023 00:00:00",
          "departureCityId": "SAN",
          "arrivalCityId": "SAN",
          "code": "DW2304075SD"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "5134",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5136",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5138",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5140",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5632",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5634",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5636",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5638",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5640",
          "deck": {
            "id": 261,
            "name": "Deck 5",
            "description": "Buena Vista Theater, Oceaneer Lab, Oceaneer Club, and Flounder's Reef Nursery, Atrium, It's A Small World Nursery,  Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "6134",
          "deck": {
            "id": 260,
            "name": "Deck 6",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "6136",
          "deck": {
            "id": 260,
            "name": "Deck 6",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "6138",
          "deck": {
            "id": 260,
            "name": "Deck 6",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "6140",
          "deck": {
            "id": 260,
            "name": "Deck 6",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "6142",
          "deck": {
            "id": 260,
            "name": "Deck 6",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "6634",
          "deck": {
            "id": 260,
            "name": "Deck 6",
            "description": "Staterooms."
          },
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
        "age": 32,
        "address": {
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
        "age": 32,
        "address": {
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
