# Dining Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with Paid Transfer Package > Dining Availability

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
                },
                "cabins": [
                    {
                        "number": "GUAR"
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
Date: Thu, 09 Mar 2023 12:05:04 GMT
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
      "requestId": "0a7ea14c-8fdc-4b78-9fff-2d09c415caf4",
      "timeStamp": "09-Mar-2023 07:05:03",
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
      "dinings": [
        {
          "id": 8,
          "code": "3",
          "name": "Early Seating Upper Level 5:45 PM",
          "status": 2,
          "tableSizeOptions": []
        },
        {
          "id": 7,
          "code": "4",
          "name": "Early Seating Lower Level 6:15 PM",
          "status": 3,
          "tableSizeOptions": []
        },
        {
          "id": 16,
          "code": "5",
          "name": "Main Seating Upper Level 8:00PM",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 15,
          "code": "6",
          "name": "Main Seating Lower Level 8:30PM",
          "status": 3,
          "tableSizeOptions": []
        },
        {
          "id": 3,
          "code": "8",
          "name": "Open Seating",
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
