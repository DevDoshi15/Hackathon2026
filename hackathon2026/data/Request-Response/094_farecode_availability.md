# Farecode Availability

**Path:** Create Reservation > Create Reservation For Resident Farecodes Disney > Farecode Availability

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
        }
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
                },
                "city": {
                    "id": "MIA"
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
Date: Mon, 20 Feb 2023 07:24:03 GMT
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
      "requestId": "b4bfa0aa-4a18-455d-9978-9477a4b40bff",
      "timeStamp": "20-Feb-2023 02:23:57",
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
      "fareCodes": [
        {
          "code": "BESTPRICE",
          "name": "BEST_PRICE",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": ""
          },
          "groups": [
            {}
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
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
