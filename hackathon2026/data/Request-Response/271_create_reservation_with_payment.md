# Create Reservation with Payment

**Path:** Create Reservation > Create Reservation with Payment

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
// Below Fields are mandatory For Above API
// categories - > code
// categories - > fare - > fareCode - > code
// categories - > cabins - > number
{
    "cruiseReservation": {
        "pos": { // Either id or currency is mandatory
            //"id": 1,
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
            "packageId": 1381475,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "V4",
                "fare": {
                    "fareCode": {
                        "code": "I9625411"
                    }
                },
                "cabins": [
                    {
                        "number": "9446"
                    }
                ]
            }
        ],
        "dinings": [ // Dinings Information retrieved by list dining - some cruiselines always requires this information
            {
                "id": 1,
                "code": "M",
                "name": "05:30 PM",
                "status": 1
            }
        ]
    },
    "paymentToProcess": {
        "cardToken": "c26e83fe-20ae-48cf-b1ea-d25c43a1ba03", //Note: First generate this token by using TokenizedCard 
        "amount": 7424.22,
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
Date: Fri, 21 Jul 2023 13:20:29 GMT
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
      "requestId": "a00c7294-00fb-4ad7-9659-380bce2836cc",
      "timeStamp": "21-Jul-2023 09:20:16",
      "token": "EQTEMPKEN"
    },
    "id": 75757,
    "agencyConfirmation": "W49AR9U",
    "cruiseReservation": {
      "id": 123734,
      "status": 7,
      "reservationReferences": {
        "confirmationNumber": "436103"
      },
      "pos": {
        "id": 2467,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "Any",
        "system": "Test",
        "apiId": "RCCL"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 64845,
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 64840
        }
      ],
      "currencyInfo": {
        "currencyId": "USD"
      },
      "cruise": {
        "packageId": 1381475,
        "packageTourId": -1
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
            "id": 1728345,
            "name": "$25 Digital Costco Shop Card",
            "groupName": "nonexcl",
            "type": 3,
            "externalGroupId": "ShopCard",
            "externalId": "ShopCard",
            "details": {
              "bestValue": true,
              "displayToCustomer": true,
              "displayStep": "All",
              "customerDetails": "<b>Member Exclusive: Digital Shop Card with every sailing</b><br/>The digital Costco Shop Card is per stateroom and will be emailed to the member at the email address on file 1 to 4 weeks after your trip. The Digital Costco Shop Card promotion is nontransferable and may not be combined with any other promotion. Digital Costco Shop Cards are not redeemable for cash, except as required by law. To view full Terms & Conditions visit CostcoTravel.com for additional information.",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "https://costco.odysol.com/site/images/promotions/Costco-Shop-Card-En-vODY-638120883878905274.png"
            }
          },
          {
            "id": 1728346,
            "name": "$45 Digital Costco Shop Card",
            "groupName": "nonexcl",
            "type": 3,
            "externalGroupId": "ShopCard",
            "externalId": "",
            "details": {
              "bestValue": true,
              "displayToCustomer": false,
              "displayStep": "All",
              "customerDetails": "<b>Member Exclusive: Digital Shop Card with every sailing</b><br/>The digital Costco Shop Card is per stateroom and will be emailed to the member at the email address on file 1 to 4 weeks after your trip. The Digital Costco Shop Card promotion is nontransferable and may not be combined with any other promotion. Digital Costco Shop Cards are not redeemable for cash, except as required by law. To view full Terms & Conditions visit CostcoTravel.com for additional information.",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "https://costco.odysol.com/site/images/promotions/Costco-Shop-Card-En-vODY-638120883878905274.png"
            }
          },
          {
            "id": 1728347,
            "name": "$70 Digital Costco Shop Card",
            "groupName": "excl_1728347",
            "type": 3,
            "externalGroupId": "ShopCard",
            "externalId": "",
            "details": {
              "displayToCustomer": false,
              "displayStep": "CruiseCategory",
              "customerDetails": "<b>Member Exclusive: Digital Shop Card with every sailing</b><br/>The digital Costco Shop Card is per stateroom and will be emailed to the member at the email address on file 1 to 4 weeks after your trip. The Digital Costco Shop Card promotion is nontransferable and may not be combined with any other promotion. Digital Costco Shop Cards are not redeemable for cash, except as required by law. To view full Terms & Conditions visit CostcoTravel.com for additional information.",
              "agencyDetails": "",
              "redemptionDetails": "",
              "customLink": "",
              "imageUrl": "https://costco.odysol.com/site/images/promotions/Costco-Shop-Card-En-vODY-638120883878905274.png"
            }
          },
          {
            "id": 1728349,
            "name": "$95 Digital Shop Card",
            "groupName": "excl_1728349",
            "type": 3,
            "externalGroupId": "ShopCard",
            "externalId": "",
            "details": {
              "displayToCustomer": false,
              "displayStep": "All",
              "customerDetails": "<strong>Member Exclusive: Digital Shop Card with every sailing</strong><br>The digital  Shop Card is per stateroom and will be emailed to the member at the email address on file 1 to 4 weeks after your trip. The Digital Shop Card promotion is nontransferable and may not be combined with any other promotion. Digital Shop Cards are not redeemable for cash, except as required by law.",
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
            "id": 1728424,
            "groupName": "excl_1728424",
            "type": 3,
            "externalGroupId": "AMENITY",
            "externalId": "",
            "details": {
              "displayToCustomer": true,
              "displayStep": "All"
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
              "bestValue": true,
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
          "id": 667463448,
          "code": "V4",
          "fares": [
            {
              "fareCode": {
                "code": "I9625411",
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
