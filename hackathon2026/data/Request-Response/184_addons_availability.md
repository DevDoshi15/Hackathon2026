# AddOns Availability

**Path:** Create Reservation > Create Reservation With AddOns > AddOns Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listaddons`

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
            "id": 1,
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
            "packageId": 1324816
        },
        "categories": [
            {
                "code": "IR1",
                "fare": {
                    "fareCode": {
                        "code": "EZAT35DZE"
                    }
                },
                "cabins": [
                    {
                        "number": "9068"
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970",
            "age": 52,
            "address": {
                "city": {
                    "id": "MIA"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "age": 57,
            "address": {
                "city": {
                    "id": "MIA"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Thu, 16 Mar 2023 10:03:17 GMT
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
      "requestId": "b8a50c8b-6d1f-4a0b-946b-ed69ca68a722",
      "timeStamp": "16-Mar-2023 06:03:08"
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
          "ageGroup": "Adult",
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
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
      "addOns": [
        {
          "code": "ALLDIG59",
          "name": "All Inclusive Digital",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "CELEBPCK",
          "name": "MSC Celebrations Photo Package Â Make any occasion unforgettable.",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "MM10PHOT",
          "name": "Mix&Match 10 photos",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "MM20PHOT",
          "name": "Mix&Match 20 photos",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "MM30PHOT",
          "name": "Mix&Match 30 photos",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "MM5PHOTS",
          "name": "Mix&Match 5 photos",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "PHTWED01",
          "name": "Wedding Photo Package",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "PHTWED02",
          "name": "Wedding Storybook Package",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "PHTWED03",
          "name": "Wedding Storybook and Framed Photo Package",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "PHTWED04",
          "name": "Wedding and Shoreside Photo Package",
          "startDate": "01-Apr-2023",
          "type": 25,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "B10213M",
          "name": "Browse - 1 device",
          "startDate": "01-Apr-2023",
          "type": 12,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "B20213M",
          "name": "Browse - 2 devices",
          "startDate": "01-Apr-2023",
          "type": 12,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "B30213M",
          "name": "Browse - 3 devices",
          "startDate": "01-Apr-2023",
          "type": 12,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "B40213M",
          "name": "Browse - 4 devices",
          "startDate": "01-Apr-2023",
          "type": 12,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "BALI50",
          "name": "TRADITIONAL BALINESE MASSAGE - 50 min",
          "startDate": "01-Apr-2023",
          "type": 30,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "BALIHLS",
          "name": "BALI MASSAGE WITH HOT LAVA STONES",
          "startDate": "01-Apr-2023",
          "type": 30,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "BS10213M",
          "name": "Browse & Stream - 1 device",
          "startDate": "01-Apr-2023",
          "type": 12,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "BS20213M",
          "name": "Browse & Stream - 2 devices",
          "startDate": "01-Apr-2023",
          "type": 12,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "BS30213M",
          "name": "Browse & Stream - 3 devices",
          "startDate": "01-Apr-2023",
          "type": 12,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "BS40213M",
          "name": "Browse & Stream - 4 devices",
          "startDate": "01-Apr-2023",
          "type": 12,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "NSPATAIS",
          "name": "THERMAL AREA CRUISE PASS",
          "startDate": "01-Apr-2023",
          "type": 30,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "PTNS09D",
          "name": "PERSONAL TRAINER PROGRAM",
          "startDate": "01-Apr-2023",
          "type": 30,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SPANAIL",
          "name": "SPA MANICURE AND PEDICURE TREATMENT",
          "startDate": "01-Apr-2023",
          "type": 30,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "446FW22",
          "name": "EASY PLUS PACKAGE",
          "startDate": "01-Apr-2023",
          "type": 6,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "447FW22",
          "name": "PREMIUM EXTRA PACKAGE",
          "startDate": "01-Apr-2023",
          "type": 6,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "448FW22",
          "name": "ALCOHOL-FREE PACKAGE",
          "startDate": "01-Apr-2023",
          "type": 6,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "471NW22",
          "name": "EASY PACKAGE",
          "startDate": "01-Apr-2023",
          "type": 6,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SB025USD",
          "name": "Shipboard Credit 25 USD - Non Refundable",
          "startDate": "01-Apr-2023",
          "type": 27,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SB050GVS",
          "name": "Shipboard credit 50 Eur/Usd - 40 Gbp",
          "startDate": "01-Apr-2023",
          "type": 27,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SB050USD",
          "name": "Shipboard Credit 50 USD - Non Refundable",
          "startDate": "01-Apr-2023",
          "type": 27,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SB075USD",
          "name": "Shipboard Credit 75 USD - Non Refundable",
          "startDate": "01-Apr-2023",
          "type": 27,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SB100USD",
          "name": "Shipboard Credit 100 USD - Non Refundable",
          "startDate": "01-Apr-2023",
          "type": 27,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SB150USD",
          "name": "Shipboard Credit 150 USD - Non Refundable",
          "startDate": "01-Apr-2023",
          "type": 27,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SC2223ME",
          "name": "LBL_CruiseAddON_PayNow",
          "startDate": "01-Apr-2023",
          "type": 28,
          "customerReferences": [
            {
              "rph": 1
            },
            {
              "rph": 2
            }
          ],
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
          "combinableCodes": []
        },
        {
          "code": "SC2223ME_Onboard",
          "name": "LBL_CruiseAddON_Onboard",
          "startDate": "01-Apr-2023",
          "type": 28,
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
          "combinableCodes": []
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "age": 52,
        "address": {
          "city": {
            "id": "MIA"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      },
      {
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "age": 57,
        "address": {
          "city": {
            "id": "MIA"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
