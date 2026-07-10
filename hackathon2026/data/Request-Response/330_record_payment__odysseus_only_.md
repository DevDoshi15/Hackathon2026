# Record Payment (Odysseus Only)

**Path:** Record Payment (Odysseus Only) > Record Payment (Odysseus Only)

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/recordpayment`

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
    "trackingInfo": {
        "requestId": "cf87e672-1f98-4ae5-bb17-6b0b936a4a4f",
        "token": "EQTEMPKEN"
    },
    "id": 97269,
    "cruiseReservation": {
        "id": 146131,
        "syncInfo": {
            "supplierSyncInfo": {
                "token": "e0b14b",
                "lastSyncOn": "19-Jan-2024 03:53:02"
            },
            "apiSyncInfo": {
                "token": "fT1fDswY3Eih6YPKyMsDRankF5ttC1Mn",
                "sessionId": "ca83e9a1-cbc8-4503-a9e4-179b6d0b5327",
                "lastSyncOn": "19-Jan-2024 03:53:07"
            }
        }
    },
    "paymentToProcess": {
        "amount": 1136.4,
        "currency": "USD",
        "paymentForm": "Check",
        "paymentPreferences": {
            "confirmReservation": true // pass this flag to mark the existing 'Held' reservation as 'Confirmed' in Odysseus system
        },
        "maskedCard": {
            "number": "XXXXXXXXXXXX1111",// masked card information
            "cardHolderName": "John Doe",
            "billingAddress": {
                "city": {
                    "id": "MIA"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                },
                "addressline1": "NE 4th Avenue",
                "postalCode": "33109"
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
Date: Fri, 19 Jan 2024 08:54:22 GMT
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
            "requestId": "835e99bc-fe50-4271-80de-1569789899bf",
            "timeStamp": "19-Jan-2024 03:54:22",
            "token": "EQTEMPKEN"
        },
        "id": 97269,
        "agencyConfirmation": "OHZ9WPQ",
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "09-Feb-2024 00:00:00",
                "arrivalDateTime": "12-Feb-2024 00:00:00",
                "departureCityId": "MIA",
                "arrivalCityId": "MIA",
                "duration": 3
            },
            "id": 146131,
            "status": 7, // reservation marked as 'Confirmed'
            "reservationReferences": {
                "confirmationNumber": "53031"
            },
            "pos": {
                "id": 2516,
                "officeId": "O100US6797",
                "currency": "USD",
                "type": "B2B",
                "system": "Test",
                "apiId": "RCCL"
            },
            "customerReferences": [
                {
                    "rph": 1,
                    "ageGroup": "Adult",
                    "odyCustomerRef": 65991,
                    "supplierCustomerRef": "587532579",
                    "isPrimaryContact": true
                },
                {
                    "rph": 2,
                    "ageGroup": "Adult",
                    "odyCustomerRef": 64840,
                    "supplierCustomerRef": "587532587"
                }
            ],
            "paymentSchedules": {
                "customerPaymentSchedules": [
                    {
                        "id": 589472,
                        "type": 2,
                        "amount": 1116.4,
                        "dueDate": "24-Jan-2024 16:59:00"
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "id": 589473,
                        "type": 2,
                        "amount": 1116.4,
                        "dueDate": "24-Jan-2024 16:59:00"
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "id": 589471,
                        "type": 2,
                        "amount": 963.68,
                        "dueDate": "26-Jan-2024 16:59:00"
                    }
                ]
            },
            "prices": [
                {
                    "id": 1,
                    "code": "49",
                    "amount": 1565,
                    "priority": 5,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "60",
                    "amount": 180,
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
                    "code": "30%SavingsNRD",
                    "amount": 0,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 5,
                    "code": "KickerNRD",
                    "amount": -100,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 5,
                    "code": "ExtraSavNRD",
                    "amount": -76,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 5,
                    "code": "AirPromo",
                    "amount": 0,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 5,
                    "code": "30%SavingsNR",
                    "amount": -542,
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
                    "amount": 847,
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
                    "amount": -5,
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
                    "amount": 842,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 662,
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
                    "amount": 244.4,
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
                    "amount": 1116.4,
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
                    "id": 128,
                    "code": "P1",
                    "amount": 10,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": -1
                },
                {
                    "id": 128,
                    "code": "P2",
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
                    "amount": 1116.4,
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
                    "amount": 1116.4,
                    "priority": 355,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "8",
                    "amount": 1066.4,
                    "priority": 359,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 24,
                    "code": "6",
                    "amount": 250,
                    "priority": 360,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
                    "priority": 360,
                    "display": true,
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
                    "amount": 1066.4,
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
                    "amount": 102.72,
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
                    "amount": 963.68,
                    "priority": 510,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 66,
                    "code": "42",
                    "amount": 963.68,
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
                    "amount": 152.72,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 1116.4,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 1,
                    "code": "49",
                    "amount": 782.5,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 2,
                    "code": "60",
                    "amount": 90,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 73,
                    "code": "NCD",
                    "amount": 0,
                    "priority": 7,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 5,
                    "code": "AirPromo",
                    "amount": 0,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 5,
                    "code": "ExtraSavNRD",
                    "amount": -38,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 5,
                    "code": "KickerNRD",
                    "amount": -50,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 5,
                    "code": "30%SavingsNRD",
                    "amount": 0,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 5,
                    "code": "30%SavingsNR",
                    "amount": -271,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 7,
                    "code": "1",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 74,
                    "code": "SER",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 423.5,
                    "priority": 10,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 122,
                    "code": "",
                    "amount": 0,
                    "priority": 11,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 48,
                    "code": "",
                    "amount": 12.5,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 49,
                    "code": "",
                    "amount": 0,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 44,
                    "code": "",
                    "amount": -2.5,
                    "priority": 12,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 46,
                    "code": "",
                    "amount": 421,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 331,
                    "priority": 16,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 54,
                    "code": "",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 58,
                    "code": "108",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 41,
                    "code": "13",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 9,
                    "code": "46",
                    "amount": 0,
                    "priority": 23,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 10,
                    "code": "44",
                    "amount": 0,
                    "priority": 24,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 12,
                    "code": "33",
                    "amount": 0,
                    "priority": 25,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 3,
                    "code": "18",
                    "amount": 122.2,
                    "details": {
                        "isTax": true,
                        "isCommission": false
                    },
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 70,
                    "code": "70",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 75,
                    "code": "DSC",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 76,
                    "code": "SOC",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 6,
                    "code": "52",
                    "amount": 0,
                    "priority": 90,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 17,
                    "code": "",
                    "amount": 563.2,
                    "priority": 100,
                    "display": true,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 86,
                    "code": "",
                    "amount": 10,
                    "priority": 100,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 14,
                    "code": "107",
                    "amount": 0,
                    "priority": 105,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 60,
                    "code": "",
                    "amount": 0,
                    "priority": 200,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 84,
                    "code": "",
                    "amount": 0,
                    "priority": 200,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 128,
                    "code": "P2",
                    "amount": 10,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 128,
                    "code": "P1",
                    "amount": 0,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 40,
                    "code": "",
                    "amount": 0,
                    "priority": 300,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 23,
                    "code": "",
                    "amount": 563.2,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 563.2,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 50,
                    "code": "8",
                    "amount": 533.2,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 24,
                    "code": "6",
                    "amount": 125,
                    "priority": 360,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
                    "priority": 360,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 26,
                    "code": "IAR",
                    "amount": 0,
                    "priority": 380,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 63,
                    "code": "3",
                    "amount": 533.2,
                    "priority": 382,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
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
                    "odyCustomerRef": 65991
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
                    "odyCustomerRef": 65991
                },
                {
                    "id": 32,
                    "code": "80",
                    "amount": 51.36,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "priority": 509,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 65,
                    "code": "",
                    "amount": 481.84,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 66,
                    "code": "42",
                    "amount": 481.84,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
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
                    "odyCustomerRef": 65991
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 81.36,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 563.2,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 65991
                },
                {
                    "id": 1,
                    "code": "49",
                    "amount": 782.5,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 2,
                    "code": "60",
                    "amount": 90,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 73,
                    "code": "NCD",
                    "amount": 0,
                    "priority": 7,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 5,
                    "code": "AirPromo",
                    "amount": 0,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 5,
                    "code": "ExtraSavNRD",
                    "amount": -38,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 5,
                    "code": "KickerNRD",
                    "amount": -50,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 5,
                    "code": "30%SavingsNRD",
                    "amount": 0,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 5,
                    "code": "30%SavingsNR",
                    "amount": -271,
                    "priority": 9,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 7,
                    "code": "1",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 74,
                    "code": "SER",
                    "amount": 0,
                    "priority": 10,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 423.5,
                    "priority": 10,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 122,
                    "code": "",
                    "amount": 0,
                    "priority": 11,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 48,
                    "code": "",
                    "amount": 12.5,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 49,
                    "code": "",
                    "amount": 0,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 44,
                    "code": "",
                    "amount": -2.5,
                    "priority": 12,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 46,
                    "code": "",
                    "amount": 421,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 331,
                    "priority": 16,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 54,
                    "code": "",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 58,
                    "code": "108",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 41,
                    "code": "13",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 9,
                    "code": "46",
                    "amount": 0,
                    "priority": 23,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 10,
                    "code": "44",
                    "amount": 0,
                    "priority": 24,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 12,
                    "code": "33",
                    "amount": 0,
                    "priority": 25,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 3,
                    "code": "18",
                    "amount": 122.2,
                    "details": {
                        "isTax": true,
                        "isCommission": false
                    },
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 70,
                    "code": "70",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 75,
                    "code": "DSC",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 76,
                    "code": "SOC",
                    "amount": 0,
                    "priority": 80,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 6,
                    "code": "52",
                    "amount": 0,
                    "priority": 90,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 17,
                    "code": "",
                    "amount": 563.2,
                    "priority": 100,
                    "display": true,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 86,
                    "code": "",
                    "amount": 10,
                    "priority": 100,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 14,
                    "code": "107",
                    "amount": 0,
                    "priority": 105,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 60,
                    "code": "",
                    "amount": 0,
                    "priority": 200,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 84,
                    "code": "",
                    "amount": 0,
                    "priority": 200,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 128,
                    "code": "P2",
                    "amount": 10,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 128,
                    "code": "P1",
                    "amount": 0,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 40,
                    "code": "",
                    "amount": 0,
                    "priority": 300,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 23,
                    "code": "",
                    "amount": 563.2,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 563.2,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 50,
                    "code": "8",
                    "amount": 533.2,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 24,
                    "code": "6",
                    "amount": 125,
                    "priority": 360,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
                    "priority": 360,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 26,
                    "code": "IAR",
                    "amount": 0,
                    "priority": 380,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 63,
                    "code": "3",
                    "amount": 533.2,
                    "priority": 382,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
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
                    "odyCustomerRef": 64840
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
                    "odyCustomerRef": 64840
                },
                {
                    "id": 32,
                    "code": "80",
                    "amount": 51.36,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "priority": 509,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 65,
                    "code": "",
                    "amount": 481.84,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 66,
                    "code": "42",
                    "amount": 481.84,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
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
                    "odyCustomerRef": 64840
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 81.36,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 563.2,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 64840
                }
            ],
            "syncInfo": {
                "apiSyncInfo": {
                    "token": "ridJO8wY3EipEnQR1GlrS66wL7LSQQWz",
                    "sessionId": "117412a9-69d4-4b6b-aeb0-2fb2d24105b3",
                    "lastSyncOn": "19-Jan-2024 03:54:22"
                }
            },
            "timeStamps": {
                "system": {
                    "createdOn": "19-Jan-2024 02:27:57",
                    "lastModifiedOn": "19-Jan-2024 03:53:03"
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
                "currencyId": "USD",
                "countryId": "US"
            },
            "supplierCommunicationInfo": {
                "agent": {
                    "contactInfo": {
                        "email": "QATeam@odysol.com",
                        "phone1": {
                            "number": "1234567891"
                        }
                    }
                }
            },
            "cruise": {
                "packageId": 1330761,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 8,
                    "ships": [
                        {
                            "id": 116
                        }
                    ]
                },
                "itinerary": {
                    "id": 353818,
                    "destination": {
                        "id": 7
                    }
                },
                "voyage": {
                    "departureDateTime": "09-Feb-2024 00:00:00",
                    "arrivalDateTime": "12-Feb-2024 00:00:00",
                    "departureCityId": "MIA",
                    "arrivalCityId": "MIA",
                    "code": "FR3BH074"
                },
                "transportationType": 29
            },
            "rulesInfo": {
                "applicableRules": [
                    {
                        "id": 1728532,
                        "name": "Demo Value Add Offer B2B and B2C",
                        "groupName": "nonexcl",
                        "type": 40,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "This is for Customer view only",
                            "agencyDetails": "This is for Agent's view only",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "https://sandbox.odysol.com/site/images/promotions/1180486.png"
                        }
                    },
                    {
                        "id": 1728533,
                        "name": "Demo Value Add Offer B2C",
                        "groupName": "nonexcl",
                        "type": 40,
                        "externalGroupId": "",
                        "externalId": "",
                        "offeredBy": 2,
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "This is for Customer view only",
                            "agencyDetails": "This is for Agent's view only",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "https://sandbox.odysol.com/site/images/promotions/dfdfdfdf.png"
                        }
                    },
                    {
                        "id": 1728534,
                        "name": "Demo Value Add Offer B2B",
                        "groupName": "nonexcl",
                        "type": 40,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "This is for Customer view only",
                            "agencyDetails": "This is for Agent's view only",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "https://sandbox.odysol.com/site/images/promotions/sale-dollar.gif"
                        }
                    },
                    {
                        "id": 1728342,
                        "name": "Cruise Discount (5$)",
                        "groupName": "excl_1728342",
                        "type": 1,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728343,
                        "name": "Cruise Markup (25$)",
                        "groupName": "excl_1728343",
                        "type": 2,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728421,
                        "name": "VAO One Exclusive",
                        "groupName": "excl_1728421",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "pink-circle.png"
                        }
                    },
                    {
                        "id": 1728422,
                        "name": "VAO Non Exclusive",
                        "groupName": "nonexcl",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "CruiseCategory",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "va_anchor-vODY-635382737153437500.png"
                        }
                    },
                    {
                        "id": 1728423,
                        "name": "VAO Two Non Exclusive",
                        "groupName": "nonexcl",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "CruiseCategory",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "va_sale.png"
                        }
                    },
                    {
                        "id": 1728419,
                        "name": "Cruise Addon",
                        "groupName": "excl_1728419",
                        "type": 9,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728344,
                        "name": "Cruise Service Fee (20$)",
                        "groupName": "excl_1728344",
                        "type": 13,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728415,
                        "name": "Package Service Doc (10)",
                        "groupName": "P1",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728416,
                        "name": "Package Service Doc One (15)",
                        "groupName": "P1",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728417,
                        "name": "Package Service Travel (25) BEST Value YES",
                        "groupName": "P2",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728418,
                        "name": "Package Service Travel (20) BEST Value NO",
                        "groupName": "P2",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    }
                ]
            },
            "categories": [
                {
                    "id": 358460536,
                    "code": "2D",
                    "type": 3,
                    "cabins": [
                        {
                            "number": "8280",
                            "beds": [
                                {
                                    "code": "U"
                                }
                            ],
                            "position": "Midship",
                            "occupancy": {
                                "min": 0,
                                "max": 2
                            }
                        }
                    ],
                    "fares": [
                        {
                            "upgradeFrom": "2D",
                            "rules": [
                                {
                                    "id": 1728532,
                                    "calculatedAmount": {
                                        "0": 50,
                                        "1": 25,
                                        "2": 25
                                    }
                                },
                                {
                                    "id": 1728533,
                                    "calculatedAmount": {
                                        "0": 50,
                                        "1": 25,
                                        "2": 25
                                    }
                                },
                                {
                                    "id": 1728534,
                                    "calculatedAmount": {
                                        "0": 50,
                                        "1": 25,
                                        "2": 25
                                    }
                                },
                                {
                                    "id": 1728342,
                                    "calculatedAmount": {
                                        "0": 5,
                                        "1": 2.5,
                                        "2": 2.5
                                    }
                                },
                                {
                                    "id": 1728343,
                                    "calculatedAmount": {
                                        "0": 25,
                                        "1": 12.5,
                                        "2": 12.5
                                    }
                                },
                                {
                                    "id": 1728421
                                },
                                {
                                    "id": 1728422
                                },
                                {
                                    "id": 1728423
                                },
                                {
                                    "id": 1728419,
                                    "calculatedAmount": {
                                        "0": 12,
                                        "1": 6,
                                        "2": 6
                                    }
                                },
                                {
                                    "id": 1728344,
                                    "calculatedAmount": {
                                        "0": 20,
                                        "1": 10,
                                        "2": 10
                                    }
                                },
                                {
                                    "id": 1728415,
                                    "calculatedAmount": {
                                        "0": 10,
                                        "1": 5,
                                        "2": 5
                                    }
                                },
                                {
                                    "id": 1728416,
                                    "calculatedAmount": {
                                        "0": 15,
                                        "1": 7.5,
                                        "2": 7.5
                                    }
                                },
                                {
                                    "id": 1728417,
                                    "calculatedAmount": {
                                        "0": 25,
                                        "1": 12.5,
                                        "2": 12.5
                                    }
                                },
                                {
                                    "id": 1728418,
                                    "calculatedAmount": {
                                        "0": 20,
                                        "1": 10,
                                        "2": 10
                                    }
                                }
                            ],
                            "status": -1,
                            "fareCode": {
                                "code": "J2161620",
                                "name": "30% Savings NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "combinableFares": [
                                    {
                                        "code": "H3829346",
                                        "description": "Extra Sav NRD",
                                        "type": 0,
                                        "refundableType": 2
                                    },
                                    {
                                        "code": "M9569090",
                                        "description": "Air Promo",
                                        "type": 0,
                                        "refundableType": 2
                                    },
                                    {
                                        "code": "M9569091",
                                        "description": "Kicker NRD",
                                        "type": 0,
                                        "refundableType": 2
                                    }
                                ],
                                "dynamicRules": [
                                    {
                                        "type": 6
                                    }
                                ],
                                "bookOnline": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below",
                                    "qualifierCodes": ""
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
                        "group": "Language",
                        "customerReferences": [
                            {
                                "rph": 1,
                                "odyCustomerRef": 65991
                            },
                            {
                                "rph": 2,
                                "odyCustomerRef": 64840
                            }
                        ]
                    },
                    {
                        "code": "en-LND",
                        "name": "English",
                        "description": "English",
                        "type": "DOCUMENTLANGUAGE",
                        "group": "Language",
                        "customerReferences": [
                            {
                                "rph": 1,
                                "odyCustomerRef": 65991
                            },
                            {
                                "rph": 2,
                                "odyCustomerRef": 64840
                            }
                        ]
                    }
                ]
            },
            "packages": [],
            "dinings": [
                {
                    "id": 1,
                    "code": "M",
                    "name": "06:00 PM",
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
                "odyCustomerRef": 65991,
                "firstName": "John",
                "middleName": "",
                "lastName": "Doe",
                "dateOfBirth": "02-Jan-1970",
                "age": 54,
                "address": {
                    "city": {
                        "name": "CHICAGO"
                    },
                    "country": {
                        "id": "US"
                    },
                    "state": {
                        "id": "IL"
                    },
                    "addressline1": "Test Address 1",
                    "addressline2": "",
                    "postalCode": "39020"
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
                "odyCustomerRef": 64840,
                "firstName": "Maria",
                "middleName": "",
                "lastName": "Doe",
                "dateOfBirth": "01-Jan-1965",
                "age": 59,
                "nationality": {
                    "id": "US"
                },
                "contactInfo": {
                    "email": "maria@domain.com",
                    "phone1": {
                        "countryCode": "1",
                        "number": "+14165554566"
                    },
                    "phone2": {
                        "countryCode": "1",
                        "number": "+14165554566"
                    }
                }
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
