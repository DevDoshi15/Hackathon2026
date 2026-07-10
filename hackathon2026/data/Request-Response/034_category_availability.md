# Category Availability

**Path:** Category Availability > Category Availability

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
            "packageId": 1269434
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
Date: Wed, 01 Feb 2023 11:02:04 GMT
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
      "requestId": "c386e0fd-f6ae-4e0e-9300-2c62c1ed5558",
      "timeStamp": "01-Feb-2023 06:01:56",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 311051,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
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
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I1071484_GRP",
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
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I0507001_GRP",
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
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I0507023_GRP",
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
              "code": "1179594",
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
              "code": "1179594",
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
              "code": "1179594",
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
              "code": "1179594",
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
              "code": "1179594",
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
              "code": "1179594",
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
          "code": "G0684253_GRP",
          "name": "BOGO60_GRP",
          "description": "4n or less",
          "specialFare": -1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "4n or less"
          },
          "groups": [
            {
              "code": "1179594",
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
              "code": "I7515175",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I7522610",
              "type": 0,
              "refundableType": 1
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
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "combinableFares": [
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
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
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ],
          "combinableFares": [
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I9582251_GRP",
          "name": "CC MARKET2 DOM_GRP",
          "description": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9582007_GRP",
          "name": "CC MILITARY_GRP",
          "description": "CC QUALIFIER PROMO - MILITARY ONLY",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CC QUALIFIER PROMO - MILITARY ONLY"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9582012_GRP",
          "name": "CC SENIOR_GRP",
          "description": "AGE SPECIFIC PROMO - SENIOR",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "AGE SPECIFIC PROMO - SENIOR"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9581957_GRP",
          "name": "ES FIRE_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9582003_GRP",
          "name": "ES FIRE2_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9581966_GRP",
          "name": "ES MILITAR_GRP",
          "description": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY"
          },
          "groups": [
            {
              "code": "1179594",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I9582097_GRP",
          "name": "ES Militar2_GRP",
          "description": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE"
          },
          "groups": [
            {
              "code": "1179594",
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
          "code": "I0507001",
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
          "code": "I0507023",
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
          "code": "G0684253",
          "name": "BOGO60",
          "description": "4n or less",
          "specialFare": 1,
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "Buy One and Get One Free - Special Offer",
            "fareTypeDescription": "Discount",
            "remarks": "4n or less",
            "qualifierCodes": "1"
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
              "code": "I7515175",
              "type": 0,
              "refundableType": 1
            },
            {
              "code": "I7522610",
              "type": 0,
              "refundableType": 1
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
          ],
          "combinableFares": [
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            }
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
          ],
          "combinableFares": [
            {
              "code": "G0684253",
              "type": 0,
              "refundableType": 1
            }
          ]
        }
      ],
      "categories": [
        {
          "code": "2B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 539,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "G0737880_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 599,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I7997687_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 599,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "G0684253_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 658.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I7522610_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 658.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I0507001_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1412,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I0507023_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 941,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 599,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I7997687",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 599,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 658.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I7522610",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 658.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 941,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "cabinCount": 10,
            "guarantee": false
          }
        },
        {
          "code": "2D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 479,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "G0737880_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 529,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I7997687_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 529,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "G0684253_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 588.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I7522610_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 588.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I0507001_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1262,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I0507023_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 841,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 529,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I7997687",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 529,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 588.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I7522610",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 588.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 841,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "cabinCount": 10,
            "guarantee": false
          }
        },
        {
          "code": "2N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 389,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "G0737880_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I7996069_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "G0684253_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 478.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I7515175_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 478.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I0507001_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1026,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I0507023_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 684,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 429,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 478.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 478.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 684,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "cabinCount": 10,
            "guarantee": false
          }
        },
        {
          "code": "2T",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 359,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "G0737880_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I7996069_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "G0684253_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 438.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I7515175_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 438.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I0507001_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 941,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I0507023_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 627,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 438.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 438.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 627,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "cabinCount": 5,
            "guarantee": false
          }
        },
        {
          "code": "2V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 349,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "G0737880_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 378.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I7996069_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 378.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 77,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "G0684253_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I7515175_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I0507001_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 899,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I0507023_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 599,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 378.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 378.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 599,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "cabinCount": 5,
            "guarantee": false
          }
        },
        {
          "code": "RS",
          "type": 4,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "RS",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2641,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "RS",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3962,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "OS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1339,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1339,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1913,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2870,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "GT",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1239,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1239,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1770,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2655,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "GS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1119,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1119,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1599,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "VP",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 889,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 889,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 979,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 979,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "VP",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "J3",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 739,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 739,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 819,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 819,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1170,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "J4",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 718.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 718.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 798.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 798.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J4",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1141,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "WS",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 699,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 699,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 999,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1056,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1584,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "3B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1027,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1541,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4B",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 588.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I7997687",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 588.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 648.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I7522610",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 648.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 927,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "CB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 578.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I7997687",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 578.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 639,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I7522610",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 639,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 913,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1D",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 941,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1412,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "5D",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 884,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1326,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I7997687",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 578.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I7522610",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 578.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 827,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "XB",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I7997687",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 713,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1070,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1K",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1170,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1755,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1L",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 569,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 569,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 629,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 629,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1L",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 899,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "3M",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 856,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "3M",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1284,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4M",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 508.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 508.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 559,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 559,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 799,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1N",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 770,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1155,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "3N",
          "type": 2,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 727,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1091,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4N",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 469,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 469,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 670,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "YO",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 399,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 570,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 855,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": true
          }
        },
        {
          "code": "1Q",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 927,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1Q",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1391,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1R",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 548.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 548.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 609,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 609,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "1R",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 870,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "CP",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 419,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 469,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 469,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CP",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 670,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "1V",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 713,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1070,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "3V",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 641,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 962,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "4V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 368.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 368.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "G0684253",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 408.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I7515175",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 408.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 584,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": false
          }
        },
        {
          "code": "ZI",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 349,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 349,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I0507023",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I0507001",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 749,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 113.25,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "guarantee": true
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
