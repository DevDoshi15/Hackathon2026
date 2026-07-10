# Category Availability

**Path:** Cabin Availability > Guaranteed Cabin Indicator > Category Availability

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
        "cruise": {
            "packageId": 1275651
        },
        "fareCodes": [
            {
                "code": "G0738129"
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
Date: Thu, 16 Mar 2023 14:38:48 GMT
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
      "requestId": "02fd73cd-716f-4665-ae4d-071baf9c8c33",
      "timeStamp": "16-Mar-2023 10:38:47",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "19-Mar-2023 00:00:00",
        "arrivalDateTime": "24-Mar-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 5
      },
      "pos": {
        "id": 2114,
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
        "packageId": 1275651,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 75
            }
          ]
        },
        "itinerary": {
          "id": 364197,
          "destination": {
            "id": 14
          }
        },
        "tourCode": "GR05W392",
        "voyage": {
          "departureDateTime": "19-Mar-2023 00:00:00",
          "arrivalDateTime": "24-Mar-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "GR05W392"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "RS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "RS",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1860
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2169,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 102.84,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 244.08,
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
          "code": "OS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1345
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1568.5,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 102.84,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 172.02,
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
          "code": "GT",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1165
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1358.5,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 102.84,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 146.82,
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
          "code": "GS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 1054
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1229,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 102.84,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 131.28,
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
          "code": "WS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 720
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 150
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 839,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 102.84,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 84.48,
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
          "code": "XB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 582
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 75
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 679,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 102.84,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 65.28,
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
          "code": "YO",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 402
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 469,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 102.84,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
            "guarantee": true
          }
        },
        {
          "code": "ZI",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "G0738129",
                "name": "BOGO60 NRD",
                "type": 0,
                "refundableType": 2,
                "status": 1,
                "details": {},
                "supplierRules": [
                  {
                    "description": "BOGO60 NRD",
                    "discountType": 2,
                    "amount": 368
                  },
                  {
                    "description": "BOGO60 NRD",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 50
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 102.84,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 35.28,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": true
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
