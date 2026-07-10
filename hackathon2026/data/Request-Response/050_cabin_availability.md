# Cabin Availability

**Path:** Cabin Details > Cabin Position & Remarks > Cabin Availability

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
            "packageId": 1282255
        },
        "categories": [
            {
                "code": "PO",
                "fare": {
                    "fareCode": {
                        "code": "H8212136"
                    }
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52
        },
        {
            "rph": 2,
            "age": 57
        }
    ],
    "trackingInfo": {}
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Thu, 16 Mar 2023 14:59:38 GMT
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
      "requestId": "42d37a1b-ff68-44ae-a4e2-28000fbd8490",
      "timeStamp": "16-Mar-2023 10:59:37"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "09-Apr-2023 00:00:00",
        "arrivalDateTime": "16-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 7
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
        "id": 2109,
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
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
        }
      ],
      "cruise": {
        "packageId": 1282255,
        "packageTourId": -1,
        "cruiseline": {
          "id": 2,
          "ships": [
            {
              "id": 14948
            }
          ]
        },
        "itinerary": {
          "id": 364303,
          "destination": {
            "id": 14
          }
        },
        "tourCode": "BY07W480",
        "voyage": {
          "departureDateTime": "09-Apr-2023 00:00:00",
          "arrivalDateTime": "16-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "BY07W480"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "6236",
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
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6239",
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
          "obstruction": {
            "isObstructed": true,
            "percent": 25
          },
          "deck": {
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6135",
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
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6132",
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
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6131",
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
          "obstruction": {
            "isObstructed": true,
            "percent": 50
          },
          "deck": {
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6128",
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
          "obstruction": {
            "isObstructed": true,
            "percent": 10
          },
          "deck": {
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "6237",
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
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6238",
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
          "obstruction": {
            "isObstructed": true,
            "percent": 10
          },
          "deck": {
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6134",
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
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6133",
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
          "obstruction": {
            "isObstructed": true,
            "percent": 10
          },
          "deck": {
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6130",
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
          "obstruction": {
            "isObstructed": true,
            "percent": 50
          },
          "deck": {
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6129",
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
          "obstruction": {
            "isObstructed": true,
            "percent": 10
          },
          "deck": {
            "id": 12365,
            "name": "Deck 6",
            "description": "Eden, Ramp to Deck 5."
          },
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
        "age": 52
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
