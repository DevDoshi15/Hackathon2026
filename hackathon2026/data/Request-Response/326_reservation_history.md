# Reservation History

**Path:** Reservation History (Supplier) > Reservation History

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/HistoryFromSupplier`

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
Date: Mon, 10 Jul 2023 12:00:06 GMT
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
      "requestId": "08574eec-a137-474e-a23f-e3ee1c6161e0",
      "timeStamp": "10-Jul-2023 08:00:04",
      "token": "EQTEMPKEN"
    },
    "historyInfo": [
      {
        "description": "BOOKING STATUS FROM OF TO CX - CANCELLATION NUMBER IS D142S7H",
        "timeStamp": {
          "system": {
            "createdOn": "09-May-2023 05:46:59"
          }
        },
        "user": {
          "name": "BA"
        }
      },
      {
        "description": "JOHN           DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "09-May-2023 05:46:59"
          }
        },
        "user": {
          "name": "BA"
        }
      },
      {
        "description": "MARK           DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "09-May-2023 05:46:59"
          }
        },
        "user": {
          "name": "BA"
        }
      },
      {
        "description": "JOHN DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:28"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARK DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:28"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:28"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARK DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:28"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE DINING SEATING FROM  TO 07:45 PM",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:28"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARK DOE DINING SEATING FROM  TO 07:45 PM",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:28"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:27"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARK DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:27"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "CABIN FROM 9633 TO 7533",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:27"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:27"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARK DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:27"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN           DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:27"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA          DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:27"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "ALTERNATE PHONE# FROM 416-555-4566 TO 12121212",
        "timeStamp": {
          "system": {
            "createdOn": "25-Apr-2023 03:23:27"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:34"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:34"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:34"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:34"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:34"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:34"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:33"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:33"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:33"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:33"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN           DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:33"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA          DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:11:33"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "DINING X-REF ADDED FOR BOOKING 0395756",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN           DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA          DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:08:38"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "DINING X-REF ADDED FOR BOOKING 0395759",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:23"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:23"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:23"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:23"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:23"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:23"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:22"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:22"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:22"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:22"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:22"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN           DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:22"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA          DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 11:05:22"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "DINING X-REF ADDED FOR BOOKING 0395756",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE ADDED TO BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN           DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA          DOE CANCELLED",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:38:50"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "CREATED BOOKING",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "PI"
        }
      },
      {
        "description": "JOHN DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "BA"
        }
      },
      {
        "description": "MARIA DOE MAIL DIRECT FLAG FROM  TO C",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "BA"
        }
      },
      {
        "description": "DEPOSIT AMOUNT DUE FROM           0.00 TO         900.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "Created Thru:  ODYSSEUSSO",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "CRUISEMATCH AIRLINE CODE FROM  TO PI",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "SAILING FROM   TO OV 23JUN23",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "CABIN FROM  TO 9633",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "AGENT FROM  TO 6318642424",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "BOOKING STATUS FROM  TO OF",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "PSGR COUNT FROM 0 TO 2",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "Accessible Qualifier Changed From   To N",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "PI"
        }
      },
      {
        "description": "PACKAGE CODE FROM  TO OV07A221",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "CONTACT NAME FROM  TO BA",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE BASE PRICE FROM 0.00 TO 1201.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE NCCF PRICE FROM 0.00 TO 235.00",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "TOTAL PRICE FROM           0.00 TO        3339.50",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "BERTHING CATEGORY FROM  TO 4U",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "OPTION DATE FROM  TO 29APR23",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "JOHN DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "MARIA DOE DINING SEATING FROM  TO 05:00 PM",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "CABIN RATE CATEGORY FROM  TO 4U",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "PRICE FROM   TO STANDARD",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "PRICING BOOKING CHANNEL CHANGED FROM  TO PI",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      },
      {
        "description": "ALTERNATE PHONE# FROM  TO 416-555-4566",
        "timeStamp": {
          "system": {
            "createdOn": "24-Apr-2023 10:23:59"
          }
        },
        "user": {
          "name": "CMOEXTTOOL"
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
