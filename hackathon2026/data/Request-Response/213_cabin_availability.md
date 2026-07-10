# Cabin Availability

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 3 (2 Adults + 1 Child) (RCCL) > Cabin Availability

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
//This request contains only mandatory elements
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1269434,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "ZI",
                "fare": {
                    "fareCode": {
                        "code": "I0507023"
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
Date: Mon, 27 Mar 2023 08:49:29 GMT
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
      "requestId": "73d948e9-c34b-49e5-9cb5-fd85ecefcb88",
      "timeStamp": "27-Mar-2023 04:49:28",
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
      "reservationIndicators": {
        "modifyIndicators": [
          {
            "type": 6,
            "value": false
          },
          {
            "type": 9,
            "value": false
          },
          {
            "type": 11,
            "value": false
          },
          {
            "type": 12,
            "value": false
          },
          {
            "type": 14,
            "value": false
          },
          {
            "type": 15,
            "value": false
          },
          {
            "type": 16,
            "value": false
          },
          {
            "type": 45,
            "value": false
          },
          {
            "type": 600,
            "value": false
          },
          {
            "type": 700,
            "value": false
          },
          {
            "type": 1001,
            "value": false
          }
        ],
        "mandatoryIndicators": [
          {
            "type": "CitizenShip",
            "value": true
          },
          {
            "type": "Insurance",
            "value": true
          },
          {
            "type": "Age",
            "value": true
          },
          {
            "type": "Title",
            "value": true
          },
          {
            "type": "Gender",
            "value": true
          },
          {
            "type": "PhoneNumber",
            "value": true
          },
          {
            "type": "DiningSeating",
            "value": true
          },
          {
            "type": "TableSize",
            "value": true
          },
          {
            "type": "FlightInformation",
            "value": true
          },
          {
            "type": 700,
            "value": true
          },
          {
            "type": "EMail",
            "value": true
          }
        ]
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
      "cabins": [
        {
          "number": "GTY",
          "isGuarantee": true,
          "beds": [
            {
              "code": "A",
              "name": "",
              "description": "Apart",
              "type": 281
            },
            {
              "code": "T",
              "name": "",
              "description": "Together",
              "type": 282
            }
          ]
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
