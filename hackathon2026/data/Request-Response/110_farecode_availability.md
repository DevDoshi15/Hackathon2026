# Farecode Availability

**Path:** Create Reservation > Create Reservation With Grats For Carnival > Farecode Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listfarecodes`

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
            "currency":"USD"
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
            "packageId": 1281377
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
Date: Fri, 17 Feb 2023 14:57:32 GMT
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
      "requestId": "11a1d9fe-eac6-4fb5-b2c0-2189a7d8d783",
      "timeStamp": "17-Feb-2023 09:57:21",
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
      "prices": [
        {
          "id": 3,
          "amount": 119.86
        },
        {
          "id": 2,
          "amount": 99
        }
      ],
      "insurances": [
        {
          "code": "I"
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
      "fareCodes": [
        {
          "code": "PNS",
          "name": "FUN SELECT",
          "description": "CPNS - UPGRADES MAY APPLY",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Public fare",
            "remarks": "CPNS - UPGRADES MAY APPLY",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "TB3",
          "name": "Senior Offer (SHOPv1)",
          "description": "CTB3 - NO UPGRADES APPLY",
          "bookOnline": true,
          "type": 1,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "CTB3 - NO UPGRADES APPLY"
          },
          "groups": [
            {}
          ]
        }
      ],
      "dinings": [
        {
          "id": 22,
          "code": "1",
          "name": "Early",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 11,
          "code": "2",
          "name": "Late Seating",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 44,
          "code": "O",
          "name": "Your Time Dining",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 21,
          "code": "U",
          "name": "Unassigned Seating",
          "status": 2,
          "tableSizeOptions": []
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
