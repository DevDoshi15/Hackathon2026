# Dining Availability

**Path:** Create Reservation > Create Reservation - Payment Pending Confirmation Flag > Dining Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/ListDinings`

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
      "packageId": 1353464,
      "packageTourId": -1
    },
    "categories": [
      {
        "code": "SB",
        "fare": {
          "fareCode": {
            "code": "N11"
          }
        },
        "cabins": [
          {
            "number": "8162"
          }
        ]
      }
    ]
  },
  "customers": [
    {
      "rph": 1,      
      "age": 52
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
Date: Mon, 25 Sep 2023 11:20:22 GMT
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
      "requestId": "e9d1375d-ca7a-4999-8d2f-4e732b8a04b0",
      "timeStamp": "25-Sep-2023 07:20:15",
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
          "id": 26937,
          "code": "SB",
          "fares": [
            {
              "fareCode": {
                "code": "N11",
                "type": 0
              }
            }
          ]
        }
      ],
      "dinings": [
        {
          "id": 8,
          "code": "3",
          "name": "Early Seating Upper Level 5:45 PM",
          "status": 1,
          "tableSizeOptions": [
            2,
            4,
            6,
            8,
            10
          ],
          "diningRoom": {
            "type": "Early Upper Dining"
          }
        },
        {
          "id": 7,
          "code": "4",
          "name": "Early Seating Lower Level 6:15 PM",
          "status": 3,
          "tableSizeOptions": [
            2,
            4,
            6,
            8,
            10
          ],
          "diningRoom": {
            "type": "Early Lower Dining"
          }
        },
        {
          "id": 16,
          "code": "5",
          "name": "Main Seating Upper Level 8:00PM",
          "status": 1,
          "tableSizeOptions": [
            2,
            4,
            6,
            8,
            10
          ],
          "diningRoom": {
            "type": "Main Upper Dining"
          }
        },
        {
          "id": 15,
          "code": "6",
          "name": "Main Seating Lower Level 8:30PM",
          "status": 3,
          "tableSizeOptions": [
            2,
            4,
            6,
            8,
            10
          ],
          "diningRoom": {
            "type": "Main Lower Dining"
          }
        },
        {
          "id": 3,
          "code": "8",
          "name": "Open Seating",
          "status": 1,
          "diningRoom": {
            "type": "OPEN SEATING"
          }
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 52
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
