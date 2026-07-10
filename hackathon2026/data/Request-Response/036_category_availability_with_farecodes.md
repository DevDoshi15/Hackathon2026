# Category Availability with FareCodes

**Path:** Category Availability > Category Availability with FareCodes

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
        "pos": { //Either id or currency is mandatory
            //"id": 1,
            "currency": "USD"
        },
        "customerReferences": [
            {
                "rph": 1,
                "isPrimaryContact": true // customer residency is required for the customer whose isPrimaryContact is true
            },
            {
                "rph": 2
            }
        ],
        "cruise": {
            "packageId": 1269434
        },
        "fareCodes": [
            {
                "code": "I9581957"
            },
            {
                "code": "I7996069"
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
Date: Wed, 01 Feb 2023 09:52:46 GMT
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
      "requestId": "c57c3685-655f-4089-b419-f3285ab2353c",
      "timeStamp": "01-Feb-2023 04:52:45",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 4
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 311051,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "RS",
          "type": 4,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "RS",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2641,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "OS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1339,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1339,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "GT",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1239,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1239,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "GS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1119,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1119,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "VP",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 889,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 889,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "J3",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 739,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 739,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "J4",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 718.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 718.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "WS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 699,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 699,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1056,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "3B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1027,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "2B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 599,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "4B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 588.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "CB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 578.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "1D",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 941,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "5D",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 884,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "2D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 529,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "4D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "XB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1K",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1170,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "1L",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 569,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 569,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "3M",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 856,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "4M",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 508.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 508.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "1N",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 770,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "3N",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 727,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "2N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "4N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "YO",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1Q",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 927,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "1R",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 548.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 548.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "CP",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "2T",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "1V",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 713,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "3V",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 641,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "2V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 378.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 378.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "4V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 368.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 368.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
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
          "code": "ZI",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 349,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 349,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
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
