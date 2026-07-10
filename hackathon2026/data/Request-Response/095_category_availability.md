# Category Availability

**Path:** Create Reservation > Create Reservation For Resident Farecodes Disney > Category Availability

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
            "packageId": 1310995,
            "packageTourId": -1
        },
        "fareCodes": [
            {
                "code": "FLR"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 32,
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
            "age": 32,
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
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
Date: Mon, 20 Feb 2023 07:24:38 GMT
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
      "requestId": "d3cb3046-f398-41bb-935a-ce79752a2909",
      "timeStamp": "20-Feb-2023 02:24:36",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Apr-2023 00:00:00",
        "arrivalDateTime": "12-Apr-2023 00:00:00",
        "departureCityId": "SAN",
        "arrivalCityId": "SAN",
        "duration": 5
      },
      "pos": {
        "id": 2110,
        "apiId": "Seaware",
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
        "packageId": 1310995,
        "packageTourId": -1,
        "cruiseline": {
          "id": 4,
          "ships": [
            {
              "id": 33
            }
          ]
        },
        "itinerary": {
          "id": 349515,
          "destination": {
            "id": 56
          }
        },
        "voyage": {
          "departureDateTime": "07-Apr-2023 00:00:00",
          "arrivalDateTime": "12-Apr-2023 00:00:00",
          "departureCityId": "SAN",
          "arrivalCityId": "SAN",
          "code": "DW2304075SD"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "07A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "07A",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2229.64,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "10B",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "10B",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1574.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "05B",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "05B",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2439.64,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "09C",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "09C",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1784.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "09A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "09A",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1984.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "10A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "10A",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1749.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "11B",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "11B",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1494.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "06A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "06A",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2319.64,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "05A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "05A",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2689.64,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "10C",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "10C",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1539.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "11A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "11A",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1519.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "09B",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "09B",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1809.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "05C",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "05C",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2374.64,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "09D",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "09D",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1749.6399999999999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "04E",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "04E",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2854.64,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "04A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "04A",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3084.64,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        },
        {
          "code": "04B",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "04B",
              "fareCode": {
                "code": "FLR",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2949.64,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 122.46,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 125,
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
        "rph": 1,
        "age": 32,
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
        "age": 32,
        "address": {
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
