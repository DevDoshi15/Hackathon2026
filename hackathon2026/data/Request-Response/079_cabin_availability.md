# Cabin Availability

**Path:** Create Reservation > Create Reservation using POS Id > Cabin Availability

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
            "id": 2114
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
            "packageId": 1269434,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "2B",
                "fare": {
                    "fareCode": {
                        "code": "G0737880"
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
Date: Fri, 17 Feb 2023 08:20:32 GMT
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
      "requestId": "ea9ac291-3703-4db8-b61a-1594efc35cad",
      "timeStamp": "17-Feb-2023 03:20:31",
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
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
          "id": 311051,
          "destination": {
            "id": 7
          }
        },
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
          "number": "1330",
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
            "id": 12140,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9252",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9640",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9642",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9622",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9620",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9630",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
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
          "deck": {
            "id": 12142,
            "name": "Deck 8",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8246",
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
            "id": 12142,
            "name": "Deck 8",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9586",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9588",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9590",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9592",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9276",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9278",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9340",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9342",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9320",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9322",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9290",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9292",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9286",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9288",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1630",
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
            "id": 12140,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9332",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9300",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9304",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9612",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9616",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1608",
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
            "id": 12140,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1270",
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
            "id": 12140,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9632",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1308",
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
            "id": 12140,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9600",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9604",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1288",
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
            "id": 12140,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1588",
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
            "id": 12140,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9312",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "9316",
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
            "id": 12143,
            "name": "Deck 9",
            "description": "Staterooms.\n"
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1570",
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
            "id": 12140,
            "name": "Deck 10",
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
