# Read Reservation From Supplier (Pay)

**Path:** Apply Payment - After Reservation is Created > Read Reservation From Supplier (Pay)

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
    "id": 66110,
    "cruiseReservation": {
        "id": 114090,
        "readPreferences": {
            "mode": "Pay", //Possible values are View/Modify/Pay
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
Date: Mon, 20 Feb 2023 10:29:59 GMT
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
      "requestId": "73d5264c-bc35-4680-8274-486a4694bfd0",
      "timeStamp": "20-Feb-2023 05:29:53",
      "token": "EQTEMPKEN"
    },
    "id": 66110,
    "agencyConfirmation": "L1D5DDJ",
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Apr-2023 00:00:00",
        "arrivalDateTime": "10-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 3
      },
      "id": 114090,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "378173"
      },
      "paymentSchedules": {
        "customerPaymentSchedules": [
          {
            "id": 463465,
            "type": 2,
            "amount": 1053.46,
            "dueDate": "25-Feb-2023"
          }
        ],
        "affiliatePaymentSchedules": [
          {
            "id": 463466,
            "type": 2,
            "amount": 1053.46,
            "dueDate": "25-Feb-2023"
          }
        ],
        "supplierPaymentSchedules": [
          {
            "id": 463464,
            "type": 2,
            "amount": 939.54,
            "dueDate": "27-Feb-2023"
          }
        ]
      },
      "prices": [
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 1244,
          "rph": -1
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 126,
          "rph": -1
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": -54,
          "rph": -1
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -406,
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
          "amount": 838,
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
          "amount": 838,
          "rph": -1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 712,
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
          "amount": 215.46,
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
          "amount": 1053.46,
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
          "amount": 1053.46,
          "rph": -1
        },
        {
          "id": 42,
          "code": "59",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 50,
          "rph": -1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 1053.46,
          "rph": -1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 1053.46,
          "rph": -1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 200,
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
          "amount": 1053.46,
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
          "amount": 113.92,
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
          "amount": 939.54,
          "rph": -1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 939.54,
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
          "amount": 1053.46,
          "rph": -1
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 113.92,
          "rph": -1
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 649,
          "rph": 1
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 90,
          "rph": 1
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": 0,
          "rph": 1
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -50,
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
          "amount": 599,
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
          "id": 44,
          "code": "",
          "priority": 12,
          "display": true,
          "displayType": 2,
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
          "id": 46,
          "code": "",
          "priority": 15,
          "display": true,
          "displayType": 1,
          "amount": 599,
          "rph": 1
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 509,
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
          "amount": 107.73,
          "details": {
            "isTax": true
          },
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
          "id": 70,
          "code": "70",
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
          "amount": 706.73,
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
          "id": 14,
          "code": "107",
          "priority": 105,
          "display": true,
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
          "id": 60,
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
          "amount": 706.73,
          "rph": 1
        },
        {
          "id": 42,
          "code": "59",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 25,
          "rph": 1
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 706.73,
          "rph": 1
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 706.73,
          "rph": 1
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 134.17,
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
          "amount": 526.73,
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
          "amount": 81.44,
          "details": {
            "isCommission": true
          },
          "rph": 1
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 625.29,
          "rph": 1
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 625.29,
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
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 81.44,
          "rph": 1
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 706.73,
          "rph": 1
        },
        {
          "id": 1,
          "code": "49",
          "priority": 5,
          "displayType": 4,
          "amount": 595,
          "rph": 2
        },
        {
          "id": 2,
          "code": "60",
          "priority": 6,
          "displayType": 4,
          "amount": 36,
          "rph": 2
        },
        {
          "id": 73,
          "code": "NCD",
          "priority": 7,
          "displayType": 4,
          "amount": -54,
          "rph": 2
        },
        {
          "id": 5,
          "code": "BOGO60NRD",
          "priority": 9,
          "display": true,
          "displayType": 4,
          "amount": -356,
          "rph": 2
        },
        {
          "id": 7,
          "code": "1",
          "priority": 10,
          "display": true,
          "displayType": 1,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 74,
          "code": "SER",
          "priority": 10,
          "display": true,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 45,
          "code": "",
          "priority": 10,
          "displayType": 4,
          "amount": 239,
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
          "id": 48,
          "code": "",
          "priority": 12,
          "displayType": 4,
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
          "amount": 239,
          "rph": 2
        },
        {
          "id": 114,
          "code": "",
          "priority": 16,
          "displayType": 4,
          "amount": 203,
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
          "id": 58,
          "code": "108",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 41,
          "code": "13",
          "priority": 22,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 9,
          "code": "46",
          "priority": 23,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 10,
          "code": "44",
          "priority": 24,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 12,
          "code": "33",
          "priority": 25,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 3,
          "code": "18",
          "priority": 50,
          "display": true,
          "displayType": 8,
          "amount": 107.73,
          "details": {
            "isTax": true
          },
          "rph": 2
        },
        {
          "id": 75,
          "code": "DSC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 76,
          "code": "SOC",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 70,
          "code": "70",
          "priority": 80,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 6,
          "code": "52",
          "priority": 90,
          "display": true,
          "displayType": 2,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 17,
          "code": "",
          "priority": 100,
          "display": true,
          "amount": 346.73,
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
          "id": 14,
          "code": "107",
          "priority": 105,
          "display": true,
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
          "id": 60,
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
          "amount": 346.73,
          "rph": 2
        },
        {
          "id": 42,
          "code": "59",
          "priority": 351,
          "display": true,
          "displayType": 9,
          "amount": 25,
          "rph": 2
        },
        {
          "id": 47,
          "code": "",
          "priority": 355,
          "displayType": 4,
          "amount": 346.73,
          "rph": 2
        },
        {
          "id": 50,
          "code": "8",
          "priority": 359,
          "displayType": 4,
          "amount": 346.73,
          "rph": 2
        },
        {
          "id": 24,
          "code": "6",
          "priority": 360,
          "displayType": 4,
          "amount": 65.83,
          "rph": 2
        },
        {
          "id": 26,
          "code": "",
          "priority": 380,
          "displayType": 4,
          "amount": 0,
          "rph": 2
        },
        {
          "id": 63,
          "code": "3",
          "priority": 382,
          "displayType": 4,
          "amount": 526.73,
          "rph": 2
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
          "rph": 2
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
          "rph": 2
        },
        {
          "id": 32,
          "code": "80",
          "priority": 509,
          "displayType": 4,
          "amount": 32.48,
          "details": {
            "isCommission": true
          },
          "rph": 2
        },
        {
          "id": 65,
          "code": "",
          "priority": 510,
          "displayType": 4,
          "amount": 314.25,
          "rph": 2
        },
        {
          "id": 66,
          "code": "42",
          "priority": 510,
          "displayType": 4,
          "amount": 314.25,
          "rph": 2
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
          "rph": 2
        },
        {
          "id": 83,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 32.48,
          "rph": 2
        },
        {
          "id": 112,
          "code": "",
          "priority": 600,
          "displayType": 4,
          "amount": 346.73,
          "rph": 2
        }
      ],
      "syncInfo": {
        "supplierSyncInfo": {
          "token": "417983",
          "lastSyncOn": "20-Feb-2023 05:29:55",
          "lastModifiedOn": "20-Feb-2023 05:44:54"
        },
        "apiSyncInfo": {
          "token": "X7sgay0T20iRYDSnVxpdSYJiRWwAVpMA",
          "sessionId": "a7346091-1a57-495d-8262-456c00569300",
          "lastSyncOn": "20-Feb-2023 05:29:59"
        }
      },
      "usersInfo": {
        "createdFor": {
          "name": "Online User"
        },
        "createdBy": {}
      },
      "cruise": {
        "packageId": 1269619,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 1093
            }
          ]
        },
        "itinerary": {
          "id": 349022,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "07-Apr-2023 00:00:00",
          "arrivalDateTime": "10-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "LB3BH045"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "2N",
          "type": 2,
          "cabins": [
            {
              "number": "2616",
              "occupancy": {
                "min": 0,
                "max": 0
              }
            }
          ],
          "fares": [
            {
              "status": -1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "G0737880",
                "type": 0,
                "refundableType": 2
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 3,
                  "amount": 0,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 0,
                  "type": "AVGPP"
                }
              ],
              "addOns": []
            }
          ]
        }
      ],
      "dinings": [
        {
          "id": 1,
          "code": "M",
          "name": "05:30 PM",
          "status": 7,
          "tableSizeOptions": [
            0
          ]
        }
      ]
    },
    "customers": [
      {
        "firstName": "John",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "age": 53
      },
      {
        "firstName": "Maria",
        "middleName": "",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "age": 58
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
