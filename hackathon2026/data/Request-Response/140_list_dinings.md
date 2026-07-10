# List Dinings

**Path:** Create Reservation > Create Reservation With Combinable FareCodes > List Dinings

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
            "packageId": 1269619,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "2N",
                "fare": {
                    "fareCode": {
                        "code": "G0738129",
                        "combinableFares": [
                            {
                                "code": "I7996069",
                                "type": 0
                            },
                            {
                                "code": "I7997687",
                                "type": 0
                            }
                        ]
                    }
                },
                "cabins": [
                    {
                        "number": "2616"
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
Date: Fri, 17 Feb 2023 16:30:31 GMT
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
      "requestId": "621df00c-50d3-4c7c-871d-5d529bed58d6",
      "timeStamp": "17-Feb-2023 11:30:30",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Apr-2023 00:00:00",
        "arrivalDateTime": "10-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 3
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269619,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 1093
            }
          ]
        },
        "itinerary": {
          "id": 349022,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "07-Apr-2023 00:00:00",
          "arrivalDateTime": "10-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "LB3BH045"
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
