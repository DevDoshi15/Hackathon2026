# Reservation History

**Path:** Reservation History (Odysseus Only) > Reservation History

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/History`

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
    "id": 69332,
    "cruiseReservation": {
        "id": 117312
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
Date: Mon, 10 Jul 2023 11:59:01 GMT
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
      "requestId": "5e1aac8b-190f-405d-adfe-26c23d607acb",
      "timeStamp": "10-Jul-2023 07:59:01",
      "token": "EQTEMPKEN"
    },
    "id": 69332,
    "cruiseReservationId": 117312,
    "historyInfo": [
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "23-Jun-2023 09:37:39"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "16-Jun-2023 09:48:06"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "14-Jun-2023 09:39:05"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "14-Jun-2023 09:38:55"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "13-Jun-2023 15:50:16"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "09-Jun-2023 18:31:22"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "09-Jun-2023 13:06:45"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "09-Jun-2023 03:30:40"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "09-Jun-2023 02:31:55"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "06-Jun-2023 09:23:50"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "06-Jun-2023 09:23:45"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "02-Jun-2023 17:43:39"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "01-Jun-2023 19:09:05"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "31-May-2023 12:23:52"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "31-May-2023 12:23:46"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "30-May-2023 10:47:12"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "30-May-2023 05:50:09"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "30-May-2023 05:49:58"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "27-May-2023 16:04:37"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "26-May-2023 11:45:51"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "24-May-2023 17:08:35"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "24-May-2023 17:08:16"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "24-May-2023 03:11:04"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "24-May-2023 03:10:43"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "23-May-2023 23:00:47"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "23-May-2023 22:43:00"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "23-May-2023 15:52:30"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "23-May-2023 12:15:07"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "23-May-2023 12:14:58"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "22-May-2023 09:47:14"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "16-May-2023 10:44:59"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "16-May-2023 10:42:30"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "15-May-2023 11:25:09"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 IS DENIED. SECURED BOOKING<Br>Code: CSE0097<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "12-May-2023 04:26:16"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: Validation<Br>Text: OfficeId / API setup is missing (SetupApiProperties)130386 - 130386 - 1<Br>",
        "timeStamp": {
          "system": {
            "createdOn": "11-May-2023 06:18:40"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: Validation<Br>Text: OfficeId / API setup is missing (SetupApiProperties)130386 - 130386 - 1<Br>",
        "timeStamp": {
          "system": {
            "createdOn": "11-May-2023 06:12:33"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: Validation<Br>Text: OfficeId / API setup is missing (SetupApiProperties)130386 - 130386 - 1<Br>",
        "timeStamp": {
          "system": {
            "createdOn": "11-May-2023 05:14:05"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: Validation<Br>Text: OfficeId / API setup is missing (SetupApiProperties)130386 - 130386 - 1<Br>",
        "timeStamp": {
          "system": {
            "createdOn": "11-May-2023 04:27:56"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: Validation<Br>Text: OfficeId / API setup is missing (SetupApiProperties)130386 - 130386 - 1<Br>",
        "timeStamp": {
          "system": {
            "createdOn": "10-May-2023 12:37:00"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: Validation<Br>Text: OfficeId / API setup is missing (SetupApiProperties)130386 - 130386 - 5<Br>",
        "timeStamp": {
          "system": {
            "createdOn": "09-May-2023 18:52:30"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "09-May-2023 11:06:47"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "09-May-2023 08:35:01"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "",
        "timeStamp": {
          "system": {
            "createdOn": "09-May-2023 05:46:59"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Booking Status Updated from 6 to 14 (internal trigger)",
        "timeStamp": {
          "system": {
            "createdOn": "09-May-2023 05:46:59"
          }
        },
        "type": "StatusChange",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "08-May-2023 08:30:13"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Cruise DestinationName from  to Alaska <br>\nModify Pax #1 Country from  to US<br>\nModify Pax #1 State from  to FL<br>\nModify Pax #2 Country from  to US<br>\nModify Pax #2 State from  to FL<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "08-May-2023 08:30:04"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "05-May-2023 10:54:38"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Cruise DestinationName from  to Alaska <br>\nModify Pax #1 Country from  to US<br>\nModify Pax #1 State from  to FL<br>\nModify Pax #2 Country from  to US<br>\nModify Pax #2 State from  to FL<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "05-May-2023 10:54:28"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "05-May-2023 05:50:16"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Cruise DestinationName from  to Alaska <br>\nModify Pax #1 Country from  to US<br>\nModify Pax #1 State from  to FL<br>\nModify Pax #2 Country from  to US<br>\nModify Pax #2 State from  to FL<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "05-May-2023 05:50:13"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "05-May-2023 03:11:54"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Cruise DestinationName from  to Alaska <br>\nModify Pax #1 Country from  to US<br>\nModify Pax #1 State from  to FL<br>\nModify Pax #2 Country from  to US<br>\nModify Pax #2 State from  to FL<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "05-May-2023 03:11:50"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "CruisePaymentFailed",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:32:55"
          }
        },
        "type": "General",
        "user": {
          "id": -5,
          "name": "Auto Process"
        }
      },
      {
        "description": "<strong>Customer Unknown</strong><br>Amount: 3339.5, Currency: USD, Payment type: Full, Mode: Card, Status: Unknown, Transaction Type: Purchase, Processed With: Supplier, Successful: False, Payment Gateway: PCIPay",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:32:55"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:24:07"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Cruise DestinationName from  to Alaska <br>\nModify Pax #1 Country from  to US<br>\nModify Pax #1 State from  to FL<br>\nModify Pax #2 Country from  to US<br>\nModify Pax #2 State from  to FL<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:24:04"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "CruisePaymentFailed",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:23:06"
          }
        },
        "type": "General",
        "user": {
          "id": -5,
          "name": "Auto Process"
        }
      },
      {
        "description": "<strong>Customer Unknown</strong><br>Amount: 1193.46, Currency: USD, Payment type: Full, Mode: Card, Status: Unknown, Transaction Type: Purchase, Processed With: Supplier, Successful: False, Payment Gateway: PCIPay",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:23:06"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:07:36"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Cruise DestinationName from  to Alaska <br>\nModify Pax #1 Country from  to US<br>\nModify Pax #1 State from  to FL<br>\nModify Pax #2 Country from  to US<br>\nModify Pax #2 State from  to FL<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:07:33"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : False.<br><strong>Total errors:</strong> 1<Br>#: 1Type: RCCL<Br>Text: ACCESS TO BOOKING ID 0395750 DENIED. BOOKING IS LOCKED<Br>Code: Msg_CruiseBookingIsLocked<br/>",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:05:57"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:04:37"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Special Services for Passenger #1 from 0 to 2<br>Modify Special Services for Passenger #2 from 0 to 2<br>Modify Cruise DestinationName from  to Alaska <br>\nModify Pax #1 Country from  to US<br>\nModify Pax #1 State from  to FL<br>\nModify Pax #2 Country from  to US<br>\nModify Pax #2 State from  to FL<br>\nModify pax #1 special service #0 Code from  to en-LNP<br>\nModify pax #1 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 AssociationType from  to P<br>\nModify pax #1 special service #0 Name from  to English<br>\nModify pax #1 special service #0 Description from  to English<br>\nModify pax #1 special service #0 Group from  to Language<br>\nModify pax #1 special service #0 OfferPerPassenger from  to True<br>\nModify pax #1 special service #0 IsMandatory from  to False<br>\nModify pax #1 special service #0 ServiceDateRequired from  to False<br>\nModify pax #1 special service #1 Code from  to en-LND<br>\nModify pax #1 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 AssociationType from  to P<br>\nModify pax #1 special service #1 Name from  to English<br>\nModify pax #1 special service #1 Description from  to English<br>\nModify pax #1 special service #1 Group from  to Language<br>\nModify pax #1 special service #1 OfferPerPassenger from  to True<br>\nModify pax #1 special service #1 IsMandatory from  to False<br>\nModify pax #1 special service #1 ServiceDateRequired from  to False<br>\nModify pax #2 special service #0 Code from  to en-LNP<br>\nModify pax #2 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 AssociationType from  to P<br>\nModify pax #2 special service #0 Name from  to English<br>\nModify pax #2 special service #0 Description from  to English<br>\nModify pax #2 special service #0 Group from  to Language<br>\nModify pax #2 special service #0 OfferPerPassenger from  to True<br>\nModify pax #2 special service #0 IsMandatory from  to False<br>\nModify pax #2 special service #0 ServiceDateRequired from  to False<br>\nModify pax #2 special service #1 Code from  to en-LND<br>\nModify pax #2 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 AssociationType from  to P<br>\nModify pax #2 special service #1 Name from  to English<br>\nModify pax #2 special service #1 Description from  to English<br>\nModify pax #2 special service #1 Group from  to Language<br>\nModify pax #2 special service #1 OfferPerPassenger from  to True<br>\nModify pax #2 special service #1 IsMandatory from  to False<br>\nModify pax #2 special service #1 ServiceDateRequired from  to False<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 04:04:33"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:39:17"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Special Services for Passenger #1 from 3 to 5<br>Modify Special Services for Passenger #2 from 3 to 5<br>Modify Cruise DestinationName from  to Alaska <br>\nModify Cruise ClassTypeID from 0 to 1<br>\nModify Cruise ClassTypeName from  to Interior<br>\nModify Cruise DiningStatusID from 1 to 7<br>\nModify Cruise DiningStatusName from  to Confirmed<br>\nModify Cruise DiningStatusPseudoCode from  to 39<br>\nModify Pax #1 Country from  to US<br>\nModify Pax #1 State from  to FL<br>\nModify Pax #2 Country from  to US<br>\nModify Pax #2 State from  to FL<br>\nModify pax #1 special service #2 Code from ANV to <br>\nModify pax #1 special service #2 Type from ANNIVERSARY to <br>\nModify pax #2 special service #2 Code from ANV to <br>\nModify pax #2 special service #2 Type from ANNIVERSARY to <br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:39:13"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:19:32"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Cruise DestinationName from  to Alaska <br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:19:28"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 01:53:23"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Cruise DestinationName from  to Alaska <br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 01:53:20"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 01:52:14"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Special Services for Passenger #1 from 0 to 2<br>Modify Special Services for Passenger #2 from 0 to 2<br>Modify Cruise DestinationName from  to Alaska <br>\nModify Cruise ClassTypeID from 0 to 1<br>\nModify Cruise ClassTypeName from  to Interior<br>\nModify Cruise DiningStatusID from 1 to 7<br>\nModify Cruise DiningStatusName from  to Confirmed<br>\nModify Cruise DiningStatusPseudoCode from  to 39<br>\nModify Pax #1 PhoneOne from +14165554566 to 416-555-4566<br>\nModify Pax #2 Title from MRS to MR<br>\nModify Pax #2 Gender from 1 to 0<br>\nModify pax #1 special service #0 Code from  to en-LNP<br>\nModify pax #1 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 AssociationType from  to P<br>\nModify pax #1 special service #0 Name from  to English<br>\nModify pax #1 special service #0 Description from  to English<br>\nModify pax #1 special service #0 Group from  to Language<br>\nModify pax #1 special service #0 OfferPerPassenger from  to True<br>\nModify pax #1 special service #0 IsMandatory from  to False<br>\nModify pax #1 special service #0 ServiceDateRequired from  to False<br>\nModify pax #1 special service #1 Code from  to en-LND<br>\nModify pax #1 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 AssociationType from  to P<br>\nModify pax #1 special service #1 Name from  to English<br>\nModify pax #1 special service #1 Description from  to English<br>\nModify pax #1 special service #1 Group from  to Language<br>\nModify pax #1 special service #1 OfferPerPassenger from  to True<br>\nModify pax #1 special service #1 IsMandatory from  to False<br>\nModify pax #1 special service #1 ServiceDateRequired from  to False<br>\nModify pax #2 special service #0 Code from  to en-LNP<br>\nModify pax #2 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 AssociationType from  to P<br>\nModify pax #2 special service #0 Name from  to English<br>\nModify pax #2 special service #0 Description from  to English<br>\nModify pax #2 special service #0 Group from  to Language<br>\nModify pax #2 special service #0 OfferPerPassenger from  to True<br>\nModify pax #2 special service #0 IsMandatory from  to False<br>\nModify pax #2 special service #0 ServiceDateRequired from  to False<br>\nModify pax #2 special service #1 Code from  to en-LND<br>\nModify pax #2 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 AssociationType from  to P<br>\nModify pax #2 special service #1 Name from  to English<br>\nModify pax #2 special service #1 Description from  to English<br>\nModify pax #2 special service #1 Group from  to Language<br>\nModify pax #2 special service #1 OfferPerPassenger from  to True<br>\nModify pax #2 special service #1 IsMandatory from  to False<br>\nModify pax #2 special service #1 ServiceDateRequired from  to False<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 01:52:10"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:57"
          }
        },
        "type": "General",
        "user": {
          "id": 1021984,
          "name": "Sheron Parmar (Sheron_Sandbox)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:10:50"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify LinkedBookings from 0 to 2<br>Modify Special Services for Passenger #1 from 0 to 2<br>Modify Special Services for Passenger #2 from 0 to 2<br>Modify LinkedBookings Type from  to NotSpecified<br>\nModify LinkedBookings ReferenceNumber from  to 395756<br>\nModify LinkedBookings Type from  to NotSpecified<br>\nModify LinkedBookings ReferenceNumber from  to 395759<br>\nModify Cruise DestinationName from  to Alaska <br>\nModify Cruise ClassTypeID from 0 to 1<br>\nModify Cruise ClassTypeName from  to Interior<br>\nModify Cruise DiningStatusID from 1 to 7<br>\nModify Cruise DiningStatusName from  to Confirmed<br>\nModify Cruise DiningStatusPseudoCode from  to 39<br>\nModify Pax #1 Title from  to MR<br>\nModify Pax #2 Title from  to MR<br>\nModify pax #1 special service #0 Code from  to en-LNP<br>\nModify pax #1 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 AssociationType from  to P<br>\nModify pax #1 special service #0 Name from  to English<br>\nModify pax #1 special service #0 Description from  to English<br>\nModify pax #1 special service #0 Group from  to Language<br>\nModify pax #1 special service #0 OfferPerPassenger from  to True<br>\nModify pax #1 special service #0 IsMandatory from  to False<br>\nModify pax #1 special service #0 ServiceDateRequired from  to False<br>\nModify pax #1 special service #1 Code from  to en-LND<br>\nModify pax #1 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 AssociationType from  to P<br>\nModify pax #1 special service #1 Name from  to English<br>\nModify pax #1 special service #1 Description from  to English<br>\nModify pax #1 special service #1 Group from  to Language<br>\nModify pax #1 special service #1 OfferPerPassenger from  to True<br>\nModify pax #1 special service #1 IsMandatory from  to False<br>\nModify pax #1 special service #1 ServiceDateRequired from  to False<br>\nModify pax #2 special service #0 Code from  to en-LNP<br>\nModify pax #2 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 AssociationType from  to P<br>\nModify pax #2 special service #0 Name from  to English<br>\nModify pax #2 special service #0 Description from  to English<br>\nModify pax #2 special service #0 Group from  to Language<br>\nModify pax #2 special service #0 OfferPerPassenger from  to True<br>\nModify pax #2 special service #0 IsMandatory from  to False<br>\nModify pax #2 special service #0 ServiceDateRequired from  to False<br>\nModify pax #2 special service #1 Code from  to en-LND<br>\nModify pax #2 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 AssociationType from  to P<br>\nModify pax #2 special service #1 Name from  to English<br>\nModify pax #2 special service #1 Description from  to English<br>\nModify pax #2 special service #1 Group from  to Language<br>\nModify pax #2 special service #1 OfferPerPassenger from  to True<br>\nModify pax #2 special service #1 IsMandatory from  to False<br>\nModify pax #2 special service #1 ServiceDateRequired from  to False<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:10:46"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:09:09"
          }
        },
        "type": "General",
        "user": {
          "id": 1021984,
          "name": "Sheron Parmar (Sheron_Sandbox)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:07:47"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify LinkedBookings from 0 to 1<br>Modify Special Services for Passenger #1 from 0 to 2<br>Modify Special Services for Passenger #2 from 0 to 2<br>Modify LinkedBookings Type from  to NotSpecified<br>\nModify LinkedBookings ReferenceNumber from  to 395759<br>\nModify Cruise DestinationName from  to Alaska <br>\nModify Cruise ClassTypeID from 0 to 1<br>\nModify Cruise ClassTypeName from  to Interior<br>\nModify Cruise DiningStatusID from 1 to 7<br>\nModify Cruise DiningStatusName from  to Confirmed<br>\nModify Cruise DiningStatusPseudoCode from  to 39<br>\nModify Pax #1 Title from  to MR<br>\nModify Pax #2 Title from  to MR<br>\nModify pax #1 special service #0 Code from  to en-LNP<br>\nModify pax #1 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 AssociationType from  to P<br>\nModify pax #1 special service #0 Name from  to English<br>\nModify pax #1 special service #0 Description from  to English<br>\nModify pax #1 special service #0 Group from  to Language<br>\nModify pax #1 special service #0 OfferPerPassenger from  to True<br>\nModify pax #1 special service #0 IsMandatory from  to False<br>\nModify pax #1 special service #0 ServiceDateRequired from  to False<br>\nModify pax #1 special service #1 Code from  to en-LND<br>\nModify pax #1 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 AssociationType from  to P<br>\nModify pax #1 special service #1 Name from  to English<br>\nModify pax #1 special service #1 Description from  to English<br>\nModify pax #1 special service #1 Group from  to Language<br>\nModify pax #1 special service #1 OfferPerPassenger from  to True<br>\nModify pax #1 special service #1 IsMandatory from  to False<br>\nModify pax #1 special service #1 ServiceDateRequired from  to False<br>\nModify pax #2 special service #0 Code from  to en-LNP<br>\nModify pax #2 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 AssociationType from  to P<br>\nModify pax #2 special service #0 Name from  to English<br>\nModify pax #2 special service #0 Description from  to English<br>\nModify pax #2 special service #0 Group from  to Language<br>\nModify pax #2 special service #0 OfferPerPassenger from  to True<br>\nModify pax #2 special service #0 IsMandatory from  to False<br>\nModify pax #2 special service #0 ServiceDateRequired from  to False<br>\nModify pax #2 special service #1 Code from  to en-LND<br>\nModify pax #2 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 AssociationType from  to P<br>\nModify pax #2 special service #1 Name from  to English<br>\nModify pax #2 special service #1 Description from  to English<br>\nModify pax #2 special service #1 Group from  to Language<br>\nModify pax #2 special service #1 OfferPerPassenger from  to True<br>\nModify pax #2 special service #1 IsMandatory from  to False<br>\nModify pax #2 special service #1 ServiceDateRequired from  to False<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:07:43"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:55"
          }
        },
        "type": "General",
        "user": {
          "id": 1021984,
          "name": "Sheron Parmar (Sheron_Sandbox)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:04:41"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify LinkedBookings from 0 to 1<br>Modify Special Services for Passenger #1 from 0 to 2<br>Modify Special Services for Passenger #2 from 0 to 2<br>Modify LinkedBookings Type from  to NotSpecified<br>\nModify LinkedBookings ReferenceNumber from  to 395756<br>\nModify Cruise DestinationName from  to Alaska <br>\nModify Cruise ClassTypeID from 0 to 1<br>\nModify Cruise ClassTypeName from  to Interior<br>\nModify Cruise DiningStatusID from 1 to 7<br>\nModify Cruise DiningStatusName from  to Confirmed<br>\nModify Cruise DiningStatusPseudoCode from  to 39<br>\nModify Pax #1 Title from  to MR<br>\nModify Pax #2 Title from  to MR<br>\nModify pax #1 special service #0 Code from  to en-LNP<br>\nModify pax #1 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 AssociationType from  to P<br>\nModify pax #1 special service #0 Name from  to English<br>\nModify pax #1 special service #0 Description from  to English<br>\nModify pax #1 special service #0 Group from  to Language<br>\nModify pax #1 special service #0 OfferPerPassenger from  to True<br>\nModify pax #1 special service #0 IsMandatory from  to False<br>\nModify pax #1 special service #0 ServiceDateRequired from  to False<br>\nModify pax #1 special service #1 Code from  to en-LND<br>\nModify pax #1 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 AssociationType from  to P<br>\nModify pax #1 special service #1 Name from  to English<br>\nModify pax #1 special service #1 Description from  to English<br>\nModify pax #1 special service #1 Group from  to Language<br>\nModify pax #1 special service #1 OfferPerPassenger from  to True<br>\nModify pax #1 special service #1 IsMandatory from  to False<br>\nModify pax #1 special service #1 ServiceDateRequired from  to False<br>\nModify pax #2 special service #0 Code from  to en-LNP<br>\nModify pax #2 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 AssociationType from  to P<br>\nModify pax #2 special service #0 Name from  to English<br>\nModify pax #2 special service #0 Description from  to English<br>\nModify pax #2 special service #0 Group from  to Language<br>\nModify pax #2 special service #0 OfferPerPassenger from  to True<br>\nModify pax #2 special service #0 IsMandatory from  to False<br>\nModify pax #2 special service #0 ServiceDateRequired from  to False<br>\nModify pax #2 special service #1 Code from  to en-LND<br>\nModify pax #2 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 AssociationType from  to P<br>\nModify pax #2 special service #1 Name from  to English<br>\nModify pax #2 special service #1 Description from  to English<br>\nModify pax #2 special service #1 Group from  to Language<br>\nModify pax #2 special service #1 OfferPerPassenger from  to True<br>\nModify pax #2 special service #1 IsMandatory from  to False<br>\nModify pax #2 special service #1 ServiceDateRequired from  to False<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:04:37"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:03:54"
          }
        },
        "type": "General",
        "user": {
          "id": 1021984,
          "name": "Sheron Parmar (Sheron_Sandbox)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:41:00"
          }
        },
        "type": "General",
        "user": {
          "id": 1021984,
          "name": "Sheron Parmar (Sheron_Sandbox)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:10"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Modify Special Services for Passenger #1 from 0 to 2<br>Modify Special Services for Passenger #2 from 0 to 2<br>Modify Cruise DestinationName from  to Alaska <br>\nModify Cruise ClassTypeID from 0 to 1<br>\nModify Cruise ClassTypeName from  to Interior<br>\nModify Cruise DiningStatusID from 1 to 7<br>\nModify Cruise DiningStatusName from  to Confirmed<br>\nModify Cruise DiningStatusPseudoCode from  to 39<br>\nModify Pax #1 Title from  to MR<br>\nModify Pax #2 Title from  to MR<br>\nModify pax #1 special service #0 Code from  to en-LNP<br>\nModify pax #1 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #1 special service #0 AssociationType from  to P<br>\nModify pax #1 special service #0 Name from  to English<br>\nModify pax #1 special service #0 Description from  to English<br>\nModify pax #1 special service #0 Group from  to Language<br>\nModify pax #1 special service #0 OfferPerPassenger from  to True<br>\nModify pax #1 special service #0 IsMandatory from  to False<br>\nModify pax #1 special service #0 ServiceDateRequired from  to False<br>\nModify pax #1 special service #1 Code from  to en-LND<br>\nModify pax #1 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #1 special service #1 AssociationType from  to P<br>\nModify pax #1 special service #1 Name from  to English<br>\nModify pax #1 special service #1 Description from  to English<br>\nModify pax #1 special service #1 Group from  to Language<br>\nModify pax #1 special service #1 OfferPerPassenger from  to True<br>\nModify pax #1 special service #1 IsMandatory from  to False<br>\nModify pax #1 special service #1 ServiceDateRequired from  to False<br>\nModify pax #2 special service #0 Code from  to en-LNP<br>\nModify pax #2 special service #0 Type from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 Category from  to PREFERREDLANGUAGE<br>\nModify pax #2 special service #0 AssociationType from  to P<br>\nModify pax #2 special service #0 Name from  to English<br>\nModify pax #2 special service #0 Description from  to English<br>\nModify pax #2 special service #0 Group from  to Language<br>\nModify pax #2 special service #0 OfferPerPassenger from  to True<br>\nModify pax #2 special service #0 IsMandatory from  to False<br>\nModify pax #2 special service #0 ServiceDateRequired from  to False<br>\nModify pax #2 special service #1 Code from  to en-LND<br>\nModify pax #2 special service #1 Type from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 Category from  to DOCUMENTLANGUAGE<br>\nModify pax #2 special service #1 AssociationType from  to P<br>\nModify pax #2 special service #1 Name from  to English<br>\nModify pax #2 special service #1 Description from  to English<br>\nModify pax #2 special service #1 Group from  to Language<br>\nModify pax #2 special service #1 OfferPerPassenger from  to True<br>\nModify pax #2 special service #1 IsMandatory from  to False<br>\nModify pax #2 special service #1 ServiceDateRequired from  to False<br>\nModify Prices Service Fee - DisplayIndicator| from False to True<br>\nModify Pax #1 Service Fee - DisplayIndicator| from False to True<br>\nModify Pax #1 Addon Options - DisplayIndicator| from False to True<br>\nModify Pax #1 Best Price Guarantee - DisplayIndicator| from False to True<br>\nModify Pax #2 Service Fee - DisplayIndicator| from False to True<br>\nModify Pax #2 Addon Options - DisplayIndicator| from False to True<br>\nModify Pax #2 Best Price Guarantee - DisplayIndicator| from False to True<br>\nModify PaymentSchedule PaymentNumber from 0 to 1<br>\n",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:05"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      },
      {
        "description": "Read Booking : True.",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:31:57"
          }
        },
        "type": "General",
        "user": {
          "id": 1021984,
          "name": "Sheron Parmar (Sheron_Sandbox)"
        }
      },
      {
        "description": "CruiseOption",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:24:04"
          }
        },
        "type": "General",
        "user": {
          "id": -5,
          "name": "Auto Process"
        }
      },
      {
        "description": "The booking was successfully created with the cruise line.<br> An email has been sent with your booking details, please allow a few minutes for this email to arrive.<br>",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:24:04"
          }
        },
        "type": "General",
        "user": {
          "name": "Online (b2c)"
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
