# Category Availability

**Path:** Modify Reservation > Create Reservation With Gratuities then Modify By Adding Insurance > Category Availability

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
        "cruise": {
            "packageId": 1307173,
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
Date: Thu, 04 May 2023 08:31:10 GMT
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
      "requestId": "bbe14878-8d0e-403a-a27f-849303026861",
      "timeStamp": "04-May-2023 04:31:05",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "15-Mar-2024 00:00:00",
        "arrivalDateTime": "22-Mar-2024 00:00:00",
        "departureCityId": "GLS",
        "arrivalCityId": "GLS",
        "duration": 7
      },
      "pos": {
        "id": 2250,
        "apiId": "NCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2B"
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
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1307173,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 15089
            }
          ]
        },
        "itinerary": {
          "id": 363332,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "15-Mar-2024 00:00:00",
          "arrivalDateTime": "22-Mar-2024 00:00:00",
          "departureCityId": "GLS",
          "arrivalCityId": "GLS",
          "code": "18440175"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 667460304,
          "code": "H2",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "H2",
              "status": 1,
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
                  "amount": 19824,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 2342.88,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460305,
          "code": "H3",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "H3",
              "status": 1,
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
                  "amount": 15118,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1778.16,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460306,
          "code": "H4",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "H4",
              "status": 1,
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
                  "amount": 9619,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1118.28,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460307,
          "code": "H5",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "H5",
              "status": 1,
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
                  "amount": 8709,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1009.08,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460308,
          "code": "H6",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "H6",
              "status": 1,
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
                  "amount": 8475,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 981,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460310,
          "code": "HB",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "HB",
              "status": 1,
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
                  "amount": 7149,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 821.88,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460309,
          "code": "HE",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "HE",
              "status": 1,
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
                  "amount": 6590,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 754.8,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460312,
          "code": "SH",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SH",
              "status": 1,
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
                  "amount": 5719,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 650.28,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460313,
          "code": "SI",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SI",
              "status": 1,
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
                  "amount": 5160,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 583.2,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460314,
          "code": "SJ",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SJ",
              "status": 1,
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
                  "amount": 5043,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 569.16,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460315,
          "code": "SK",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SK",
              "status": 1,
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
                  "amount": 4978,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 561.36,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460316,
          "code": "SL",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SL",
              "status": 1,
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
                  "amount": 4861,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 547.32,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460317,
          "code": "M2",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "M2",
              "status": 1,
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
                  "amount": 2846,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 305.52,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460318,
          "code": "M4",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "M4",
              "status": 1,
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
                  "amount": 2729,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
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
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460319,
          "code": "MA",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "MA",
              "status": 1,
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
                  "amount": 2664,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 283.68,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460320,
          "code": "MB",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "MB",
              "status": 1,
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
                  "amount": 2599,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 275.88,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460324,
          "code": "B9",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "B9",
              "status": 1,
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
                  "amount": 2183,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 225.96,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460322,
          "code": "B1",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "B1",
              "status": 1,
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
                  "amount": 2989,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 322.68,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460323,
          "code": "B4",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "B4",
              "status": 1,
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
                  "amount": 1806,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 180.72,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460325,
          "code": "BA",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "BA",
              "status": 1,
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
                  "amount": 1780,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 177.6,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460326,
          "code": "BB",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "BB",
              "status": 1,
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
                  "amount": 1754,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 174.48,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460327,
          "code": "BF",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "BF",
              "status": 1,
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
                  "amount": 1728,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 171.36,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667463301,
          "code": "O2",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "O2",
              "status": 1,
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
                  "amount": 1663,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
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
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460329,
          "code": "O4",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "O4",
              "status": 1,
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
                  "amount": 1663,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
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
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460330,
          "code": "OA",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "OA",
              "status": 1,
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
                  "amount": 1559,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
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
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460331,
          "code": "OB",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "OB",
              "status": 1,
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
                  "amount": 1494,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 143.28,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Outside"
          }
        },
        {
          "id": 667460333,
          "code": "I4",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "I4",
              "status": 1,
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
                  "amount": 1260,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 115.2,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Inside"
          }
        },
        {
          "id": 667460334,
          "code": "IA",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "IA",
              "status": 1,
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
                  "amount": 1260,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 115.2,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Inside"
          }
        },
        {
          "id": 667460335,
          "code": "IB",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "IB",
              "status": 1,
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
                  "amount": 1221,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 110.52,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Inside"
          }
        },
        {
          "id": 667460336,
          "code": "IF",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "IF",
              "status": 1,
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
                  "amount": 1195,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 163.38,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 107.4,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "Inside"
          }
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 52,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
