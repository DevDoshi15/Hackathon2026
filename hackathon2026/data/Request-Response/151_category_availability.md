# Category Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with Paid Transfer Package > Category Availability

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
            "packageId": 1298928
        },
        "fareCodes": [
            {
                "code": "NH1"
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
Date: Thu, 09 Mar 2023 12:02:28 GMT
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
      "requestId": "999260db-2974-4b9f-8aee-d6899351df33",
      "timeStamp": "09-Mar-2023 07:02:27",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Jun-2023 00:00:00",
        "arrivalDateTime": "14-Jun-2023 00:00:00",
        "departureCityId": "YVR",
        "arrivalCityId": "YVR",
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
      "cruise": {
        "packageId": 1298928,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 43
            }
          ]
        },
        "itinerary": {
          "id": 269387,
          "destination": {
            "id": 1
          }
        },
        "voyage": {
          "departureDateTime": "07-Jun-2023 00:00:00",
          "arrivalDateTime": "14-Jun-2023 00:00:00",
          "departureCityId": "YVR",
          "arrivalCityId": "YVR",
          "code": "V329"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "PS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "PS",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 6969,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 808.08,
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
          "code": "SA",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SA",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3238,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 360.36,
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
          "code": "SB",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SB",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3069,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 340.08,
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
          "code": "A",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "A",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1757,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 182.64,
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
          "code": "AA",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "AA",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1693,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 174.96,
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
          "code": "B",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "B",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1667,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 171.84,
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
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BB",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 163.68,
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
          "code": "BC",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BC",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 163.68,
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
          "code": "CA",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CA",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1399,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 139.68,
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
          "code": "C",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "C",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1013,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 93.36,
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
          "code": "D",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "D",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 997,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 91.44,
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
          "code": "DA",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "DA",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 981,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 89.52,
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
          "code": "DD",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "DD",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 965,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 87.6,
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
          "code": "E",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "E",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 948,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.56,
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
          "code": "EE",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "EE",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 932,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 83.64,
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
          "code": "F",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "F",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 915,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 81.6,
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
          "code": "FF",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "FF",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 79.68,
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
          "code": "G",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "G",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 713,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 57.36,
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
          "code": "H",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "H",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 699,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 55.68,
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
          "code": "HH",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "HH",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 699,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 55.68,
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
          "code": "I",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "I",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 43.68,
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
          "code": "J",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "J",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 589,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 42.48,
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
          "code": "K",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "K",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 579,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 41.28,
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
          "code": "L",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "L",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 569,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 40.08,
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
          "code": "M",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "M",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 559,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 38.88,
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
          "code": "MM",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "MM",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 549,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 37.68,
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
          "code": "N",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "N",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 549,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 320,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 235,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 37.68,
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
