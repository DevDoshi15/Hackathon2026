# Hold Cabin

**Path:** Create Reservation > Create Reservation With AddOns > Hold Cabin

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
            "packageId": 1324816
        },
        "categories": [
            {
                "code": "IR1",
                "fare": {
                    "fareCode": {
                        "code": "EZAT35DZE"
                    }
                },
                "cabins": [
                    {
                        "number": "9068"
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
Date: Thu, 16 Mar 2023 10:01:45 GMT
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
      "requestId": "c4e00fc7-ee5a-412b-8d3f-ff3061c7d729",
      "timeStamp": "16-Mar-2023 06:01:42",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Apr-2023 00:00:00",
        "arrivalDateTime": "08-Apr-2023 00:00:00",
        "departureCityId": "MRS",
        "arrivalCityId": "MRS",
        "duration": 7
      },
      "reservationIndicators": {
        "modifyIndicators": [
          {
            "type": 2001,
            "value": false
          },
          {
            "type": 15,
            "value": false
          },
          {
            "type": 1001,
            "value": false
          },
          {
            "type": 6,
            "value": false
          }
        ],
        "mandatoryIndicators": [
          {
            "type": 2001,
            "value": true
          },
          {
            "type": "PhoneNumber",
            "value": true
          },
          {
            "type": "EMail",
            "value": true
          },
          {
            "type": "CitizenShip",
            "value": true
          }
        ]
      },
      "pos": {
        "id": 2119,
        "apiId": "MSC",
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
        "packageId": 1324816,
        "packageTourId": -1,
        "cruiseline": {
          "id": 982,
          "ships": [
            {
              "id": 14091
            }
          ]
        },
        "itinerary": {
          "id": 362627,
          "destination": {
            "id": 18
          }
        },
        "voyage": {
          "departureDateTime": "01-Apr-2023 00:00:00",
          "arrivalDateTime": "08-Apr-2023 00:00:00",
          "departureCityId": "MRS",
          "arrivalCityId": "MRS",
          "code": "GR20230401MRSMRS"
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
