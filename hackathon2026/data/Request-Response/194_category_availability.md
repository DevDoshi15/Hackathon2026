# Category Availability

**Path:** Create Reservation > Group Reservation > Norwegian Cruiseline > Category Availability

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
    "cruiseReservation": {
        "cruise": {
            "packageId": 1313262
        },
        "fareCodes": [
            {
                "code": "A1612559",
                "groups": [ // group code to be used for fetching the categories
                    {
                        "code": "A1612559"
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
Date: Wed, 15 Mar 2023 12:33:56 GMT
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
      "requestId": "dcbe113a-b656-4c49-afdb-b9f3dae091b2",
      "timeStamp": "15-Mar-2023 08:33:50",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "16-Dec-2023 00:00:00",
        "arrivalDateTime": "23-Dec-2023 00:00:00",
        "departureCityId": "XPC",
        "arrivalCityId": "XPC",
        "duration": 7
      },
      "pos": {
        "id": 2112,
        "apiId": "NCL",
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
        "packageId": 1313262,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13669
            }
          ]
        },
        "itinerary": {
          "id": 363167,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "16-Dec-2023 00:00:00",
          "arrivalDateTime": "23-Dec-2023 00:00:00",
          "departureCityId": "XPC",
          "arrivalCityId": "XPC",
          "code": "18439927"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "MA",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "MA",
              "fareCode": {
                "code": "A1612559",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "A1612559",
                    "type": 1
                  }
                ],
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1767,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 197.33,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 176.04,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 3,
            "guarantee": false
          }
        },
        {
          "code": "MB",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "MB",
              "fareCode": {
                "code": "A1612559",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "A1612559",
                    "type": 1
                  }
                ],
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1754,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 197.33,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 174.48,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 3,
            "guarantee": false
          }
        },
        {
          "code": "BA",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BA",
              "fareCode": {
                "code": "A1612559",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "A1612559",
                    "type": 1
                  }
                ],
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1663,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 197.33,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 163.56,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 3,
            "guarantee": false
          }
        },
        {
          "code": "BB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BB",
              "fareCode": {
                "code": "A1612559",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "A1612559",
                    "type": 1
                  }
                ],
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1650,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 197.33,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 162,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 3,
            "guarantee": false
          }
        },
        {
          "code": "BC",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BC",
              "fareCode": {
                "code": "A1612559",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "A1612559",
                    "type": 1
                  }
                ],
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1650,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 197.33,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 162,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 3,
            "guarantee": false
          }
        },
        {
          "code": "BD",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BD",
              "fareCode": {
                "code": "A1612559",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "A1612559",
                    "type": 1
                  }
                ],
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1637,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 197.33,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 160.44,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 3,
            "guarantee": false
          }
        },
        {
          "code": "IA",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IA",
              "fareCode": {
                "code": "A1612559",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "A1612559",
                    "type": 1
                  }
                ],
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1286,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 197.33,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 118.32,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 3,
            "guarantee": false
          }
        },
        {
          "code": "IB",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IB",
              "fareCode": {
                "code": "A1612559",
                "type": 0,
                "refundableType": 1,
                "groups": [
                  {
                    "code": "A1612559",
                    "type": 1
                  }
                ],
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1273,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 197.33,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 116.76,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 3,
            "guarantee": false
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
