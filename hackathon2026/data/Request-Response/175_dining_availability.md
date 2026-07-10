# Dining Availability

**Path:** Create Reservation > Create Reservation With Transfer (Pre/Post Airport Transfer) > Dining Availability

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
            "packageId": 1269292
        },
        "categories": [
            {
                "code": "4V",
                "fare": {
                    "fareCode": {
                        "code": "I0452040"
                    }
                },
                "cabins": [
                    {
                        "number": "8671"
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
Date: Mon, 06 Mar 2023 10:10:27 GMT
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
      "requestId": "b511b973-f8fb-4042-a154-c93f07dda0c5",
      "timeStamp": "06-Mar-2023 05:10:18",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "30-Mar-2023 00:00:00",
        "arrivalDateTime": "03-Apr-2023 00:00:00",
        "departureCityId": "GLS",
        "arrivalCityId": "GLS",
        "duration": 4
      },
      "pos": {
        "id": 2114,
        "apiId": "RCCL",
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
        "packageId": 1269292,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 71
            }
          ]
        },
        "itinerary": {
          "id": 355501,
          "destination": {
            "id": 14
          }
        },
        "tourCode": "AD04W115",
        "voyage": {
          "departureDateTime": "30-Mar-2023 00:00:00",
          "arrivalDateTime": "03-Apr-2023 00:00:00",
          "departureCityId": "GLS",
          "arrivalCityId": "GLS",
          "code": "AD04W115"
        },
        "transportationType": 29
      },
      "dinings": [
        {
          "id": 1,
          "code": "M",
          "name": "05:30 PM",
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
