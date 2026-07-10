# Price Reservation

**Path:** Create Reservation > Occupancy Based Samples > Single Occupancy (NCL) > Price Reservation

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listprices`

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
            "packageId": 1238898
        },
        "categories": [
            {
                "code": "IA",
                "fare": {
                    "fareCode": {
                        "code": "BESTFARE"
                    }
                }
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
                "country": {
                    "id": "US"
                }
            }
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
Date: Thu, 23 Mar 2023 12:06:23 GMT
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
      "requestId": "f673d36c-37a0-451f-8d62-48945ee17177",
      "timeStamp": "23-Mar-2023 08:06:21",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "05-May-2023 00:00:00",
        "arrivalDateTime": "08-May-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 3
      },
      "pos": {
        "id": 2112,
        "apiId": "NCL",
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
        }
      ],
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "type": 2,
            "amount": 1679.26,
            "dueDate": "23-Mar-2023"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 1679.26,
            "dueDate": "23-Mar-2023"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 1477.76,
            "dueDate": "23-Mar-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 1916.2,
          "rph": -1
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 143,
          "rph": -1
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -436.8,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1479.4,
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
          "amount": 1479.4,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1336.4,
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
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 199.86,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": -1
        },
        {
          "id": 6,
          "code": "",
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
          "amount": 1679.26,
          "rph": -1
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 16,
          "code": "15",
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
          "amount": 1679.26,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 1679.26,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 1679.26,
          "rph": -1
        },
        {
          "id": 24,
          "code": "",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 26,
          "code": "2",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 62,
          "code": "",
          "priority": 382,
          "displayType": 4,
          "amount": 1679.26,
          "rph": -1
        },
        {
          "id": 98,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
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
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 201.5,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 36,
          "code": "85",
          "priority": 510,
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1477.76,
          "rph": -1
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1679.26,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 201.5,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 1916.2,
          "rph": 1
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 143,
          "rph": 1
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -436.8,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 1479.4,
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
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
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
          "amount": 1479.4,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 1336.4,
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
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 199.86,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": 1
        },
        {
          "id": 6,
          "code": "",
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
          "amount": 1679.26,
          "rph": 1
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 16,
          "code": "15",
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
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
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
          "amount": 1679.26,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 1679.26,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 1679.26,
          "rph": 1
        },
        {
          "id": 24,
          "code": "",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 26,
          "code": "2",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 62,
          "code": "",
          "priority": 382,
          "displayType": 4,
          "amount": 1679.26,
          "rph": 1
        },
        {
          "id": 28,
          "code": "",
          "priority": 500,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
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
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 201.5,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 36,
          "code": "85",
          "priority": 510,
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1477.76,
          "rph": 1
        },
        {
          "id": 61,
          "code": "",
          "priority": 599,
          "displayType": 4,
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1679.26,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 201.5,
          "rph": 1
        }
      ],
      "cruise": {
        "packageId": 1238898,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 1179
            }
          ]
        },
        "itinerary": {
          "id": 363194,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "05-May-2023 00:00:00",
          "arrivalDateTime": "08-May-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "17183730"
        },
        "transportationType": 29
      },
      "addOns": [
        {
          "code": "34CHO",
          "name": "FAS_Taxes Only 3-4",
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
          "combinableCodes": [
            "ALL4CHO",
            "BVSXIN",
            "DISC35",
            "DISXIN",
            "EASYFARE",
            "FLEXNET",
            "INTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "ALL4CHO",
          "name": "FAS_Beverage, Dining, Internet, $50 per port Shore Ex Credit",
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
          "combinableCodes": [
            "34CHO",
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "BVSXIN",
          "name": "FAS_Beverage, Internet, $50 per port Shore Ex Credit",
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
          "combinableCodes": [
            "34CHO",
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "DISXIN",
          "name": "FAS_Dining Package, Internet, $50 per port Shore Ex Credit",
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
          "combinableCodes": [
            "34CHO",
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "EASYFARE",
          "name": "OTH_Early Booking Fare - Upgrades - A/S",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC35",
            "DISXIN",
            "FLEXNET",
            "INTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "FLEXNET",
          "name": "OTH_NET RATES",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC35",
            "DISXIN",
            "EASYFARE",
            "INTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "INTSHO",
          "name": "FAS_Internet Package and $50 per port Shore Ex Credit",
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
          "combinableCodes": [
            "34CHO",
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "KOSHER MEAL",
          "name": "OTH_Kosher Meal",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC35",
            "DISXIN",
            "EASYFARE",
            "FLEXNET",
            "INTSHO",
            "PPSRVCHG"
          ]
        },
        {
          "code": "PPSRVCHG",
          "name": "OTH_Prepaid Service Charges",
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
          "combinableCodes": [
            "34CHO",
            "ALL4CHO",
            "BVSXIN",
            "DISC35",
            "DISXIN",
            "EASYFARE",
            "FLEXNET",
            "INTSHO",
            "KOSHER MEAL"
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
          "country": {
            "id": "US"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
