# Fare Availability

**Path:** Modify Reservation > Insurance & Special Service - Princess Cruise line > Fare Availability

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
// for fetching insurance information, to sent in the Modify Booking request
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1316566
        }
    },
    "customers": [
        {
            "rph": 1,
            "age": 53
        },
        {
            "rph": 2,
            "age": 58
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
Date: Thu, 04 May 2023 11:04:13 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "70f707ab-7eed-4d09-966d-1f23bfa54d8c",
      "timeStamp": "04-May-2023 07:04:12",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Dec-2023 00:00:00",
        "arrivalDateTime": "04-Dec-2023 00:00:00",
        "departureCityId": "BNE",
        "arrivalCityId": "BNE",
        "duration": 3
      },
      "pos": {
        "id": 2198,
        "apiId": "Carnival",
        "officeId": "O212USTP17",
        "system": "Test",
        "currency": "USD",
        "type": "B2B"
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
      "insurances": [
        {
          "code": "F",
          "type": "Supplier"
        },
        {
          "code": "G",
          "type": "Supplier"
        }
      ],
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1316566,
        "packageTourId": -1,
        "cruiseline": {
          "id": 7,
          "ships": [
            {
              "id": 58
            }
          ]
        },
        "itinerary": {
          "id": 334555,
          "destination": {
            "id": 29
          }
        },
        "voyage": {
          "departureDateTime": "01-Dec-2023 00:00:00",
          "arrivalDateTime": "04-Dec-2023 00:00:00",
          "departureCityId": "BNE",
          "arrivalCityId": "BNE",
          "code": "6319"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "BNN",
          "name": "BEST AVAL NON-PAST PSG W/O AIR",
          "description": "EXCLUDES NON-REF FARES",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "EXCLUDES NON-REF FARES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "BNP",
          "name": "BEST AVAL PAST PSG W/O AIR",
          "description": "EXCLUDES NON-REF FARES",
          "type": 10,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "EXCLUDES NON-REF FARES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "NNN",
          "name": "BEST AVAL NON-PAST PSG W/O AIR",
          "description": "INCLUDES NON-REF FARES",
          "type": 0,
          "refundableType": 3,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "INCLUDES NON-REF FARES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "NNP",
          "name": "BEST AVAL PAST PSG W/O AIR",
          "description": "INCLUDES NON-REF FARES",
          "type": 10,
          "refundableType": 3,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "INCLUDES NON-REF FARES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "NL1",
          "name": "STANDARD PUBLIC FARE",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "specialFare": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "",
            "qualifierCodes": ""
          }
        },
        {
          "code": "NP1",
          "name": "Princess Plus",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": ""
          }
        },
        {
          "code": "NR3",
          "name": "Princess Premier",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": ""
          }
        },
        {
          "code": "NR5",
          "name": "PREMIER SSVS",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": ""
          }
        }
      ],
      "dinings": [
        {
          "id": 45,
          "code": "PCL8",
          "name": "Anytime Dining",
          "status": 1,
          "tableSizeOptions": [],
          "gratuityRequired": false
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 53
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 58
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
