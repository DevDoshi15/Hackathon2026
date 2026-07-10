# Cabin Availability

**Path:** Create Reservation > Create Reservation - Payment Pending Confirmation Flag > Cabin Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listcabins`

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
                }
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
Date: Mon, 25 Sep 2023 11:16:57 GMT
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
      "requestId": "3dad44c5-a5b2-4b4a-96c7-aea80e80c3a8",
      "timeStamp": "25-Sep-2023 07:16:55",
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
      "cabins": [
        {
          "number": "8162",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5136,
            "name": "Navigation Deck",
            "description": "Staterooms."
          },
          "location": "Aft Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "8173",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5136,
            "name": "Navigation Deck",
            "description": "Staterooms."
          },
          "location": "Aft Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "7132",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5137,
            "name": "Rotterdam Deck",
            "description": "Neptune Lounge. Staterooms."
          },
          "location": "Aft Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "7137",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5137,
            "name": "Rotterdam Deck",
            "description": "Neptune Lounge. Staterooms."
          },
          "location": "Aft Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "6061",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5138,
            "name": "Upper Veranda Deck",
            "description": "Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6064",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5138,
            "name": "Upper Veranda Deck",
            "description": "Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6062",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5138,
            "name": "Upper Veranda Deck",
            "description": "Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6060",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5138,
            "name": "Upper Veranda Deck",
            "description": "Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "6164",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5138,
            "name": "Upper Veranda Deck",
            "description": "Staterooms."
          },
          "location": "Aft Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "6175",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5138,
            "name": "Upper Veranda Deck",
            "description": "Staterooms."
          },
          "location": "Aft Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5186",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5139,
            "name": "Verandah Deck",
            "description": "Staterooms."
          },
          "location": "Aft Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "5187",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "KG",
              "description": "King Bed ",
              "type": 226,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5139,
            "name": "Verandah Deck",
            "description": "Staterooms."
          },
          "location": "Aft Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "GUAR",
          "isGuarantee": true,
          "beds": [
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            },
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            }
          ],
          "location": "Oceanview",
          "occupancy": {
            "min": 0,
            "max": 2
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
