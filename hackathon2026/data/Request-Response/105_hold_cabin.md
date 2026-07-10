# Hold Cabin

**Path:** Create Reservation > Create Reservation With Insurance > Hold Cabin

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/holdcabin`

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
            "packageId": 1324816
        },
        "addOns": [
            {
                "code": "EXP2B",
                "name": "Fantastica Experience Benefits",
                "description": "",
                "prices": [
                    {
                        "amount": 0.0,
                        "type": "AVGPP"
                    },
                    {
                        "amount": 0.0,
                        "type": "TOTAL"
                    }
                ],
                "startDate": "01-Apr-2023",
                "endDate": "01-Apr-2023",
                "type": 23,
                "autoInclude": true,
                "additionalCode": "636713325",
                "combinableCodes": []
            },
            {
                "code": "600",
                "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                "description": "",
                "prices": [
                    {
                        "amount": 0.0,
                        "type": "AVGPP"
                    },
                    {
                        "amount": 0.0,
                        "type": "TOTAL"
                    }
                ],
                "startDate": "01-Apr-2023",
                "endDate": "01-Apr-2023",
                "type": 6,
                "autoInclude": true,
                "additionalCode": "636713572",
                "combinableCodes": []
            }
        ],
        "categories": [
            {
                "code": "IR1",
                "fare": {
                    "fareCode": {
                        "code": "EZAT35DZE"
                    }
                },
                "cabins": [
                    {
                        "number": "10320"
                    }
                ]
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
Date: Fri, 17 Feb 2023 12:11:04 GMT
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
      "requestId": "65b7f189-1e45-4961-b120-cffcff70755c",
      "timeStamp": "17-Feb-2023 07:11:00",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Apr-2023 00:00:00",
        "arrivalDateTime": "08-Apr-2023 00:00:00",
        "departureCityId": "MRS",
        "arrivalCityId": "MRS",
        "duration": 7
      },
      "pos": {
        "id": 2119,
        "apiId": "MSC",
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
      "insurances": [
        {
          "code": "CSA2CP"
        }
      ],
      "cruise": {
        "packageId": 1324816,
        "packageTourId": -1,
        "cruiseline": {
          "id": 982,
          "ships": [
            {
              "id": 14091
            }
          ]
        },
        "itinerary": {
          "id": 362627,
          "destination": {
            "id": 18
          }
        },
        "voyage": {
          "departureDateTime": "01-Apr-2023 00:00:00",
          "arrivalDateTime": "08-Apr-2023 00:00:00",
          "departureCityId": "MRS",
          "arrivalCityId": "MRS",
          "code": "GR20230401MRSMRS"
        },
        "transportationType": 29
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
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
