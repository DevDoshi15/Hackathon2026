# Farecode Availability

**Path:** Create Reservation > Group Reservation > Royal Carribean Cruiseline > Farecode Availability

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
Date: Tue, 14 Mar 2023 09:38:40 GMT
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
      "requestId": "fa841b46-b707-4050-85db-588e1cc7ceb6",
      "timeStamp": "14-Mar-2023 05:38:38",
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
          "ageGroup": "Adult",
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
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
          "id": 364180,
          "destination": {
            "id": 7
          }
        },
        "tourCode": "FR4BH098",
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
          "code": "F4169636_GRP",
          "name": "Nets NRD_GRP",
          "description": "Net Rates",
          "isEligible": true,
          "type": 12,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Net Rates"
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
          "code": "I9610945_GRP",
          "name": "BPG OFF_GRP",
          "description": "BPG AMOUNT DISCOUNT",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "BPG AMOUNT DISCOUNT"
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
          "code": "F4348105_GRP",
          "name": "Nets_GRP",
          "description": "Net Rates",
          "isEligible": true,
          "type": 12,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "Net Rates"
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
              "code": "I9610945",
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
              "code": "I9610945",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I9602229_GRP",
          "name": "TARGETED NRD 1_GRP",
          "description": "TARGETED NRD 1",
          "bookOnline": true,
          "isEligible": true,
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "TARGETED NRD 1"
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
          }
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
          }
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
          }
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
          }
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
          "code": "F4169636",
          "name": "Nets NRD",
          "description": "Net Rates",
          "isEligible": true,
          "type": 12,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Net Rates",
            "remarks": "Net Rates",
            "qualifierCodes": "2"
          }
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
          "code": "I9610945",
          "name": "BPG OFF",
          "description": "BPG AMOUNT DISCOUNT",
          "isEligible": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "BPG AMOUNT DISCOUNT"
          },
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
          "code": "F4348105",
          "name": "Nets",
          "description": "Net Rates",
          "isEligible": true,
          "type": 12,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Net Rates",
            "remarks": "Net Rates",
            "qualifierCodes": "1"
          }
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
          "combinableFares": [
            {
              "code": "I9610945",
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
          "combinableFares": [
            {
              "code": "I9610945",
              "type": 0,
              "refundableType": 1
            }
          ]
        },
        {
          "code": "I9602229",
          "name": "TARGETED NRD 1",
          "description": "TARGETED NRD 1",
          "type": 0,
          "refundableType": 2,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "TARGETED NRD 1"
          }
        },
        {
          "code": "I9582251",
          "name": "CC MARKET2 DOM",
          "description": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CALL CENTER MARKET DOMESTIC ONLY (USD CAD)"
          }
        },
        {
          "code": "I9582007",
          "name": "CC MILITARY",
          "description": "CC QUALIFIER PROMO - MILITARY ONLY",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "CC QUALIFIER PROMO - MILITARY ONLY"
          }
        },
        {
          "code": "I9582012",
          "name": "CC SENIOR",
          "description": "AGE SPECIFIC PROMO - SENIOR",
          "bookOnline": true,
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "AGE SPECIFIC PROMO - SENIOR"
          }
        },
        {
          "code": "I9581957",
          "name": "ES FIRE",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY"
          }
        },
        {
          "code": "I9582003",
          "name": "ES FIRE2",
          "description": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - FIRE ONLY LIMI"
          }
        },
        {
          "code": "I9581966",
          "name": "ES MILITAR",
          "description": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER PROMOTION - MILITAR ONLY"
          }
        },
        {
          "code": "I9582097",
          "name": "ES Militar2",
          "description": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "Discount",
            "remarks": "ESPRESSO QUALIFIER MILITAR ONLY - UNIQUE UNRE"
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
