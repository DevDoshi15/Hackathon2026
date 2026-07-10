# Category Availability

**Path:** Category Availability > B2B > Category Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listcategories`

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
            "type": "B2B" // Here Type of Office should be passed
        },
        "cruise": {
            "packageId": 1340642
        }
    },
    "customers": [
        {
            "rph": 1,
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 30
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
Date: Mon, 27 Mar 2023 14:33:21 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "057cac32-09fc-4ced-acc6-9e376046c1f8",
      "timeStamp": "30-Mar-2023 13:57:55",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "11-Apr-2024 00:00:00",
        "arrivalDateTime": "01-May-2024 00:00:00",
        "departureCityId": "CIV",
        "arrivalCityId": "VCE",
        "duration": 20
      },
      "pos": {
        "id": 2231,
        "apiId": "NVS",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2B"
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
        "packageId": 1340642,
        "packageTourId": -1,
        "cruiseline": {
          "id": 14,
          "ships": [
            {
              "id": 15084
            }
          ]
        },
        "itinerary": {
          "id": 357643,
          "destination": {
            "id": 51
          }
        },
        "voyage": {
          "departureDateTime": "11-Apr-2024 00:00:00",
          "arrivalDateTime": "01-May-2024 00:00:00",
          "departureCityId": "CIV",
          "arrivalCityId": "VCE",
          "code": "VIS240411A"
        },
        "transportationType": 29
      },
      "fareCodes": [
        {
          "code": "FIT",
          "name": "FIT RATE",
          "description": "Standard FIT Pricing",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "Standard FIT Pricing",
            "qualifierCodes": ""
          }
        },
        {
          "code": "EBS",
          "name": "EBS RATE",
          "description": "Early Booking Savings",
          "type": 0,
          "refundableType": 1,
          "dynamicRules": [
            {
              "type": 6
            }
          ],
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "fareTypeDescription": "",
            "remarks": "Early Booking Savings",
            "qualifierCodes": ""
          }
        },
        {
          "code": "VISOLCC",
          "name": "PROMO: Cruise Only Fare/OLife Credit",
          "description": "NO AIR &amp; NO AMENITIES",
          "type": 0,
          "refundableType": 1,
          "bookOnline": true,
          "status": 1,
          "details": {
            "agencyDescription": "",
            "remarks": "NO AIR &amp; NO AMENITIES"
          }
        }
      ],
      "categories": [
        {
          "code": "OS",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "OS",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 25899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 25899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 54198,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 25899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 54198,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 25899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 54198,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "VS",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "VS",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 19899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "VS",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 19899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 42198,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "VS",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 19899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 42198,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "VS",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 19899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 42198,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "OC",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OC",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 17999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1988.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OC",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 17999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 38398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1988.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OC",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 17999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 38398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1988.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "OC",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 17999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 38398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1988.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 1,
            "guarantee": false
          }
        },
        {
          "code": "PH1",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "PH1",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11499,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1208.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "PH1",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11499,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 25398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1208.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "PH1",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11499,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 25398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1208.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "PH1",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11499,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 25398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1208.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 26,
            "guarantee": false
          }
        },
        {
          "code": "PH2",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "PH2",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11099,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1160.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "PH2",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11099,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 24598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1160.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "PH2",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11099,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 24598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1160.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "PH2",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 11099,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 24598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 1160.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 14,
            "guarantee": false
          }
        },
        {
          "code": "PH3",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "PH3",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 10699,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "PH3",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 10699,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 23798,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "PH3",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 10699,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 23798,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "PH3",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 10699,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 23798,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "A1",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "A1",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 860.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A1",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 860.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A1",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 860.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A1",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8599,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 860.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 29,
            "guarantee": false
          }
        },
        {
          "code": "A2",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "A2",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8549,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 854.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A2",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8549,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19498,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 854.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A2",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8549,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19498,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 854.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A2",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8549,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19498,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 854.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 42,
            "guarantee": false
          }
        },
        {
          "code": "A3",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "A3",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8499,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 848.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A3",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8499,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 848.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A3",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8499,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 848.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A3",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8499,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 848.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 43,
            "guarantee": false
          }
        },
        {
          "code": "A4",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "A4",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8399,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 836.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A4",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8399,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19198,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 836.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A4",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8399,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19198,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 836.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "A4",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8399,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 19198,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 836.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 7,
            "guarantee": false
          }
        },
        {
          "code": "B1",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "B1",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8099,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 800.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B1",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8099,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 800.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B1",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8099,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 800.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B1",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 8099,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18598,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 800.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 32,
            "guarantee": false
          }
        },
        {
          "code": "B2",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "B2",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 788.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B2",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 788.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B2",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 788.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B2",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18398,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 788.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 34,
            "guarantee": false
          }
        },
        {
          "code": "B3",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "B3",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 776.76,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B3",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18198,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 776.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B3",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18198,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 776.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 1,
              "upgradeFrom": "B3",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7899,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 18198,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 776.76,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 19,
            "guarantee": false
          }
        },
        {
          "code": "B4",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "B4",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7799,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "B4",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7799,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 17998,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "B4",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7799,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 17998,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "B4",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 7799,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 17998,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "B5",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "B5",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 6999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "B5",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 6999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 16398,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "B5",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 6999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 16398,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 2,
              "upgradeFrom": "B5",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 2,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 6999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 16398,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        },
        {
          "code": "S",
          "type": 1,
          "fares": [
            {
              "status": 3,
              "upgradeFrom": "S",
              "displayOnly": true,
              "fareCode": {
                "code": "CRUISE ONLY",
                "name": "CRUISE ONLY WITHOUT AMENITIES",
                "description": "",
                "type": 0,
                "refundableType": 1,
                "specialFare": 1,
                "bookOnline": true,
                "status": 3,
                "details": {
                  "agencyDescription": "<b> This special \"Cruise Only Fare\" is only valid for reservations made with us over the phone. It is not combinable with any bonus offer, unless noted otherwise.</b><br/><br/>Please <U>call us</U> to check availability, or select Request a Quote below to easily fill out a Quote Request.",
                  "fareTypeDescription": "",
                  "remarks": "",
                  "qualifierCodes": ""
                }
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 13999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                }
              ]
            },
            {
              "status": 3,
              "upgradeFrom": "S",
              "fareCode": {
                "code": "EBS",
                "name": "EBS RATE",
                "description": "Early Booking Savings",
                "type": 0,
                "refundableType": 1,
                "dynamicRules": [
                  {
                    "type": 6
                  }
                ],
                "bookOnline": true,
                "status": 3,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Early Booking Savings"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 13999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 30398,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 3,
              "upgradeFrom": "S",
              "fareCode": {
                "code": "FIT",
                "name": "FIT RATE",
                "description": "Standard FIT Pricing",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 3,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "",
                  "remarks": "Standard FIT Pricing"
                },
                "supplierRules": [
                  {
                    "description": "US$600 OLife Choice Shipboard Credit",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 1200
                  },
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 13999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 30398,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "AOLIFE000403",
                  "name": "US$600 OLife Choice Shipboard Credit",
                  "description": "",
                  "type": 1,
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 600,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 1200,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000413",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000413",
                  "name": "OLife Choice - 6 Free Shorex (Guests 1 &amp; 2)",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000424"
                  ]
                },
                {
                  "code": "AOLIFE000424",
                  "name": "OLife Choice Free House Select Beverage Package",
                  "description": "",
                  "type": 1,
                  "prices": [
                    {
                      "amount": 0,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 0,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": [],
                  "nonCombinableCodes": [
                    "AOLIFE000403",
                    "AOLIFE000413"
                  ]
                },
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            },
            {
              "status": 3,
              "upgradeFrom": "S",
              "fareCode": {
                "code": "VISOLCC",
                "name": "PROMO: Cruise Only Fare/OLife Credit",
                "description": "NO AIR &amp; NO AMENITIES",
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 3,
                "details": {
                  "agencyDescription": "",
                  "remarks": "NO AIR &amp; NO AMENITIES"
                },
                "supplierRules": [
                  {
                    "description": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                    "currency": "USD",
                    "type": 1,
                    "discountType": 2,
                    "amount": 300
                  }
                ]
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 13999,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 1426,
                  "type": "AVGPP"
                },
                {
                  "id": 4,
                  "amount": 30398,
                  "type": "AVGPP"
                }
              ],
              "addOns": [
                {
                  "code": "CLUBCO3-1B",
                  "name": "US$300 ClubCorp Evergreen Shipboard Credit Offer",
                  "description": "",
                  "autoInclude": true,
                  "prices": [
                    {
                      "amount": 300,
                      "type": "AVGPP"
                    },
                    {
                      "amount": 300,
                      "type": "TOTAL"
                    }
                  ],
                  "combinableCodes": []
                }
              ]
            }
          ]
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 30,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 2,
        "age": 30
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
