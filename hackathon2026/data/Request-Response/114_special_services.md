# Special Services

**Path:** Create Reservation > Create Reservation With Grats For Carnival > Special Services

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listSpecialservices`

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
Date: Mon, 20 Feb 2023 06:56:30 GMT
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
      "requestId": "767aa852-c050-4f96-a8a7-be2fc4f0a38f",
      "timeStamp": "20-Feb-2023 01:56:23",
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
      "serviceCollection": {
        "maxSelection": 5,
        "services": [
          {
            "code": "2",
            "name": "WheelchairAssistance",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "D",
            "name": "Diabetic",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "I",
            "name": "Blind",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "J",
            "name": "Deaf",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "O",
            "name": "Allergies",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "R",
            "name": "SharpsContainer",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "S",
            "name": "Dialysis",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "W",
            "name": "Wheelchair",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "Z",
            "name": "Oxygen",
            "description": "MED",
            "type": "Medical"
          },
          {
            "code": "F",
            "name": "Anniversary",
            "description": "OCC",
            "type": "Celebration",
            "associationType": "PAX",
            "dateRequired": true
          },
          {
            "code": "E",
            "name": "Birthday",
            "description": "OCC",
            "type": "Celebration",
            "dateRequired": true
          },
          {
            "code": "H",
            "name": "Honeymoon",
            "description": "OCC",
            "type": "Celebration",
            "associationType": "PAX"
          },
          {
            "code": "GRATS",
            "name": "PrePaidGratuities",
            "type": "PrePaidGratuities",
            "prices": [
              {
                "amount": 111.92,
                "breadownType": "TOTAL"
              }
            ]
          }
        ]
      }
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
