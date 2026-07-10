# Category Availability

**Path:** Create Reservation > Create Reservation With Grats For Carnival > Category Availability

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
            "packageId": 1281377,
            "packageTourId": -1
        }
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
Date: Fri, 17 Feb 2023 14:58:14 GMT
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
      "requestId": "9cdd7aa6-be24-46fa-b2e6-00c9558417f2",
      "timeStamp": "17-Feb-2023 09:58:00",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-May-2023 00:00:00",
        "arrivalDateTime": "05-May-2023 00:00:00",
        "departureCityId": "LAX",
        "arrivalCityId": "LAX",
        "duration": 4
      },
      "pos": {
        "id": 2108,
        "apiId": "Carnival",
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
        "packageId": 1281377,
        "packageTourId": -1,
        "cruiseline": {
          "id": 1,
          "ships": [
            {
              "id": 14383
            }
          ]
        },
        "itinerary": {
          "id": 303143,
          "destination": {
            "id": 55
          }
        },
        "voyage": {
          "departureDateTime": "01-May-2023 00:00:00",
          "arrivalDateTime": "05-May-2023 00:00:00",
          "departureCityId": "LAX",
          "arrivalCityId": "LAX",
          "code": "20230501RD04"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "PNS",
          "name": "FUN SELECT",
          "description": "CPNS - UPGRADES MAY APPLY",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Public fare",
            "remarks": "CPNS - UPGRADES MAY APPLY",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "TB3",
          "name": "Senior Offer (SHOPv1)",
          "description": "CTB3 - NO UPGRADES APPLY",
          "bookOnline": true,
          "type": 1,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "CTB3 - NO UPGRADES APPLY"
          },
          "groups": [
            {}
          ]
        }
      ],
      "categories": [
        {
          "code": "CS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CS",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3160,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CS",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1869,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "ES",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "ES",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2700,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "ES",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1409,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2450,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1159,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2000,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 709,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "9C",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "9C",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1801,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "9C",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 615,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8S",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8S",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1640,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "8S",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 454,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8P",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8P",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1630,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "8P",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 444,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8N",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8N",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1695,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "8N",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 509,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8M",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8M",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1678,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "8M",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 492,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8E",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8E",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1620,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "8E",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 434,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8D",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1615,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "8B",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 417,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "8C",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8C",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8C",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1605,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "8A",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 414,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "6C",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "6C",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1210,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "6A",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 344,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "6B",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 349,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "4S",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4S",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 875,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4S",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 369,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "4J",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4J",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 860,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4J",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 354,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "4H",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4H",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 845,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4H",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 339,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "4G",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4G",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 825,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4E",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 309,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4F",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 314,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "4F",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4F",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 820,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 304,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "4E",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4E",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 815,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4C",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 299,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 810,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 297,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "4C",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4C",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 805,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4A",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 294,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "PT",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "PT",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 800,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "PT",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 314,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "1A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1A",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 300,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1A",
              "fareCode": {
                "code": "PNS",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 274,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8B",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1603,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "8A",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "8A",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1600,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "BL",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BL",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1600,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "6B",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "6B",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1205,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "6A",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "6A",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1200,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "OV",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OV",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1200,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 803,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "4A",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4A",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 800,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
          "code": "IS",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IS",
              "fareCode": {
                "code": "TB3",
                "type": 1,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 800,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 119.86,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 99,
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
