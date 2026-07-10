# Category Availability

**Path:** Cabin Details > Cabin Position & Remarks > Category Availability

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
            "packageId": 1282255
        },
        "fareCodes": [
            {
                "code": "H8212136"
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
Date: Thu, 16 Mar 2023 14:44:32 GMT
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
      "requestId": "783a8ce8-d092-42f0-9aa1-1d9a08607db2",
      "timeStamp": "16-Mar-2023 10:44:30",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "09-Apr-2023 00:00:00",
        "arrivalDateTime": "16-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 7
      },
      "pos": {
        "id": 2109,
        "apiId": "RCCL",
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
        "packageId": 1282255,
        "packageTourId": -1,
        "cruiseline": {
          "id": 2,
          "ships": [
            {
              "id": 14948
            }
          ]
        },
        "itinerary": {
          "id": 364303,
          "destination": {
            "id": 14
          }
        },
        "tourCode": "BY07W480",
        "voyage": {
          "departureDateTime": "09-Apr-2023 00:00:00",
          "arrivalDateTime": "16-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "BY07W480"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "A1",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "A1",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 714
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2974,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 439.84,
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
          "code": "A2",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "A2",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 694
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2874,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 423.84,
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
          "code": "XA",
          "type": 3,
          "fares": [
            {
              "status": 13,
              "upgradeFrom": "XA",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 1,
                "status": 13,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 694
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2874,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
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
          "code": "C1",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "C1",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 654
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2674,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 391.84,
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
          "code": "C2",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "C2",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 634
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2574,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 375.84,
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
          "code": "C3",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "C3",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 614
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2474,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 359.84,
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
          "code": "XC",
          "type": 3,
          "fares": [
            {
              "status": 13,
              "upgradeFrom": "XC",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 1,
                "status": 13,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 614
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2474,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
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
          "code": "E1",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "E1",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 592
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2364,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 342.24,
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
          "code": "E2",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "E2",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 582
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2314,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 334.24,
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
          "code": "E3",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "E3",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 578
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2294,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 331.04,
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
          "code": "E4",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "E4",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 574
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2274,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 327.84,
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
          "code": "E5",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "E5",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 574
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2274,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 327.84,
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
          "code": "EX",
          "type": 3,
          "fares": [
            {
              "status": 13,
              "upgradeFrom": "EX",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 1,
                "status": 13,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 574
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2274,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
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
          "code": "SV",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "SV",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 558
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2194,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 315.04,
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
          "code": "P1",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "P1",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 554
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2174,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 311.84,
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
          "code": "P2",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "P2",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 544
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2124,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 303.84,
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
          "code": "X",
          "type": 3,
          "fares": [
            {
              "status": 13,
              "upgradeFrom": "X",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 1,
                "status": 13,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 544
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2124,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
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
          "code": "PO",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "PO",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 522
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2014,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 286.24,
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
          "code": "06",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "06",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 518
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1994,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 283.04,
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
          "code": "07",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "07",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 508
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1944,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 275.04,
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
          "code": "08",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "08",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 504
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1924,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 271.84,
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
          "code": "Y",
          "type": 2,
          "fares": [
            {
              "status": 13,
              "upgradeFrom": "Y",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 1,
                "status": 13,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 504
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1924,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
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
          "code": "09",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "09",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 476
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1784,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 249.44,
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
          "code": "10",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "10",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 472
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1764,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 246.24,
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
          "code": "11",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "11",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 468
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1744,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 243.04,
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
          "code": "12",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "12",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 464
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1724,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 239.84,
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
          "code": "Z",
          "type": 1,
          "fares": [
            {
              "status": 13,
              "upgradeFrom": "Z",
              "fareCode": {
                "code": "H8212136",
                "name": "ALWAYS INC NRD",
                "type": 0,
                "refundableType": 1,
                "status": 13,
                "details": {},
                "supplierRules": [
                  {
                    "description": "ALWAYS INC NRD",
                    "discountType": 2,
                    "amount": 464
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1724,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 166.88,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 225,
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
