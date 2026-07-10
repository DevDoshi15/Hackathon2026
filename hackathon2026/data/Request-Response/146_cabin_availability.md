# Cabin Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with No Transfer Package > Cabin Availability

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
            "packageId": 1277420,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "MM",
                "fare": {
                    "fareCode": {
                        "code": "NH1"
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
Date: Mon, 06 Mar 2023 08:39:56 GMT
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
      "requestId": "8dcbfbae-9deb-432d-9c00-ec5f2aa287c9",
      "timeStamp": "06-Mar-2023 03:39:55",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Apr-2023 00:00:00",
        "arrivalDateTime": "09-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 7
      },
      "pos": {
        "id": 2111,
        "apiId": "Carnival",
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
        "packageId": 1277420,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 13250
            }
          ]
        },
        "itinerary": {
          "id": 311682,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "02-Apr-2023 00:00:00",
          "arrivalDateTime": "09-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "I330"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "8142",
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261
            }
          ],
          "deck": {
            "id": 5144,
            "name": "Navigation Deck",
            "description": "Neptune Lounge. Staterooms."
          },
          "location": "Aft Port Inside",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8146",
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261
            }
          ],
          "deck": {
            "id": 5144,
            "name": "Navigation Deck",
            "description": "Neptune Lounge. Staterooms."
          },
          "location": "Aft Port Inside",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8149",
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261
            }
          ],
          "deck": {
            "id": 5144,
            "name": "Navigation Deck",
            "description": "Neptune Lounge. Staterooms."
          },
          "location": "Aft Starboard Inside",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8153",
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261
            }
          ],
          "deck": {
            "id": 5144,
            "name": "Navigation Deck",
            "description": "Neptune Lounge. Staterooms."
          },
          "location": "Aft Starboard Inside",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8150",
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261
            }
          ],
          "deck": {
            "id": 5144,
            "name": "Navigation Deck",
            "description": "Neptune Lounge. Staterooms."
          },
          "location": "Aft Port Inside",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "8159",
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261
            }
          ],
          "deck": {
            "id": 5144,
            "name": "Navigation Deck",
            "description": "Neptune Lounge. Staterooms."
          },
          "location": "Aft Starboard Inside",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "GUAR",
          "isGuarantee": true,
          "beds": [
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261
            },
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243
            }
          ],
          "location": "Inside",
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
