# Read Reservation From Supplier (Modify)

**Path:** Modify Reservation > Category, Fare code and Cabin - Royal Caribbean > Read Reservation From Supplier (Modify)

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/readfromsupplier`

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
    "id": 69734,
    "cruiseReservation": {
        "id": 117714,
        "readPreferences": {
            "mode": "Modify",
            "autoSyncOption": "NOLOCK"
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
Date: Thu, 04 May 2023 10:36:06 GMT
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
      "requestId": "f1cf0df9-59d1-4f0e-88a1-0cb7bdc687fe",
      "timeStamp": "04-May-2023 06:36:00",
      "token": "EQTEMPKEN"
    },
    "id": 69734,
    "agencyConfirmation": "FPXZA67",
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Dec-2023 00:00:00",
        "arrivalDateTime": "09-Dec-2023 00:00:00",
        "departureCityId": "ONX",
        "arrivalCityId": "ONX",
        "duration": 7
      },
      "id": 117714,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "400566"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 63119,
          "supplierCustomerRef": "384898090"
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 63121,
          "supplierCustomerRef": "384898108"
        }
      ],
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "id": 471224,
            "type": 0,
            "amount": 20,
            "dueDate": "09-May-2023 16:59:00"
          },
          {
            "id": 471225,
            "type": 1,
            "amount": 2005.9,
            "dueDate": "12-Sep-2023 16:59:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "id": 471226,
            "type": 0,
            "amount": 20,
            "dueDate": "09-May-2023 16:59:00"
          },
          {
            "id": 471227,
            "type": 1,
            "amount": 2005.9,
            "dueDate": "12-Sep-2023 16:59:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "id": 471222,
            "type": 0,
            "amount": 20,
            "dueDate": "11-May-2023 16:59:00"
          },
          {
            "id": 471223,
            "type": 1,
            "amount": 1739.18,
            "dueDate": "03-Oct-2023 16:59:00"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "49",
          "amount": 2668,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "60",
          "amount": 200,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 73,
          "code": "NCD",
          "amount": 0,
          "priority": 7,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 5,
          "code": "BOGO60",
          "amount": -801,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 7,
          "code": "1",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 1867,
          "priority": 10,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 74,
          "code": "SER",
          "amount": 0,
          "priority": 10,
          "display": true,
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
          "amount": 1867,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 1667,
          "priority": 16,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 41,
          "code": "13",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
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
          "id": 58,
          "code": "108",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 9,
          "code": "46",
          "amount": 0,
          "priority": 23,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 10,
          "code": "44",
          "amount": 0,
          "priority": 24,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 12,
          "code": "33",
          "amount": 0,
          "priority": 25,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 3,
          "code": "18",
          "amount": 158.9,
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
          "id": 70,
          "code": "70",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 75,
          "code": "DSC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 76,
          "code": "SOC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 6,
          "code": "52",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 17,
          "code": "",
          "amount": 2025.9,
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
          "id": 14,
          "code": "107",
          "amount": 0,
          "priority": 105,
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
          "amount": 2025.9,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 42,
          "code": "59",
          "amount": 0,
          "priority": 351,
          "display": true,
          "displayType": 9,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 2025.9,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "amount": 2025.9,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "amount": 20,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 26,
          "code": "IAR",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 63,
          "code": "3",
          "amount": 2025.9,
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
          "code": "80",
          "amount": 266.72,
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
          "amount": 1759.18,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 66,
          "code": "42",
          "amount": 1759.18,
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
          "amount": 266.72,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "amount": 2025.9,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "49",
          "amount": 1334,
          "priority": 5,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 2,
          "code": "60",
          "amount": 100,
          "priority": 6,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 73,
          "code": "NCD",
          "amount": 0,
          "priority": 7,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 5,
          "code": "BOGO60",
          "amount": 0,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 7,
          "code": "1",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 45,
          "code": "",
          "amount": 1334,
          "priority": 10,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 74,
          "code": "SER",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 48,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 46,
          "code": "",
          "amount": 1334,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 114,
          "code": "",
          "amount": 1234,
          "priority": 16,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 41,
          "code": "13",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 58,
          "code": "108",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 9,
          "code": "46",
          "amount": 0,
          "priority": 23,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 10,
          "code": "44",
          "amount": 0,
          "priority": 24,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 12,
          "code": "33",
          "amount": 0,
          "priority": 25,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 3,
          "code": "18",
          "amount": 79.45,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 70,
          "code": "70",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 75,
          "code": "DSC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 76,
          "code": "SOC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 6,
          "code": "52",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 17,
          "code": "",
          "amount": 1413.45,
          "priority": 100,
          "display": true,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 86,
          "code": "",
          "amount": 0,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 14,
          "code": "107",
          "amount": 0,
          "priority": 105,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 23,
          "code": "",
          "amount": 1413.45,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 47,
          "code": "",
          "amount": 1413.45,
          "priority": 355,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 50,
          "code": "8",
          "amount": 1413.45,
          "priority": 359,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 24,
          "code": "6",
          "amount": 10,
          "priority": 360,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 63,
          "code": "3",
          "amount": 1012.95,
          "priority": 382,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
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
          "odyCustomerRef": 63119
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
          "odyCustomerRef": 63119
        },
        {
          "id": 32,
          "code": "80",
          "amount": 197.44,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 65,
          "code": "",
          "amount": 1216.01,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 66,
          "code": "42",
          "amount": 1216.01,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
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
          "odyCustomerRef": 63119
        },
        {
          "id": 112,
          "code": "",
          "amount": 1413.45,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 83,
          "code": "",
          "amount": 197.44,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 63119
        },
        {
          "id": 1,
          "code": "49",
          "amount": 1334,
          "priority": 5,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 2,
          "code": "60",
          "amount": 100,
          "priority": 6,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 73,
          "code": "NCD",
          "amount": 0,
          "priority": 7,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 5,
          "code": "BOGO60",
          "amount": -801,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 7,
          "code": "1",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 45,
          "code": "",
          "amount": 533,
          "priority": 10,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 74,
          "code": "SER",
          "amount": 0,
          "priority": 10,
          "display": true,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 48,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 46,
          "code": "",
          "amount": 533,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 114,
          "code": "",
          "amount": 433,
          "priority": 16,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 41,
          "code": "13",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 58,
          "code": "108",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 9,
          "code": "46",
          "amount": 0,
          "priority": 23,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 10,
          "code": "44",
          "amount": 0,
          "priority": 24,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 12,
          "code": "33",
          "amount": 0,
          "priority": 25,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 3,
          "code": "18",
          "amount": 79.45,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 70,
          "code": "70",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 75,
          "code": "DSC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 76,
          "code": "SOC",
          "amount": 0,
          "priority": 80,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 6,
          "code": "52",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 17,
          "code": "",
          "amount": 612.45,
          "priority": 100,
          "display": true,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 86,
          "code": "",
          "amount": 0,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 14,
          "code": "107",
          "amount": 0,
          "priority": 105,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 23,
          "code": "",
          "amount": 612.45,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 47,
          "code": "",
          "amount": 612.45,
          "priority": 355,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 50,
          "code": "8",
          "amount": 612.45,
          "priority": 359,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 24,
          "code": "6",
          "amount": 10,
          "priority": 360,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 63,
          "code": "3",
          "amount": 1012.95,
          "priority": 382,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
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
          "odyCustomerRef": 63121
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
          "odyCustomerRef": 63121
        },
        {
          "id": 32,
          "code": "80",
          "amount": 69.28,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 65,
          "code": "",
          "amount": 543.17,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 66,
          "code": "42",
          "amount": 543.17,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
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
          "odyCustomerRef": 63121
        },
        {
          "id": 112,
          "code": "",
          "amount": 612.45,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        },
        {
          "id": 83,
          "code": "",
          "amount": 69.28,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 63121
        }
      ],
      "syncInfo": {
        "supplierSyncInfo": {
          "token": "1af477",
          "lastSyncOn": "04-May-2023 06:36:02",
          "lastModifiedOn": "04-May-2023 06:51:01"
        },
        "apiSyncInfo": {
          "token": "cvYWXotM20gY0xRMNQiES7l4S/1gs3Ju",
          "sessionId": "4c14d318-0835-4b84-b978-4bfd60b3726e",
          "lastSyncOn": "04-May-2023 06:36:06"
        }
      },
      "usersInfo": {
        "createdFor": {
          "name": "Online User"
        },
        "createdBy": {}
      },
      "currencyInfo": {
        "currencyId": "USD"
      },
      "cruise": {
        "packageId": 1336123,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 84
            }
          ]
        },
        "itinerary": {
          "id": 364276,
          "destination": {
            "id": 9
          }
        },
        "tourCode": "RH07D356",
        "voyage": {
          "departureDateTime": "02-Dec-2023 00:00:00",
          "arrivalDateTime": "09-Dec-2023 00:00:00",
          "departureCityId": "ONX",
          "arrivalCityId": "ONX",
          "code": "RH07D356"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 353805213,
          "code": "1N",
          "type": 2,
          "cabins": [
            {
              "number": "2596"
            }
          ]
        }
      ],
      "serviceCollection": {
        "services": [
          {
            "code": "en-LNP",
            "name": "English",
            "description": "English",
            "type": "PREFERREDLANGUAGE",
            "customerReferences": [
              {
                "rph": 1,
                "odyCustomerRef": 63119
              },
              {
                "rph": 2,
                "odyCustomerRef": 63121
              }
            ],
            "group": "Language"
          },
          {
            "code": "en-LND",
            "name": "English",
            "description": "English",
            "type": "DOCUMENTLANGUAGE",
            "customerReferences": [
              {
                "rph": 1,
                "odyCustomerRef": 63119
              },
              {
                "rph": 2,
                "odyCustomerRef": 63121
              }
            ],
            "group": "Language"
          }
        ]
      },
      "dinings": [
        {
          "id": 1,
          "code": "M",
          "name": "05:30 PM",
          "status": 7,
          "tableSizeOptions": [
            0
          ],
          "gratuityRequired": false
        }
      ]
    },
    "customers": [
      {
        "title": "MR",
        "gender": "Male",
        "rph": 1,
        "odyCustomerRef": 63119,
        "firstName": "Johny",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "11-Jan-1991",
        "age": 32,
        "address": {
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL",
            "country": {
              "id": "US"
            }
          }
        },
        "nationality": {
          "id": "US"
        },
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
        },
        "passportInfo": {
          "number": "1212121212",
          "expirationDate": "02-Jan-2026",
          "issueDate": "02-Jan-2021",
          "issueCountry": {
            "id": "US"
          }
        }
      },
      {
        "title": "MR",
        "gender": "Male",
        "rph": 2,
        "odyCustomerRef": 63121,
        "firstName": "Jack",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "21-Jan-1991",
        "age": 32,
        "address": {
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL",
            "country": {
              "id": "US"
            }
          }
        },
        "nationality": {
          "id": "US"
        },
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
        },
        "passportInfo": {
          "number": "2121212121",
          "expirationDate": "02-Jan-2026",
          "issueDate": "02-Jan-2021",
          "issueCountry": {
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
