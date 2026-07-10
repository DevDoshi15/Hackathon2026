# Read Reservation From Supplier With Reservation Id

**Path:** Modify Reservation > Create Reservation With Insurance then Modify By Adding Gratuities > Read Reservation From Supplier With Reservation Id

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
    "id": 69733,
    "cruiseReservation": {
        "id": 117713,
        "readPreferences": {
            "mode": "modify",
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
Date: Thu, 04 May 2023 09:14:56 GMT
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
      "requestId": "bee7619e-fa0b-4fe7-b34e-91c286d53292",
      "timeStamp": "04-May-2023 05:14:48",
      "token": "EQTEMPKEN"
    },
    "id": 69733,
    "agencyConfirmation": "AYX9662",
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "15-Mar-2024 00:00:00",
        "arrivalDateTime": "22-Mar-2024 00:00:00",
        "departureCityId": "GLS",
        "arrivalCityId": "GLS",
        "duration": 7
      },
      "id": 117713,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "52029826"
      },
      "reservationIndicators": {
        "modifyIndicators": [
          {
            "type": "Category",
            "value": false
          },
          {
            "type": "Cabin",
            "value": false
          },
          {
            "type": "FareCode",
            "value": false
          },
          {
            "type": "Dining",
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
            "type": "FirstName",
            "value": false
          },
          {
            "type": "LastName",
            "value": false
          },
          {
            "type": "SpecialService",
            "value": false
          }
        ]
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 57895,
          "supplierCustomerRef": "267110788"
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 57894,
          "supplierCustomerRef": "267110789"
        }
      ],
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "id": 471218,
            "type": 0,
            "amount": 972.14,
            "dueDate": "04-May-2023 05:07:00"
          },
          {
            "id": 471219,
            "type": 1,
            "amount": 10155.800000000001,
            "dueDate": "26-Oct-2023 23:59:59"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "id": 471220,
            "type": 0,
            "amount": 972.14,
            "dueDate": "04-May-2023 05:07:00"
          },
          {
            "id": 471221,
            "type": 1,
            "amount": 10155.800000000001,
            "dueDate": "26-Oct-2023 23:59:59"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "id": 471216,
            "type": 0,
            "amount": 972.14,
            "dueDate": "05-May-2023 05:07:43"
          },
          {
            "id": 471217,
            "type": 1,
            "amount": 8496.58,
            "dueDate": "16-Nov-2023 23:59:59"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "5",
          "amount": 14956,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 390,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 5,
          "code": "34",
          "amount": -5234.6,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 9721.4,
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
          "amount": 9721.4,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 9331.4,
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
          "code": "18",
          "amount": 368.54,
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
          "code": "10",
          "amount": 1038,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 17,
          "code": "",
          "amount": 11127.94,
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
          "id": 16,
          "code": "15",
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
          "amount": 11127.94,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 11127.94,
          "priority": 355,
          "display": true,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "amount": 11127.94,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "amount": 972.14,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 26,
          "code": "2",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 62,
          "code": "",
          "amount": 11127.94,
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
          "code": "66",
          "amount": 1659.22,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 36,
          "code": "85",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 510,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "amount": 9468.72,
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
          "amount": 1659.22,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "amount": 11127.94,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "5",
          "amount": 7478,
          "priority": 5,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 195,
          "priority": 6,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 5,
          "code": "34",
          "amount": -2617.3,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 45,
          "code": "",
          "amount": 4860.7,
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
          "amount": 4860.7,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 114,
          "code": "",
          "amount": 4665.7,
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
          "code": "18",
          "amount": 184.27,
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
          "code": "10",
          "amount": 519,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 17,
          "code": "",
          "amount": 5563.97,
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
          "id": 16,
          "code": "15",
          "amount": 0,
          "priority": 105,
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
          "amount": 5563.97,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 47,
          "code": "",
          "amount": 5563.97,
          "priority": 355,
          "display": true,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 50,
          "code": "8",
          "amount": 5563.97,
          "priority": 359,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 24,
          "code": "6",
          "amount": 486.07,
          "priority": 360,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 26,
          "code": "2",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 62,
          "code": "",
          "amount": 5563.97,
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
          "code": "66",
          "amount": 829.61,
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
          "id": 36,
          "code": "85",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 510,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 65,
          "code": "",
          "amount": 4734.36,
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
          "amount": 829.61,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 112,
          "code": "",
          "amount": 5563.97,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 1,
          "code": "5",
          "amount": 7478,
          "priority": 5,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 2,
          "code": "POC",
          "amount": 195,
          "priority": 6,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 5,
          "code": "34",
          "amount": -2617.3,
          "priority": 9,
          "display": true,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 45,
          "code": "",
          "amount": 4860.7,
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
          "amount": 4860.7,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 114,
          "code": "",
          "amount": 4665.7,
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
          "code": "18",
          "amount": 184.27,
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
          "code": "10",
          "amount": 519,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 17,
          "code": "",
          "amount": 5563.97,
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
          "id": 16,
          "code": "15",
          "amount": 0,
          "priority": 105,
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
          "amount": 5563.97,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 47,
          "code": "",
          "amount": 5563.97,
          "priority": 355,
          "display": true,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 50,
          "code": "8",
          "amount": 5563.97,
          "priority": 359,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 24,
          "code": "6",
          "amount": 486.07,
          "priority": 360,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 26,
          "code": "2",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 62,
          "code": "",
          "amount": 5563.97,
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
          "code": "66",
          "amount": 829.61,
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
          "id": 36,
          "code": "85",
          "amount": 0,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 510,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 65,
          "code": "",
          "amount": 4734.36,
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
          "amount": 829.61,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 112,
          "code": "",
          "amount": 5563.97,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        }
      ],
      "insurances": [
        {
          "code": "STD",
          "type": "Supplier"
        }
      ],
      "syncInfo": {
        "apiSyncInfo": {
          "token": "Nnd2B4BM20jYACa1EBL0RZCeOSnDhpI7",
          "sessionId": "b52600d8-1210-45f4-909e-3929c386923b",
          "lastSyncOn": "04-May-2023 05:14:56"
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
        "packageId": 1307173,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 15089
            }
          ]
        },
        "itinerary": {
          "id": 363332,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "15-Mar-2024 00:00:00",
          "arrivalDateTime": "22-Mar-2024 00:00:00",
          "departureCityId": "GLS",
          "arrivalCityId": "GLS",
          "code": "18440175"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 667460316,
          "code": "SL",
          "type": 4,
          "cabins": [
            {
              "number": "10702"
            }
          ]
        }
      ],
      "addOns": [
        {
          "code": "DISC35",
          "name": "DISC35",
          "description": "",
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
          "externalSessionInfo": {}
        },
        {
          "code": "EASYFARE",
          "name": "EASYFARE",
          "description": "",
          "autoInclude": true,
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
          "externalSessionInfo": {}
        }
      ]
    },
    "customers": [
      {
        "title": "MR",
        "gender": "Male",
        "rph": 1,
        "odyCustomerRef": 57895,
        "firstName": "John",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "age": 54,
        "pastPaxNumber": "267110788",
        "address": {
          "city": {
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          },
          "addressline1": "My Street Address",
          "addressline2": ""
        },
        "nationality": {
          "id": "US"
        },
        "contactInfo": {
          "email": "john@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "4165554566"
          },
          "phone2": {
            "countryCode": "1",
            "number": "416-555-4566"
          }
        }
      },
      {
        "title": "MR",
        "gender": "Male",
        "rph": 2,
        "odyCustomerRef": 57894,
        "firstName": "Maria",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "age": 59,
        "pastPaxNumber": "267110789",
        "nationality": {
          "id": "US"
        },
        "contactInfo": {
          "email": "maria@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "4165554566"
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
