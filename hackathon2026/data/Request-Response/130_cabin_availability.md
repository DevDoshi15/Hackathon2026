# Cabin Availability

**Path:** Create Reservation > Create Reservation With Grats For RCCL > Cabin Availability

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
            "packageId": 1269329,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "4M",
                "fare": {
                    "fareCode": {
                        "code": "G0737880" // We will pass the farecode along with category to fetch the list of cabins & addons
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
Date: Mon, 20 Feb 2023 08:29:23 GMT
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
      "requestId": "f59ab82f-0b9f-4e0b-ba9a-ef4255a63a69",
      "timeStamp": "20-Feb-2023 03:29:21",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "15-Apr-2023 00:00:00",
        "arrivalDateTime": "20-Apr-2023 00:00:00",
        "departureCityId": "TPA",
        "arrivalCityId": "TPA",
        "duration": 5
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
        "packageId": 1269329,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 72
            }
          ]
        },
        "itinerary": {
          "id": 311000,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "15-Apr-2023 00:00:00",
          "arrivalDateTime": "20-Apr-2023 00:00:00",
          "departureCityId": "TPA",
          "arrivalCityId": "TPA",
          "code": "BR05W366"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "7000",
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7002",
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7006",
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7008",
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8004",
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
            "id": 12087,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8006",
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
            "id": 12087,
            "name": "Deck 8",
            "description": "Staterooms."
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7012",
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8506",
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
            "id": 12087,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7500",
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7502",
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7506",
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
            "percent": 25
          },
          "deck": {
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "7508",
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
            "id": 10847,
            "name": "Deck 7",
            "description": "Loyalty Desk, Staterooms.\n"
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
