# Cabin Availability

**Path:** Modify Reservation > Bed & Dining - Princess Cruise line > Cabin Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/ListCabins`

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
            "packageId": 1316566
        },
        "categories": [
            {
                "code": "M1",
                "fare": {
                    "fareCode": {
                        "code": "NR3"
                    }
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 53
        },
        {
            "rph": 2,
            "age": 58
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
Date: Fri, 05 May 2023 12:08:45 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "de88395a-45b2-4286-b95f-043c7f273201",
      "timeStamp": "05-May-2023 08:08:44",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Dec-2023 00:00:00",
        "arrivalDateTime": "04-Dec-2023 00:00:00",
        "departureCityId": "BNE",
        "arrivalCityId": "BNE",
        "duration": 3
      },
      "pos": {
        "id": 2198,
        "apiId": "Carnival",
        "officeId": "O212USTP17",
        "system": "Test",
        "currency": "USD",
        "type": "B2B"
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
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1316566,
        "packageTourId": -1,
        "cruiseline": {
          "id": 7,
          "ships": [
            {
              "id": 58
            }
          ]
        },
        "itinerary": {
          "id": 334555,
          "destination": {
            "id": 29
          }
        },
        "voyage": {
          "departureDateTime": "01-Dec-2023 00:00:00",
          "arrivalDateTime": "04-Dec-2023 00:00:00",
          "departureCityId": "BNE",
          "arrivalCityId": "BNE",
          "code": "6319"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "D510",
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
          "deck": {
            "id": 6314,
            "name": "Dolphin Deck",
            "description": "Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "D512",
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
          "deck": {
            "id": 6314,
            "name": "Dolphin Deck",
            "description": "Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "D514",
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
          "deck": {
            "id": 6314,
            "name": "Dolphin Deck",
            "description": "Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "D515",
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
          "deck": {
            "id": 6314,
            "name": "Dolphin Deck",
            "description": "Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "B503",
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
          "deck": {
            "id": 6313,
            "name": "Baja Deck",
            "description": "Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "D411",
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
          "deck": {
            "id": 6314,
            "name": "Dolphin Deck",
            "description": "Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
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
          "location": "Oceanview",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 53
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 58
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
