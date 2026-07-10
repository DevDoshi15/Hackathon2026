# SilverSea Cruise line

**Path:** Read Reservation From Supplier > Cancellation Policies > SilverSea Cruise line

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
//Cancellation policies can be found under "cancellationPolicies" element in the response
{
    "cruiseReservation": {
        "reservationReferences": {
            "confirmationNumber": "58123"
        },
        "cruise": {
            "cruiseline": {
                "id": 8115
            }
        },
        "ReadPreferences": {
            "Mode": "View"
        }
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Tue, 27 Jun 2023 15:27:29 GMT
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
      "requestId": "1197f640-e270-452a-8c10-241bef87f86c",
      "timeStamp": "27-Jun-2023 11:27:15"
    },
    "id": 71301,
    "agencyConfirmation": "EZOYBPV",
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Sep-2023 00:00:00",
        "arrivalDateTime": "08-Sep-2023 00:00:00",
        "departureCityId": "CIV",
        "arrivalCityId": "MCM",
        "duration": 7
      },
      "id": 119278,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "58123"
      },
      "reservationIndicators": {
        "modifyIndicators": [
          {
            "type": "Cabin",
            "value": false
          },
          {
            "type": "Bed",
            "value": false
          },
          {
            "type": "Insurance",
            "value": false
          },
          {
            "type": "Category",
            "value": false
          },
          {
            "type": "AddPassenger",
            "value": false
          },
          {
            "type": "RemovePassenger",
            "value": false
          },
          {
            "type": "Dining",
            "value": false
          },
          {
            "type": "AddOn",
            "value": false
          },
          {
            "type": "FareCode",
            "value": false
          },
          {
            "type": "SpecialService",
            "value": false
          },
          {
            "type": "Packages",
            "value": false
          },
          {
            "type": "LinkedBooking",
            "value": false
          }
        ]
      },
      "pos": {
        "id": 2475,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "B2B",
        "system": "Test",
        "apiId": "SSC"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 60288,
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 60289
        }
      ],
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "id": 477445,
            "type": 2,
            "amount": 27045,
            "dueDate": "06-Jun-2023 00:00:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "id": 477446,
            "type": 2,
            "amount": 27045,
            "dueDate": "06-Jun-2023 00:00:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "id": 477444,
            "type": 2,
            "amount": 23539.14,
            "dueDate": "08-Jun-2023 00:00:00"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "5",
          "amount": 27025,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "60",
          "amount": 378,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 27025,
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
          "amount": 25,
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
          "amount": 27025,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 26647,
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
          "code": "",
          "amount": 0,
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
          "amount": 27045,
          "priority": 100,
          "display": true,
          "rph": -1
        },
        {
          "id": 86,
          "code": "",
          "amount": 20,
          "priority": 100,
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
          "id": 60,
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
          "amount": 27045,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 27045,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "50",
          "amount": 27000,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "",
          "amount": 0,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 26,
          "code": "58",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 62,
          "code": "",
          "amount": 27000,
          "priority": 382,
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
          "id": 27,
          "code": "73",
          "amount": 3460.86,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
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
          "id": 32,
          "code": "11",
          "amount": 3460.86,
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
          "amount": 23539.14,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 66,
          "code": "40",
          "amount": 23539.14,
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
          "id": 83,
          "code": "",
          "amount": 3505.86,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "amount": 27045,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "amount": 13512.5,
          "priority": 5,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 2,
          "code": "60",
          "amount": 189,
          "priority": 6,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 45,
          "code": "",
          "amount": 13512.5,
          "priority": 10,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 48,
          "code": "",
          "amount": 12.5,
          "priority": 12,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 46,
          "code": "",
          "amount": 13512.5,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 114,
          "code": "",
          "amount": 13323.5,
          "priority": 16,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 3,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 17,
          "code": "",
          "amount": 13522.5,
          "priority": 100,
          "display": true,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 86,
          "code": "",
          "amount": 10,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 23,
          "code": "",
          "amount": 13522.5,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 47,
          "code": "",
          "amount": 13522.5,
          "priority": 355,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 50,
          "code": "50",
          "amount": 13500,
          "priority": 359,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 24,
          "code": "",
          "amount": 0,
          "priority": 360,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 62,
          "code": "",
          "amount": 13500,
          "priority": 382,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
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
          "odyCustomerRef": 60288
        },
        {
          "id": 27,
          "code": "73",
          "amount": 1730.43,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
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
          "odyCustomerRef": 60288
        },
        {
          "id": 32,
          "code": "11",
          "amount": 1730.43,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 65,
          "code": "",
          "amount": 11769.57,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 66,
          "code": "40",
          "amount": 11769.57,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
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
          "odyCustomerRef": 60288
        },
        {
          "id": 83,
          "code": "",
          "amount": 1752.93,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 112,
          "code": "",
          "amount": 13522.5,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 60288
        },
        {
          "id": 1,
          "code": "5",
          "amount": 13512.5,
          "priority": 5,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 2,
          "code": "60",
          "amount": 189,
          "priority": 6,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 45,
          "code": "",
          "amount": 13512.5,
          "priority": 10,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 48,
          "code": "",
          "amount": 12.5,
          "priority": 12,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 46,
          "code": "",
          "amount": 13512.5,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 114,
          "code": "",
          "amount": 13323.5,
          "priority": 16,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 3,
          "code": "",
          "amount": 0,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 17,
          "code": "",
          "amount": 13522.5,
          "priority": 100,
          "display": true,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 86,
          "code": "",
          "amount": 10,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 23,
          "code": "",
          "amount": 13522.5,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 47,
          "code": "",
          "amount": 13522.5,
          "priority": 355,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 50,
          "code": "50",
          "amount": 13500,
          "priority": 359,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 24,
          "code": "",
          "amount": 0,
          "priority": 360,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 62,
          "code": "",
          "amount": 13500,
          "priority": 382,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
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
          "odyCustomerRef": 60289
        },
        {
          "id": 27,
          "code": "73",
          "amount": 1730.43,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 500,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
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
          "odyCustomerRef": 60289
        },
        {
          "id": 32,
          "code": "11",
          "amount": 1730.43,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 65,
          "code": "",
          "amount": 11769.57,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 66,
          "code": "40",
          "amount": 11769.57,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
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
          "odyCustomerRef": 60289
        },
        {
          "id": 83,
          "code": "",
          "amount": 1752.93,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        },
        {
          "id": 112,
          "code": "",
          "amount": 13522.5,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 60289
        }
      ],
      "syncInfo": {
        "apiSyncInfo": {
          "token": "VAUtBSN320i9Dk1xi+HhSoUO9Az3Jer3",
          "sessionId": "714d0ebd-e18b-4ae1-850e-f40cf725eaf7",
          "lastSyncOn": "27-Jun-2023 11:27:29"
        }
      },
      "timeStamps": {
        "system": {
          "createdOn": "05-Jun-2023 10:05:30",
          "lastModifiedOn": "27-Jun-2023 11:13:54"
        }
      },
      "usersInfo": {
        "createdFor": {
          "name": "Online User",
          "contactInfo": {}
        },
        "createdBy": {}
      },
      "currencyInfo": {
        "currencyId": "USD"
      },
      "cruise": {
        "packageId": 1321223,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8115,
          "ships": [
            {
              "id": 15112
            }
          ]
        },
        "itinerary": {
          "id": 364030,
          "destination": {
            "id": 75
          }
        },
        "voyage": {
          "departureDateTime": "01-Sep-2023 00:00:00",
          "arrivalDateTime": "08-Sep-2023 00:00:00",
          "departureCityId": "CIV",
          "arrivalCityId": "MCM",
          "code": "SN230901007"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 667461773,
          "code": "MS",
          "type": 4,
          "cabins": [
            {
              "number": "9086",
              "beds": [],
              "deck": {
                "id": 13236,
                "name": "Deck 9",
                "description": ""
              }
            }
          ],
          "fares": [
            {
              "upgradeFrom": "MS",
              "status": -1,
              "fareCode": {
                "code": "03_29",
                "name": "SILVER PRIVILEGE FARE",
                "externalSessionInfo": {
                  "externalId": "03"
                },
                "type": 0,
                "refundableType": 1,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "qualifierCodes": ""
                }
              }
            }
          ]
        }
      ],
      "addOns": [
        {
          "code": "E",
          "name": "Economy Class Air",
          "description": "",
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
          "externalSessionInfo": {}
        }
      ],
      "packages": [
        {
          "description": "PRIVATE EXECUTIVE HOME TFR PRE",
          "type": "PrePackage",
          "departureArrivalInfo": {
            "departureDateTime": "01-Sep-2023 00:00:00",
            "arrivalDateTime": "01-Sep-2023 00:00:00"
          },
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ]
        },
        {
          "description": "PRIVATE EXECUTIVE HOME TFR PST",
          "type": "PostPackage",
          "departureArrivalInfo": {
            "departureDateTime": "08-Sep-2023 00:00:00",
            "arrivalDateTime": "08-Sep-2023 00:00:00"
          },
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ]
        }
      ],
      "cancellationPolicies": [
        {
          "amount": 250,
          "amountType": "Fixed",
          "startDate": "06-Dec-2020",
          "endDate": "03-Apr-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 15,
          "amountType": "Percentage",
          "startDate": "04-Apr-2023",
          "endDate": "03-May-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 25,
          "amountType": "Percentage",
          "startDate": "04-May-2023",
          "endDate": "02-Jun-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 50,
          "amountType": "Percentage",
          "startDate": "03-Jun-2023",
          "endDate": "02-Jul-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 75,
          "amountType": "Percentage",
          "startDate": "03-Jul-2023",
          "endDate": "01-Aug-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 100,
          "amountType": "Percentage",
          "startDate": "02-Aug-2023",
          "endDate": "01-Sep-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        }
      ]
    },
    "customers": [
      {
        "title": "MR",
        "gender": "Male",
        "rph": 1,
        "odyCustomerRef": 60288,
        "firstName": "John",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1988",
        "age": 35,
        "address": {
          "city": {},
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          },
          "addressline1": ","
        },
        "nationality": {},
        "contactInfo": {
          "phone1": {
            "number": ""
          },
          "phone2": {
            "number": ""
          }
        }
      },
      {
        "title": "MR",
        "gender": "Male",
        "rph": 2,
        "odyCustomerRef": 60289,
        "firstName": "Jack",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1988",
        "age": 35,
        "address": {
          "city": {},
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          },
          "addressline1": ","
        },
        "nationality": {},
        "contactInfo": {
          "phone1": {
            "number": ""
          },
          "phone2": {
            "number": ""
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
