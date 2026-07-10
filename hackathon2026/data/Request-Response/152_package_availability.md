# Package Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with Paid Transfer Package > Package Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listPackages`

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
            "id": "0",
            "currency": "USD"
        },
        "cruise": {
            "packageId": 1298928
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
        ],
        "customerReferences": [
            {
                "RPH": "1",
                "isPrimaryContact": true
            },
            {
                "RPH": "2"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "firstName": "John",
            "lastName": "Doe"
        },
        {
            "rph": 2,
            "age": 57,
            "firstName": "Maria",
            "lastName": "Doe"
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Thu, 09 Mar 2023 12:03:06 GMT
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
      "requestId": "0321bc97-c03b-4ad3-a733-3f1b90657c90",
      "timeStamp": "09-Mar-2023 07:03:04"
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
      "packages": [
        {
          "code": "B0TNOXFR",
          "description": "NO TRANSFER",
          "type": "PrePackage",
          "departureArrivalInfo": {},
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B0TYVR-AS",
          "description": "TRANSFER YVR AIRPORT/SHIP",
          "type": "PrePackage",
          "departureArrivalInfo": {},
          "prices": [
            {
              "id": 41,
              "amount": 29,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B01SEAYVRMTC",
          "description": "SEATTLE/VANCOUVER COACH",
          "type": "PrePackage",
          "departureArrivalInfo": {},
          "prices": [
            {
              "id": 41,
              "amount": 79,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B11YVRPAN",
          "description": "PAN PACIFIC VANCOUVER       - 1 NT",
          "type": "PrePackage",
          "departureArrivalInfo": {
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 279,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B11YVRVAN",
          "description": "FAIRMONT HOTEL VANCOUVER    - 1 NT",
          "type": "PrePackage",
          "departureArrivalInfo": {
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 239,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B21YVRPAN",
          "description": "PAN PACIFIC VANCOUVER       - 2 NTS",
          "type": "PrePackage",
          "departureArrivalInfo": {
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 458,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B21YVRVAN",
          "description": "FAIRMONT HOTEL VANCOUVER    - 2 NTS",
          "type": "PrePackage",
          "departureArrivalInfo": {
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 408,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B31YVRPAN",
          "description": "PAN PACIFIC VANCOUVER       - 3 NTS",
          "type": "PrePackage",
          "departureArrivalInfo": {
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 637,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B31YVRVAN",
          "description": "FAIRMONT HOTEL VANCOUVER    - 3 NTS",
          "type": "PrePackage",
          "departureArrivalInfo": {
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 577,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A0TNOXFR",
          "description": "NO TRANSFER",
          "type": "PostPackage",
          "departureArrivalInfo": {},
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A0TYVR-SA",
          "description": "TRANSFER SHIP/YVR AIRPORT",
          "type": "PostPackage",
          "departureArrivalInfo": {},
          "prices": [
            {
              "id": 41,
              "amount": 29,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A02YVRSEAMTC",
          "description": "VANCOUVER/SEATTLE COACH",
          "type": "PostPackage",
          "departureArrivalInfo": {},
          "prices": [
            {
              "id": 41,
              "amount": 79,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A12YVRPAN",
          "description": "PAN PACIFIC VANCOUVER       - 1 NT",
          "type": "PostPackage",
          "departureArrivalInfo": {
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 279,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A12YVRVAN",
          "description": "FAIRMONT HOTEL VANCOUVER    - 1 NT",
          "type": "PostPackage",
          "departureArrivalInfo": {
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 239,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A22YVRPAN",
          "description": "PAN PACIFIC VANCOUVER       - 2 NTS",
          "type": "PostPackage",
          "departureArrivalInfo": {
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 458,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A22YVRVAN",
          "description": "FAIRMONT HOTEL VANCOUVER    - 2 NTS",
          "type": "PostPackage",
          "departureArrivalInfo": {
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 408,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A32YVRPAN",
          "description": "PAN PACIFIC VANCOUVER       - 3 NTS",
          "type": "PostPackage",
          "departureArrivalInfo": {
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 637,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A32YVRVAN",
          "description": "FAIRMONT HOTEL VANCOUVER    - 3 NTS",
          "type": "PostPackage",
          "departureArrivalInfo": {
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 577,
              "type": "AVGPP"
            }
          ]
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "age": 52
      },
      {
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
