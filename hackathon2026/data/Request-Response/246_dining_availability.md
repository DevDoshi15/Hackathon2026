# Dining Availability

**Path:** Create Reservation > RCCL switching to CruiseOnly when Cruise + Air is not available > Dining Availability

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
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "Post",
            "GateWayCity": {
                "id": "PTY" // flight departure city
            }
        },
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
            "packageId": 1317656,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "RL",
                "type": 4,
                "fare": {
                    "farecode": {
                        "code": "G0738129"
                    }
                },
                "cabins": [
                    {
                        "number": "8320"
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 35
        },
        {
            "rph": 2,
            "age": 35
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Mon, 08 May 2023 16:16:00 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "9d9e3aa4-7ac1-43a4-a56f-694c66cc3ace",
      "timeStamp": "08-May-2023 12:15:59",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "23-Jun-2023 00:00:00",
        "arrivalDateTime": "30-Jun-2023 00:00:00",
        "departureCityId": "SEA",
        "arrivalCityId": "SEA",
        "duration": 7
      },
      "pos": {
        "id": 2227,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "Any"
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
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1317656,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 13717
            }
          ]
        },
        "itinerary": {
          "id": 364268,
          "destination": {
            "id": 1
          }
        },
        "tourCode": "OV07A221",
        "voyage": {
          "departureDateTime": "23-Jun-2023 00:00:00",
          "arrivalDateTime": "30-Jun-2023 00:00:00",
          "departureCityId": "SEA",
          "arrivalCityId": "SEA",
          "code": "OV07A221"
        },
        "transportationType": 29
      },
      "dinings": [
        {
          "id": 1,
          "code": "M",
          "name": "05:00 PM",
          "status": 1,
          "tableSizeOptions": [],
          "gratuityRequired": false,
          "smokingInfo": {
            "allowed": false
          }
        },
        {
          "id": 2,
          "code": "2",
          "name": "07:45 PM",
          "status": 1,
          "tableSizeOptions": [],
          "gratuityRequired": false,
          "smokingInfo": {
            "allowed": false
          }
        },
        {
          "id": 24,
          "code": "O",
          "name": "MY TIME",
          "status": 1,
          "tableSizeOptions": [],
          "gratuityRequired": false,
          "smokingInfo": {
            "allowed": false
          }
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 35
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 35
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
