# Hold Cabin

**Path:** Create Reservation > Create Reservation With Air For SilverSea > Hold Cabin

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
                "id": "NYC"
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
            "packageId": 1252535,
            "packageTourId": -1
        },
        "categories": [
            {
                "Fare": {
                    "fareCode": {
                        "Code": "03",
                        "externalSessionInfo": {
                            "externalId": "03"
                        }
                    }
                },
                "Code": "SV",
                "cabins": [
                    {
                        "number": "704"
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
                "city": {
                    "name": "MIAMI"
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
            "title": "MR",
            "firstName": "Jack",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
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
Date: Fri, 10 Feb 2023 13:29:45 GMT
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
      "requestId": "f9e79db6-c9f4-4194-a809-ea4ef7384bf5",
      "timeStamp": "10-Feb-2023 08:29:43",
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
      }
    },
    "customers": [
      {
        "title": "MR",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
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
        "title": "MR",
        "rph": 2,
        "firstName": "Jack",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
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
