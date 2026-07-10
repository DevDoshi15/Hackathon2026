# List Dinings

**Path:** Create Reservation > Create Reservation For Resident Farecodes Disney > List Dinings

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/ListDinings`

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
            "packageId": 1310995
        },
        "categories": [
            {
                "code": "07A",
                "fare": {
                    "fareCode": {
                        "code": "FLR"
                    }
                },
                "cabins": [
                    {
                        "number": "5134"
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 32,
            "address": {
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
            "age": 32,
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
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
Date: Mon, 20 Feb 2023 07:53:26 GMT
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
      "requestId": "70602177-717d-491f-a6f6-e3e8f067cced",
      "timeStamp": "20-Feb-2023 02:53:10",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Apr-2023 00:00:00",
        "arrivalDateTime": "12-Apr-2023 00:00:00",
        "departureCityId": "SAN",
        "arrivalCityId": "SAN",
        "duration": 5
      },
      "pos": {
        "id": 2110,
        "apiId": "Seaware",
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
        "packageId": 1310995,
        "packageTourId": -1,
        "cruiseline": {
          "id": 4,
          "ships": [
            {
              "id": 33
            }
          ]
        },
        "itinerary": {
          "id": 349515,
          "destination": {
            "id": 56
          }
        },
        "voyage": {
          "departureDateTime": "07-Apr-2023 00:00:00",
          "arrivalDateTime": "12-Apr-2023 00:00:00",
          "departureCityId": "SAN",
          "arrivalCityId": "SAN",
          "code": "DW2304075SD"
        },
        "transportationType": 29
      },
      "dinings": [
        {
          "id": 2,
          "code": "SECOND",
          "name": "Second Seating",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 14,
          "code": "MAIN",
          "name": "Main Seating",
          "status": 1,
          "tableSizeOptions": []
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 32,
        "address": {
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
        "age": 32,
        "address": {
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
