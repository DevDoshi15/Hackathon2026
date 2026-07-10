# Special Services

**Path:** Modify Reservation > Insurance & Special Service - Princess Cruise line > Special Services

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listSpecialservices`

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
                "code": "S5",
                "fare": {
                    "fareCode": {
                        "code": "NR3"
                    }
                },
                "cabins": [
                    {
                        "number": "D420"
                    }
                ]
            }
        ]
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
Date: Thu, 04 May 2023 11:03:51 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "5af9a931-c367-4bdf-9d48-5c81ce9311eb",
      "timeStamp": "04-May-2023 07:03:49",
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
      "serviceCollection": {
        "services": [
          {
            "code": "1000",
            "description": "OCC",
            "type": "Anniversary",
            "associationType": "PAX",
            "dateRequired": true,
            "group": "Celebration"
          },
          {
            "code": "1001",
            "description": "OCC",
            "type": "Birthday",
            "dateRequired": true,
            "group": "Celebration"
          },
          {
            "code": "1002",
            "description": "OCC",
            "type": "Graduation",
            "dateRequired": true,
            "group": "Celebration"
          },
          {
            "code": "1003",
            "description": "OCC",
            "type": "Honeymoon",
            "associationType": "PAX",
            "group": "Celebration"
          },
          {
            "code": "1004",
            "description": "OCC",
            "type": "Retirement",
            "dateRequired": true,
            "group": "Celebration"
          },
          {
            "code": "Y",
            "name": "Yes",
            "type": "UPG",
            "associationType": "PAX",
            "group": "ComplimentaryUpgrade"
          },
          {
            "code": "N",
            "name": "No",
            "type": "UPG",
            "associationType": "PAX",
            "group": "ComplimentaryUpgrade"
          }
        ]
      }
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
