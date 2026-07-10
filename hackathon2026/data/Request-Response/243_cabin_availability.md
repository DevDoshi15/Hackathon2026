# Cabin Availability

**Path:** Create Reservation > RCCL switching to CruiseOnly when Cruise + Air is not available > Cabin Availability

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
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "Post",
            "GateWayCity": {
                "id": "PTY" // flight departure city
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
            "packageId": 1317656,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "RL",
                "type": 4,
                "fare": {
                    "farecode": {
                        "code": "G0738129" // select the fare and category code, which has "airInclusive": true in the list categories respone (prices element), to select Cruise + Air
                    }
                }
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
                    "id": "US"
                },
                "state": {
                    "id": "AL"
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
                    "id": "US"
                },
                "state": {
                    "id": "AL"
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
Date: Mon, 08 May 2023 15:51:31 GMT
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
      "requestId": "7e5d1f46-8a28-4283-9ee7-82a495b994dd",
      "timeStamp": "08-May-2023 11:51:29",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "23-Jun-2023 00:00:00",
        "arrivalDateTime": "30-Jun-2023 00:00:00",
        "departureCityId": "SEA",
        "arrivalCityId": "SEA",
        "duration": 7
      },
      "pos": {
        "id": 2227,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "Any"
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
        "packageId": 1317656,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 13717
            }
          ]
        },
        "itinerary": {
          "id": 364268,
          "destination": {
            "id": 1
          }
        },
        "tourCode": "OV07A221",
        "voyage": {
          "departureDateTime": "23-Jun-2023 00:00:00",
          "arrivalDateTime": "30-Jun-2023 00:00:00",
          "departureCityId": "SEA",
          "arrivalCityId": "SEA",
          "code": "OV07A221"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "8320",
          "isGuarantee": true,
          "beds": [
            {
              "code": "A",
              "name": "1K",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "1K",
              "description": "Together",
              "type": 282
            }
          ],
          "deck": {
            "id": 11962,
            "name": "Deck 8",
            "description": "Staterooms."
          },
          "occupancy": {
            "min": 0,
            "max": 6
          }
        }
      ]
    },
    "customers": [
      {
        "title": "MR",
        "gender": "Male",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1988",
        "age": 35,
        "address": {
          "country": {
            "id": "US"
          },
          "state": {
            "id": "AL"
          }
        }
      },
      {
        "title": "MR",
        "gender": "Male",
        "rph": 2,
        "firstName": "Jack",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1988",
        "age": 35,
        "address": {
          "country": {
            "id": "US"
          },
          "state": {
            "id": "AL"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
