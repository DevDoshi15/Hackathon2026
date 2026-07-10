# Farecode Availability

**Path:** Cabin Availability > Obstructed Cabin Indicator > Farecode Availability

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
            "currency": "USD"
        },
        "cruise": {
            "packageId": 1346847
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
Date: Thu, 16 Mar 2023 14:37:37 GMT
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
      "requestId": "3ff4b747-8b8b-44ee-827a-6e4fbbbafd10",
      "timeStamp": "16-Mar-2023 10:37:34",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "11-May-2023 00:00:00",
        "arrivalDateTime": "15-May-2023 00:00:00",
        "departureCityId": "SIN",
        "arrivalCityId": "SIN",
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
        "packageId": 1346847,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 14118
            }
          ]
        },
        "itinerary": {
          "id": 364263,
          "destination": {
            "id": 51
          }
        },
        "tourCode": "SC04I770",
        "voyage": {
          "departureDateTime": "11-May-2023 00:00:00",
          "arrivalDateTime": "15-May-2023 00:00:00",
          "departureCityId": "SIN",
          "arrivalCityId": "SIN",
          "code": "SC04I770"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "BESTRATE",
          "name": "Best Rate",
          "description": "Restrictions May Apply",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          }
        },
        {
          "code": "I9604813",
          "name": "BROCHURE",
          "description": "BROCHURE PRICE",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          }
        },
        {
          "code": "I9604829",
          "name": "STANDARD",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD"
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
