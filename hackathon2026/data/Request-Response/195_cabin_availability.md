# Cabin Availability

**Path:** Create Reservation > Group Reservation > Norwegian Cruiseline > Cabin Availability

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
            "packageId": 1313262
        },
        "categories": [
            {
                "code": "IB",
                "fare": {
                    "fareCode": {
                        "code": "A1612559",
                        "groups": [
                            {
                                "code": "A1612559"
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
Date: Wed, 15 Mar 2023 12:39:33 GMT
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
      "requestId": "d05139cb-2101-46d7-888e-9a44656455ec",
      "timeStamp": "15-Mar-2023 08:39:30",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "16-Dec-2023 00:00:00",
        "arrivalDateTime": "23-Dec-2023 00:00:00",
        "departureCityId": "XPC",
        "arrivalCityId": "XPC",
        "duration": 7
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
          "ageGroup": "Adult",
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
        }
      ],
      "cruise": {
        "packageId": 1313262,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13669
            }
          ]
        },
        "itinerary": {
          "id": 363167,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "16-Dec-2023 00:00:00",
          "arrivalDateTime": "23-Dec-2023 00:00:00",
          "departureCityId": "XPC",
          "arrivalCityId": "XPC",
          "code": "18439927"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "12655",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12651",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12649",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12639",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12637",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12635",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12633",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12629",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12627",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12625",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12623",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12621",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12619",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12617",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12615",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12613",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12611",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12607",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12601",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Middle",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "11693",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9387,
            "name": "Deck 11",
            "description": "Studio Lounge, Staterooms."
          },
          "position": "Aft",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12425",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12423",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12421",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12419",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12417",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12415",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12413",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12411",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12409",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12407",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12405",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12403",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "12401",
          "beds": [
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9386,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "11691",
          "beds": [
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9387,
            "name": "Deck 11",
            "description": "Studio Lounge, Staterooms."
          },
          "position": "Aft",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "11689",
          "beds": [
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9387,
            "name": "Deck 11",
            "description": "Studio Lounge, Staterooms."
          },
          "position": "Aft",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "11687",
          "beds": [
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9387,
            "name": "Deck 11",
            "description": "Studio Lounge, Staterooms."
          },
          "position": "Aft",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "11685",
          "beds": [
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9387,
            "name": "Deck 11",
            "description": "Studio Lounge, Staterooms."
          },
          "position": "Aft",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "11683",
          "beds": [
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9387,
            "name": "Deck 11",
            "description": "Studio Lounge, Staterooms."
          },
          "position": "Aft",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "11681",
          "beds": [
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9387,
            "name": "Deck 11",
            "description": "Studio Lounge, Staterooms."
          },
          "position": "Aft",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "11677",
          "beds": [
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 9387,
            "name": "Deck 11",
            "description": "Studio Lounge, Staterooms."
          },
          "position": "Aft",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 4
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
