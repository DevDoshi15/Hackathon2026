# Modify Reservation

**Path:** Modify Reservation > Insurance & Special Service - Princess Cruise line > Modify Reservation

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/modify`

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
    "id": 69736,
    "cruiseReservation": {
        "id": 117716,
        "cruise": {
            "packageId": 1316566
        },
        "reservationReferences": {
            "confirmationNumber": "5WDN6H"
        },
        "categories": [
            {
                "code": "S5",
                "fare": {
                    "fareCode": {
                        "code": "NR3"
                    }
                },
                "cabins": [
                    {
                        "number": "D420"
                    }
                ]
            }
        ],
        "syncInfo": { // provide the syncInfo as received in the Read From Supplier API.
            "apiSyncInfo": {
                "token": "IxVy9Y5M20ime28DbeG1S5ErW/xLVG6x",
                "sessionId": "036f7ba6-e16d-4bb5-912b-5bfc4b546eb1",
                "lastSyncOn": "04-May-2023 07:01:49"
            }
        },
        "insurance": { //insurance can be found in Fare Availability Response and varies per cruiselines
            "code": "F",
            "type": 2
        },
        "services": [ // here we are adding new special services
            {
                "code": "1000",
                "type": "Anniversary",
                "ServiceDate": "01-Dec-2023"
            }
        ],
        "dinings": [
            {
                "id": 3,
                "code": "8",
                "name": "Open Seating",
                "status": 1
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970",
            "ContactInfo": {
                "Email": "john@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "416-555-4566"
                }
            },
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                },
                "city": {
                    "id": "MIA"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "ContactInfo": {
                "Email": "maria@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "416-555-4566"
                }
            },
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                },
                "city": {
                    "id": "MIA"
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
Date: Thu, 04 May 2023 11:07:09 GMT
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
      "requestId": "6f5dac0b-792d-4098-bc4a-15150c5093b8",
      "timeStamp": "04-May-2023 07:07:02",
      "token": "EQTEMPKEN"
    },
    "id": 69736,
    "agencyConfirmation": "L3148JS",
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Dec-2023 00:00:00",
        "arrivalDateTime": "04-Dec-2023 00:00:00",
        "departureCityId": "BNE",
        "arrivalCityId": "BNE",
        "duration": 3
      },
      "id": 117716,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "5WDN6H"
      },
      "customerReferences": [
        {
          "ageGroup": "Adult",
          "odyCustomerRef": 57895,
          "isPrimaryContact": true
        },
        {
          "ageGroup": "Adult",
          "odyCustomerRef": 57894
        }
      ],
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "id": 471233,
            "type": 0,
            "amount": 400,
            "dueDate": "05-May-2023 23:59:00"
          },
          {
            "id": 471234,
            "type": 1,
            "amount": 2832.24,
            "dueDate": "27-Aug-2023 23:59:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "id": 471235,
            "type": 0,
            "amount": 400,
            "dueDate": "05-May-2023 23:59:00"
          },
          {
            "id": 471236,
            "type": 1,
            "amount": 2832.24,
            "dueDate": "27-Aug-2023 23:59:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "id": 471231,
            "type": 0,
            "amount": 400,
            "dueDate": "07-May-2023 23:59:00"
          },
          {
            "id": 471232,
            "type": 1,
            "amount": 2383.7,
            "dueDate": "17-Sep-2023 23:59:00"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "AMCT",
          "amount": 3016,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "NCFR",
          "amount": 150,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 3016,
          "priority": 10,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 48,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 46,
          "code": "",
          "amount": 3016,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 2866,
          "priority": 16,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 3,
          "code": "TXFS",
          "amount": 216.24,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": -1
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 17,
          "code": "",
          "amount": 3232.24,
          "priority": 100,
          "display": true,
          "rph": -1
        },
        {
          "id": 86,
          "code": "",
          "amount": 0,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 23,
          "code": "",
          "amount": 3232.24,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 3232.24,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 3232.24,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 400,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 26,
          "code": "PMTS",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 62,
          "code": "",
          "amount": 3232.24,
          "priority": 382,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 32,
          "code": "COMM",
          "amount": 448.54,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "amount": 2783.7,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 2783.7,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "amount": 3232.24,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "amount": 448.53999999999996,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 137,
          "code": "GSTA",
          "amount": 62.48,
          "priority": 610,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 110,
          "code": "GSTT",
          "amount": 0,
          "priority": 610,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "AMCT",
          "amount": 1508,
          "priority": 5,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 2,
          "code": "NCFR",
          "amount": 75,
          "priority": 6,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 45,
          "code": "",
          "amount": 1508,
          "priority": 10,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 48,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 46,
          "code": "",
          "amount": 1508,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 114,
          "code": "",
          "amount": 1433,
          "priority": 16,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 3,
          "code": "TXFS",
          "amount": 108.12,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 17,
          "code": "",
          "amount": 1616.12,
          "priority": 100,
          "display": true,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 86,
          "code": "",
          "amount": 0,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 23,
          "code": "",
          "amount": 1616.12,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 47,
          "code": "",
          "amount": 1616.12,
          "priority": 355,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 1616.12,
          "priority": 359,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 200,
          "priority": 360,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 62,
          "code": "",
          "amount": 1616.12,
          "priority": 382,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 32,
          "code": "COMM",
          "amount": 224.27,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 65,
          "code": "",
          "amount": 1391.85,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 1391.85,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 83,
          "code": "",
          "amount": 224.26999999999998,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 112,
          "code": "",
          "amount": 1616.12,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 110,
          "code": "GSTT",
          "amount": 0,
          "priority": 610,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 137,
          "code": "GSTA",
          "amount": 31.24,
          "priority": 610,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 1,
          "code": "AMCT",
          "amount": 1508,
          "priority": 5,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 2,
          "code": "NCFR",
          "amount": 75,
          "priority": 6,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 45,
          "code": "",
          "amount": 1508,
          "priority": 10,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 48,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 46,
          "code": "",
          "amount": 1508,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 114,
          "code": "",
          "amount": 1433,
          "priority": 16,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 3,
          "code": "TXFS",
          "amount": 108.12,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 17,
          "code": "",
          "amount": 1616.12,
          "priority": 100,
          "display": true,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 86,
          "code": "",
          "amount": 0,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 23,
          "code": "",
          "amount": 1616.12,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 47,
          "code": "",
          "amount": 1616.12,
          "priority": 355,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 1616.12,
          "priority": 359,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 200,
          "priority": 360,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 62,
          "code": "",
          "amount": 1616.12,
          "priority": 382,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 98,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 28,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 32,
          "code": "COMM",
          "amount": 224.27,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 65,
          "code": "",
          "amount": 1391.85,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 1391.85,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 61,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 599,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 83,
          "code": "",
          "amount": 224.26999999999998,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 112,
          "code": "",
          "amount": 1616.12,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 110,
          "code": "GSTT",
          "amount": 0,
          "priority": 610,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 137,
          "code": "GSTA",
          "amount": 31.24,
          "priority": 610,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        }
      ],
      "insurances": [
        {
          "code": "F",
          "type": "Supplier"
        }
      ],
      "syncInfo": {
        "apiSyncInfo": {
          "token": "b+x8tI9M20iS3ms2I4QISbOIDpXLAmWc",
          "sessionId": "366bde92-8423-4908-b388-0e95cb02659c",
          "lastSyncOn": "04-May-2023 07:07:09"
        }
      },
      "usersInfo": {},
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1316566,
        "packageTourId": -1,
        "cruiseline": {
          "id": 7,
          "ships": [
            {
              "id": 58
            }
          ]
        },
        "itinerary": {
          "id": 334555,
          "destination": {
            "id": 29
          }
        },
        "voyage": {
          "departureDateTime": "01-Dec-2023 00:00:00",
          "arrivalDateTime": "04-Dec-2023 00:00:00",
          "departureCityId": "BNE",
          "arrivalCityId": "BNE",
          "code": "6319"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 56674,
          "code": "S5",
          "cabins": [
            {
              "number": "D420",
              "isGuarantee": true
            }
          ]
        }
      ],
      "serviceCollection": {
        "services": [
          {
            "code": "1000",
            "type": "Anniversary",
            "serviceDate": "01-Dec-2023",
            "customerReferences": [
              {
                "rph": 1,
                "odyCustomerRef": 57895
              },
              {
                "rph": 2,
                "odyCustomerRef": 57894
              }
            ]
          }
        ]
      },
      "dinings": [
        {
          "id": 3,
          "code": "8",
          "name": "Open Seating",
          "status": 1,
          "tableSizeOptions": [
            0
          ],
          "gratuityRequired": false
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "odyCustomerRef": 57895,
        "firstName": "John",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "age": 53,
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
        },
        "nationality": {},
        "contactInfo": {
          "email": "john@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "416-555-4566"
          },
          "phone2": {
            "countryCode": "1",
            "number": "416-555-4566"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "odyCustomerRef": 57894,
        "firstName": "Maria",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "age": 58,
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
        },
        "nationality": {},
        "contactInfo": {
          "email": "maria@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "416-555-4566"
          },
          "phone2": {
            "countryCode": "1",
            "number": "416-555-4566"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
