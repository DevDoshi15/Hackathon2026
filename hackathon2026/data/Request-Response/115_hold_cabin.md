# Hold Cabin

**Path:** Create Reservation > Create Reservation With Grats For Carnival > Hold Cabin

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
            "packageId": 1281377,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "6C",
                "fare": {
                    "fareCode": {
                        "code": "PNS"
                    }
                },
                "cabins": [
                    {
                        "number": "2280"
                    }
                ]
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
Date: Fri, 17 Feb 2023 15:01:18 GMT
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
      "requestId": "1a549d84-618d-4e89-a426-63875c2bf2ec",
      "timeStamp": "17-Feb-2023 10:01:11",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-May-2023 00:00:00",
        "arrivalDateTime": "05-May-2023 00:00:00",
        "departureCityId": "LAX",
        "arrivalCityId": "LAX",
        "duration": 4
      },
      "pos": {
        "id": 2108,
        "apiId": "Carnival",
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
        "packageId": 1281377,
        "packageTourId": -1,
        "cruiseline": {
          "id": 1,
          "ships": [
            {
              "id": 14383
            }
          ]
        },
        "itinerary": {
          "id": 303143,
          "destination": {
            "id": 55
          }
        },
        "voyage": {
          "departureDateTime": "01-May-2023 00:00:00",
          "arrivalDateTime": "05-May-2023 00:00:00",
          "departureCityId": "LAX",
          "arrivalCityId": "LAX",
          "code": "20230501RD04"
        },
        "transportationType": 29
      }
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
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
