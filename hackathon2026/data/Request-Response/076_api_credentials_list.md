# API Credentials List

**Path:** Create Reservation > Create Reservation using POS Id > API Credentials List

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listpos`

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
    "cruiseReservation": {
        "cruise": {
            "packageId": 1269434 // Here packageId is mandatory
        }
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Fri, 17 Feb 2023 08:02:56 GMT
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
      "requestId": "a57cb15e-dba6-4d30-9716-4466be03e319",
      "timeStamp": "17-Feb-2023 03:02:56"
    },
    "cruiseReservation": {
      "cruise": {
        "packageId": 1269434,
        "cruiseline": {
          "id": 8
        }
      },
      "pointOfSales": [
        {
          "id": 2114,
          "name": "NitroAPI Sandbox - USD | O100US6797",
          "priority": 5,
          "apiId": "RCCL",
          "officeId": "O100US6797",
          "system": "Test",
          "currency": "USD",
          "type": "B2C"
        }
      ]
    }
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
