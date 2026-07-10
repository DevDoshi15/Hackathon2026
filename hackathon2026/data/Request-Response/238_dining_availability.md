# Dining Availability

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 4 – All Adults (NCL) > Dining Availability

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
        "cruise": {
            "packageId": 1312610,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "H5",
                "fare": {
                    "fareCode": {
                        "code": "BESTFARE"
                    }
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 31,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 30
        },
        {
            "rph": 3,
            "age": 30
        },
        {
            "rph": 4,
            "age": 40
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
Date: Fri, 31 Mar 2023 08:50:10 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "e8141c59-8344-4c6e-bff3-c453bceeddd3",
      "timeStamp": "31-Mar-2023 04:50:08",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "27-Jun-2023 00:00:00",
        "arrivalDateTime": "08-Jul-2023 00:00:00",
        "departureCityId": "SEA",
        "arrivalCityId": "SEA",
        "duration": 11
      },
      "pos": {
        "id": 2250,
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
        },
        {
          "rph": 3,
          "ageGroup": "Adult"
        },
        {
          "rph": 4,
          "ageGroup": "Adult"
        }
      ],
      "cruise": {
        "packageId": 1312610,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13670
            }
          ]
        },
        "itinerary": {
          "id": 351639,
          "destination": {
            "id": 1
          }
        },
        "tourCode": "18707348",
        "voyage": {
          "departureDateTime": "01-Jul-2023 00:00:00",
          "arrivalDateTime": "08-Jul-2023 00:00:00",
          "departureCityId": "SEA",
          "arrivalCityId": "SEA",
          "code": "18506272"
        },
        "transportationType": 28
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
        "age": 31,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 2,
        "age": 30
      },
      {
        "rph": 3,
        "age": 30
      },
      {
        "rph": 4,
        "age": 40
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
