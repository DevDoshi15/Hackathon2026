# Read Reservation From Supplier (View)

**Path:** Read Reservation From Supplier > Read Reservation From Supplier (View)

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/readfromsupplier`

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
    "id": 65822,
    "cruiseReservation": {
        "id": 113802,
        "readPreferences": {
            "mode": "View", //Possible values are View/Modify/Pay
            "autoSyncOption": "NOLOCK" //Possible values are NOLOCK,LOCK,LOCKPRICES
        }
    },
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
Date: Thu, 02 Feb 2023 08:22:39 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "97f8276f-9e5d-42ce-847f-6081d69a7ef5",
      "timeStamp": "02-Feb-2023 03:22:32",
      "token": "EQTEMPKEN"
    },
    "agencyConfirmation": "EHD1KW6",
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Apr-2023 00:00:00",
        "arrivalDateTime": "08-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 6
      },
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "368181"
      },
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "id": 462517,
            "type": 2,
            "amount": 2120.66,
            "dueDate": "05-Feb-2023",
            "payments": [
              {
                "amount": 2120.66,
                "currency": "USD",
                "paymentDateTime": "31-Jan-2023"
              }
            ]
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "id": 462518,
            "type": 2,
            "amount": 2120.66,
            "dueDate": "05-Feb-2023",
            "payments": [
              {
                "amount": 2120.66,
                "currency": "USD",
                "paymentDateTime": "31-Jan-2023"
              }
            ]
          }
        ],
        "supplierPaymentSchedules": [
          {
            "id": 462516,
            "type": 2,
            "amount": 1846.74,
            "dueDate": "07-Feb-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 2858,
          "rph": -1
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 266,
          "rph": -1
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": -114,
          "rph": -1
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -880,
          "rph": -1
        },
        {
          "id": 7,
          "code": "1",
          "priority": 10,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1978,
          "rph": -1
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 1978,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1712,
          "rph": -1
        },
        {
          "id": 41,
          "code": "13",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 9,
          "code": "46",
          "priority": 23,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 10,
          "code": "44",
          "priority": 24,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 12,
          "code": "33",
          "priority": 25,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 142.66,
          "details": {
            "isTax": true
          },
          "rph": -1
        },
        {
          "id": 75,
          "code": "DSC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 76,
          "code": "SOC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 70,
          "code": "70",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 6,
          "code": "52",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 2120.66,
          "rph": -1
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 14,
          "code": "107",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 2120.66,
          "rph": -1
        },
        {
          "id": 42,
          "code": "59",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 75,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 2120.66,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 2120.66,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 450,
          "rph": -1
        },
        {
          "id": 26,
          "code": "IAR",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 63,
          "code": "3",
          "priority": 382,
          "displayType": 4,
          "amount": 2120.66,
          "rph": -1
        },
        {
          "id": 98,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 28,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 32,
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 273.92,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 1846.74,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1846.74,
          "rph": -1
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 2120.66,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 273.91999999999985,
          "rph": -1
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 2858,
          "rph": 1
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 266,
          "rph": 1
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": -114,
          "rph": 1
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -880,
          "rph": 1
        },
        {
          "id": 7,
          "code": "1",
          "priority": 10,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1978,
          "rph": 1
        },
        {
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 1978,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1712,
          "rph": 1
        },
        {
          "id": 41,
          "code": "13",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 9,
          "code": "46",
          "priority": 23,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 10,
          "code": "44",
          "priority": 24,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 12,
          "code": "33",
          "priority": 25,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 142.66,
          "details": {
            "isTax": true
          },
          "rph": 1
        },
        {
          "id": 70,
          "code": "70",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 75,
          "code": "DSC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 76,
          "code": "SOC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 6,
          "code": "52",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 2120.66,
          "rph": 1
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 14,
          "code": "107",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 2120.66,
          "rph": 1
        },
        {
          "id": 42,
          "code": "59",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 75,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 2120.66,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 2120.66,
          "rph": 1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 450,
          "rph": 1
        },
        {
          "id": 26,
          "code": "",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 63,
          "code": "3",
          "priority": 382,
          "displayType": 4,
          "amount": 2120.66,
          "rph": 1
        },
        {
          "id": 28,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 98,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 32,
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 273.92,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1846.74,
          "rph": 1
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 1846.74,
          "rph": 1
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 2120.66,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 273.91999999999985,
          "rph": 1
        }
      ],
      "syncInfo": {
        "apiSyncInfo": {
          "token": "pnckpvYE20iQUImD6FVdRZ/S7rth2O+c",
          "sessionId": "83895090-55e8-455d-9fd2-eebb61d8ef9c",
          "lastSyncOn": "02-Feb-2023 03:22:39"
        }
      },
      "usersInfo": {
        "createdFor": {
          "email": "",
          "name": "First TravelSA"
        },
        "createdBy": {}
      },
      "cruise": {
        "packageId": 1273059,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "name": "Royal Caribbean",
          "ships": [
            {
              "id": 14698,
              "name": "Odyssey of the Seas"
            }
          ]
        },
        "itinerary": {
          "id": 311261,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "02-Apr-2023 00:00:00",
          "arrivalDateTime": "08-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "OY06W145"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 513457307,
          "code": "4V",
          "name": "Interior Stateroom",
          "type": 1,
          "cabins": [
            {
              "description": "The color scheme for the cabin is: NUTRL. The cabin contains following furniture items: TWO TWINS CONVERT TO ROYAL KING, HAIR DRYER, ADJUSTABLE A/C, CLOSET, PRIVATE BATHROOM W/SHOWER, TV, PHONE, VANITY AREA W/CHAIR, NIGHTSTANDS, SOFA, SAFE",
              "number": "11267",
              "beds": [
                {
                  "code": "A",
                  "name": "2K",
                  "description": "Apart",
                  "type": 281
                },
                {
                  "code": "T",
                  "name": "2K",
                  "description": "Together",
                  "type": 282
                }
              ],
              "deck": {
                "id": 10904,
                "name": "Deck 11",
                "description": "Adventure Ocean, Staterooms.\n"
              },
              "location": "",
              "occupancy": {
                "min": 0,
                "max": 2
              }
            }
          ],
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
                  "amount": 1978,
                  "type": "AVGPP",
                  "details": {
                    "nccfInclusive": true
                  }
                },
                {
                  "id": 3,
                  "amount": 142.66,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 380,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ],
          "details": {
            "styleClass": "#d1ab98"
          }
        }
      ],
      "dinings": [
        {
          "id": 1,
          "code": "M",
          "name": "05:15 PM",
          "status": 7,
          "tableSizeOptions": [
            0
          ]
        }
      ]
    },
    "customers": [
      {
        "firstName": "Hina",
        "middleName": "",
        "lastName": "Javed",
        "dateOfBirth": "16-Jun-2000",
        "age": 22,
        "pastPaxNumber": ""
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
