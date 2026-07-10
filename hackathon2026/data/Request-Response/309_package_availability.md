# Package Availability

**Path:** Modify Reservation > Packages - Princess Cruise line > Package Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listpackages`

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
        "cruise": {
            "packageId": 1316566
        },
        "categories": [
            {
                "code": "M1",
                "fare": {
                    "fareCode": {
                        "code": "NR3"
                    }
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970"
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965"
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
Date: Thu, 04 May 2023 14:16:12 GMT
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
      "requestId": "83b79246-0bf4-4258-b811-395b823f704e",
      "timeStamp": "04-May-2023 10:16:06",
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
      "packages": [
        {
          "code": "B0TNOXFR",
          "description": "NO TRANSFER",
          "type": "PrePackage",
          "status": 1,
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
          "code": "B0TBNE-AS",
          "description": "TRANSFER: AIRPORT 3UTBNE-AS",
          "type": "PrePackage",
          "status": 1,
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
          "code": "B11BNEFPB",
          "description": "FOUR POINTS BRISBA3U1BNEFPB - 1 NT",
          "type": "PrePackage",
          "status": 1,
          "departureArrivalInfo": {
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 199,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B21BNEFPB",
          "description": "FOUR POINTS BRISBA3U1BNEFPB - 2 NTS",
          "type": "PrePackage",
          "status": 1,
          "departureArrivalInfo": {
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 288,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B31BNEFPB",
          "description": "FOUR POINTS BRISBA3U1BNEFPB - 3 NTS",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 377,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A0TNOXFR",
          "description": "NO TRANSFER",
          "type": "PostPackage",
          "status": 1,
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
          "code": "A0TBNE-SA",
          "description": "TRANSFER: SHIP TO 3UTBNE-SA",
          "type": "PostPackage",
          "status": 1,
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
          "code": "A12BNEFPB",
          "description": "FOUR POINTS BRISBA3U2BNEFPB - 1 NT",
          "type": "PostPackage",
          "status": 1,
          "departureArrivalInfo": {
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 199,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A22BNEFPB",
          "description": "FOUR POINTS BRISBA3U2BNEFPB - 2 NTS",
          "type": "PostPackage",
          "status": 1,
          "departureArrivalInfo": {
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 288,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A32BNEFPB",
          "description": "FOUR POINTS BRISBA3U2BNEFPB - 3 NTS",
          "type": "PostPackage",
          "status": 1,
          "departureArrivalInfo": {
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 377,
              "type": "AVGPP"
            }
          ]
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970"
      },
      {
        "gender": "Male",
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965"
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
