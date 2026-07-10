# SilverSea Cruise line

**Path:** Price Reservation > Cancellation Policies > SilverSea Cruise line

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listprices`

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
//Cancellation policies can be found under "cancellationPolicies" element in the response
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1321223,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "MS",
                "fare": {
                    "fareCode": {
                        "code": "03_29",
                        "externalSessionInfo": {
                            "externalId": "03"
                        }
                    }
                },
                "cabins": [
                    {
                        "number": "9086"
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970",
            "age": 52,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "age": 57,
            "address": {
                "country": {
                    "id": "US"
                }
            }
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
Date: Tue, 27 Jun 2023 15:28:38 GMT
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
      "requestId": "8f32c216-f0f0-4f87-b32a-8c447b6ca66e",
      "timeStamp": "27-Jun-2023 11:28:34",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Sep-2023 00:00:00",
        "arrivalDateTime": "08-Sep-2023 00:00:00",
        "departureCityId": "CIV",
        "arrivalCityId": "MCM",
        "duration": 7
      },
      "pos": {
        "id": 2475,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "B2B",
        "system": "Test",
        "apiId": "SSC"
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
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "type": 2,
            "amount": 27045,
            "dueDate": "28-Jun-2023 00:00:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 27045,
            "dueDate": "28-Jun-2023 00:00:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 23539.14,
            "dueDate": "30-Jun-2023 00:00:00"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "5",
          "amount": 27025,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "60",
          "amount": 378,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 27025,
          "priority": 10,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 48,
          "code": "",
          "amount": 25,
          "priority": 12,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 46,
          "code": "",
          "amount": 27025,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 26647,
          "priority": 16,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 3,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": -1
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 17,
          "code": "",
          "amount": 27045,
          "priority": 100,
          "display": true,
          "rph": -1
        },
        {
          "id": 86,
          "code": "",
          "amount": 20,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 23,
          "code": "",
          "amount": 27045,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 27045,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "50",
          "amount": 27000,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "amount": 0,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 27,
          "code": "73",
          "amount": 3460.86,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 32,
          "code": "11",
          "amount": 3460.86,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "amount": 23539.14,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "amount": 27045,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "amount": 3505.8600000000006,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "amount": 13512.5,
          "priority": 5,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 2,
          "code": "60",
          "amount": 189,
          "priority": 6,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "amount": 13512.5,
          "priority": 10,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 48,
          "code": "",
          "amount": 12.5,
          "priority": 12,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 46,
          "code": "",
          "amount": 13512.5,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "amount": 13323.5,
          "priority": 16,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 3,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 1
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 17,
          "code": "",
          "amount": 13522.5,
          "priority": 100,
          "display": true,
          "rph": 1
        },
        {
          "id": 86,
          "code": "",
          "amount": 10,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 1
        },
        {
          "id": 23,
          "code": "",
          "amount": 13522.5,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "amount": 13522.5,
          "priority": 355,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 50,
          "code": "50",
          "amount": 13500,
          "priority": 359,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 24,
          "amount": 0,
          "priority": 360,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 27,
          "code": "73",
          "amount": 1730.43,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 32,
          "code": "11",
          "amount": 1730.43,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "amount": 11769.57,
          "priority": 510,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 112,
          "code": "",
          "amount": 13522.5,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "amount": 1752.9300000000003,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 1,
          "code": "5",
          "amount": 13512.5,
          "priority": 5,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 2,
          "code": "60",
          "amount": 189,
          "priority": 6,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "amount": 13512.5,
          "priority": 10,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 48,
          "code": "",
          "amount": 12.5,
          "priority": 12,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 46,
          "code": "",
          "amount": 13512.5,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "amount": 13323.5,
          "priority": 16,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 3,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 2
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 17,
          "code": "",
          "amount": 13522.5,
          "priority": 100,
          "display": true,
          "rph": 2
        },
        {
          "id": 86,
          "code": "",
          "amount": 10,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 2
        },
        {
          "id": 23,
          "code": "",
          "amount": 13522.5,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "amount": 13522.5,
          "priority": 355,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 50,
          "code": "50",
          "amount": 13500,
          "priority": 359,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 24,
          "amount": 0,
          "priority": 360,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 27,
          "code": "73",
          "amount": 1730.43,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 32,
          "code": "11",
          "amount": 1730.43,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "amount": 11769.57,
          "priority": 510,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 112,
          "code": "",
          "amount": 13522.5,
          "priority": 600,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "amount": 1752.9300000000003,
          "priority": 600,
          "displayType": 4,
          "rph": 2
        }
      ],
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1321223,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8115,
          "ships": [
            {
              "id": 15112
            }
          ]
        },
        "itinerary": {
          "id": 364030,
          "destination": {
            "id": 75
          }
        },
        "voyage": {
          "departureDateTime": "01-Sep-2023 00:00:00",
          "arrivalDateTime": "08-Sep-2023 00:00:00",
          "departureCityId": "CIV",
          "arrivalCityId": "MCM",
          "code": "SN230901007"
        },
        "transportationType": 29
      },
      "rulesInfo": {
        "applicableRules": [
          {
            "id": 1728343,
            "name": "Cruise Markup",
            "type": 2
          },
          {
            "id": 1728344,
            "name": "Cruise Service Fee",
            "type": 13
          }
        ],
        "rules": [
          {
            "ruleId": 1728343,
            "calculatedAmount": {
              "total": 25
            }
          },
          {
            "ruleId": 1728344,
            "calculatedAmount": {
              "total": 20
            }
          }
        ]
      },
      "cancellationPolicies": [
        {
          "amount": 250,
          "amountType": "Fixed",
          "startDate": "06-Dec-2020",
          "endDate": "03-Apr-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 15,
          "amountType": "Percentage",
          "startDate": "04-Apr-2023",
          "endDate": "03-May-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 25,
          "amountType": "Percentage",
          "startDate": "04-May-2023",
          "endDate": "02-Jun-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 50,
          "amountType": "Percentage",
          "startDate": "03-Jun-2023",
          "endDate": "02-Jul-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 75,
          "amountType": "Percentage",
          "startDate": "03-Jul-2023",
          "endDate": "01-Aug-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 100,
          "amountType": "Percentage",
          "startDate": "02-Aug-2023",
          "endDate": "01-Sep-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
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
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "age": 57,
        "address": {
          "country": {
            "id": "US"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
