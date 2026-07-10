# Cabin Availability

**Path:** Create Reservation > Occupancy Based Samples > Single Occupancy (NCL) > Cabin Availability

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
            "packageId": 1238898,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "IA",
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
Date: Thu, 23 Mar 2023 10:39:42 GMT
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
      "requestId": "d1401f14-c449-4497-aaeb-1001d3df3d50",
      "timeStamp": "23-Mar-2023 06:39:39",
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
      "reservationIndicators": {
        "modifyIndicators": [
          {
            "type": 6,
            "value": false
          },
          {
            "type": 9,
            "value": false
          },
          {
            "type": 11,
            "value": false
          },
          {
            "type": 12,
            "value": false
          },
          {
            "type": 14,
            "value": false
          },
          {
            "type": 15,
            "value": false
          },
          {
            "type": 16,
            "value": false
          },
          {
            "type": 45,
            "value": false
          },
          {
            "type": 600,
            "value": false
          },
          {
            "type": 700,
            "value": false
          },
          {
            "type": 1001,
            "value": false
          }
        ],
        "mandatoryIndicators": [
          {
            "type": "CitizenShip",
            "value": true
          },
          {
            "type": "Insurance",
            "value": true
          },
          {
            "type": "Age",
            "value": true
          },
          {
            "type": "Title",
            "value": true
          },
          {
            "type": "Gender",
            "value": true
          },
          {
            "type": "PhoneNumber",
            "value": true
          },
          {
            "type": "DiningSeating",
            "value": true
          },
          {
            "type": "TableSize",
            "value": true
          },
          {
            "type": "FlightInformation",
            "value": true
          },
          {
            "type": 700,
            "value": true
          },
          {
            "type": "EMail",
            "value": true
          }
        ]
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
          "ageGroup": "Adult",
          "isPrimaryContact": true
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
          "id": 364180,
          "destination": {
            "id": 7
          }
        },
        "tourCode": "FR4BH098",
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
          "number": "1856",
          "beds": [
            {
              "code": "A",
              "name": "2K",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "2K",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 10757,
            "name": "Deck 12",
            "description": "Vitality at Sea, Spa, The Lime & Coconut, Movie Screen, Running Track, Arcade, Nursery, Adventure Ocean, Johnny Rockets, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1806",
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
            "id": 10757,
            "name": "Deck 12",
            "description": "Vitality at Sea, Spa, The Lime & Coconut, Movie Screen, Running Track, Arcade, Nursery, Adventure Ocean, Johnny Rockets, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1816",
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
            "id": 10757,
            "name": "Deck 12",
            "description": "Vitality at Sea, Spa, The Lime & Coconut, Movie Screen, Running Track, Arcade, Nursery, Adventure Ocean, Johnny Rockets, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1818",
          "beds": [
            {
              "code": "A",
              "name": "2K",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "2K",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 10757,
            "name": "Deck 12",
            "description": "Vitality at Sea, Spa, The Lime & Coconut, Movie Screen, Running Track, Arcade, Nursery, Adventure Ocean, Johnny Rockets, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1866",
          "beds": [
            {
              "code": "A",
              "name": "2K",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "2K",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 10757,
            "name": "Deck 12",
            "description": "Vitality at Sea, Spa, The Lime & Coconut, Movie Screen, Running Track, Arcade, Nursery, Adventure Ocean, Johnny Rockets, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1868",
          "beds": [
            {
              "code": "A",
              "name": "2K",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "2K",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 10757,
            "name": "Deck 12",
            "description": "Vitality at Sea, Spa, The Lime & Coconut, Movie Screen, Running Track, Arcade, Nursery, Adventure Ocean, Johnny Rockets, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1876",
          "beds": [
            {
              "code": "A",
              "name": "2K",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "2K",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 10757,
            "name": "Deck 12",
            "description": "Vitality at Sea, Spa, The Lime & Coconut, Movie Screen, Running Track, Arcade, Nursery, Adventure Ocean, Johnny Rockets, Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1826",
          "beds": [
            {
              "code": "A",
              "name": "2K",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "2K",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 10757,
            "name": "Deck 12",
            "description": "Vitality at Sea, Spa, The Lime & Coconut, Movie Screen, Running Track, Arcade, Nursery, Adventure Ocean, Johnny Rockets, Staterooms."
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
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
