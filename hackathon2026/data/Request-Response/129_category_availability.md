# Category Availability

**Path:** Create Reservation > Create Reservation With Grats For RCCL > Category Availability

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
            "packageId": 1269329,
            "packageTourId": -1
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
Date: Mon, 20 Feb 2023 08:28:19 GMT
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
      "requestId": "6a8e08a3-a722-413f-b29a-726b58c5334b",
      "timeStamp": "20-Feb-2023 03:28:15",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "15-Apr-2023 00:00:00",
        "arrivalDateTime": "20-Apr-2023 00:00:00",
        "departureCityId": "TPA",
        "arrivalCityId": "TPA",
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269329,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 72
            }
          ]
        },
        "itinerary": {
          "id": 311000,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "15-Apr-2023 00:00:00",
          "arrivalDateTime": "20-Apr-2023 00:00:00",
          "departureCityId": "TPA",
          "arrivalCityId": "TPA",
          "code": "BR05W366"
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
              "code": "9557711",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I1066453_GRP",
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
              "code": "9557711",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I0484775_GRP",
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
              "code": "9557711",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I1242394_GRP",
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
              "code": "9557711",
              "name": "TLN ADD USD",
              "type": 2,
              "subType": 2
            }
          ]
        },
        {
          "code": "I1922307_GRP",
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
              "code": "9557711",
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
              "code": "9557711",
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
              "code": "9557711",
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
              "code": "9557711",
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
              "code": "9557711",
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
              "code": "9557711",
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
              "code": "9557711",
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
              "code": "9557711",
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
          "code": "I0484775",
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
          "code": "I1242394",
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
      ],
      "categories": [
        {
          "code": "2D",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I1066453_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 669,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 728.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 94.5,
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
                  "amount": 728.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 94.5,
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
                  "amount": 1127,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I0484775_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1691,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I1242394_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1127,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I1922307_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 655,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 728.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 728.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1127,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1127,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "2E",
          "type": 3,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I1066453_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "G0737880_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 669,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 94.5,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I7997687_GRP",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 669,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 94.5,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I7522610_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I0484775_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I1242394_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I1922307_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 669,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I7997687",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 669,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2E",
              "fareCode": {
                "code": "I7522610",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I1066453_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 539,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 94.5,
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
                  "amount": 539,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 94.5,
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
                  "amount": 827,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I0484775_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1241,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I1242394_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I1922307_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 504,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 539,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 539,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 827,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "2V",
          "type": 1,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I1066453_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 489,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 94.5,
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
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 94.5,
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
                  "amount": 799,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I0484775_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1199,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I1242394_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I1922307_GRP",
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
                  "amount": 111.47,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 799,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "RS",
          "type": 4,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "RS",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4027,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "RS",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 6041,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "OT",
          "type": 4,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "OT",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2319,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OT",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2319,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OT",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3313,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OT",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4970,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1598.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1598.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2284,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "OS",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 3426,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 2058.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 2058.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2941,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GT",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 4412,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1189,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1189,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1699,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "GS",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 2549,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 949,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 949,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "J3",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1456,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1456,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
              "status": 13,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "G0738129",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 949,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 13,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I7996069",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 949,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 13,
              "upgradeFrom": "WS",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1356,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "1B",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1299,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1B",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1949,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "3B",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1926,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "2B",
          "type": 3,
          "fares": [
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
                  "amount": 809,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 809,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1241,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1241,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 798.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 798.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4B",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1227,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1227,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 749,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 749,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CB",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1156,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1156,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1199,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1D",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1799,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "3D",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "3D",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1184,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "3D",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1776,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1156,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "5D",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1734,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 709,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 709,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4D",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1084,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 1084,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "1E",
          "type": 3,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1E",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1041,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1E",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1562,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 629,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 629,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "XB",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1349,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1K",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1926,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 609,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 609,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4M",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 941,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "CO",
          "type": 2,
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "CO",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CO",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CO",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "CO",
              "fareCode": {
                "code": "I7515175",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1N",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1305,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "3N",
              "fareCode": {
                "code": "I0484775",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 518.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4N",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 799,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "YO",
              "fareCode": {
                "code": "I0484775",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "1V",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "1V",
              "fareCode": {
                "code": "I0484775",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "3V",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1241,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 499,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "4V",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 770,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
          "code": "2W",
          "type": 1,
          "fares": [
            {
              "status": 2,
              "upgradeFrom": "2W",
              "fareCode": {
                "code": "I1242394",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 813,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 2,
              "upgradeFrom": "2W",
              "fareCode": {
                "code": "I0484775",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 1220,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 478.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
                  "amount": 478.5,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I1242394",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            },
            {
              "status": 1,
              "upgradeFrom": "ZI",
              "fareCode": {
                "code": "I0484775",
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
                  "amount": 111.35,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 135,
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
