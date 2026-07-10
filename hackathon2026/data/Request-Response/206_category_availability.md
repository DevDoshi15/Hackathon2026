# Category Availability

**Path:** Create Reservation > Occupancy Based Samples > Single Occupancy (NCL) > Category Availability

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
        "cruise": {
            "packageId": 1238898,
            "packageTourId": -1
        },
        "fareCodes": [
            {
                "code": "BESTFARE"
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
Date: Thu, 23 Mar 2023 12:03:06 GMT
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
      "requestId": "df48bd6e-4fca-4095-afa1-0c6b3a3ca5a3",
      "timeStamp": "23-Mar-2023 08:03:04",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "05-May-2023 00:00:00",
        "arrivalDateTime": "08-May-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 3
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
        }
      ],
      "cruise": {
        "packageId": 1238898,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 1179
            }
          ]
        },
        "itinerary": {
          "id": 363194,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "05-May-2023 00:00:00",
          "arrivalDateTime": "08-May-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "17183730"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "SE",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SE",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3715,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 419.4,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
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
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2649,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 291.48,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "BF",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BF",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2597,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 285.24,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "O4",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "O4",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1635,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 169.8,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "OA",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OA",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1609,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 166.68,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "OB",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OB",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1609,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 166.68,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "OC",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OC",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1583,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
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
            "guarantee": false
          }
        },
        {
          "code": "OD",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OD",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1557,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
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
            "guarantee": false
          }
        },
        {
          "code": "OF",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OF",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1557,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
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
            "guarantee": false
          }
        },
        {
          "code": "I4",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "I4",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1479,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 151.08,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
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
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1479,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 151.08,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "ID",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "ID",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1453,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 147.96,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "IF",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IF",
              "fareCode": {
                "code": "BESTFARE",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1427,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 199.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 144.84,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
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
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
