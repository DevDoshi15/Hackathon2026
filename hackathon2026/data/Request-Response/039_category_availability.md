# Category Availability

**Path:** Cabin Availability > Obstructed Cabin Indicator > Category Availability

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
            "packageId": 1346847
        },
        "fareCodes": [
            {
                "code": "I9604829"
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
Date: Thu, 16 Mar 2023 14:37:10 GMT
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
      "requestId": "485edca8-8b78-48e8-ac7c-deddaca8573f",
      "timeStamp": "16-Mar-2023 10:37:09",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "11-May-2023 00:00:00",
        "arrivalDateTime": "15-May-2023 00:00:00",
        "departureCityId": "SIN",
        "arrivalCityId": "SIN",
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
          "ageGroup": "Adult",
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
        }
      ],
      "cruise": {
        "packageId": 1346847,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 14118
            }
          ]
        },
        "itinerary": {
          "id": 364263,
          "destination": {
            "id": 51
          }
        },
        "tourCode": "SC04I770",
        "voyage": {
          "departureDateTime": "11-May-2023 00:00:00",
          "arrivalDateTime": "15-May-2023 00:00:00",
          "departureCityId": "SIN",
          "arrivalCityId": "SIN",
          "code": "SC04I770"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "US",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "US",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 15007,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1788.84,
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
          "code": "GL",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GL",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 5676,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 669.12,
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
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3841,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 448.92,
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
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2126,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 243.12,
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
          "code": "J1",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "J1",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1562,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 175.44,
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
          "code": "J4",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1321,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 146.52,
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
              "status": 2,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 2,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 981,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
          "code": "XS",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "XS",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 2,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1632,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
          "code": "1C",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1C",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1032,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 111.84,
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
          "code": "3C",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "3C",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1032,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 111.84,
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
          "code": "2C",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2C",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1003,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 108.36,
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
          "code": "4C",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4C",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1039,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 112.68,
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
          "code": "CB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 996,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 107.52,
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
          "code": "1D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1053,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 114.36,
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
          "code": "3D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "3D",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1010,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 109.2,
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
          "code": "5D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1010,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 109.2,
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
          "code": "2D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 982,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 105.84,
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
          "code": "4D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 982,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 105.84,
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
          "code": "1E",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1E",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 967,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 104.04,
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
          "code": "2E",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 935,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 100.2,
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
          "code": "2F",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2F",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 2,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 882,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
          "code": "XB",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 2,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 853,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
          "code": "3M",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 832,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 87.84,
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
          "code": "4M",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 808,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 84.96,
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
          "code": "1N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 853,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 90.36,
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
          "code": "2N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 818,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 86.16,
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
          "code": "YO",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 2,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 705,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
          "code": "CI",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CI",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 720,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 74.4,
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
          "code": "1U",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1U",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 791,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 82.92,
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
          "code": "2U",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2U",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 791,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 82.92,
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
          "code": "1V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 791,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 82.92,
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
          "code": "3V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 791,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 82.92,
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
          "code": "2V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 748,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 77.76,
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
          "code": "4V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 720,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 74.4,
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
          "code": "2W",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2W",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 2,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 720,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
          "code": "ZI",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I9604829",
                "type": 0,
                "refundableType": 1,
                "status": 2,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 663,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 55.93,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 100,
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
