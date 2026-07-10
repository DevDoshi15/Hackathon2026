# Cabin Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with Paid Transfer Package > Cabin Availability

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
            "packageId": 1298928,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "MM",
                "fare": {
                    "fareCode": {
                        "code": "NH1"
                    }
                }
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
Date: Thu, 09 Mar 2023 12:04:16 GMT
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
      "requestId": "77f188a8-2ff9-46bc-a666-c241490edeff",
      "timeStamp": "09-Mar-2023 07:04:14",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Jun-2023 00:00:00",
        "arrivalDateTime": "14-Jun-2023 00:00:00",
        "departureCityId": "YVR",
        "arrivalCityId": "YVR",
        "duration": 7
      },
      "pos": {
        "id": 2111,
        "apiId": "Carnival",
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
        "packageId": 1298928,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 43
            }
          ]
        },
        "itinerary": {
          "id": 269387,
          "destination": {
            "id": 1
          }
        },
        "voyage": {
          "departureDateTime": "07-Jun-2023 00:00:00",
          "arrivalDateTime": "14-Jun-2023 00:00:00",
          "departureCityId": "YVR",
          "arrivalCityId": "YVR",
          "code": "V329"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "GUAR",
          "isGuarantee": true,
          "beds": [
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261
            },
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243
            }
          ],
          "location": "Inside",
          "occupancy": {
            "min": 0,
            "max": 2
          }
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
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
