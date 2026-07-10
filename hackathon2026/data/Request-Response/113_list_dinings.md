# List Dinings

**Path:** Create Reservation > Create Reservation With Grats For Carnival > List Dinings

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
                        "number": "2284"
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
Date: Fri, 17 Feb 2023 15:03:13 GMT
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
      "requestId": "ac2bafe4-ae49-48d6-973d-a38b235115c7",
      "timeStamp": "17-Feb-2023 10:03:07",
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
      },
      "dinings": [
        {
          "id": 22,
          "code": "1",
          "name": "Early",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 11,
          "code": "2",
          "name": "Late Seating",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 44,
          "code": "O",
          "name": "Your Time Dining",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 21,
          "code": "U",
          "name": "Unassigned Seating",
          "status": 2,
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
