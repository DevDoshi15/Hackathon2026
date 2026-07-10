# Carnival Cruise line

**Path:** Read Reservation From Supplier > Cancellation Policies > Carnival Cruise line

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
            "confirmationNumber": "4JKGN7"
        },
        "cruise": {
            "cruiseline": {
                "id": 1
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
Date: Tue, 27 Jun 2023 15:26:44 GMT
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
      "requestId": "99f5b66f-719e-467d-8290-e783ee58d6d5",
      "timeStamp": "27-Jun-2023 11:26:32"
    },
    "id": 73227,
    "agencyConfirmation": "SAZUV8H",
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "31-Oct-2023 00:00:00",
        "arrivalDateTime": "05-Nov-2023 00:00:00",
        "departureCityId": "SYD",
        "arrivalCityId": "SYD",
        "duration": 5
      },
      "id": 121204,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "4JKGN7"
      },
      "pos": {
        "id": 2460,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "B2B",
        "system": "Test",
        "apiId": "Carnival"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 50279,
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 64505
        }
      ],
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "id": 484867,
            "type": 0,
            "amount": 215.52,
            "dueDate": "27-Jun-2023 09:56:00"
          },
          {
            "id": 484868,
            "type": 1,
            "amount": 641.5,
            "dueDate": "27-Jul-2023 23:59:00"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "id": 484869,
            "type": 0,
            "amount": 215.52,
            "dueDate": "27-Jun-2023 09:56:00"
          },
          {
            "id": 484870,
            "type": 1,
            "amount": 641.5,
            "dueDate": "27-Jul-2023 23:59:00"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "id": 484865,
            "type": 0,
            "amount": 215.52,
            "dueDate": "29-Jun-2023 09:56:00"
          },
          {
            "id": 484866,
            "type": 1,
            "amount": 535.88,
            "dueDate": "17-Aug-2023 23:59:00"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "CRUS",
          "amount": 642.8,
          "priority": 5,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 2,
          "code": "PTCH",
          "amount": 162.92,
          "priority": 6,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 45,
          "code": "",
          "amount": 642.8,
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
          "amount": 642.8,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "amount": 479.88,
          "priority": 16,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 41,
          "code": "PKGS",
          "amount": 0,
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
          "id": 12,
          "code": "TADD",
          "amount": 0,
          "priority": 25,
          "display": true,
          "displayType": 2,
          "rph": -1
        },
        {
          "id": 3,
          "code": "MISC",
          "amount": 194.22,
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
          "amount": 857.02,
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
          "amount": 857.02,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "amount": 857.02,
          "priority": 355,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 812.02,
          "priority": 359,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 215.52,
          "priority": 360,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 126,
          "code": "",
          "amount": 195.52,
          "priority": 360,
          "display": true,
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
          "amount": 812.02,
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
          "amount": 60.62,
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
          "amount": 751.4,
          "priority": 510,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 751.4,
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
          "amount": 105.62,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 112,
          "code": "",
          "amount": 857.02,
          "priority": 600,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 140,
          "code": "CGST",
          "amount": 0,
          "priority": 610,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 141,
          "code": "NCOM",
          "amount": 60.62,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 610,
          "displayType": 4,
          "rph": -1
        },
        {
          "id": 1,
          "code": "CRUS",
          "amount": 321.4,
          "priority": 5,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 2,
          "code": "PTCH",
          "amount": 81.46,
          "priority": 6,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 45,
          "code": "",
          "amount": 321.4,
          "priority": 10,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 48,
          "code": "",
          "amount": 12.5,
          "priority": 12,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 46,
          "code": "",
          "amount": 321.4,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 114,
          "code": "",
          "amount": 239.94,
          "priority": 16,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 3,
          "code": "MISC",
          "amount": 97.11,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 17,
          "code": "",
          "amount": 428.51,
          "priority": 100,
          "display": true,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 86,
          "code": "",
          "amount": 10,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 23,
          "code": "",
          "amount": 428.51,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 47,
          "code": "",
          "amount": 428.51,
          "priority": 355,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 406.01,
          "priority": 359,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 107.76,
          "priority": 360,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 126,
          "code": "",
          "amount": 97.76,
          "priority": 360,
          "display": true,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 62,
          "code": "",
          "amount": 406.01,
          "priority": 382,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
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
          "odyCustomerRef": 50279
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
          "odyCustomerRef": 50279
        },
        {
          "id": 32,
          "code": "COMM",
          "amount": 30.31,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 65,
          "code": "",
          "amount": 375.7,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 375.7,
          "priority": 510,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
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
          "odyCustomerRef": 50279
        },
        {
          "id": 83,
          "code": "",
          "amount": 52.81,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 112,
          "code": "",
          "amount": 428.51,
          "priority": 600,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 141,
          "code": "NCOM",
          "amount": 30.31,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 610,
          "displayType": 4,
          "rph": 1,
          "odyCustomerRef": 50279
        },
        {
          "id": 1,
          "code": "CRUS",
          "amount": 321.4,
          "priority": 5,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 2,
          "code": "PTCH",
          "amount": 81.46,
          "priority": 6,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 45,
          "code": "",
          "amount": 321.4,
          "priority": 10,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 122,
          "code": "",
          "amount": 0,
          "priority": 11,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 44,
          "code": "",
          "amount": 0,
          "priority": 12,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 48,
          "code": "",
          "amount": 12.5,
          "priority": 12,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 49,
          "code": "",
          "amount": 0,
          "priority": 12,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 46,
          "code": "",
          "amount": 321.4,
          "priority": 15,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 114,
          "code": "",
          "amount": 239.94,
          "priority": 16,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 54,
          "code": "",
          "amount": 0,
          "priority": 22,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 3,
          "code": "MISC",
          "amount": 97.11,
          "details": {
            "isTax": true,
            "isCommission": false
          },
          "priority": 50,
          "display": true,
          "displayType": 8,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 6,
          "code": "",
          "amount": 0,
          "priority": 90,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 17,
          "code": "",
          "amount": 428.51,
          "priority": 100,
          "display": true,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 86,
          "code": "",
          "amount": 10,
          "priority": 100,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 84,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 60,
          "code": "",
          "amount": 0,
          "priority": 200,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 40,
          "code": "",
          "amount": 0,
          "priority": 300,
          "display": true,
          "displayType": 2,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 23,
          "code": "",
          "amount": 428.51,
          "priority": 350,
          "display": true,
          "displayType": 1,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 47,
          "code": "",
          "amount": 428.51,
          "priority": 355,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 50,
          "code": "GRSS",
          "amount": 406.01,
          "priority": 359,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 24,
          "code": "DPST",
          "amount": 107.76,
          "priority": 360,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 126,
          "code": "",
          "amount": 97.76,
          "priority": 360,
          "display": true,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 26,
          "code": "",
          "amount": 0,
          "priority": 380,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 62,
          "code": "",
          "amount": 406.01,
          "priority": 382,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
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
          "odyCustomerRef": 64505
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
          "odyCustomerRef": 64505
        },
        {
          "id": 32,
          "code": "COMM",
          "amount": 30.31,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 509,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 65,
          "code": "",
          "amount": 375.7,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 66,
          "code": "NETD",
          "amount": 375.7,
          "priority": 510,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
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
          "odyCustomerRef": 64505
        },
        {
          "id": 83,
          "code": "",
          "amount": 52.81,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 112,
          "code": "",
          "amount": 428.51,
          "priority": 600,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        },
        {
          "id": 141,
          "code": "NCOM",
          "amount": 30.31,
          "details": {
            "isTax": false,
            "isCommission": true
          },
          "priority": 610,
          "displayType": 4,
          "rph": 2,
          "odyCustomerRef": 64505
        }
      ],
      "syncInfo": {
        "apiSyncInfo": {
          "token": "qeJF6iJ320g1BF3pViXFSqaY36cPLLWl",
          "sessionId": "e95d0435-2556-4ac5-a698-dfa70f2cb5a5",
          "lastSyncOn": "27-Jun-2023 11:26:44"
        }
      },
      "timeStamps": {
        "supplier": {
          "createdOn": "27-Jun-2023 09:56:15"
        },
        "system": {
          "createdOn": "27-Jun-2023 09:56:15",
          "lastModifiedOn": "27-Jun-2023 11:02:54"
        }
      },
      "usersInfo": {
        "createdFor": {
          "name": "Ninad Sawarkar",
          "contactInfo": {
            "email": "ninad_sawarkar@odysseussolutions.com"
          }
        },
        "createdBy": {}
      },
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1316422,
        "packageTourId": -1,
        "cruiseline": {
          "id": 1,
          "name": "Carnival Cruise Lines",
          "ships": [
            {
              "id": 1163,
              "name": "Carnival Splendor"
            }
          ]
        },
        "itinerary": {
          "id": 296522,
          "destination": {
            "id": 104
          }
        },
        "voyage": {
          "departureDateTime": "31-Oct-2023 00:00:00",
          "arrivalDateTime": "05-Nov-2023 00:00:00",
          "departureCityId": "SYD",
          "arrivalCityId": "SYD",
          "code": "20231031SL05"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 26895,
          "code": "4E",
          "name": "Interior Stateroom",
          "type": 1,
          "cabins": [
            {
              "number": "7229",
              "smokingInfo": {
                "allowed": true,
                "description": "SMOKING PROHIBITED"
              },
              "beds": [],
              "deck": {
                "id": 1683,
                "name": "Empress",
                "description": "The Splendor, Staterooms.\n"
              },
              "location": "INSIDE FORWARD STARBOARD",
              "occupancy": {
                "min": 0,
                "max": 2
              }
            }
          ],
          "fares": [
            {
              "upgradeFrom": "4E",
              "rules": [
                {
                  "ruleId": 1728343,
                  "calculatedAmount": {
                    "total": 25
                  }
                },
                {
                  "ruleId": 1728344,
                  "calculatedAmount": {
                    "total": 20
                  }
                }
              ],
              "status": 1,
              "fareCode": {
                "code": "KCH",
                "name": "CHOICE FARE",
                "description": "CKCH - NO UPGRADES APPLY",
                "type": 0,
                "refundableType": 2,
                "bookOnline": true,
                "status": 1,
                "details": {
                  "agencyDescription": "",
                  "fareTypeDescription": "Public fare",
                  "remarks": "CKCH - NO UPGRADES APPLY"
                }
              }
            }
          ]
        }
      ],
      "dinings": [
        {
          "id": 22,
          "code": "1",
          "name": "Early",
          "status": 7,
          "tableSizeOptions": [
            0
          ],
          "diningRoom": {
            "type": "EARLY DINING"
          }
        }
      ],
      "cancellationPolicies": [
        {
          "amount": 195.52,
          "amountType": "Fixed",
          "startDate": "16-Aug-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 50,
          "amountType": "Percentage",
          "startDate": "05-Sep-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 75,
          "amountType": "Percentage",
          "startDate": "01-Oct-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        },
        {
          "amount": 100,
          "amountType": "Percentage",
          "startDate": "16-Oct-2023",
          "penaltyAmountApplicableOn": "PerCabin"
        }
      ]
    },
    "customers": [
      {
        "title": "MR",
        "gender": "Male",
        "rph": 1,
        "odyCustomerRef": 50279,
        "firstName": "Monish",
        "middleName": "",
        "lastName": "Luthra",
        "dateOfBirth": "15-Nov-1970",
        "age": 52,
        "pastPaxNumber": "0",
        "address": {
          "city": {
            "id": "FLL",
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          },
          "addressline1": "Test",
          "addressline2": "Test",
          "postalCode": "39020"
        },
        "nationality": {
          "id": "US"
        },
        "contactInfo": {
          "email": "",
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
        "odyCustomerRef": 64505,
        "firstName": "Pramod",
        "middleName": "",
        "lastName": "Navani",
        "dateOfBirth": "21-Aug-1967",
        "age": 56,
        "pastPaxNumber": "0",
        "address": {
          "city": {
            "id": "FLL",
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          },
          "addressline1": "Test",
          "addressline2": "Test",
          "postalCode": "39020"
        },
        "nationality": {
          "id": "US"
        },
        "contactInfo": {
          "phone1": {
            "countryCode": "1",
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
