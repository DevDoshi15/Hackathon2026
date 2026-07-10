# Farecode Availability

**Path:** Create Reservation > Create Reservation With Transfer (Pre/Post Airport Transfer) > Farecode Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listfarecodes`

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
            "packageId": 1269292
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
Date: Mon, 06 Mar 2023 10:06:22 GMT
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
      "requestId": "4da9c68b-570a-4cfc-b925-b6d68a8aa277",
      "timeStamp": "06-Mar-2023 05:06:18",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "30-Mar-2023 00:00:00",
        "arrivalDateTime": "03-Apr-2023 00:00:00",
        "departureCityId": "GLS",
        "arrivalCityId": "GLS",
        "duration": 4
      },
      "pos": {
        "id": 2114,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2C"
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
      "cruise": {
        "packageId": 1269292,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 71
            }
          ]
        },
        "itinerary": {
          "id": 355501,
          "destination": {
            "id": 14
          }
        },
        "tourCode": "AD04W115",
        "voyage": {
          "departureDateTime": "30-Mar-2023 00:00:00",
          "arrivalDateTime": "03-Apr-2023 00:00:00",
          "departureCityId": "GLS",
          "arrivalCityId": "GLS",
          "code": "AD04W115"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "BESTRATE_GRP",
          "name": "Best Rate_GRP",
          "description": "Best fare",
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Best fare"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I1064941_GRP",
          "name": "STANDARD GROUP_GRP",
          "description": "STANDARD GROUP",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD GROUP"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9601784_GRP",
          "name": "BROCHURE_GRP",
          "description": "BROCHURE PRICE",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I0453091_GRP",
          "name": "BROCHURE_GRP",
          "description": "BROCHURE PRICE",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9601786_GRP",
          "name": "TEST ONLY_GRP",
          "description": "TEST ONLY",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "TEST ONLY"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I0453105_GRP",
          "name": "STANDARD_GRP",
          "description": "STANDARD",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I5286484_GRP",
          "name": "STANDARD GROUP_GRP",
          "description": "STANDARD GROUP",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD GROUP"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "BVL_GRP",
          "name": "Best Value_GRP",
          "description": "Restrictions May Apply",
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "remarks": "Restrictions May Apply"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "G0738129_GRP",
          "name": "BOGO60 NRD_GRP",
          "description": "GS and above",
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "GS and above"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "combinableFares": [
            {
              "code": "I7996069",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "type": 0,
              "refundableType": 2
            }
          ]
        },
        {
          "code": "G0737880_GRP",
          "name": "BOGO60 NRD_GRP",
          "description": "JS Below",
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "JS Below"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "combinableFares": [
            {
              "code": "I7996069",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "type": 0,
              "refundableType": 2
            }
          ]
        },
        {
          "code": "I7996069_GRP",
          "name": "WOW Sale NRD_GRP",
          "description": "5N or Less Inside Oceanview Deluxe",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "combinableFares": [
            {
              "code": "G0737880",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "type": 0,
              "refundableType": 2
            }
          ]
        },
        {
          "code": "I7997687_GRP",
          "name": "WOW Sale NRD_GRP",
          "description": "5N or Less Balcony",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "combinableFares": [
            {
              "code": "G0737880",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "type": 0,
              "refundableType": 2
            }
          ]
        },
        {
          "code": "I7522610_GRP",
          "name": "WOW Sale_GRP",
          "description": "5N or Less Balcony",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I7515175_GRP",
          "name": "WOW Sale_GRP",
          "description": "5N or Less Inside Oceanview Deluxe",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          },
          "groups": [
            {
              "code": "9377322",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "BESTRATE",
          "name": "Best Rate",
          "description": "Restrictions May Apply",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "BVL",
          "name": "Best Value",
          "description": "Restrictions May Apply",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "I9601784",
          "name": "BROCHURE",
          "description": "BROCHURE PRICE",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "I0453091",
          "name": "BROCHURE",
          "description": "BROCHURE PRICE",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "I0453105",
          "name": "STANDARD",
          "description": "STANDARD",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "STANDARD"
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "G0738129",
          "name": "BOGO60 NRD",
          "description": "GS and above",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "GS and above",
            "qualifierCodes": "2"
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "combinableFares": [
            {
              "code": "I7996069",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "type": 0,
              "refundableType": 2
            }
          ]
        },
        {
          "code": "G0737880",
          "name": "BOGO60 NRD",
          "description": "JS Below",
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "JS Below",
            "qualifierCodes": "2"
          },
          "groups": [
            {}
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "combinableFares": [
            {
              "code": "I7996069",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "type": 0,
              "refundableType": 2
            }
          ]
        },
        {
          "code": "I7996069",
          "name": "WOW Sale NRD",
          "description": "5N or Less Inside Oceanview Deluxe",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          },
          "groups": [
            {}
          ],
          "combinableFares": [
            {
              "code": "G0737880",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "type": 0,
              "refundableType": 2
            }
          ]
        },
        {
          "code": "I7997687",
          "name": "WOW Sale NRD",
          "description": "5N or Less Balcony",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          },
          "groups": [
            {}
          ],
          "combinableFares": [
            {
              "code": "G0737880",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "type": 0,
              "refundableType": 2
            }
          ]
        },
        {
          "code": "I7522610",
          "name": "WOW Sale",
          "description": "5N or Less Balcony",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          },
          "groups": [
            {}
          ]
        },
        {
          "code": "I7515175",
          "name": "WOW Sale",
          "description": "5N or Less Inside Oceanview Deluxe",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          },
          "groups": [
            {}
          ]
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
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
