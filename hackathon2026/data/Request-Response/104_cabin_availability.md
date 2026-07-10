# Cabin Availability

**Path:** Create Reservation > Create Reservation With Insurance > Cabin Availability

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
            "packageId": 1324816
        },
        "categories": [
            {
                "code": "IR1",
                "fare": {
                    "fareCode": {
                        "code": "GRUS306R3"
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
Date: Fri, 17 Feb 2023 14:46:17 GMT
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
      "requestId": "7aa2510f-5bbd-465d-a3db-799749bb8eec",
      "timeStamp": "17-Feb-2023 09:46:02",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Apr-2023 00:00:00",
        "arrivalDateTime": "08-Apr-2023 00:00:00",
        "departureCityId": "MRS",
        "arrivalCityId": "MRS",
        "duration": 7
      },
      "pos": {
        "id": 2119,
        "apiId": "MSC",
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
        "packageId": 1324816,
        "packageTourId": -1,
        "cruiseline": {
          "id": 982,
          "ships": [
            {
              "id": 14091
            }
          ]
        },
        "itinerary": {
          "id": 362627,
          "destination": {
            "id": 18
          }
        },
        "voyage": {
          "departureDateTime": "01-Apr-2023 00:00:00",
          "arrivalDateTime": "08-Apr-2023 00:00:00",
          "departureCityId": "MRS",
          "arrivalCityId": "MRS",
          "code": "GR20230401MRSMRS"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "9014",
          "occupancy": {
            "min": 0,
            "max": 0
          }
        },
        {
          "number": "9068",
          "isAccessible": true,
          "occupancy": {
            "min": 0,
            "max": 0
          }
        }
      ],
      "addOns": [
        {
          "code": "ALLDIG59",
          "name": "All Inclusive Digital",
          "prices": [
            {
              "amount": 105,
              "type": "AVGPP"
            },
            {
              "amount": 210,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "CELEBPCK",
          "name": "MSC Celebrations Photo Package Â Make any occasion unforgettable.",
          "prices": [
            {
              "amount": 203,
              "type": "AVGPP"
            },
            {
              "amount": 406,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "MM10PHOT",
          "name": "Mix&Match 10 photos",
          "prices": [
            {
              "amount": 108,
              "type": "AVGPP"
            },
            {
              "amount": 216,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "MM20PHOT",
          "name": "Mix&Match 20 photos",
          "prices": [
            {
              "amount": 143,
              "type": "AVGPP"
            },
            {
              "amount": 286,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "MM30PHOT",
          "name": "Mix&Match 30 photos",
          "prices": [
            {
              "amount": 179,
              "type": "AVGPP"
            },
            {
              "amount": 358,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "MM5PHOTS",
          "name": "Mix&Match 5 photos",
          "prices": [
            {
              "amount": 72,
              "type": "AVGPP"
            },
            {
              "amount": 144,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "PHTWED01",
          "name": "Wedding Photo Package",
          "prices": [
            {
              "amount": 566,
              "type": "AVGPP"
            },
            {
              "amount": 1132,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "PHTWED02",
          "name": "Wedding Storybook Package",
          "prices": [
            {
              "amount": 1012,
              "type": "AVGPP"
            },
            {
              "amount": 2024,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "PHTWED03",
          "name": "Wedding Storybook and Framed Photo Package",
          "prices": [
            {
              "amount": 1100,
              "type": "AVGPP"
            },
            {
              "amount": 2200,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "PHTWED04",
          "name": "Wedding and Shoreside Photo Package",
          "prices": [
            {
              "amount": 1600,
              "type": "AVGPP"
            },
            {
              "amount": 3200,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 25,
          "combinableCodes": []
        },
        {
          "code": "B10213M",
          "name": "Browse - 1 device",
          "prices": [
            {
              "amount": 62.09,
              "type": "AVGPP"
            },
            {
              "amount": 124.18,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 12,
          "combinableCodes": []
        },
        {
          "code": "B20213M",
          "name": "Browse - 2 devices",
          "prices": [
            {
              "amount": 99.33,
              "type": "AVGPP"
            },
            {
              "amount": 198.66,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 12,
          "combinableCodes": []
        },
        {
          "code": "B30213M",
          "name": "Browse - 3 devices",
          "prices": [
            {
              "amount": 130.34,
              "type": "AVGPP"
            },
            {
              "amount": 260.68,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 12,
          "combinableCodes": []
        },
        {
          "code": "B40213M",
          "name": "Browse - 4 devices",
          "prices": [
            {
              "amount": 148.96,
              "type": "AVGPP"
            },
            {
              "amount": 297.92,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 12,
          "combinableCodes": []
        },
        {
          "code": "BALI50",
          "name": "TRADITIONAL BALINESE MASSAGE - 50 min",
          "prices": [
            {
              "amount": 131,
              "type": "AVGPP"
            },
            {
              "amount": 262,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 30,
          "combinableCodes": []
        },
        {
          "code": "BALIHLS",
          "name": "BALI MASSAGE WITH HOT LAVA STONES",
          "prices": [
            {
              "amount": 125,
              "type": "AVGPP"
            },
            {
              "amount": 250,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 30,
          "combinableCodes": []
        },
        {
          "code": "BS10213M",
          "name": "Browse & Stream - 1 device",
          "prices": [
            {
              "amount": 93.17,
              "type": "AVGPP"
            },
            {
              "amount": 186.34,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 12,
          "combinableCodes": []
        },
        {
          "code": "BS20213M",
          "name": "Browse & Stream - 2 devices",
          "prices": [
            {
              "amount": 161.49,
              "type": "AVGPP"
            },
            {
              "amount": 322.98,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 12,
          "combinableCodes": []
        },
        {
          "code": "BS30213M",
          "name": "Browse & Stream - 3 devices",
          "prices": [
            {
              "amount": 223.58,
              "type": "AVGPP"
            },
            {
              "amount": 447.16,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 12,
          "combinableCodes": []
        },
        {
          "code": "BS40213M",
          "name": "Browse & Stream - 4 devices",
          "prices": [
            {
              "amount": 273.28,
              "type": "AVGPP"
            },
            {
              "amount": 546.56,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 12,
          "combinableCodes": []
        },
        {
          "code": "NSPATAIS",
          "name": "THERMAL AREA CRUISE PASS",
          "prices": [
            {
              "amount": 110,
              "type": "AVGPP"
            },
            {
              "amount": 220,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 30,
          "combinableCodes": []
        },
        {
          "code": "PTNS09D",
          "name": "PERSONAL TRAINER PROGRAM",
          "prices": [
            {
              "amount": 207,
              "type": "AVGPP"
            },
            {
              "amount": 414,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 30,
          "combinableCodes": []
        },
        {
          "code": "SPANAIL",
          "name": "SPA MANICURE AND PEDICURE TREATMENT",
          "prices": [
            {
              "amount": 90,
              "type": "AVGPP"
            },
            {
              "amount": 180,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 30,
          "combinableCodes": []
        },
        {
          "code": "446FW22",
          "name": "EASY PLUS PACKAGE",
          "prices": [
            {
              "amount": 357,
              "type": "AVGPP"
            },
            {
              "amount": 714,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 6,
          "combinableCodes": []
        },
        {
          "code": "447FW22",
          "name": "PREMIUM EXTRA PACKAGE",
          "prices": [
            {
              "amount": 497,
              "type": "AVGPP"
            },
            {
              "amount": 994,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 6,
          "combinableCodes": []
        },
        {
          "code": "448FW22",
          "name": "ALCOHOL-FREE PACKAGE",
          "prices": [
            {
              "amount": 182,
              "type": "AVGPP"
            },
            {
              "amount": 364,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 6,
          "combinableCodes": []
        },
        {
          "code": "471NW22",
          "name": "EASY PACKAGE",
          "prices": [
            {
              "amount": 266,
              "type": "AVGPP"
            },
            {
              "amount": 532,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 6,
          "combinableCodes": []
        },
        {
          "code": "SB025USD",
          "name": "Shipboard Credit 25 USD - Non Refundable",
          "prices": [
            {
              "amount": 25,
              "type": "AVGPP"
            },
            {
              "amount": 50,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 27,
          "combinableCodes": []
        },
        {
          "code": "SB050GVS",
          "name": "Shipboard credit 50 Eur/Usd - 40 Gbp",
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
          "startDate": "01-Apr-2023",
          "type": 27,
          "combinableCodes": []
        },
        {
          "code": "SB050USD",
          "name": "Shipboard Credit 50 USD - Non Refundable",
          "prices": [
            {
              "amount": 50,
              "type": "AVGPP"
            },
            {
              "amount": 100,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 27,
          "combinableCodes": []
        },
        {
          "code": "SB075USD",
          "name": "Shipboard Credit 75 USD - Non Refundable",
          "prices": [
            {
              "amount": 75,
              "type": "AVGPP"
            },
            {
              "amount": 150,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 27,
          "combinableCodes": []
        },
        {
          "code": "SB100USD",
          "name": "Shipboard Credit 100 USD - Non Refundable",
          "prices": [
            {
              "amount": 100,
              "type": "AVGPP"
            },
            {
              "amount": 200,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 27,
          "combinableCodes": []
        },
        {
          "code": "SB150USD",
          "name": "Shipboard Credit 150 USD - Non Refundable",
          "prices": [
            {
              "amount": 150,
              "type": "AVGPP"
            },
            {
              "amount": 300,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 27,
          "combinableCodes": []
        },
        {
          "code": "SC2223ME",
          "name": "LBL_CruiseAddON_PayNow",
          "prices": [
            {
              "amount": 84,
              "type": "AVGPP"
            },
            {
              "amount": 168,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 28,
          "combinableCodes": []
        },
        {
          "code": "SC2223ME_Onboard",
          "name": "LBL_CruiseAddON_Onboard",
          "prices": [
            {
              "amount": 84,
              "type": "AVGPP"
            },
            {
              "amount": 168,
              "type": "TOTAL"
            }
          ],
          "startDate": "01-Apr-2023",
          "type": 28,
          "combinableCodes": []
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
