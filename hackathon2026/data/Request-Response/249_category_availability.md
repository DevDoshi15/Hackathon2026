# Category Availability

**Path:** Create Reservation > Create Reservation - Payment Declined Flag > Category Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listcategories`

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
        "cruise": {
            "packageId": 1313282
        },
        "fareCodes": [
            {
                "code": "DISC35"
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
Date: Wed, 06 Sep 2023 09:37:56 GMT
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
      "requestId": "601028e7-3246-413b-a5e2-d402d825533c",
      "timeStamp": "06-Sep-2023 05:37:45",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Jan-2024 00:00:00",
        "arrivalDateTime": "11-Jan-2024 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 9
      },
      "pos": {
        "id": 2520,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "B2B",
        "system": "Test",
        "apiId": "NCL"
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
        "packageId": 1313282,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 1100
            }
          ]
        },
        "itinerary": {
          "id": 372547,
          "destination": {
            "id": 10
          }
        },
        "voyage": {
          "departureDateTime": "02-Jan-2024 00:00:00",
          "arrivalDateTime": "11-Jan-2024 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "18439803"
        },
        "transportationType": 29
      },
      "rulesInfo": {
        "applicableRules": [
          {
            "id": 1728342,
            "name": "Cruise Discount (5$)",
            "groupName": "excl_1728342",
            "type": 1,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728343,
            "name": "Cruise Markup (25$)",
            "groupName": "excl_1728343",
            "type": 2,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728420,
            "name": "VAO Exclusive",
            "groupName": "excl_1728420",
            "type": 3,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "va_earlysaver.png"
            }
          },
          {
            "id": 1728421,
            "name": "VAO One Exclusive",
            "groupName": "excl_1728421",
            "type": 3,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "pink-circle.png"
            }
          },
          {
            "id": 1728422,
            "name": "VAO Non Exclusive",
            "groupName": "nonexcl",
            "type": 3,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "CruiseCategory",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "va_anchor-vODY-635382737153437500.png"
            }
          },
          {
            "id": 1728423,
            "name": "VAO Two Non Exclusive",
            "groupName": "nonexcl",
            "type": 3,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "CruiseCategory",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "va_sale.png"
            }
          },
          {
            "id": 1728419,
            "name": "Cruise Addon",
            "groupName": "excl_1728419",
            "type": 9,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728344,
            "name": "Cruise Service Fee (20$)",
            "groupName": "excl_1728344",
            "type": 13,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728415,
            "name": "Package Service Doc (10)",
            "groupName": "P1",
            "type": 18,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<strong>Customer Details</strong> added here",
              "agencyDetails": "Agency Details Added Here",
              "redemptionDetails": "Redemption details goes here",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728416,
            "name": "Package Service Doc One (15)",
            "groupName": "P1",
            "type": 18,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<strong>Customer Details</strong> added here",
              "agencyDetails": "Agency Details Added Here",
              "redemptionDetails": "Redemption details goes here",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728417,
            "name": "Package Service Travel (25) BEST Value YES",
            "groupName": "P2",
            "type": 18,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<strong>Customer Details</strong> added here",
              "agencyDetails": "Agency Details Added Here",
              "redemptionDetails": "Redemption details goes here",
              "customLink": "",
              "imageUrl": ""
            }
          },
          {
            "id": 1728418,
            "name": "Package Service Travel (20) BEST Value NO",
            "groupName": "P2",
            "type": 18,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<strong>Customer Details</strong> added here",
              "agencyDetails": "Agency Details Added Here",
              "redemptionDetails": "Redemption details goes here",
              "customLink": "",
              "imageUrl": ""
            }
          }
        ]
      },
      "categories": [
        {
          "id": 60316,
          "code": "H1",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "H1",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 16865,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1995.06,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 60317,
          "code": "H2",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "H2",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8857,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1034.1,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72973,
          "code": "H6",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "H6",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7050,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 817.26,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72968,
          "code": "S4",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "S4",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 5282,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 605.1,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72975,
          "code": "SD",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SD",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4788,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 545.82,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72967,
          "code": "SF",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SF",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4580,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 520.86,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72976,
          "code": "SN",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SN",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3930,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 442.86,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53518,
          "code": "M1",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "M1",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3397,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 378.9,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53519,
          "code": "MA",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "MA",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2513,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 272.82,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53520,
          "code": "MB",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "MB",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2461,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 266.58,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53521,
          "code": "B1",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "B1",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3111,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 344.58,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72979,
          "code": "B4",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "B4",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2240,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 240.06,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 4052,
          "code": "BA",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "BA",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2214,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 236.94,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72977,
          "code": "BF",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "BF",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2300,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 247.26,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72972,
          "code": "O4",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "O4",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1681,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 172.98,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53525,
          "code": "OA",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "OA",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1629,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 166.74,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53526,
          "code": "OB",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "OB",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1551,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 157.38,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53528,
          "code": "OF",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "OF",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1499,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 151.14,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53530,
          "code": "OK",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "OK",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1460,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 146.46,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 72978,
          "code": "I4",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "I4",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1226,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 118.38,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53532,
          "code": "IA",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "IA",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1213,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 116.82,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53533,
          "code": "IB",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "IB",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1174,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 112.14,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
          "id": 53537,
          "code": "IF",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "IF",
              "rules": [
                {
                  "id": 1728342,
                  "calculatedAmount": {
                    "0": 5,
                    "1": 2.5,
                    "2": 2.5
                  }
                },
                {
                  "id": 1728343,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728420
                },
                {
                  "id": 1728421
                },
                {
                  "id": 1728422
                },
                {
                  "id": 1728423
                },
                {
                  "id": 1728419,
                  "calculatedAmount": {
                    "0": 12,
                    "1": 6,
                    "2": 6
                  }
                },
                {
                  "id": 1728344,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                },
                {
                  "id": 1728415,
                  "calculatedAmount": {
                    "0": 10,
                    "1": 5,
                    "2": 5
                  }
                },
                {
                  "id": 1728416,
                  "calculatedAmount": {
                    "0": 15,
                    "1": 7.5,
                    "2": 7.5
                  }
                },
                {
                  "id": 1728417,
                  "calculatedAmount": {
                    "0": 25,
                    "1": 12.5,
                    "2": 12.5
                  }
                },
                {
                  "id": 1728418,
                  "calculatedAmount": {
                    "0": 20,
                    "1": 10,
                    "2": 10
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "DISC35",
                "type": 0,
                "refundableType": 1,
                "status": 1,
                "details": {}
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1135,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 282.32,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 214.5,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 107.46,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
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
