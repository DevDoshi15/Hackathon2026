# Category Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with No Transfer Package > Category Availability

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
            "packageId": 1277420,
            "packageTourId": -1
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
Date: Mon, 06 Mar 2023 08:38:59 GMT
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
      "requestId": "a86099cb-b322-4e2f-8cc4-30e495c9c64c",
      "timeStamp": "06-Mar-2023 03:38:57",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Apr-2023 00:00:00",
        "arrivalDateTime": "09-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
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
        "packageId": 1277420,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 13250
            }
          ]
        },
        "itinerary": {
          "id": 311682,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "02-Apr-2023 00:00:00",
          "arrivalDateTime": "09-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "I330"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "PS",
          "type": 4,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "PS",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "SQ",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SQ",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3431,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 388.92,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 3299,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 373.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 3057,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 344.04,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "SC",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SC",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2849,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 319.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "SS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SS",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2342,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 258.24,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "SY",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SY",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2249,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 247.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "SZ",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SZ",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2249,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 247.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VQ",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VQ",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1059,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 104.28,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "V",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "V",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1029,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 100.68,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VA",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VA",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 97.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VB",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 969,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 93.48,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VC",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VC",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 939,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 89.88,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VD",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VD",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 909,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 86.28,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VE",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VE",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 879,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 82.68,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VF",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VF",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 849,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 79.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VH",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VH",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 849,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 79.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "CQ",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CQ",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 799,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 73.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 789,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 71.88,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 779,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 70.68,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 769,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 69.48,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 759,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.28,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 749,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 67.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 719,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 63.48,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 61.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 61.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "IQ",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IQ",
              "fareCode": {
                "code": "NH1",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 659,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 56.28,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 649,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 55.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 639,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 53.88,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 629,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.68,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 619,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 51.48,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 609,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 50.28,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 49.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
                  "amount": 599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 185,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 49.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
