# Price Reservation

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 4 – All Adults (NCL) > Price Reservation

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
            "packageId": 1312610,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "H5",
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
            "dateOfBirth": "02-Jan-1992",
            "age": 31,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1993",
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 3,
            "firstName": "Johny",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1993",
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 4,
            "firstName": "Johny",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1983",
            "age": 40,
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
Date: Fri, 31 Mar 2023 08:51:18 GMT
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
      "requestId": "d4796017-dc11-4bf5-a34a-63ca801a4c13",
      "timeStamp": "31-Mar-2023 04:51:16",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "27-Jun-2023 00:00:00",
        "arrivalDateTime": "08-Jul-2023 00:00:00",
        "departureCityId": "SEA",
        "arrivalCityId": "SEA",
        "duration": 11
      },
      "pos": {
        "id": 2250,
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
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
        },
        {
          "rph": 3,
          "ageGroup": "Adult"
        },
        {
          "rph": 4,
          "ageGroup": "Adult"
        }
      ],
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "type": 2,
            "amount": 36032,
            "dueDate": "31-Mar-2023"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "type": 2,
            "amount": 36032,
            "dueDate": "31-Mar-2023"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "type": 2,
            "amount": 31092.44,
            "dueDate": "31-Mar-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 50028,
          "rph": -1
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 962,
          "rph": -1
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -15187.2,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 34840.8,
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
          "amount": 34840.8,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 33878.8,
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
          "amount": 1191.2,
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
          "amount": 36032,
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
          "amount": 36032,
          "rph": -1
        },
        {
          "id": 42,
          "code": "96",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 0,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 36032,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 36032,
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
          "amount": 36032,
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
          "amount": 4939.56,
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
          "amount": 31092.44,
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
          "amount": 36032,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 4939.560000000001,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 22157,
          "rph": 1
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 240.5,
          "rph": 1
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -7174.3,
          "rph": 1
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 14982.7,
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
          "amount": 14982.7,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 14742.2,
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
          "amount": 299.8,
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
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 15282.5,
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
          "amount": 15282.5,
          "rph": 1
        },
        {
          "id": 42,
          "code": "96",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 15282.5,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 15282.5,
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
          "amount": 15282.5,
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
          "amount": 1234.89,
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
          "amount": 14047.61,
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
          "amount": 15282.5,
          "rph": 1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1234.8899999999994,
          "rph": 1
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 22157,
          "rph": 2
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 240.5,
          "rph": 2
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -7174.3,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 14982.7,
          "rph": 2
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 14982.7,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 14742.2,
          "rph": 2
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 299.8,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": 2
        },
        {
          "id": 6,
          "code": "",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 15282.5,
          "rph": 2
        },
        {
          "id": 16,
          "code": "15",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 15282.5,
          "rph": 2
        },
        {
          "id": 42,
          "code": "96",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 15282.5,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 15282.5,
          "rph": 2
        },
        {
          "id": 24,
          "code": "",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 26,
          "code": "2",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 62,
          "code": "",
          "priority": 382,
          "displayType": 4,
          "amount": 15282.5,
          "rph": 2
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
          "rph": 2
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
          "rph": 2
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 1234.89,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 2
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
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 14047.61,
          "rph": 2
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
          "rph": 2
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 15282.5,
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1234.8899999999994,
          "rph": 2
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 2857,
          "rph": 3
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 240.5,
          "rph": 3
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -419.3,
          "rph": 3
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 2437.7,
          "rph": 3
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 2437.7,
          "rph": 3
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 2197.2,
          "rph": 3
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 295.8,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": 3
        },
        {
          "id": 6,
          "code": "",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 2733.5,
          "rph": 3
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 16,
          "code": "15",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 2733.5,
          "rph": 3
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 2733.5,
          "rph": 3
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 2733.5,
          "rph": 3
        },
        {
          "id": 24,
          "code": "",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 26,
          "code": "2",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 3
        },
        {
          "id": 62,
          "code": "",
          "priority": 382,
          "displayType": 4,
          "amount": 2733.5,
          "rph": 3
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
          "rph": 3
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
          "rph": 3
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 1234.89,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 3
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
          "rph": 3
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1498.61,
          "rph": 3
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
          "rph": 3
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 2733.5,
          "rph": 3
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1234.89,
          "rph": 3
        },
        {
          "id": 1,
          "code": "5",
          "priority": 5,
          "displayType": 4,
          "amount": 2857,
          "rph": 4
        },
        {
          "id": 2,
          "code": "POC",
          "priority": 6,
          "displayType": 4,
          "amount": 240.5,
          "rph": 4
        },
        {
          "id": 5,
          "code": "34",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -419.3,
          "rph": 4
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 2437.7,
          "rph": 4
        },
        {
          "id": 122,
          "code": "",
          "priority": 11,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 49,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 2437.7,
          "rph": 4
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 2197.2,
          "rph": 4
        },
        {
          "id": 54,
          "code": "",
          "priority": 22,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 295.8,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "rph": 4
        },
        {
          "id": 6,
          "code": "",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 2733.5,
          "rph": 4
        },
        {
          "id": 86,
          "code": "",
          "priority": 100,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 16,
          "code": "15",
          "priority": 105,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 60,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 84,
          "code": "",
          "priority": 200,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 40,
          "code": "",
          "priority": 300,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 23,
          "code": "",
          "priority": 350,
          "display": true,
          "displayType": 1,
          "amount": 2733.5,
          "rph": 4
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 2733.5,
          "rph": 4
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 2733.5,
          "rph": 4
        },
        {
          "id": 24,
          "code": "",
          "priority": 360,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 26,
          "code": "2",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 4
        },
        {
          "id": 62,
          "code": "",
          "priority": 382,
          "displayType": 4,
          "amount": 2733.5,
          "rph": 4
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
          "rph": 4
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
          "rph": 4
        },
        {
          "id": 32,
          "code": "66",
          "priority": 509,
          "displayType": 4,
          "amount": 1234.89,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "rph": 4
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
          "rph": 4
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 1498.61,
          "rph": 4
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
          "rph": 4
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 2733.5,
          "rph": 4
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 1234.89,
          "rph": 4
        }
      ],
      "cruise": {
        "packageId": 1312610,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 13670
            }
          ]
        },
        "itinerary": {
          "id": 351639,
          "destination": {
            "id": 1
          }
        },
        "tourCode": "18707348",
        "voyage": {
          "departureDateTime": "01-Jul-2023 00:00:00",
          "arrivalDateTime": "08-Jul-2023 00:00:00",
          "departureCityId": "SEA",
          "arrivalCityId": "SEA",
          "code": "18506272"
        },
        "transportationType": 28
      },
      "addOns": [
        {
          "code": "CHOALL4M",
          "name": "FAS_Ultimate Beverage, Dining Package, Internet, Shorex Credit",
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
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG",
            "FITOBC"
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
            "CHOALL4M",
            "DISC35",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG",
            "FITOBC"
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
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "HSBVSXIN",
          "name": "FAS_Ultimate Beverage, Internet, Shorex Credit",
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
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG",
            "FITOBC"
          ]
        },
        {
          "code": "HSDISXIN",
          "name": "FAS_Specialty Dining Package, Internet, Shorex Credit",
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
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG",
            "FITOBC"
          ]
        },
        {
          "code": "HSINTSHO",
          "name": "FAS_Internet, Shorex Credit",
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
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "KOSHER MEAL",
            "PPSRVCHG",
            "FITOBC"
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
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "PPSRVCHG",
            "FITOBC"
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
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "FITOBC"
          ]
        },
        {
          "code": "FITOBC",
          "name": "OTH_FIT ONLY- Onboard Credit Offer",
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
            "CHOALL4M",
            "DISC35",
            "EASYFARE",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1992",
        "age": 31,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1993",
        "age": 30,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 3,
        "firstName": "Johny",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1993",
        "age": 30,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 4,
        "firstName": "Johny",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1983",
        "age": 40,
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
