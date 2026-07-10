# Category Availability

**Path:** Cabin Availability > Location > Category Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listCategories`

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
            "packageId": 1310045
        },
        "fareCodes": [
            {
                "code": "BESTPRICE"
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
                },
                "state": {
                    "id": "FL"
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
Date: Thu, 16 Mar 2023 14:31:55 GMT
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
      "requestId": "45aab465-c368-4b7f-9076-740215160a40",
      "timeStamp": "16-Mar-2023 10:31:51",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Apr-2023 00:00:00",
        "arrivalDateTime": "08-Apr-2023 00:00:00",
        "departureCityId": "PIRA",
        "arrivalCityId": "PIRA",
        "duration": 7
      },
      "pos": {
        "id": 2131,
        "apiId": "Seaware",
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
        "packageId": 1310045,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8224,
          "ships": [
            {
              "id": 14065
            }
          ]
        },
        "itinerary": {
          "id": 364154,
          "destination": {
            "id": 16
          }
        },
        "voyage": {
          "departureDateTime": "01-Apr-2023 00:00:00",
          "arrivalDateTime": "08-Apr-2023 00:00:00",
          "departureCityId": "PIRA",
          "arrivalCityId": "PIRA",
          "code": "CC07230401-NP"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "S",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "S",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1270,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "XB",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 940,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "SB",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SB",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1520,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "IC",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IC",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 810,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "XA",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XA",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 850,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "IB",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IB",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 760,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "XBO",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XBO",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 850,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "IA",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IA",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 690,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "XD",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XD",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1040,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
            }
          ]
        },
        {
          "code": "XC",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XC",
              "fareCode": {
                "code": "BESTPRICE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 990,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ]
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
          },
          "state": {
            "id": "FL"
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
