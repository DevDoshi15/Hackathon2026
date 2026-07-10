# Hold Cabin

**Path:** Create Reservation > Create Reservation With Air For P&O Cruise line > Hold Cabin

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/holdcabin`

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
        "CruiselineAir": {
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "MAN"
            }
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
            "packageId": 1501519,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "B2",
                "fare": {
                    "farecode": {
                        "code": "KD1"
                    }
                },
                "cabins": [
                    {
                        "number": "R412" // use any cabin number received from ListCabins API
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "title": "MR",
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "country": {
                    "id": "GB"
                }
            }
        },
        {
            "rph": 2,
            "title": "MR",
            "firstName": "Jack",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "country": {
                    "id": "GB"
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
Date: Wed, 08 Feb 2023 09:03:09 GMT
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
      "requestId": "4e3718e4-6f5d-4313-a61b-b9bf10176080",
      "timeStamp": "23-Jun-2026 07:34:31",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "03-Jun-2027 00:00:00",
        "arrivalDateTime": "10-Jun-2027 00:00:00",
        "departureCityId": "VLT",
        "arrivalCityId": "VLT",
        "duration": 7
      },
      "pos": {
        "id": 3487,
        "officeId": "O212GBTP17",
        "currency": "GBP",
        "type": "B2B",
        "system": "Test",
        "apiId": "Carnival"
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
        "currencyId": "GBP",
        "countryId": "GB"
      },
      "externalSessionInfo": {
        "externalId": "a@#$A721"
      },
      "type": "Cruise",
      "cruise": {
        "packageId": 1501519,
        "packageTourId": -1,
        "cruiseline": {
          "id": 16,
          "ships": [
            {
              "id": 13257,
              "code": "AZ"
            }
          ]
        },
        "voyage": {
          "departureDateTime": "03-Jun-2027 00:00:00",
          "arrivalDateTime": "10-Jun-2027 00:00:00",
          "departureCityId": "VLT",
          "arrivalCityId": "VLT",
          "code": "A721"
        },
        "itinerary": {
          "id": 433252,
          "destination": {
            "id": 51
          }
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 60438,
          "code": "B2",
          "fares": [
            {
              "fareCode": {
                "code": "KD1",
                "type": 0
              }
            }
          ]
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
