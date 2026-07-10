# Carnival Cruise line

**Path:** Price Reservation > Cancellation Policies > Carnival Cruise line

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
            "packageId": 1316422,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "OS",
                "fare": {
                    "fareCode": {
                        "code": "KCH"
                    }
                },
                "cabins": [
                    {
                        "number": "7231"
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
Date: Tue, 27 Jun 2023 15:28:07 GMT
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
  "advisories": [
    {
      "code": "1215",
      "message": "All staterooms, inclusive of balconies, are an entirely smoke-free environment. Smoking is prohibited in all staterooms and balconies. Guest who smoke in theseareas will be assesd a $250 AUD cleaning and refreshing fee on their Sail and Sign account.",
      "description": "CCL-",
      "type": "Warning"
    }
  ],
  "data": {
    "trackingInfo": {
      "requestId": "94d1de8c-de75-47df-b539-1d9bf8a51e2e",
      "timeStamp": "27-Jun-2023 11:28:00",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "31-Oct-2023 00:00:00",
        "arrivalDateTime": "05-Nov-2023 00:00:00",
        "departureCityId": "SYD",
        "arrivalCityId": "SYD",
        "duration": 5
      },
      "pos": {
        "id": 2460,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "B2B",
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
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "type": 0,
            "amount": 215.52,
            "dueDate": "27-Jun-2023 11:28:00"
          },
          {
            "type": 1,
            "amount": 1997.04,
            "dueDate": "27-Jul-2023 23:59:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 0,
            "amount": 215.52,
            "dueDate": "27-Jun-2023 23:59:00"
          },
          {
            "type": 1,
            "amount": 1997.04,
            "dueDate": "27-Jul-2023 23:59:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 0,
            "amount": 215.52,
            "dueDate": "29-Jun-2023 11:28:00"
          },
          {
            "type": 1,
            "amount": 1710.76,
            "dueDate": "17-Aug-2023 23:59:00"
          }
        ]
      },
      "prices": [
        {
          "id": 126,
          "amount": 195.52,
          "display": true,
          "rph": -1
        },
        {
          "id": 1,
          "code": "CRUS",
          "amount": 1998.34,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "PTCH",
          "amount": 162.92,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 1998.34,
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
          "amount": 1998.34,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 1835.4199999999998,
          "priority": 16,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 41,
          "code": "PKGS",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
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
          "id": 12,
          "code": "TADD",
          "amount": 0,
          "priority": 25,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 3,
          "code": "MISC",
          "amount": 194.22,
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
          "amount": 2212.56,
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
          "amount": 2212.56,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 2212.56,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 2167.56,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 215.52,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 26,
          "code": "PMTS",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 62,
          "code": "",
          "amount": 2167.56,
          "priority": 382,
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
          "code": "COMM",
          "amount": 241.28,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 1926.28,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "amount": 1926.28,
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
          "amount": 2212.56,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "amount": 286.28,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 140,
          "code": "CGST",
          "amount": 0,
          "priority": 610,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 141,
          "code": "NCOM",
          "amount": 241.28,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 610,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 126,
          "amount": 97.76,
          "display": true,
          "rph": 1
        },
        {
          "id": 1,
          "code": "CRUS",
          "amount": 999.17,
          "priority": 5,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 2,
          "code": "PTCH",
          "amount": 81.46,
          "priority": 6,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "amount": 999.17,
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
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 46,
          "code": "",
          "amount": 999.17,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "amount": 917.7099999999999,
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
          "code": "MISC",
          "amount": 97.11,
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
          "amount": 1106.28,
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
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
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
          "amount": 1106.28,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "amount": 1106.28,
          "priority": 355,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 1083.78,
          "priority": 359,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 107.76,
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
          "id": 62,
          "code": "",
          "amount": 1083.78,
          "priority": 382,
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
          "id": 32,
          "code": "COMM",
          "amount": 120.64,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 963.14,
          "priority": 510,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "amount": 963.14,
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
          "amount": 1106.28,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "amount": 143.14,
          "priority": 600,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 141,
          "code": "NCOM",
          "amount": 120.64,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 610,
          "displayType": 4,
          "rph": 1
        },
        {
          "id": 126,
          "amount": 97.76,
          "display": true,
          "rph": 2
        },
        {
          "id": 1,
          "code": "CRUS",
          "amount": 999.17,
          "priority": 5,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 2,
          "code": "PTCH",
          "amount": 81.46,
          "priority": 6,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "amount": 999.17,
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
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 46,
          "code": "",
          "amount": 999.17,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "amount": 917.7099999999999,
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
          "code": "MISC",
          "amount": 97.11,
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
          "amount": 1106.28,
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
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
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
          "amount": 1106.28,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "amount": 1106.28,
          "priority": 355,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 1083.78,
          "priority": 359,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 107.76,
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
          "id": 62,
          "code": "",
          "amount": 1083.78,
          "priority": 382,
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
          "id": 32,
          "code": "COMM",
          "amount": 120.64,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 963.14,
          "priority": 510,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "amount": 963.14,
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
          "amount": 1106.28,
          "priority": 600,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "amount": 143.14,
          "priority": 600,
          "displayType": 4,
          "rph": 2
        },
        {
          "id": 141,
          "code": "NCOM",
          "amount": 120.64,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 610,
          "displayType": 4,
          "rph": 2
        }
      ],
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1316422,
        "packageTourId": -1,
        "cruiseline": {
          "id": 1,
          "ships": [
            {
              "id": 1163
            }
          ]
        },
        "itinerary": {
          "id": 296522,
          "destination": {
            "id": 104
          }
        },
        "voyage": {
          "departureDateTime": "31-Oct-2023 00:00:00",
          "arrivalDateTime": "05-Nov-2023 00:00:00",
          "departureCityId": "SYD",
          "arrivalCityId": "SYD",
          "code": "20231031SL05"
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
          "amount": 195.52,
          "amountType": "Fixed",
          "startDate": "16-Aug-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 50,
          "amountType": "Percentage",
          "startDate": "05-Sep-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 75,
          "amountType": "Percentage",
          "startDate": "01-Oct-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 100,
          "amountType": "Percentage",
          "startDate": "16-Oct-2023",
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
