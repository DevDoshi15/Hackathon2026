# Farecode Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with No Transfer Package > Farecode Availability

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
            "packageId": 1277420
        }
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                },
                "city": {
                    "id": "MIA"
                }
            }
        },
        {
            "rph": 2,
            "age": 57,
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                },
                "city": {
                    "id": "MIA"
                }
            }
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
Date: Mon, 06 Mar 2023 08:38:44 GMT
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
      "requestId": "d2530667-c2ee-4a14-bcc2-6e712c129667",
      "timeStamp": "06-Mar-2023 03:38:43",
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
      "insurances": [
        {
          "code": "S"
        },
        {
          "code": "P"
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
      "fareCodes": [
        {
          "code": "BNN",
          "name": "BEST AVAL NON-PAST PSG W/O AIR",
          "description": "EXCLUDES NON-REF FARES",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "EXCLUDES NON-REF FARES",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "NNN",
          "name": "BEST AVAL NON-PAST PSG W/O AIR",
          "description": "INCLUDES NON-REF FARES",
          "bookOnline": true,
          "type": 0,
          "refundableType": 3,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "INCLUDES NON-REF FARES",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "NH1",
          "name": "ADVANTAGE FARES",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "N11",
          "name": "HAVE IT ALL",
          "description": "",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
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
          ]
        },
        {
          "code": "QF1",
          "name": "FLASH SPECIALS NON-REFUNDABLE",
          "description": "NON-REFUNDABLE FARE",
          "bookOnline": true,
          "type": 0,
          "refundableType": 3,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "NON-REFUNDABLE FARE",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        }
      ],
      "dinings": [
        {
          "id": 8,
          "code": "3",
          "name": "Early Seating Upper Level 5:45 PM",
          "status": 1,
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
        "age": 52,
        "address": {
          "city": {
            "id": "MIA"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      },
      {
        "rph": 2,
        "age": 57,
        "address": {
          "city": {
            "id": "MIA"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
