# Category Availability

**Path:** Create Reservation > Create Reservation With Packages > Auto-Inclusion of Packages > Create Reservation WITH DoNotAutoIncludePackages Preference > Category Availability

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
            "packageId": 1353443
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
Date: Fri, 03 Nov 2023 08:13:13 GMT
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
      "requestId": "adb81ab4-8937-4e65-9175-c6e3e5187e33",
      "timeStamp": "03-Nov-2023 04:13:11",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "03-Feb-2024 00:00:00",
        "arrivalDateTime": "10-Feb-2024 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 7
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
        "packageId": 1353443,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 13250
            }
          ]
        },
        "itinerary": {
          "id": 370945,
          "destination": {
            "id": 9
          }
        },
        "voyage": {
          "departureDateTime": "03-Feb-2024 00:00:00",
          "arrivalDateTime": "10-Feb-2024 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "I416"
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
          "code": "NH2",
          "name": "SUS SCENARIO 9.2",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "validity": {
              "from": "01-Jan-2023",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "NH3",
          "name": "SUS SCENARIO 9.3",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "validity": {
              "from": "01-Jan-2022",
              "to": "31-Dec-2024"
            }
          }
        },
        {
          "code": "NH4",
          "name": "SUS SCENARIO 9.4",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
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
              "to": "04-Nov-2023"
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
          "id": 52898,
          "code": "PS",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "PS",
              "status": 2,
              "fareCode": {
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2899,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 5799,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "PS",
              "status": 2,
              "fareCode": {
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 2899,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "PS",
              "status": 2,
              "fareCode": {
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 2899,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
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
                  "amount": 6149,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 5799,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
          "id": 59077,
          "code": "SQ",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SQ",
              "status": 2,
              "fareCode": {
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SQ",
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
                  "amount": 3649,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SQ",
              "status": 2,
              "fareCode": {
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SQ",
              "status": 2,
              "fareCode": {
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SQ",
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
                  "amount": 3999,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SQ",
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
                  "amount": 3614,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
          "id": 52900,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 3424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 385.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 427.08,
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
                  "amount": 3389,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 380.88,
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
          "id": 52901,
          "code": "SB",
          "type": 4,
          "fares": [
            {
              "upgradeFrom": "SB",
              "status": 2,
              "fareCode": {
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1574,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SB",
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
                  "amount": 3149,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SB",
              "status": 2,
              "fareCode": {
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 1574,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SB",
              "status": 2,
              "fareCode": {
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 1574,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SB",
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
                  "amount": 3499,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "SB",
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
                  "amount": 3114,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
          "id": 52902,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 2924,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 325.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 3274,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 367.08,
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
                  "amount": 2889,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 320.88,
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
          "id": 59076,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1149,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 112.08,
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
                  "amount": 2274,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 247.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 1149,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 112.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 1149,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 112.08,
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
                  "amount": 2624,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 289.08,
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
                  "amount": 2239,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 242.88,
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
          "id": 59075,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1074,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 103.08,
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
                  "amount": 2124,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 229.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 1074,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 103.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 1074,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 103.08,
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
                  "amount": 2474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 271.08,
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
                  "amount": 2089,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 224.88,
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
          "id": 59074,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1074,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 103.08,
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
                  "amount": 2124,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 229.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 1074,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 103.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 1074,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 103.08,
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
                  "amount": 2474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 271.08,
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
                  "amount": 2089,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 224.88,
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
          "id": 59069,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 754,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 64.68,
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
                  "amount": 1484,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 754,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 64.68,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 754,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 64.68,
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
                  "amount": 1834,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 194.28,
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
                  "amount": 1449,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 148.08,
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
          "id": 52907,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 739,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 62.88,
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
                  "amount": 1454,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 739,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 62.88,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 739,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 62.88,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 190.68,
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
                  "amount": 1419,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 144.48,
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
          "id": 52908,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 61.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 145.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 61.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 724,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 61.08,
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
                  "amount": 1774,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 187.08,
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
                  "amount": 1389,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 140.88,
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
          "id": 52909,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 709,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 59.28,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 709,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 59.28,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 709,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 59.28,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 1359,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 137.28,
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
          "id": 59072,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 694,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 57.48,
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
                  "amount": 1364,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 694,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 57.48,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 694,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 57.48,
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
                  "amount": 1714,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 179.88,
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
                  "amount": 1329,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 133.68,
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
          "id": 59073,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 679,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 55.68,
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
                  "amount": 1334,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 134.28,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 679,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 55.68,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 679,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 55.68,
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
                  "amount": 1684,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 1299,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 130.08,
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
          "id": 59071,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 664,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 53.88,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 130.68,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 664,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 53.88,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 664,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 53.88,
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
                  "amount": 1654,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 172.68,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 126.48,
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
          "id": 52913,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 649,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 127.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 649,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 649,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.08,
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
                  "amount": 1624,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 169.08,
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
                  "amount": 1239,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 122.88,
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
          "id": 59070,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 649,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 127.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 649,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 649,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 52.08,
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
                  "amount": 1624,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 169.08,
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
                  "amount": 1239,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 122.88,
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
          "id": 58234,
          "code": "CQ",
          "type": 2,
          "fares": [
            {
              "upgradeFrom": "CQ",
              "status": 2,
              "fareCode": {
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 1049,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "CQ",
              "status": 2,
              "fareCode": {
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "CQ",
              "status": 2,
              "fareCode": {
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
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
                  "amount": 1399,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 1014,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
          "id": 52916,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 544,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 39.48,
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
                  "amount": 1064,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 101.88,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 544,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 39.48,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 544,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 39.48,
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
                  "amount": 1414,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 1029,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 97.68,
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
          "id": 52917,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 539,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 38.88,
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
                  "amount": 1054,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 100.68,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 539,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 38.88,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 539,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 38.88,
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
                  "amount": 1404,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 142.68,
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
                  "amount": 1019,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 96.48,
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
          "id": 52918,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 534,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 38.28,
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
                  "amount": 1044,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 99.48,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 534,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 38.28,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 534,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 38.28,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 1009,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 95.28,
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
          "id": 52919,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 529,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 37.68,
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
                  "amount": 1034,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 98.28,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 529,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 37.68,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 529,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 37.68,
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
                  "amount": 1384,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 140.28,
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
                  "amount": 999,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 94.08,
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
          "id": 52920,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 37.08,
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
                  "amount": 1024,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 97.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 37.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 524,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 37.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 139.08,
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
                  "amount": 989,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 92.88,
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
          "id": 59068,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 479,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.68,
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
                  "amount": 934,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 86.28,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 479,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.68,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 479,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.68,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 128.28,
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
                  "amount": 899,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 82.08,
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
          "id": 59067,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.08,
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
                  "amount": 924,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 127.08,
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
                  "amount": 889,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 80.88,
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
          "id": 59066,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.08,
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
                  "amount": 924,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 85.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 474,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 31.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 127.08,
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
                  "amount": 889,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 80.88,
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
          "id": 58235,
          "code": "IQ",
          "type": 1,
          "fares": [
            {
              "upgradeFrom": "IQ",
              "status": 2,
              "fareCode": {
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 859,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "IQ",
              "status": 2,
              "fareCode": {
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 429,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "upgradeFrom": "IQ",
              "status": 2,
              "fareCode": {
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 429,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                }
              ]
            },
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
                  "amount": 1209,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 824,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
          "id": 59065,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 449,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 28.08,
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
                  "amount": 874,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 79.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 449,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 28.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 449,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 28.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 839,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 74.88,
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
          "id": 52927,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 444,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 27.48,
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
                  "amount": 864,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 77.88,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 444,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 27.48,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 444,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 27.48,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 119.88,
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
                  "amount": 829,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 73.68,
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
          "id": 52928,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 439,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 26.88,
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
                  "amount": 854,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 76.68,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 439,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 26.88,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 439,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 26.88,
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
                  "amount": 1204,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 819,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 72.48,
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
          "id": 59064,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 434,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 26.28,
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
                  "amount": 844,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 75.48,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 434,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 26.28,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 434,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 26.28,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 809,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 71.28,
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
          "id": 59078,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.68,
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
                  "amount": 834,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 74.28,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 429,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.68,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 429,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.68,
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
                  "amount": 1184,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 799,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 70.08,
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
          "id": 62289,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.08,
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
                  "amount": 824,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 73.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 789,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.88,
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
          "id": 59061,
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
                "code": "NH3",
                "name": "SUS SCENARIO 9.3",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.08,
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
                  "amount": 824,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 73.08,
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
                "code": "NH2",
                "name": "SUS SCENARIO 9.2",
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
                  "amount": 424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.08,
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
                "code": "NH4",
                "name": "SUS SCENARIO 9.4",
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
                  "amount": 424,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 25.08,
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
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
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
                  "amount": 789,
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  },
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 195,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 190,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 68.88,
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
