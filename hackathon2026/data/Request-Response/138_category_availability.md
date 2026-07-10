# Category Availability

**Path:** Create Reservation > Create Reservation With Combinable FareCodes > Category Availability

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
            "packageId": 1272011,
            "packageTourId": -1
        },
        "fareCodes": [
            {
                "code": "G0737880",
                "combinableFares": [
                    {
                        "code": "I7996069",
                        "type": 0,
                        "refundableType": 2
                    },
                    {
                        "code": "I7997687",
                        "type": 0,
                        "refundableType": 2
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
Date: Fri, 17 Feb 2023 16:23:29 GMT
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
      "requestId": "b5b4183e-dba7-46f1-b9f1-6f382ae5fa30",
      "timeStamp": "17-Feb-2023 11:23:27",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Apr-2023 00:00:00",
        "arrivalDateTime": "06-Apr-2023 00:00:00",
        "departureCityId": "XPC",
        "arrivalCityId": "XPC",
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1272011,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 79
            }
          ]
        },
        "itinerary": {
          "id": 311167,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "01-Apr-2023 00:00:00",
          "arrivalDateTime": "06-Apr-2023 00:00:00",
          "departureCityId": "XPC",
          "arrivalCityId": "XPC",
          "code": "MA05W388"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "VP",
          "type": 4,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1799,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 928.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 879,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "1B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1470,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1427,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 835.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 786.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 747.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1127,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1113,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 658.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 648.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "1K",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1456,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 729,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1070,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 629,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 970,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 913,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 539,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 529,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 529,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 508.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 885,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 842,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 479.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 459,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "2W",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2W",
              "fareCode": {
                "code": "I9072781",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 870,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 107.48,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
