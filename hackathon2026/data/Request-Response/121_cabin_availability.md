# Cabin Availability

**Path:** Create Reservation > Create Reservation With Grats/AddOns For NCL > Cabin Availability

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
            "packageId": 1238898,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "OC",
                "fare": {
                    "fareCode": {
                        "code": "DISC50" // We will pass the farecode along with category to fetch the list of cabins & addons
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
Date: Fri, 17 Feb 2023 15:31:47 GMT
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
      "requestId": "3390f12e-a06e-48f3-b512-631052b6dce3",
      "timeStamp": "17-Feb-2023 10:31:45",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "05-May-2023 00:00:00",
        "arrivalDateTime": "08-May-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 3
      },
      "pos": {
        "id": 2112,
        "apiId": "NCL",
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
        "packageId": 1238898,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 1179
            }
          ]
        },
        "itinerary": {
          "id": 363194,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "05-May-2023 00:00:00",
          "arrivalDateTime": "08-May-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "17183730"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "8031",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8030",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8048",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8248",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8029",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8229",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8249",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8028",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8250",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8027",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8051",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8251",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8052",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8252",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8053",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8253",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8224",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8054",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8254",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8023",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8221",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8020",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8220",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8038",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8240",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8241",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8242",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8243",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8244",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8245",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8055",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8255",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8256",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8057",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8257",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8058",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8258",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8059",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8259",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8260",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9429,
            "name": "Deck 8",
            "description": "Hot Tubs, Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        }
      ],
      "addOns": [
        {
          "code": "34CHO",
          "name": "FAS_Taxes Only 3-4",
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
          "combinableCodes": [
            "ALL4CHO",
            "BVSXIN",
            "DISC50",
            "DISXIN",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "INTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "ALL4CHO",
          "name": "FAS_Beverage, Dining, Internet, $50 per port Shore Ex Credit",
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
          "combinableCodes": [
            "34CHO",
            "DISC50",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "BVSXIN",
          "name": "FAS_Beverage, Internet, $50 per port Shore Ex Credit",
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
          "combinableCodes": [
            "34CHO",
            "DISC50",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "DISXIN",
          "name": "FAS_Dining Package, Internet, $50 per port Shore Ex Credit",
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
          "combinableCodes": [
            "34CHO",
            "DISC50",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "EASYFARE",
          "name": "OTH_Early Booking Fare - Upgrades - A/S",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC50",
            "DISXIN",
            "FITOBC",
            "FLEXNET",
            "INTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "FITOBC",
          "name": "OTH_FIT ONLY- Onboard Credit Offer",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC50",
            "DISXIN",
            "EASYFARE",
            "INTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "FLEXNET",
          "name": "OTH_NET RATES",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC50",
            "DISXIN",
            "EASYFARE",
            "INTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "INTSHO",
          "name": "FAS_Internet Package and $50 per port Shore Ex Credit",
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
          "combinableCodes": [
            "34CHO",
            "DISC50",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "KOSHER MEAL",
          "name": "OTH_Kosher Meal",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC50",
            "DISXIN",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "INTSHO",
            "PPSRVCHG"
          ]
        },
        {
          "code": "PPSRVCHG",
          "name": "OTH_Prepaid Service Charges",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC50",
            "DISXIN",
            "EASYFARE",
            "FITOBC",
            "FLEXNET",
            "INTSHO",
            "KOSHER MEAL"
          ]
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
