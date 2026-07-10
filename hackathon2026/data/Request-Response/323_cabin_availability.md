# Cabin Availability

**Path:** Modify Reservation > Create Reservation then Modify Cabin (NCL) > Cabin Availability

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
            "packageId": 1307173,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "SL",
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
Date: Thu, 04 May 2023 08:33:09 GMT
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
      "requestId": "e7590db0-1f33-4229-a7f4-6ad5f6bdb196",
      "timeStamp": "04-May-2023 04:33:07",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "15-Mar-2024 00:00:00",
        "arrivalDateTime": "22-Mar-2024 00:00:00",
        "departureCityId": "GLS",
        "arrivalCityId": "GLS",
        "duration": 7
      },
      "pos": {
        "id": 2250,
        "apiId": "NCL",
        "officeId": "O100US6797",
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
        "packageId": 1307173,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 15089
            }
          ]
        },
        "itinerary": {
          "id": 363332,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "15-Mar-2024 00:00:00",
          "arrivalDateTime": "22-Mar-2024 00:00:00",
          "departureCityId": "GLS",
          "arrivalCityId": "GLS",
          "code": "18440175"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "9702",
          "beds": [
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 12381,
            "name": "Deck 9",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "10102",
          "beds": [
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 12380,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "10702",
          "beds": [
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 12380,
            "name": "Deck 10",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "12102",
          "beds": [
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 12378,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "12702",
          "beds": [
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "26",
              "name": "MT",
              "description": "2 Lower Twin Conv To Dble ",
              "type": 198
            }
          ],
          "deck": {
            "id": 12378,
            "name": "Deck 12",
            "description": "Staterooms."
          },
          "position": "Forward",
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
        "gender": "Male",
        "rph": 1,
        "age": 52,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
