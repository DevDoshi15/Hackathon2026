# Cabin Availabililty

**Path:** Modify Reservation > Category, Fare code and Cabin - Royal Caribbean > Cabin Availabililty

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
            "packageId": 1336123
        },
        "categories": [
            {
                "code": "OS",
                "fare": {
                    "fareCode": {
                        "code": "G0738129"
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
Date: Thu, 04 May 2023 10:39:40 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "5653598f-c394-44ea-b610-c8e2e62dad54",
      "timeStamp": "04-May-2023 06:39:39",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Dec-2023 00:00:00",
        "arrivalDateTime": "09-Dec-2023 00:00:00",
        "departureCityId": "ONX",
        "arrivalCityId": "ONX",
        "duration": 7
      },
      "pos": {
        "id": 2227,
        "apiId": "RCCL",
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
        "packageId": 1336123,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 84
            }
          ]
        },
        "itinerary": {
          "id": 364276,
          "destination": {
            "id": 9
          }
        },
        "tourCode": "RH07D356",
        "voyage": {
          "departureDateTime": "02-Dec-2023 00:00:00",
          "arrivalDateTime": "09-Dec-2023 00:00:00",
          "departureCityId": "ONX",
          "arrivalCityId": "ONX",
          "code": "RH07D356"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "8004",
          "beds": [
            {
              "code": "A",
              "name": "1Q",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "1Q",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 12144,
            "name": "Deck 8",
            "description": "Staterooms."
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
