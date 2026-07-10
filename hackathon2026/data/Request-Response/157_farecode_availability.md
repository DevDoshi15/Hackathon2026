# Farecode Availability

**Path:** Create Reservation > Create Reservation With Packages > Auto-Inclusion of Packages > Create Reservation WITH DoNotAutoIncludePackages Preference > Farecode Availability

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
            "packageId": 1353443
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
Date: Fri, 03 Nov 2023 08:13:07 GMT
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
      "requestId": "d565c025-b1f0-412f-bf48-7b1f22d05b54",
      "timeStamp": "03-Nov-2023 04:13:05",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "03-Feb-2024 00:00:00",
        "arrivalDateTime": "10-Feb-2024 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 7
      },
      "pos": {
        "id": 2519,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "Any",
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
      "insurances": [
        {
          "code": "S",
          "type": "Supplier"
        },
        {
          "code": "P",
          "type": "Supplier"
        }
      ],
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1353443,
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
          "id": 370945,
          "destination": {
            "id": 9
          }
        },
        "voyage": {
          "departureDateTime": "03-Feb-2024 00:00:00",
          "arrivalDateTime": "10-Feb-2024 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "I416"
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
          "code": "NH1",
          "name": "ADVANTAGE FARES",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "qualifierCodes": "",
            "validity": {
              "from": "01-Jan-2022",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "NH2",
          "name": "SUS SCENARIO 9.2",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "validity": {
              "from": "01-Jan-2023",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "NH3",
          "name": "SUS SCENARIO 9.3",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "validity": {
              "from": "01-Jan-2022",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "NH4",
          "name": "SUS SCENARIO 9.4",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "validity": {
              "from": "01-Jan-2022",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "N11",
          "name": "HAVE IT ALL",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 2
            },
            {
              "type": 3
            },
            {
              "type": 18
            },
            {
              "type": 4
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "",
            "qualifierCodes": "",
            "validity": {
              "from": "01-Jan-2019",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "QA1",
          "name": "NON-REFUNDABLE DEPOSIT",
          "description": "NON-REFUNDABLE FARE",
          "type": 0,
          "refundableType": 2,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "NON-REFUNDABLE FARE",
            "qualifierCodes": "",
            "validity": {
              "from": "01-Jan-2022",
              "to": "04-Nov-2023"
            }
          }
        }
      ],
      "dinings": [
        {
          "id": 8,
          "code": "3",
          "name": "Early Seating Upper Level 5:45 PM",
          "status": 1,
          "diningRoom": {
            "type": "Early Upper Dining"
          }
        },
        {
          "id": 16,
          "code": "5",
          "name": "Main Seating Upper Level 8:00PM",
          "status": 1,
          "diningRoom": {
            "type": "Main Upper Dining"
          }
        },
        {
          "id": 3,
          "code": "8",
          "name": "Open Seating",
          "status": 1,
          "diningRoom": {
            "type": "Open Seating"
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
