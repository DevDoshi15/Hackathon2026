# Category Availability

**Path:** Create Reservation > Create Reservation With AddOns > Category Availability

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
            "packageId": 1324816
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
Date: Thu, 16 Mar 2023 09:22:10 GMT
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
      "requestId": "0d884ebc-7a72-41cd-b2f5-1d4f81596d85",
      "timeStamp": "16-Mar-2023 05:22:07",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Apr-2023 00:00:00",
        "arrivalDateTime": "08-Apr-2023 00:00:00",
        "departureCityId": "MRS",
        "arrivalCityId": "MRS",
        "duration": 7
      },
      "pos": {
        "id": 2119,
        "apiId": "MSC",
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
        "packageId": 1324816,
        "packageTourId": -1,
        "cruiseline": {
          "id": 982,
          "ships": [
            {
              "id": 14091
            }
          ]
        },
        "itinerary": {
          "id": 362627,
          "destination": {
            "id": 18
          }
        },
        "voyage": {
          "departureDateTime": "01-Apr-2023 00:00:00",
          "arrivalDateTime": "08-Apr-2023 00:00:00",
          "departureCityId": "MRS",
          "arrivalCityId": "MRS",
          "code": "GR20230401MRSMRS"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "EZAT35DZE",
          "name": "ESCAPE TO SEA CRUISE ONLY",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "EZAT"
          }
        },
        {
          "code": "GRUS306R3",
          "name": "BROCHURE RATES",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 24
            },
            {
              "type": 25
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "EZBR"
          }
        }
      ],
      "categories": [
        {
          "code": "IR1",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IR1",
              "fareCode": {
                "code": "EZAT35DZE",
                "name": "ESCAPE TO SEA CRUISE ONLY",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZAT"
                },
                "supplierRules": [
                  {
                    "code": "OBS|TRIOPR|636713197|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|EXP2B|636713325|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|636713572|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 718,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 67.08,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "636713197",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "636713325",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "636713572",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "IR1",
              "fareCode": {
                "code": "GRUS306R3",
                "name": "BROCHURE RATES",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZBR"
                },
                "supplierRules": [
                  {
                    "code": "OBS|EXP2B|183426727|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|183426728|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|TRIOPR|183426779|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1699,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 184.8,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "183426727",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "183426728",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "183426779",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "IR2",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "IR2",
              "fareCode": {
                "code": "EZAT35DZE",
                "name": "ESCAPE TO SEA CRUISE ONLY",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZAT"
                },
                "supplierRules": [
                  {
                    "code": "OBS|TRIOPR|636713206|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|EXP2B|636713337|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|636713589|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 748,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 70.68,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "636713206",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "636713337",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "636713589",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "IR2",
              "fareCode": {
                "code": "GRUS306R3",
                "name": "BROCHURE RATES",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZBR"
                },
                "supplierRules": [
                  {
                    "code": "OBS|EXP2B|183426729|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|183426730|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|TRIOPR|183426780|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1759,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 192,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "183426729",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "183426730",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "183426780",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "OM2",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OM2",
              "fareCode": {
                "code": "EZAT35DZE",
                "name": "ESCAPE TO SEA CRUISE ONLY",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZAT"
                },
                "supplierRules": [
                  {
                    "code": "OBS|TRIOPR|636713248|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|EXP2B|636713359|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|636713618|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 888,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 87.48,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "636713248",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "636713359",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "636713618",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OM2",
              "fareCode": {
                "code": "GRUS306R3",
                "name": "BROCHURE RATES",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZBR"
                },
                "supplierRules": [
                  {
                    "code": "OBS|EXP2B|183426735|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|183426736|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|TRIOPR|183426783|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2039,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 225.6,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "183426735",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "183426736",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "183426783",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "BP",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BP",
              "fareCode": {
                "code": "EZAT35DZE",
                "name": "ESCAPE TO SEA CRUISE ONLY",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZAT"
                },
                "supplierRules": [
                  {
                    "code": "OBS|TRIOPR|636713151|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|EXP2B|636713448|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|636713641|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1048,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 106.68,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "636713151",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "636713448",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "636713641",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "BP",
              "fareCode": {
                "code": "GRUS306R3",
                "name": "BROCHURE RATES",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZBR"
                },
                "supplierRules": [
                  {
                    "code": "OBS|EXP2B|183426745|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|183426746|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|TRIOPR|183426774|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2359,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 264,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "183426745",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "183426746",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "183426774",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "BR1",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BR1",
              "fareCode": {
                "code": "EZAT35DZE",
                "name": "ESCAPE TO SEA CRUISE ONLY",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZAT"
                },
                "supplierRules": [
                  {
                    "code": "OBS|TRIOPR|636713156|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|EXP2B|636713405|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|636713711|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1108,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 113.88,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "636713156",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "636713405",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "636713711",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "BR1",
              "fareCode": {
                "code": "GRUS306R3",
                "name": "BROCHURE RATES",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZBR"
                },
                "supplierRules": [
                  {
                    "code": "OBS|EXP2B|183426747|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|183426748|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|TRIOPR|183426775|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2479,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 278.4,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "183426747",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "183426748",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "183426775",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "BR2",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BR2",
              "fareCode": {
                "code": "EZAT35DZE",
                "name": "ESCAPE TO SEA CRUISE ONLY",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZAT"
                },
                "supplierRules": [
                  {
                    "code": "OBS|TRIOPR|636713166|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|EXP2B|636713419|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|636713726|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1158,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 119.88,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "636713166",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "636713419",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "636713726",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "BR2",
              "fareCode": {
                "code": "GRUS306R3",
                "name": "BROCHURE RATES",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZBR"
                },
                "supplierRules": [
                  {
                    "code": "OBS|EXP2B|183426749|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|183426750|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|TRIOPR|183426776|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2579,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 290.4,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "183426749",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "183426750",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "183426776",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "BR3",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BR3",
              "fareCode": {
                "code": "EZAT35DZE",
                "name": "ESCAPE TO SEA CRUISE ONLY",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZAT"
                },
                "supplierRules": [
                  {
                    "code": "OBS|TRIOPR|636713181|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|EXP2B|636713431|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|636713743|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1188,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 123.48,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "636713181",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "636713431",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "636713743",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "BR3",
              "fareCode": {
                "code": "GRUS306R3",
                "name": "BROCHURE RATES",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Fantastica Experience Benefits",
                    "type": 23
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZBR"
                },
                "supplierRules": [
                  {
                    "code": "OBS|EXP2B|183426751|2023-04-01|2023-04-01|0",
                    "description": "Fantastica Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|183426752|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|TRIOPR|183426777|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2639,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 297.6,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "EXP2B",
                  "name": "Fantastica Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "183426751",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "183426752",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "183426777",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "BA",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "BA",
              "fareCode": {
                "code": "EZAT35DZE",
                "name": "ESCAPE TO SEA CRUISE ONLY",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Aurea Experience Benefits",
                    "type": 24
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZAT"
                },
                "supplierRules": [
                  {
                    "code": "OBS|SPABAEXP|636713031|2023-04-01|2023-04-01|0",
                    "description": "Balinese Massage 50 Minute",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|TRIOPR|636713085|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|EXP3B|636713459|2023-04-01|2023-04-01|0",
                    "description": "Aurea Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|636713755|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1348,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 142.68,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "SPABAEXP",
                  "name": "Balinese Massage 50 Minute",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 30,
                  "additionalCode": "636713031",
                  "prices": [
                    {
                      "amount": 108,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 216,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "636713085",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "EXP3B",
                  "name": "Aurea Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "636713459",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "636713755",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "BA",
              "fareCode": {
                "code": "GRUS306R3",
                "name": "BROCHURE RATES",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "description": "Aurea Experience Benefits",
                    "type": 24
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "EZBR"
                },
                "supplierRules": [
                  {
                    "code": "OBS|EXP3B|183426753|2023-04-01|2023-04-01|0",
                    "description": "Aurea Experience Benefits",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|600|183426754|2023-04-01|2023-04-01|0",
                    "description": "MINERAL WATER AND COFFEE IN DINING ROOM",
                    "type": 1,
                    "discountType": 2,
                    "quantity": 1
                  },
                  {
                    "code": "OBS|SPABAEXP|183426769|2023-04-01|2023-04-01|0",
                    "description": "Balinese Massage 50 Minute",
                    "type": 1,
                    "discountType": 2
                  },
                  {
                    "code": "OBS|TRIOPR|183426773|2023-04-01|2023-04-01|0",
                    "description": "Trilogy - Three Exclusive Dining Experiences",
                    "type": 1,
                    "discountType": 2
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2959,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 65.1,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 159,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 336,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "EXP3B",
                  "name": "Aurea Experience Benefits",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 23,
                  "additionalCode": "183426753",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "600",
                  "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 6,
                  "additionalCode": "183426754",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "SPABAEXP",
                  "name": "Balinese Massage 50 Minute",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 30,
                  "additionalCode": "183426769",
                  "prices": [
                    {
                      "amount": 108,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 216,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                },
                {
                  "code": "TRIOPR",
                  "name": "Trilogy - Three Exclusive Dining Experiences",
                  "description": "",
                  "startDate": "01-Apr-2023",
                  "endDate": "01-Apr-2023",
                  "type": 16,
                  "additionalCode": "183426773",
                  "prices": [
                    {
                      "amount": 100,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
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
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
