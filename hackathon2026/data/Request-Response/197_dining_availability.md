# Dining Availability

**Path:** Create Reservation > Group Reservation > Norwegian Cruiseline > Dining Availability

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
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1313262
        },
        "categories": [
            {
                "code": "IB",
                "fare": {
                    "fareCode": {
                        "code": "A1612559",
                        "groups": [
                            {
                                "code": "A1612559"
                            }
                        ]
                    }
                },
                "cabins": [
                    {
                        "number": "12655"
                    }
                ]
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
Date: Wed, 15 Mar 2023 12:41:08 GMT
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
      "requestId": "a9bbf203-1525-4570-87ea-5f46c44f01ec",
      "timeStamp": "15-Mar-2023 08:41:08",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "16-Dec-2023 00:00:00",
        "arrivalDateTime": "23-Dec-2023 00:00:00",
        "departureCityId": "XPC",
        "arrivalCityId": "XPC",
        "duration": 7
      },
      "pos": {
        "id": 2112,
        "apiId": "NCL",
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
        "packageId": 1313262,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13669
            }
          ]
        },
        "itinerary": {
          "id": 363167,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "16-Dec-2023 00:00:00",
          "arrivalDateTime": "23-Dec-2023 00:00:00",
          "departureCityId": "XPC",
          "arrivalCityId": "XPC",
          "code": "18439927"
        },
        "transportationType": 29
      },
      "dinings": [
        {
          "id": 4,
          "code": "FREEST",
          "name": "Freestyle",
          "status": 1,
          "tableSizeOptions": []
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
