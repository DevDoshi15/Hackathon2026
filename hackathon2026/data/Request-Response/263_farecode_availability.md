# Farecode Availability

**Path:** Create Reservation > Create Reservation With Air For P&O Cruise line > Farecode Availability

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
{
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "MAN" // flight departure city
            }
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
            "packageId": 1501519
        }
    },
    "customers": [
         {
            "rph": 1,
            "age": 52,
            "address": {
                "country": {
                    "id": "GB"
                }
            }
        },
        {
            "rph": 2,
            "age": 57
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 08 Feb 2023 08:30:23 GMT
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
      "requestId": "6eef1570-cff4-49dd-ac5a-f65c8c7966a4",
      "timeStamp": "23-Jun-2026 07:11:46",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "03-Jun-2027 00:00:00",
        "arrivalDateTime": "10-Jun-2027 00:00:00",
        "departureCityId": "VLT",
        "arrivalCityId": "VLT",
        "duration": 7
      },
      "pos": {
        "id": 3487,
        "officeId": "O212GBTP17",
        "currency": "GBP",
        "type": "B2B",
        "system": "Test",
        "apiId": "Carnival"
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
        "currencyId": "GBP",
        "countryId": "GB"
      },
      "externalSessionInfo": {
        "externalId": "a@#$A721"
      },
      "type": "Cruise",
      "cruise": {
        "packageId": 1501519,
        "packageTourId": -1,
        "cruiseline": {
          "id": 16,
          "ships": [
            {
              "id": 13257,
              "code": "AZ"
            }
          ]
        },
        "voyage": {
          "departureDateTime": "03-Jun-2027 00:00:00",
          "arrivalDateTime": "10-Jun-2027 00:00:00",
          "departureCityId": "VLT",
          "arrivalCityId": "VLT",
          "code": "A721"
        },
        "itinerary": {
          "id": 433252,
          "destination": {
            "id": 51
          }
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "BYN",
          "name": "BEST AVAL NON-PAST PSG W/ AIR",
          "description": "EXCLUDES NON-REF FARES",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "EXCLUDES NON-REF FARES"
          }
        },
        {
          "code": "BYP",
          "name": "BEST AVAL PAST PSG W/ AIR",
          "description": "EXCLUDES NON-REF FARES",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "EXCLUDES NON-REF FARES"
          }
        },
        {
          "code": "NYN",
          "name": "BEST AVAL NON-PAST PSG W/ AIR",
          "description": "INCLUDES NON-REF FARES",
          "type": 0,
          "refundableType": 3,
          "dynamicRules": [
            {
              "type": 16
            }
          ],
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "INCLUDES NON-REF FARES"
          }
        },
        {
          "code": "NYP",
          "name": "BEST AVAL PAST PSG W/ AIR",
          "description": "INCLUDES NON-REF FARES",
          "type": 0,
          "refundableType": 3,
          "dynamicRules": [
            {
              "type": 16
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "INCLUDES NON-REF FARES"
          }
        },
        {
          "code": "KD1",
          "name": "SELECT PRICE - OBC",
          "description": "Available",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 1
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Available",
            "qualifierCodes": "",
            "validity": {
              "from": "01-Mar-2025",
              "to": "31-Dec-2027"
            }
          }
        },
        {
          "code": "KT1",
          "name": "SELECT BENEFIT CLASSIC OBC",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 1
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "",
            "validity": {
              "from": "18-Dec-2025",
              "to": "31-Dec-2027"
            }
          }
        },
        {
          "code": "KT5",
          "name": "SELECT BENEFIT DELUXE OBC",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 1
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "",
            "validity": {
              "from": "18-Dec-2025",
              "to": "31-Dec-2027"
            }
          }
        },
        {
          "code": "KU2",
          "name": "EARLY SAVER T AND C",
          "description": "Available",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 6
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Available",
            "validity": {
              "from": "01-Mar-2025",
              "to": "31-Dec-2027"
            }
          }
        },
        {
          "code": "KWW",
          "name": "EARLY SAVER CLASSIC PACKAGE",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 6
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "",
            "validity": {
              "from": "18-Dec-2025",
              "to": "31-Dec-2027"
            }
          }
        },
        {
          "code": "KWX",
          "name": "EARLY SAVER DELUXE PACKAGE",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 6
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "",
            "validity": {
              "from": "18-Dec-2025",
              "to": "31-Dec-2027"
            }
          }
        }
      ],
      "dinings": [
        {
          "id": 22,
          "code": "1",
          "name": "Early",
          "status": 1,
          "diningRoom": {
            "type": "FIRST SEATING"
          }
        },
        {
          "id": 11,
          "code": "2",
          "name": "Late Seating",
          "status": 1,
          "diningRoom": {
            "type": "SECOND SEATING"
          }
        },
        {
          "id": 3,
          "code": "8",
          "name": "Open Seating",
          "status": 1,
          "diningRoom": {
            "type": "Anytime Dining"
          }
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 52,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
