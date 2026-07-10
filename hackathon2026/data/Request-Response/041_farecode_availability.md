# Farecode Availability

**Path:** Cabin Availability > Guaranteed Cabin Indicator > Farecode Availability

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
            "packageId": 1275651
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
Date: Thu, 16 Mar 2023 14:38:30 GMT
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
      "requestId": "45fe7725-2bc9-4e29-9022-114bd7d0a2fd",
      "timeStamp": "16-Mar-2023 10:38:28",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "19-Mar-2023 00:00:00",
        "arrivalDateTime": "24-Mar-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 5
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
        "packageId": 1275651,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 75
            }
          ]
        },
        "itinerary": {
          "id": 364197,
          "destination": {
            "id": 14
          }
        },
        "tourCode": "GR05W392",
        "voyage": {
          "departureDateTime": "19-Mar-2023 00:00:00",
          "arrivalDateTime": "24-Mar-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "GR05W392"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "BESTRATE_GRP",
          "name": "Best Rate_GRP",
          "description": "Best fare",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Best fare"
          }
        },
        {
          "code": "I1635974_GRP",
          "name": "STANDARD GROUP_GRP",
          "description": "STANDARD GROUP",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD GROUP"
          }
        },
        {
          "code": "I1366409_GRP",
          "name": "BROCHURE_GRP",
          "description": "BROCHURE PRICE",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          }
        },
        {
          "code": "I8383870_GRP",
          "name": "STANDARD GROUP_GRP",
          "description": "STANDARD GROUP",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD GROUP"
          }
        },
        {
          "code": "I1366425_GRP",
          "name": "STANDARD_GRP",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "STANDARD"
          }
        },
        {
          "code": "BVL_GRP",
          "name": "Best Value_GRP",
          "description": "Restrictions May Apply",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "remarks": "Restrictions May Apply"
          }
        },
        {
          "code": "G0738129_GRP",
          "name": "BOGO60 NRD_GRP",
          "description": "GS and above",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "GS and above"
          }
        },
        {
          "code": "G0737880_GRP",
          "name": "BOGO60 NRD_GRP",
          "description": "JS Below",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "JS Below"
          }
        },
        {
          "code": "I7996069_GRP",
          "name": "WOW Sale NRD_GRP",
          "description": "5N or Less Inside Oceanview Deluxe",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          }
        },
        {
          "code": "I7997687_GRP",
          "name": "WOW Sale NRD_GRP",
          "description": "5N or Less Balcony",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          }
        },
        {
          "code": "I7522610_GRP",
          "name": "WOW Sale_GRP",
          "description": "5N or Less Balcony",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          }
        },
        {
          "code": "I7515175_GRP",
          "name": "WOW Sale_GRP",
          "description": "5N or Less Inside Oceanview Deluxe",
          "type": 0,
          "refundableType": 1,
          "groups": [
            {
              "code": "979199",
              "name": "TLN ADD US",
              "type": 2,
              "subType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          }
        },
        {
          "code": "BESTRATE",
          "name": "Best Rate",
          "description": "Restrictions May Apply",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          }
        },
        {
          "code": "BVL",
          "name": "Best Value",
          "description": "Restrictions May Apply",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "Restrictions May Apply",
            "fareTypeDescription": "Public fare - base or best rate",
            "remarks": "Restrictions May Apply",
            "qualifierCodes": ""
          }
        },
        {
          "code": "I1366409",
          "name": "BROCHURE",
          "description": "BROCHURE PRICE",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "BROCHURE PRICE"
          }
        },
        {
          "code": "I1366425",
          "name": "STANDARD",
          "description": "STANDARD",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "STANDARD"
          }
        },
        {
          "code": "G0738129",
          "name": "BOGO60 NRD",
          "description": "GS and above",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "GS and above",
            "qualifierCodes": "2"
          }
        },
        {
          "code": "G0737880",
          "name": "BOGO60 NRD",
          "description": "JS Below",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "I7996069",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "I7997687",
              "description": "WOW Sale NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "dynamicRules": [
            {
              "type": 10
            }
          ],
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "JS Below",
            "qualifierCodes": "2"
          }
        },
        {
          "code": "I7996069",
          "name": "WOW Sale NRD",
          "description": "5N or Less Inside Oceanview Deluxe",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
          }
        },
        {
          "code": "I7997687",
          "name": "WOW Sale NRD",
          "description": "5N or Less Balcony",
          "type": 0,
          "refundableType": 2,
          "combinableFares": [
            {
              "code": "G0737880",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            },
            {
              "code": "G0738129",
              "description": "BOGO60 NRD",
              "type": 0,
              "refundableType": 2
            }
          ],
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          }
        },
        {
          "code": "I7522610",
          "name": "WOW Sale",
          "description": "5N or Less Balcony",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Balcony"
          }
        },
        {
          "code": "I7515175",
          "name": "WOW Sale",
          "description": "5N or Less Inside Oceanview Deluxe",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "isEligible": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "5N or Less Inside Oceanview Deluxe"
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
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
