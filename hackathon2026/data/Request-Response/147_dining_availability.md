# Dining Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with No Transfer Package > Dining Availability

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
            "packageId": 1277420,
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
                        "number": "8146"
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
Date: Mon, 06 Mar 2023 08:40:33 GMT
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
      "requestId": "54423a5b-849f-4a52-9022-5d8b7bdc8db3",
      "timeStamp": "06-Mar-2023 03:40:30",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Apr-2023 00:00:00",
        "arrivalDateTime": "09-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
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
        "packageId": 1277420,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 13250
            }
          ]
        },
        "itinerary": {
          "id": 311682,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "02-Apr-2023 00:00:00",
          "arrivalDateTime": "09-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "I330"
        },
        "transportationType": 29
      },
      "dinings": [
        {
          "id": 8,
          "code": "3",
          "name": "Early Seating Upper Level 5:45 PM",
          "status": 1,
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
