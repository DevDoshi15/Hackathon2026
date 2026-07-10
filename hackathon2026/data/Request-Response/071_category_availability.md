# Category Availability

**Path:** Create Reservation > Create Reservation With Air For SilverSea > Category Availability

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
{
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "NYC" // flight departure city
            }
        },
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
            "packageId": 1252535
        },
        "fareCode": [
            {
                "externalSessionInfo": {
                    "externalId": "03" // This is received in the response of ListFarecodes and need to be added to further messages
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "title": "MR",
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
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
            "title": "MR",
            "firstName": "Jack",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
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
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Fri, 10 Feb 2023 13:09:02 GMT
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
      "requestId": "b4936bfa-bc5b-47be-a102-7118f57f800a",
      "timeStamp": "10-Feb-2023 08:08:51",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "06-Mar-2023 00:00:00",
        "arrivalDateTime": "13-Mar-2023 00:00:00",
        "departureCityId": "SJU",
        "arrivalCityId": "BGI",
        "duration": 7
      },
      "pos": {
        "id": 2122,
        "apiId": "SSC",
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
      "cruise": {
        "packageId": 1252535,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8115,
          "ships": [
            {
              "id": 14717
            }
          ]
        },
        "itinerary": {
          "id": 291413,
          "destination": {
            "id": 9
          }
        },
        "voyage": {
          "departureDateTime": "06-Mar-2023 00:00:00",
          "arrivalDateTime": "13-Mar-2023 00:00:00",
          "departureCityId": "SJU",
          "arrivalCityId": "BGI",
          "code": "DA230306007"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "03",
          "name": "SILVER PRIVILEGE FARE",
          "description": "Air Promo included",
          "bookOnline": true,
          "externalSessionInfo": {
            "externalId": "03"
          },
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "Air Promo included",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 37
            }
          ]
        }
      ],
      "categories": [
        {
          "code": "G2",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "G2",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11900,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "S2",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "S2",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 9700,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "O1",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "O1",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 10600,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "G1",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "G1",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 9400,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "R1",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "R1",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8700,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "SL",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SL",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7500,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "DX",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "DX",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 5200,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "SV",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SV",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 5000,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "CV",
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CV",
              "fareCode": {
                "code": "03",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4900,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 154,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        }
      ]
    },
    "customers": [
      {
        "title": "MR",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
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
        "title": "MR",
        "rph": 2,
        "firstName": "Jack",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
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
