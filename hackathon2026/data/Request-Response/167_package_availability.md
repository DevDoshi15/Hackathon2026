# Package Availability

**Path:** Create Reservation > Create Reservation With Packages > Auto-Inclusion of Packages > Create Reservation WITHOUT DoNotAutoIncludePackages Preference > Package Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listpackages`

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
        "cruise": {
            "packageId": 1353443,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "I",
                "fare": {
                    "fareCode": {
                        "code": "QA1"
                    }
                }
            }
        ],
        "customerReferences": [
            {
                "RPH": "1",
                "isPrimaryContact": true
            },
            {
                "RPH": "2"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "firstName": "John",
            "lastName": "Doe"
        },
        {
            "rph": 2,
            "age": 57,
            "firstName": "Maria",
            "lastName": "Doe"
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Fri, 03 Nov 2023 11:00:55 GMT
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
      "requestId": "19a1331b-59b3-439a-b9f3-c2eee79ada3a",
      "timeStamp": "03-Nov-2023 07:00:45",
      "token": "d08643db-1ba9-406e-ade2-9d54b2608e14"
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
          "id": 59065,
          "code": "I",
          "fares": [
            {
              "fareCode": {
                "code": "QA1",
                "type": 0
              }
            }
          ]
        }
      ],
      "packages": [
        {
          "code": "B0TNOXFR",
          "description": "NO TRANSFER",
          "type": "PrePackage",
          "status": 1,
          "isComplimentary": true,
          "departureArrivalInfo": {
            "departureDateTime": "03-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00"
          },
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B0MMIAFLL-AS",
          "description": "TRANSFER MIA AIRPORT/FT LAUDERDALE",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "03-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00"
          },
          "prices": [
            {
              "id": 41,
              "amount": 29,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B0TFLL-AS",
          "description": "TRANSFER FLL AIRPORT/SHIP",
          "type": "PrePackage",
          "status": 1,
          "departureArrivalInfo": {
            "departureDateTime": "03-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00"
          },
          "prices": [
            {
              "id": 41,
              "amount": 19,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B11FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 1 NT",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "02-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 219,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B11FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 1 NT",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "02-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 189,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B11MIAFLLGEN",
          "description": "FLY/CRUISE - MIAMI HOTEL    - 1 NT",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "02-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 1
          },
          "prices": [
            {
              "id": 41,
              "amount": 9999,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B21FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 2 NTS",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "01-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 388,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B21FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 2 NTS",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "01-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 318,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B21MIAFLLGEN",
          "description": "FLY/CRUISE - MIAMI HOTEL    - 2 NTS",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "01-Feb-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 9999,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B31FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 3 NTS",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "31-Jan-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 557,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B31FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 3 NTS",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "31-Jan-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 447,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "B31MIAFLLGEN",
          "description": "FLY/CRUISE - MIAMI HOTEL    - 3 NTS",
          "type": "PrePackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "31-Jan-2024 00:00:00",
            "arrivalDateTime": "03-Feb-2024 00:00:00",
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 9999,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A0TNOXFR",
          "description": "NO TRANSFER",
          "type": "PostPackage",
          "status": 1,
          "isComplimentary": true,
          "departureArrivalInfo": {
            "departureDateTime": "10-Feb-2024 00:00:00",
            "arrivalDateTime": "10-Feb-2024 00:00:00"
          },
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A0MFLLMIA-SA",
          "description": "TRANSFER FT LAUDERDALE SHIP/MIA AIR",
          "type": "PostPackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "10-Feb-2024 00:00:00",
            "arrivalDateTime": "10-Feb-2024 00:00:00"
          },
          "prices": [
            {
              "id": 41,
              "amount": 29,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A0TFLL-SA",
          "description": "TRANSFER FLL SHIP/AIRPORT",
          "type": "PostPackage",
          "status": 1,
          "departureArrivalInfo": {
            "departureDateTime": "10-Feb-2024 00:00:00",
            "arrivalDateTime": "10-Feb-2024 00:00:00"
          },
          "prices": [
            {
              "id": 41,
              "amount": 19,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A22FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 2 NTS",
          "type": "PostPackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "10-Feb-2024 00:00:00",
            "arrivalDateTime": "12-Feb-2024 00:00:00",
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 169,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A22FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 2 NTS",
          "type": "PostPackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "10-Feb-2024 00:00:00",
            "arrivalDateTime": "12-Feb-2024 00:00:00",
            "duration": 2
          },
          "prices": [
            {
              "id": 41,
              "amount": 129,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A32FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 3 NTS",
          "type": "PostPackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "10-Feb-2024 00:00:00",
            "arrivalDateTime": "13-Feb-2024 00:00:00",
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 338,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A32FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 3 NTS",
          "type": "PostPackage",
          "status": 3,
          "departureArrivalInfo": {
            "departureDateTime": "10-Feb-2024 00:00:00",
            "arrivalDateTime": "13-Feb-2024 00:00:00",
            "duration": 3
          },
          "prices": [
            {
              "id": 41,
              "amount": 258,
              "type": "AVGPP"
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
        "age": 52
      },
      {
        "gender": "Male",
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
