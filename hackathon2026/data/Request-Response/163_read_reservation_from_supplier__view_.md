# Read Reservation From Supplier (View)

**Path:** Create Reservation > Create Reservation With Packages > Auto-Inclusion of Packages > Create Reservation WITH DoNotAutoIncludePackages Preference > Read Reservation From Supplier (View)

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
    "id": 88715,
    "cruiseReservation": {
        "id": 136582,
        "readPreferences": {
            "mode": "View", //Possible values are View/Modify/Pay
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
Date: Fri, 03 Nov 2023 10:54:29 GMT
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
            "requestId": "46952788-3393-451c-b25b-d97ff325c855",
            "timeStamp": "03-Nov-2023 06:54:25",
            "token": "EQTEMPKEN"
        },
        "id": 88715,
        "agencyConfirmation": "TKT8UA8",
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "03-Feb-2024 00:00:00",
                "arrivalDateTime": "10-Feb-2024 00:00:00",
                "departureCityId": "FLL",
                "arrivalCityId": "FLL",
                "duration": 7
            },
            "id": 136582,
            "status": 6,
            "reservationReferences": {
                "confirmationNumber": "2QWV4H"
            },
            "reservationIndicators": {
                "modifyIndicators": [
                    {
                        "type": "FirstName",
                        "value": false
                    },
                    {
                        "type": "LastName",
                        "value": false
                    },
                    {
                        "type": "Title",
                        "value": false
                    }
                ]
            },
            "pos": {
                "id": 2519,
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
                    "odyCustomerRef": 76171,
                    "supplierCustomerRef": "1",
                    "isPrimaryContact": true
                },
                {
                    "rph": 2,
                    "ageGroup": "Adult",
                    "odyCustomerRef": 76172,
                    "supplierCustomerRef": "2"
                }
            ],
            "paymentSchedules": {
                "customerPaymentSchedules": [
                    {
                        "id": 548048,
                        "type": 2,
                        "amount": 2448,
                        "dueDate": "03-Nov-2023 23:59:00"
                    }
                ],
                "affiliatePaymentSchedules": [
                    {
                        "id": 548049,
                        "type": 2,
                        "amount": 2448,
                        "dueDate": "03-Nov-2023 23:59:00"
                    }
                ],
                "supplierPaymentSchedules": [
                    {
                        "id": 548047,
                        "type": 2,
                        "amount": 2235.2,
                        "dueDate": "05-Nov-2023 23:59:00"
                    }
                ]
            },
            "prices": [
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 2033,
                    "priority": 5,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "amount": 380,
                    "priority": 6,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 2033,
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
                    "amount": 2028,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": -1
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 1648,
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
                    "amount": 390,
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
                    "amount": 2448,
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
                    "amount": 2448,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": -1
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 2448,
                    "priority": 355,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 2398,
                    "priority": 359,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 350,
                    "priority": 360,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
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
                    "amount": 2398,
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
                    "amount": 162.8,
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
                    "amount": 2235.2,
                    "priority": 510,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "amount": 2235.2,
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
                    "amount": 212.8,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 2448,
                    "priority": 600,
                    "displayType": 4,
                    "rph": -1
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 1016.5,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "amount": 190,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 1016.5,
                    "priority": 10,
                    "display": true,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 122,
                    "code": "",
                    "amount": 0,
                    "priority": 11,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 44,
                    "code": "",
                    "amount": -2.5,
                    "priority": 12,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 48,
                    "code": "",
                    "amount": 12.5,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 49,
                    "code": "",
                    "amount": 0,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 46,
                    "code": "",
                    "amount": 1014,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 824,
                    "priority": 16,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 54,
                    "code": "",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 3,
                    "code": "TXFS",
                    "amount": 195,
                    "details": {
                        "isTax": true,
                        "isCommission": false
                    },
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 6,
                    "code": "",
                    "amount": 0,
                    "priority": 90,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 17,
                    "code": "",
                    "amount": 1229,
                    "priority": 100,
                    "display": true,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 86,
                    "code": "",
                    "amount": 10,
                    "priority": 100,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 84,
                    "code": "",
                    "amount": 0,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 128,
                    "code": "P2",
                    "amount": 10,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 128,
                    "code": "P1",
                    "amount": 0,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 60,
                    "code": "",
                    "amount": 0,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 40,
                    "code": "",
                    "amount": 0,
                    "priority": 300,
                    "display": true,
                    "displayType": 2,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 23,
                    "code": "",
                    "amount": 1229,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 1229,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 1199,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 175,
                    "priority": 360,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 26,
                    "code": "",
                    "amount": 0,
                    "priority": 380,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 62,
                    "code": "",
                    "amount": 1199,
                    "priority": 382,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
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
                    "odyCustomerRef": 76171
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
                    "odyCustomerRef": 76171
                },
                {
                    "id": 32,
                    "code": "COMM",
                    "amount": 81.4,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "priority": 509,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 65,
                    "code": "",
                    "amount": 1117.6,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "amount": 1117.6,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
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
                    "odyCustomerRef": 76171
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 111.4,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 1229,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 1,
                    "odyCustomerRef": 76171
                },
                {
                    "id": 1,
                    "code": "AMCT",
                    "amount": 1016.5,
                    "priority": 5,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 2,
                    "code": "NCFR",
                    "amount": 190,
                    "priority": 6,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 45,
                    "code": "",
                    "amount": 1016.5,
                    "priority": 10,
                    "display": true,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 122,
                    "code": "",
                    "amount": 0,
                    "priority": 11,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 44,
                    "code": "",
                    "amount": -2.5,
                    "priority": 12,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 48,
                    "code": "",
                    "amount": 12.5,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 49,
                    "code": "",
                    "amount": 0,
                    "priority": 12,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 46,
                    "code": "",
                    "amount": 1014,
                    "priority": 15,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 114,
                    "code": "",
                    "amount": 824,
                    "priority": 16,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 54,
                    "code": "",
                    "amount": 0,
                    "priority": 22,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 3,
                    "code": "TXFS",
                    "amount": 195,
                    "details": {
                        "isTax": true,
                        "isCommission": false
                    },
                    "priority": 50,
                    "display": true,
                    "displayType": 8,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 6,
                    "code": "",
                    "amount": 0,
                    "priority": 90,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 17,
                    "code": "",
                    "amount": 1229,
                    "priority": 100,
                    "display": true,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 86,
                    "code": "",
                    "amount": 10,
                    "priority": 100,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 84,
                    "code": "",
                    "amount": 0,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 128,
                    "code": "P2",
                    "amount": 10,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 128,
                    "code": "P1",
                    "amount": 0,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 60,
                    "code": "",
                    "amount": 0,
                    "priority": 200,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 40,
                    "code": "",
                    "amount": 0,
                    "priority": 300,
                    "display": true,
                    "displayType": 2,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 23,
                    "code": "",
                    "amount": 1229,
                    "priority": 350,
                    "display": true,
                    "displayType": 1,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 47,
                    "code": "",
                    "amount": 1229,
                    "priority": 355,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 50,
                    "code": "GRSS",
                    "amount": 1199,
                    "priority": 359,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 24,
                    "code": "DPST",
                    "amount": 175,
                    "priority": 360,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 126,
                    "code": "",
                    "amount": 0,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 26,
                    "code": "",
                    "amount": 0,
                    "priority": 380,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 62,
                    "code": "",
                    "amount": 1199,
                    "priority": 382,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
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
                    "odyCustomerRef": 76172
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
                    "odyCustomerRef": 76172
                },
                {
                    "id": 32,
                    "code": "COMM",
                    "amount": 81.4,
                    "details": {
                        "isTax": false,
                        "isCommission": true
                    },
                    "priority": 509,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 65,
                    "code": "",
                    "amount": 1117.6,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 66,
                    "code": "NETD",
                    "amount": 1117.6,
                    "priority": 510,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
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
                    "odyCustomerRef": 76172
                },
                {
                    "id": 83,
                    "code": "",
                    "amount": 111.4,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                },
                {
                    "id": 112,
                    "code": "",
                    "amount": 1229,
                    "priority": 600,
                    "displayType": 4,
                    "rph": 2,
                    "odyCustomerRef": 76172
                }
            ],
            "syncInfo": {
                "apiSyncInfo": {
                    "token": "bAktQVvc20g4VKasfllHQZPHoVkCxhLB",
                    "sessionId": "aca65438-597e-4147-93c7-a15902c612c1",
                    "lastSyncOn": "03-Nov-2023 06:54:29"
                }
            },
            "timeStamps": {
                "supplier": {
                    "createdOn": "03-Nov-2023 03:51:00"
                },
                "system": {
                    "createdOn": "03-Nov-2023 06:51:07",
                    "lastModifiedOn": "03-Nov-2023 06:53:12"
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
                "packageId": 1353443,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 5,
                    "ships": [
                        {
                            "id": 13250
                        }
                    ]
                },
                "itinerary": {
                    "id": 370945,
                    "destination": {
                        "id": 9
                    }
                },
                "voyage": {
                    "departureDateTime": "03-Feb-2024 00:00:00",
                    "arrivalDateTime": "10-Feb-2024 00:00:00",
                    "departureCityId": "FLL",
                    "arrivalCityId": "FLL",
                    "code": "I416"
                },
                "transportationType": 29
            },
            "rulesInfo": {
                "applicableRules": [
                    {
                        "id": 1728537,
                        "name": "OBC CONSOLIDATOR RULE - DEMO PURPOSES ONLY ##PromotionAmount##",
                        "groupName": "nonexcl",
                        "type": 5,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "Customer information for Demo Purposes",
                            "agencyDetails": "Anything this rule promises you is not real.",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "https://sandbox.odysol.com/site/images/promotions/cdor_wine2.png"
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
                        "id": 1728420,
                        "name": "VAO Exclusive",
                        "groupName": "excl_1728420",
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
                            "imageUrl": "va_earlysaver.png"
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
                    "id": 52916,
                    "code": "C",
                    "type": 2,
                    "cabins": [
                        {
                            "number": "1080",
                            "beds": [
                                {
                                    "code": "QN",
                                    "description": "Queen Bed ",
                                    "type": 243
                                }
                            ],
                            "deck": {
                                "id": 5149,
                                "name": "Main Deck",
                                "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
                            },
                            "location": "Midship Port Oceanview",
                            "occupancy": {
                                "min": 0,
                                "max": 4
                            }
                        }
                    ],
                    "fares": [
                        {
                            "upgradeFrom": "C",
                            "rules": [
                                {
                                    "id": 1728537,
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
                                    "id": 1728420
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
                                "code": "QA1",
                                "name": "NON-REFUNDABLE DEPOSIT",
                                "description": "NON-REFUNDABLE FARE",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "NON-REFUNDABLE FARE",
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
                        "code": "N",
                        "name": "No",
                        "description": "Decline Complimentary Upgrade",
                        "type": "UPG",
                        "group": "ComplimentaryUpgrade",
                        "customerReferences": [
                            {
                                "rph": 1,
                                "odyCustomerRef": 76171
                            },
                            {
                                "rph": 2,
                                "odyCustomerRef": 76172
                            }
                        ],
                        "associationType": "PAX"
                    }
                ]
            },
            "packages": [
                {
                    "code": "B0TNOXFR",
                    "description": "NO TRANSFER",
                    "type": "PrePackage",
                    "isComplimentary": true,
                    "departureArrivalInfo": {
                        "departureDateTime": "03-Feb-2024 00:00:00",
                        "arrivalDateTime": "03-Feb-2024 00:00:00"
                    },
                    "prices": [
                        {
                            "id": 41, // Packages item is present but with value 0, indicating no packages was selected
                            "amount": 0,
                            "type": "AVGPP"
                        }
                    ],
                    "customerReferences": [
                        {
                            "rph": 1,
                            "odyCustomerRef": 76171
                        },
                        {
                            "rph": 2,
                            "odyCustomerRef": 76172
                        }
                    ]
                },
                {
                    "code": "A0TNOXFR",
                    "description": "NO TRANSFER",
                    "type": "PostPackage",
                    "isComplimentary": true,
                    "departureArrivalInfo": {
                        "departureDateTime": "10-Feb-2024 00:00:00",
                        "arrivalDateTime": "10-Feb-2024 00:00:00"
                    },
                    "prices": [
                        {
                            "id": 41, // Packages item is present but with value 0, indicating no packages was selected
                            "amount": 0,
                            "type": "AVGPP"
                        }
                    ],
                    "customerReferences": [
                        {
                            "rph": 1,
                            "odyCustomerRef": 76171
                        },
                        {
                            "rph": 2,
                            "odyCustomerRef": 76172
                        }
                    ]
                }
            ],
            "dinings": [
                {
                    "id": 8,
                    "code": "3",
                    "name": "Early Seating Upper Level 5:45 PM",
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
                "odyCustomerRef": 76171,
                "firstName": "Monish",
                "middleName": "",
                "lastName": "Luthra",
                "dateOfBirth": "12-Jan-1970",
                "age": 54,
                "address": {
                    "city": {
                        "id": "FLL",
                        "name": ""
                    },
                    "country": {
                        "id": "US"
                    },
                    "state": {},
                    "addressline1": "",
                    "addressline2": "",
                    "postalCode": ""
                },
                "nationality": {},
                "contactInfo": {
                    "email": "monishluthra@domain.com",
                    "phone1": {
                        "countryCode": "1",
                        "number": "+11234567890"
                    },
                    "phone2": {
                        "countryCode": "1",
                        "number": "+1123-456-7890"
                    }
                }
            },
            {
                "title": "MR",
                "gender": "Male",
                "rph": 2,
                "odyCustomerRef": 76172,
                "firstName": "Anna",
                "middleName": "",
                "lastName": "Luthra",
                "dateOfBirth": "11-Jan-1965",
                "age": 59,
                "nationality": {},
                "contactInfo": {
                    "email": "mariana@domain.com",
                    "phone1": {
                        "countryCode": "1",
                        "number": "+1123-456-7890"
                    },
                    "phone2": {
                        "countryCode": "1",
                        "number": "+1123-456-7890"
                    }
                }
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
