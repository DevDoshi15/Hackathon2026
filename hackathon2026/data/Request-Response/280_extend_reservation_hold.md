# Extend Reservation Hold

**Path:** Extend Reservation Hold > Extend Reservation Hold

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/ExtendHold`

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
    "id": 72353,
    "cruiseReservation": {
        "id": 120330,
        "syncInfo": { // token information received in the read booking response
            "supplierSyncInfo": {
                "token": "e8c7ae", // supplier token mandatory in case of RCCL API
                "lastSyncOn": "19-Jun-2023 09:17:42",
                "lastModifiedOn": "19-Jun-2023 09:32:40"
            },
            "apiSyncInfo": { // API token is required for all APIs (including RCCL)
                "token": "kQ+uksdw20jvrYTFdVWATrILOrvGTTCC",
                "sessionId": "c584adef-5575-4e80-b20b-3abbc64d3082",
                "lastSyncOn": "19-Jun-2023 09:17:46"
            }
        }
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Mon, 19 Jun 2023 13:20:50 GMT
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
            "requestId": "d93a0874-50c3-4122-ae6c-3e8ade69a1c9",
            "timeStamp": "19-Jun-2023 09:20:44"
        },
        "id": 72353,
        "agencyConfirmation": "AHEG2IW",
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "18-Aug-2023 00:00:00",
                "arrivalDateTime": "22-Aug-2023 00:00:00",
                "departureCityId": "SKB",
                "arrivalCityId": "SKB",
                "duration": 4
            },
            "id": 120330,
            "status": 6,
            "reservationReferences": {
                "confirmationNumber": "419295"
            },
            "customerReferences": [
                {
                    "rph": 1,
                    "ageGroup": "Adult",
                    "odyCustomerRef": 57895,
                    "supplierCustomerRef": "385020173",
                    "isPrimaryContact": true
                },
                {
                    "rph": 2,
                    "ageGroup": "Adult",
                    "odyCustomerRef": 57894,
                    "supplierCustomerRef": "385020181"
                }
            ],
            "paymentSchedules": {
                "customerPaymentSchedules": [
                    {
                        "id": 481622,
                        "type": 2,
                        "amount": 278.44,
                        "dueDate": "27-Jun-2023 16:59:00" // date after extending the hold
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "id": 481623,
                        "type": 2,
                        "amount": 278.44,
                        "dueDate": "27-Jun-2023 16:59:00" // date after extending the hold
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "id": 481621,
                        "type": 2,
                        "amount": 233.44,
                        "dueDate": "29-Jun-2023 16:59:00" // date after extending the hold
                    }
                ]
            },
            "prices": [
                {
                    "id": 1,
                    "code": "49",
                    "amount": 3615,
                    "priority": 5,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "60",
                    "amount": 0,
                    "priority": 6,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 73,
                    "code": "NCD",
                    "amount": -500,
                    "priority": 7,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 5,
                    "code": "FREECRUISE2",
                    "amount": -3590,
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
                    "id": 74,
                    "code": "SER",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 25,
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
                    "id": 44,
                    "code": "",
                    "amount": 0,
                    "priority": 12,
                    "display": true,
                    "displayType": 2,
                    "rph": -1
                },
                {
                    "id": 46,
                    "code": "",
                    "amount": 25,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 25,
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
                    "id": 58,
                    "code": "108",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
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
                    "amount": 233.44,
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
                    "id": 70,
                    "code": "70",
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
                    "amount": 278.44,
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
                    "id": 14,
                    "code": "107",
                    "amount": 0,
                    "priority": 105,
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
                    "amount": 278.44,
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
                    "amount": 278.44,
                    "priority": 355,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "8",
                    "amount": 233.44,
                    "priority": 359,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 24,
                    "code": "6",
                    "amount": 200,
                    "priority": 360,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
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
                    "amount": 233.44,
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
                    "amount": 0,
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
                    "amount": 233.44,
                    "priority": 510,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 66,
                    "code": "42",
                    "amount": 233.44,
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
                    "amount": 45,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 278.44,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 1,
                    "code": "49",
                    "amount": 1807.5,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 2,
                    "code": "60",
                    "amount": 0,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 73,
                    "code": "NCD",
                    "amount": -250,
                    "priority": 7,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 5,
                    "code": "FREECRUISE2",
                    "amount": -1795,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 7,
                    "code": "1",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 12.5,
                    "priority": 10,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 74,
                    "code": "SER",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
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
                    "amount": 12.5,
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
                    "amount": 12.5,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 12.5,
                    "priority": 16,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 41,
                    "code": "13",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
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
                    "id": 58,
                    "code": "108",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 9,
                    "code": "46",
                    "amount": 0,
                    "priority": 23,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 10,
                    "code": "44",
                    "amount": 0,
                    "priority": 24,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 12,
                    "code": "33",
                    "amount": 0,
                    "priority": 25,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 3,
                    "code": "18",
                    "amount": 116.72,
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
                    "id": 70,
                    "code": "70",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 75,
                    "code": "DSC",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 76,
                    "code": "SOC",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 6,
                    "code": "52",
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
                    "amount": 139.22,
                    "priority": 100,
                    "display": true,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 86,
                    "code": "",
                    "amount": 10,
                    "priority": 100,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 14,
                    "code": "107",
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
                    "amount": 139.22,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 139.22,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 50,
                    "code": "8",
                    "amount": 116.72,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 24,
                    "code": "6",
                    "amount": 100,
                    "priority": 360,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
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
                    "id": 63,
                    "code": "3",
                    "amount": 116.72,
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
                    "code": "",
                    "amount": 0,
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
                    "amount": 116.72,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 66,
                    "code": "42",
                    "amount": 116.72,
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
                    "id": 112,
                    "code": "",
                    "amount": 139.22,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 22.5,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 57895
                },
                {
                    "id": 1,
                    "code": "49",
                    "amount": 1807.5,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 2,
                    "code": "60",
                    "amount": 0,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 73,
                    "code": "NCD",
                    "amount": -250,
                    "priority": 7,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 5,
                    "code": "FREECRUISE2",
                    "amount": -1795,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 7,
                    "code": "1",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 12.5,
                    "priority": 10,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 74,
                    "code": "SER",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
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
                    "amount": 12.5,
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
                    "amount": 12.5,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 12.5,
                    "priority": 16,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 41,
                    "code": "13",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
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
                    "id": 58,
                    "code": "108",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 9,
                    "code": "46",
                    "amount": 0,
                    "priority": 23,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 10,
                    "code": "44",
                    "amount": 0,
                    "priority": 24,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 12,
                    "code": "33",
                    "amount": 0,
                    "priority": 25,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 3,
                    "code": "18",
                    "amount": 116.72,
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
                    "id": 70,
                    "code": "70",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 75,
                    "code": "DSC",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 76,
                    "code": "SOC",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 6,
                    "code": "52",
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
                    "amount": 139.22,
                    "priority": 100,
                    "display": true,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 86,
                    "code": "",
                    "amount": 10,
                    "priority": 100,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 14,
                    "code": "107",
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
                    "amount": 139.22,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 139.22,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 50,
                    "code": "8",
                    "amount": 116.72,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 24,
                    "code": "6",
                    "amount": 100,
                    "priority": 360,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
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
                    "id": 63,
                    "code": "3",
                    "amount": 116.72,
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
                    "code": "",
                    "amount": 0,
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
                    "amount": 116.72,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 66,
                    "code": "42",
                    "amount": 116.72,
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
                    "id": 112,
                    "code": "",
                    "amount": 139.22,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 22.5,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 57894
                }
            ],
            "syncInfo": {
                "supplierSyncInfo": {
                    "token": "e8c7ae",
                    "lastSyncOn": "19-Jun-2023 09:17:42",
                    "lastModifiedOn": "19-Jun-2023 09:32:40"
                },
                "apiSyncInfo": {
                    "token": "qBSHAMhw20jIwDFerYt5S64ilsuK/Y+z",
                    "sessionId": "5e31c0c8-8bad-4b79-ae22-96cb8afd8fb3",
                    "lastSyncOn": "19-Jun-2023 09:20:50"
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
                "packageId": 1381489,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 8,
                    "ships": [
                        {
                            "id": 15128
                        }
                    ]
                },
                "itinerary": {
                    "id": 370546,
                    "destination": {
                        "id": 18
                    }
                },
                "voyage": {
                    "departureDateTime": "18-Aug-2023 00:00:00",
                    "arrivalDateTime": "22-Aug-2023 00:00:00",
                    "departureCityId": "SKB",
                    "arrivalCityId": "SKB",
                    "code": "IC4ICI23"
                },
                "transportationType": 29
            },
            "categories": [
                {
                    "id": 667463455,
                    "code": "IF",
                    "type": 3,
                    "cabins": [
                        {
                            "number": "10183",
                            "beds": [],
                            "occupancy": {
                                "min": 0,
                                "max": 3
                            }
                        }
                    ],
                    "fares": [
                        {
                            "upgradeFrom": "IF",
                            "status": -1,
                            "fareCode": {
                                "code": "I9626559",
                                "name": "FREECRUISE2",
                                "description": "100% PROMOTION",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "100% PROMOTION"
                                }
                            }
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
                                "odyCustomerRef": 57895
                            },
                            {
                                "rph": 2,
                                "odyCustomerRef": 57894
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
                                "odyCustomerRef": 57895
                            },
                            {
                                "rph": 2,
                                "odyCustomerRef": 57894
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
                    "addressline1": "TEST ADDRESS",
                    "addressline2": "TEST ADDRESS 1",
                    "postalCode": "33141"
                },
                "nationality": {
                    "id": "US"
                },
                "contactInfo": {
                    "email": "john@domain.com",
                    "phone1": {
                        "countryCode": "1",
                        "number": "+1416-555-4566"
                    },
                    "phone2": {
                        "countryCode": "1",
                        "number": "+1416-555-4566"
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
                    "addressline1": "TEST ADDRESS",
                    "addressline2": "TEST ADDRESS 1",
                    "postalCode": "39020"
                },
                "nationality": {
                    "id": "US"
                },
                "contactInfo": {
                    "email": "maria@domain.com",
                    "phone1": {
                        "countryCode": "1",
                        "number": "+1416-555-4566"
                    },
                    "phone2": {
                        "countryCode": "1",
                        "number": "+1416-555-4566"
                    }
                }
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
