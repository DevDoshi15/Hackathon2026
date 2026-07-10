# Create Reservation with Payment

**Path:** Create Reservation > Create Reservation - Payment Pending Confirmation Flag > Create Reservation with Payment

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/create`

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
        ],
        "dinings": [ // Dinings Information retrieved by list dining - some cruiselines always requires this information
            {
                "id": 3,
                "code": "8",
                "name": "Open Seating",
                "status": 1
            }
        ]
    },
    "paymentToProcess": {
        "cardToken": "78f3a706-8e91-425f-8ed5-63b6a0102f4a", //Note: First generate this token by using TokenizedCard 
        "amount": 1220,
        "currency": "USD"
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970",
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "IL"
                },
                "city": {
                    "name": "Chicago"
                }
            },
            "ContactInfo": {
                "Email": "john@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "416-555-4566"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "address": {
                "country": {
                    "id": "US"
                }
            },
            "ContactInfo": {
                "Email": "maria@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "416-555-4566"
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
Date: Mon, 25 Sep 2023 11:36:39 GMT
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
  "advisories": [
    {
      "code": "PMTNOTCNF",
      "message": "TXT_Warning_PMTNOTCNF",
      "description": "HAL",
      "type": "Warning"
    },
    {
      "code": "35",
      "message": "CONSUMER ADVICE",
      "description": "NON-COMMISSIONABLE FARE OF    270.00 USD PER PERSON IS INCLUDED IN THE CRUISE FARE.",
      "type": "Information"
    },
    {
      "code": "35",
      "message": "CONSUMER ADVICE",
      "description": "CABIN NOTES:  CONNECT TO 8160",
      "type": "Information"
    },
    {
      "code": "35",
      "message": "CONSUMER ADVICE",
      "description": "NO CRUISE TICKETS WILL BE SENT FOR THIS VOYAGE.",
      "type": "Information"
    },
    {
      "description": "TXT_Warning_PMTNOTCNF",
      "type": "Information"
    }
  ],
  "data": {
    "trackingInfo": {
      "requestId": "095de802-b446-4050-af4e-ee204dc446d8",
      "timeStamp": "25-Sep-2023 07:36:09",
      "token": "EQTEMPKEN"
    },
    "id": 83926,
    "agencyConfirmation": "OS24494",
    "cruiseReservation": {
      "id": 131795,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "2PHHHV"
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
          "odyCustomerRef": 65991,
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 64840
        }
      ],
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "flags": [
        {
          "type": "PaymentPendingConfirm",
          "status": "Active"
        }
      ],
      "cruise": {
        "packageId": 1353464,
        "packageTourId": -1
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
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "address": {
          "city": {
            "name": "Chicago"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "IL"
          }
        },
        "contactInfo": {
          "email": "john@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "416-555-4566"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "address": {
          "country": {
            "id": "US"
          }
        },
        "contactInfo": {
          "email": "maria@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "416-555-4566"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
