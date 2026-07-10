# Category Availability

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 4 – All Adults (NCL) > Category Availability

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
            "packageId": 1312610
        },
        "farecodes":[
            {
                "code":"BESTFARE"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 31,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 30
        },
        {
            "rph": 3,
            "age": 30
        },
        {
            "rph": 4,
            "age": 40
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
Date: Fri, 31 Mar 2023 08:48:53 GMT
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
      "requestId": "73c984ea-3a89-46d8-b784-d3d8928bcbd4",
      "timeStamp": "31-Mar-2023 04:48:49",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "27-Jun-2023 00:00:00",
        "arrivalDateTime": "08-Jul-2023 00:00:00",
        "departureCityId": "SEA",
        "arrivalCityId": "SEA",
        "duration": 11
      },
      "pos": {
        "id": 2250,
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
        },
        {
          "rph": 3,
          "ageGroup": "Adult"
        },
        {
          "rph": 4,
          "ageGroup": "Adult"
        }
      ],
      "cruise": {
        "packageId": 1312610,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13670
            }
          ]
        },
        "itinerary": {
          "id": 351639,
          "destination": {
            "id": 1
          }
        },
        "tourCode": "18707348",
        "voyage": {
          "departureDateTime": "01-Jul-2023 00:00:00",
          "arrivalDateTime": "08-Jul-2023 00:00:00",
          "departureCityId": "SEA",
          "arrivalCityId": "SEA",
          "code": "18506272"
        },
        "transportationType": 28
      },
      "categories": [
        {
          "code": "H5",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "H5",
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
                  "amount": 8710.5,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 1000.86,
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
          "code": "H6",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "H6",
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
                  "amount": 8873,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 1020.36,
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
          "code": "HB",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "HB",
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
                  "amount": 6598,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 747.36,
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
          "code": "HC",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "HC",
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
                  "amount": 6988,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 794.16,
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
          "code": "HG",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "HG",
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
                  "amount": 6208,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 700.56,
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
          "code": "M4",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "M4",
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
                  "amount": 3796.5,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 411.18,
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
          "code": "M6",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "M6",
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
                  "amount": 3887.5,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 422.1,
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
          "code": "MA",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "MA",
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
                  "amount": 3790,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 410.4,
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
          "code": "B4",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "B4",
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
                  "amount": 3686,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 397.92,
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
          "code": "B6",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "B6",
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
                  "amount": 3939.5,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 428.34,
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
          "code": "BB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BB",
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
                  "amount": 3705.5,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 400.26,
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
                  "amount": 3660,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 394.8,
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
          "code": "O5",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "O5",
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
                  "amount": 3530,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 379.2,
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
                  "amount": 3523.5,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 378.42,
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
                  "amount": 2958,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 310.56,
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
                  "amount": 2880,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 299.8,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 370,
                  "type": "AVGPP"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDADT"
                },
                {
                  "id": 1,
                  "amount": 2438,
                  "type": "ADDCHD"
                },
                {
                  "id": 98,
                  "amount": 301.2,
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
        "age": 31,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 2,
        "age": 30
      },
      {
        "rph": 3,
        "age": 30
      },
      {
        "rph": 4,
        "age": 40
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
