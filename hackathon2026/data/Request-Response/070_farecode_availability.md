# Farecode Availability

**Path:** Create Reservation > Create Reservation With Air For SilverSea > Farecode Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listfarecodes`

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
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "NYC" // flight departure city
            }
        },
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
            "packageId": 1252535
        }
    },
    "customers": [
        {
            "rph": 1,
            "age": 55,
            "address": {
                "city": {
                    "id": "MIA"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        },
        {
            "rph": 2,
            "age": 57,
            "address": {
                "city": {
                    "id": "MIA"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Fri, 10 Feb 2023 13:08:01 GMT
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
      "requestId": "f32a64e1-6093-40eb-bb12-a93594099c63",
      "timeStamp": "10-Feb-2023 08:07:56",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "06-Mar-2023 00:00:00",
        "arrivalDateTime": "13-Mar-2023 00:00:00",
        "departureCityId": "SJU",
        "arrivalCityId": "BGI",
        "duration": 7
      },
      "pos": {
        "id": 2122,
        "apiId": "SSC",
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
        "packageId": 1252535,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8115,
          "ships": [
            {
              "id": 14717
            }
          ]
        },
        "itinerary": {
          "id": 291413,
          "destination": {
            "id": 9
          }
        },
        "voyage": {
          "departureDateTime": "06-Mar-2023 00:00:00",
          "arrivalDateTime": "13-Mar-2023 00:00:00",
          "departureCityId": "SJU",
          "arrivalCityId": "BGI",
          "code": "DA230306007"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "03",
          "name": "SILVER PRIVILEGE FARE",
          "description": "Air Promo included",
          "bookOnline": true,
          "externalSessionInfo": {
            "externalId": "03"
          },
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "Air Promo included",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 37
            }
          ]
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 55,
        "address": {
          "city": {
            "id": "MIA"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      },
      {
        "rph": 2,
        "age": 57,
        "address": {
          "city": {
            "id": "MIA"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
