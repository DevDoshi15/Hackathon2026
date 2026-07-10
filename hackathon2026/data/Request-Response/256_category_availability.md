# Category Availability

**Path:** Create Reservation > Create Reservation - Payment Pending Confirmation Flag > Category Availability

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
            "packageId": 1353464
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
Date: Mon, 25 Sep 2023 11:11:23 GMT
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
      "requestId": "32043dfd-a3a3-483a-9c92-5147f8d620a9",
      "timeStamp": "25-Sep-2023 07:11:20",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "06-Mar-2024 00:00:00",
        "arrivalDateTime": "16-Mar-2024 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 10
      },
      "pos": {
        "id": 2519,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "Any",
        "system": "Test",
        "apiId": "Carnival"
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
        "packageId": 1353464,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 1161
            }
          ]
        },
        "itinerary": {
          "id": 370988,
          "destination": {
            "id": 9
          }
        },
        "voyage": {
          "departureDateTime": "06-Mar-2024 00:00:00",
          "arrivalDateTime": "16-Mar-2024 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "D421"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "BNN",
          "name": "BEST AVAL NON-PAST PSG W/O AIR",
          "description": "EXCLUDES NON-REF FARES",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "EXCLUDES NON-REF FARES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "BNP",
          "name": "BEST AVAL PAST PSG W/O AIR",
          "description": "EXCLUDES NON-REF FARES",
          "type": 10,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "EXCLUDES NON-REF FARES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "NNN",
          "name": "BEST AVAL NON-PAST PSG W/O AIR",
          "description": "INCLUDES NON-REF FARES",
          "type": 0,
          "refundableType": 3,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "INCLUDES NON-REF FARES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "NNP",
          "name": "BEST AVAL PAST PSG W/O AIR",
          "description": "INCLUDES NON-REF FARES",
          "type": 10,
          "refundableType": 3,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "INCLUDES NON-REF FARES",
            "qualifierCodes": ""
          }
        },
        {
          "code": "NH1",
          "name": "ADVANTAGE FARES",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "qualifierCodes": "",
            "validity": {
              "from": "01-Jan-2022",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "N11",
          "name": "HAVE IT ALL",
          "description": "",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 2
            },
            {
              "type": 3
            },
            {
              "type": 18
            },
            {
              "type": 4
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "",
            "qualifierCodes": "",
            "validity": {
              "from": "01-Jan-2019",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "QA1",
          "name": "NON-REFUNDABLE DEPOSIT",
          "description": "NON-REFUNDABLE FARE",
          "type": 0,
          "refundableType": 2,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "NON-REFUNDABLE FARE",
            "qualifierCodes": "",
            "validity": {
              "from": "01-Jan-2022",
              "to": "06-Dec-2023"
            }
          }
        }
      ],
      "rulesInfo": {
        "applicableRules": [
          {
            "id": 1728537,
            "name": "OBC CONSOLIDATOR RULE - DEMO PURPOSES ONLY ##PromotionAmount##",
            "groupName": "nonexcl",
            "type": 5,
            "externalGroupId": "",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "Customer information for Demo Purposes",
              "agencyDetails": "Anything this rule promises you is not real.",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "https://sandbox.odysol.com/site/images/promotions/cdor_wine2.png"
            }
          },
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
          "id": 26935,
          "code": "PS",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "PS",
              "status": 2,
              "fareCode": {
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8099,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "PS",
              "status": 2,
              "fareCode": {
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7599,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "PS",
              "status": 3,
              "fareCode": {
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 3,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7599,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "SU"
          }
        },
        {
          "id": 26936,
          "code": "SA",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SA",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 5324,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 603.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SA",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4824,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 543.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SA",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4774,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 537.48,
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
          },
          "location": {
            "code": "SU"
          }
        },
        {
          "id": 26937,
          "code": "SB",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SB",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4824,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 543.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SB",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4324,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 483.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SB",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4274,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 477.48,
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
          },
          "location": {
            "code": "SU"
          }
        },
        {
          "id": 26938,
          "code": "SC",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SC",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4324,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 483.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SC",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3824,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 423.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SC",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3774,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 417.48,
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
          },
          "location": {
            "code": "SU"
          }
        },
        {
          "id": 59058,
          "code": "SS",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SS",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4024,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 447.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SS",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 387.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SS",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 381.48,
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
          },
          "location": {
            "code": "SU"
          }
        },
        {
          "id": 59060,
          "code": "SU",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SU",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3874,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 429.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SU",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3374,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 369.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SU",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3324,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 363.48,
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
          },
          "location": {
            "code": "SU"
          }
        },
        {
          "id": 59057,
          "code": "SY",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SY",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 411.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SY",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3224,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 351.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SY",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3174,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 345.48,
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
          },
          "location": {
            "code": "SU"
          }
        },
        {
          "id": 59056,
          "code": "SZ",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SZ",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 411.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SZ",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3224,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 351.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SZ",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3174,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 345.48,
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
          },
          "location": {
            "code": "SU"
          }
        },
        {
          "id": 59055,
          "code": "VQ",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VQ",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2844,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 305.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VQ",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2344,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 245.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VQ",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2294,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 239.88,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 59059,
          "code": "VT",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VT",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2804,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 301.08,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VT",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2304,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 241.08,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VT",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2254,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 235.08,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 26942,
          "code": "V",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "V",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2764,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 296.28,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "V",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2264,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 236.28,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "V",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 230.28,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 26943,
          "code": "VA",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VA",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 291.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VA",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2224,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 231.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VA",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2174,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 225.48,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 26944,
          "code": "VB",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VB",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2684,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 286.68,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VB",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2184,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 226.68,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VB",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2134,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 220.68,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 59054,
          "code": "VC",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VC",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2644,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 281.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VC",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2144,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 221.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VC",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2094,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 215.88,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 59053,
          "code": "VD",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VD",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2604,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 277.08,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VD",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2104,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 217.08,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VD",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2054,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 211.08,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 59052,
          "code": "VE",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VE",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2564,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 272.28,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VE",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2064,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 212.28,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VE",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2014,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 206.28,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 26948,
          "code": "VF",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VF",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 267.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VF",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2024,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 207.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VF",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1974,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 201.48,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 59051,
          "code": "VH",
          "type": 3,
          "fares": [
            {
              "upgradeFrom": "VH",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 267.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VH",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2024,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 207.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "VH",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1974,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 201.48,
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
          },
          "location": {
            "code": "OB"
          }
        },
        {
          "id": 58324,
          "code": "CQ",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "CQ",
              "status": 2,
              "fareCode": {
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2099,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "CQ",
              "status": 2,
              "fareCode": {
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1599,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "CQ",
              "status": 3,
              "fareCode": {
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 3,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1549,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 26951,
          "code": "C",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "C",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2104,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 217.08,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "C",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1604,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 157.08,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "C",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1554,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 151.08,
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
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 26952,
          "code": "D",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "D",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2084,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 214.68,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "D",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1584,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 154.68,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "D",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1534,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 148.68,
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
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 26953,
          "code": "DD",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "DD",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2064,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 212.28,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "DD",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1564,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 152.28,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "DD",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1514,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 146.28,
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
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 26954,
          "code": "E",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "E",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2044,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 209.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "E",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1544,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 149.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "E",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 143.88,
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
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 26955,
          "code": "F",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "F",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2024,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 207.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "F",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 147.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "F",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 141.48,
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
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 59050,
          "code": "G",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "G",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1944,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 197.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "G",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1444,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 137.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "G",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1394,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 131.88,
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
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 59049,
          "code": "H",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "H",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1924,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 195.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "H",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 135.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "H",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1374,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 129.48,
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
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 59048,
          "code": "HH",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "HH",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1924,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 195.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "HH",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 135.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "HH",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1374,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 129.48,
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
          },
          "location": {
            "code": "OS"
          }
        },
        {
          "id": 58325,
          "code": "IQ",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "IQ",
              "status": 2,
              "fareCode": {
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1819,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "IQ",
              "status": 2,
              "fareCode": {
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1319,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "IQ",
              "status": 3,
              "fareCode": {
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 3,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1269,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "guarantee": false
          },
          "location": {
            "code": "IS"
          }
        },
        {
          "id": 59047,
          "code": "I",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "I",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1824,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 183.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "I",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1324,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 123.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "I",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1274,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 117.48,
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
          },
          "location": {
            "code": "IS"
          }
        },
        {
          "id": 26961,
          "code": "J",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "J",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1804,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 181.08,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "J",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1304,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 121.08,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "J",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1254,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 115.08,
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
          },
          "location": {
            "code": "IS"
          }
        },
        {
          "id": 26962,
          "code": "K",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "K",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1784,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 178.68,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "K",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1284,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 118.68,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "K",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1234,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 112.68,
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
          },
          "location": {
            "code": "IS"
          }
        },
        {
          "id": 59045,
          "code": "L",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "L",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1764,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 176.28,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "L",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1264,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 116.28,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "L",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1214,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 110.28,
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
          },
          "location": {
            "code": "IS"
          }
        },
        {
          "id": 59044,
          "code": "M",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "M",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1744,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 173.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "M",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1244,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 113.88,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "M",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1194,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 107.88,
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
          },
          "location": {
            "code": "IS"
          }
        },
        {
          "id": 59046,
          "code": "MM",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "MM",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 171.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "MM",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1224,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 111.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "MM",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 105.48,
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
          },
          "location": {
            "code": "IS"
          }
        },
        {
          "id": 59043,
          "code": "N",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "N",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "N11",
                "name": "HAVE IT ALL",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 2
                  },
                  {
                    "type": 3
                  },
                  {
                    "type": 18
                  },
                  {
                    "type": 4
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 171.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "N",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "NH1",
                "name": "ADVANTAGE FARES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1224,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 111.48,
                  "type": "AVGPP"
                },
                {
                  "id": 48,
                  "amount": 27.5,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "N",
              "rules": [
                {
                  "id": 1728537,
                  "calculatedAmount": {
                    "0": 50,
                    "1": 25,
                    "2": 25
                  }
                },
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
                "code": "QA1",
                "name": "NON-REFUNDABLE DEPOSIT",
                "description": "NON-REFUNDABLE FARE",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "NON-REFUNDABLE FARE"
                }
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
                  "amount": 220,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 270,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 105.48,
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
          },
          "location": {
            "code": "IS"
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
