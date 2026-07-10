# Read Reservation From Supplier (Modify)

**Path:** Modify Reservation > Packages - Princess Cruise line > Read Reservation From Supplier (Modify)

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
    "id": 69739,
    "cruiseReservation": {
        "id": 117719,
        "readPreferences": {
            "mode": "Modify", // mode should always be "Modify" for modify booking flow
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
Date: Thu, 04 May 2023 14:11:42 GMT
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
      "requestId": "a95b89e8-f3f5-425c-abec-2ee235b67845",
      "timeStamp": "04-May-2023 10:11:34",
      "token": "EQTEMPKEN"
    },
    "id": 69739,
    "agencyConfirmation": "EBI3H15",
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-Dec-2023 00:00:00",
        "arrivalDateTime": "04-Dec-2023 00:00:00",
        "departureCityId": "BNE",
        "arrivalCityId": "BNE",
        "duration": 3
      },
      "id": 117719,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "5WDN7L"
      },
      "reservationIndicators": {
        "modifyIndicators": [
          {
            "type": "FirstName",
            "value": false
          }
        ]
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 57895,
          "supplierCustomerRef": "1"
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 57894,
          "supplierCustomerRef": "2"
        }
      ],
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "id": 471251,
            "type": 0,
            "amount": 200,
            "dueDate": "05-May-2023 23:59:00"
          },
          {
            "id": 471252,
            "type": 1,
            "amount": 1626.24,
            "dueDate": "27-Aug-2023 23:59:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "id": 471253,
            "type": 0,
            "amount": 200,
            "dueDate": "05-May-2023 23:59:00"
          },
          {
            "id": 471254,
            "type": 1,
            "amount": 1626.24,
            "dueDate": "27-Aug-2023 23:59:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "id": 471249,
            "type": 0,
            "amount": 200,
            "dueDate": "07-May-2023 23:59:00"
          },
          {
            "id": 471250,
            "type": 1,
            "amount": 1398.3,
            "dueDate": "17-Sep-2023 23:59:00"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "AMCT",
          "amount": 1610,
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
          "amount": 1610,
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
          "amount": 1610,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 1460,
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
          "amount": 1826.24,
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
          "amount": 1826.24,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 1826.24,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 1826.24,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 200,
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
          "amount": 1826.24,
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
          "code": "COMM",
          "amount": 227.94,
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
          "amount": 1598.3,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 1598.3,
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
          "amount": 227.94,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "amount": 1826.24,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 110,
          "code": "GSTT",
          "amount": 0,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 137,
          "code": "GSTA",
          "amount": 35.3,
          "priority": 610,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "AMCT",
          "amount": 805,
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
          "amount": 805,
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
          "amount": 805,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 114,
          "code": "",
          "amount": 730,
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
          "amount": 913.12,
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
          "amount": 913.12,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 47,
          "code": "",
          "amount": 913.12,
          "priority": 355,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 913.12,
          "priority": 359,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 100,
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
          "amount": 913.12,
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
          "amount": 113.97,
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
          "amount": 799.15,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 799.15,
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
          "amount": 113.97,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 112,
          "code": "",
          "amount": 913.12,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 110,
          "code": "GSTT",
          "amount": 0,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 137,
          "code": "GSTA",
          "amount": 17.65,
          "priority": 610,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 57895
        },
        {
          "id": 1,
          "code": "AMCT",
          "amount": 805,
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
          "amount": 805,
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
          "amount": 805,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 114,
          "code": "",
          "amount": 730,
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
          "amount": 913.12,
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
          "amount": 913.12,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 47,
          "code": "",
          "amount": 913.12,
          "priority": 355,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 913.12,
          "priority": 359,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 100,
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
          "amount": 913.12,
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
          "amount": 113.97,
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
          "amount": 799.15,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 799.15,
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
          "amount": 113.97,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 112,
          "code": "",
          "amount": 913.12,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 110,
          "code": "GSTT",
          "amount": 0,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        },
        {
          "id": 137,
          "code": "GSTA",
          "amount": 17.65,
          "priority": 610,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 57894
        }
      ],
      "syncInfo": {
        "apiSyncInfo": {
          "token": "8bU1fKlM20ivnispsbKuSJhxsGlOKZdb",
          "sessionId": "292b9eaf-b2b1-48ae-9871-b0694e29975b",
          "lastSyncOn": "04-May-2023 10:11:42"
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
          "id": 369692,
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
          "id": 61873,
          "code": "M1",
          "type": 4,
          "cabins": [
            {
              "number": "D507",
              "isGuarantee": true,
              "beds": [
                {
                  "code": "T2",
                  "name": "T2",
                  "description": "Twin Beds ",
                  "type": 261
                }
              ],
              "location": "Midship Starboard Oceanview"
            }
          ]
        }
      ],
      "serviceCollection": {
        "services": [
          {
            "code": "N",
            "name": "No",
            "description": "Decline Complimentary Upgrade",
            "type": "UPG",
            "customerReferences": [
              {
                "rph": 1,
                "odyCustomerRef": 57895
              },
              {
                "rph": 2,
                "odyCustomerRef": 57894
              }
            ],
            "associationType": "PAX",
            "group": "ComplimentaryUpgrade"
          }
        ]
      },
      "packages": [
        {
          "code": "B0TNOXFR",
          "description": "NO TRANSFER",
          "type": "PrePackage",
          "departureArrivalInfo": {},
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ]
        },
        {
          "code": "A0TNOXFR",
          "description": "NO TRANSFER",
          "type": "PostPackage",
          "departureArrivalInfo": {},
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ]
        }
      ],
      "dinings": [
        {
          "id": 45,
          "code": "PCL8",
          "name": "Anytime Dining",
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
        "odyCustomerRef": 57895,
        "firstName": "John",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "age": 53,
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
        "age": 58,
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
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
