# Office Credentials List (POS) - Using packageId

**Path:** Office Credentials List (POS) > Office Credentials List (POS) - Using packageId

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
Date: Wed, 01 Feb 2023 09:46:03 GMT
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
      "requestId": "97edeeb3-03ea-471b-a85c-d1a82e46ef27",
      "timeStamp": "01-Feb-2023 04:46:02"
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
