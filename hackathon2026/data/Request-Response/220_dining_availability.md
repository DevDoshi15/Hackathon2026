# Dining Availability

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 3 (2 Adults + 1 Child) Kids Special Package (RCCL) > Dining Availability

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
            "packageId": 1269434,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "VP",
                "fare": {
                    "fareCode": {
                        "code": "I9610792"
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
            "age": 10
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
Date: Mon, 27 Mar 2023 11:10:13 GMT
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
  "advisories": [
    {
      "message": "No Dinings found for requested information",
      "type": "Error"
    }
  ],
  "data": {
    "trackingInfo": {
      "requestId": "800e8faa-9f95-49ea-b558-d2de119fa9f5",
      "timeStamp": "27-Mar-2023 07:10:11",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 4
      },
      "pos": {
        "id": 2227,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2B"
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
          "ageGroup": "Child"
        }
      ],
      "cruise": {
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 364180,
          "destination": {
            "id": 7
          }
        },
        "tourCode": "FR4BH098",
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
        },
        "transportationType": 29
      },
      "dinings": [
        {
          "id": 1,
          "code": "M",
          "name": "05:15 PM",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 2,
          "code": "2",
          "name": "08:00 PM",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 24,
          "code": "O",
          "name": "MY TIME",
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
        "age": 10
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
