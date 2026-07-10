# Office Credentials List (POS) - Using CruiseLineId

**Path:** Office Credentials List (POS) > Office Credentials List (POS) - Using CruiseLineId

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
            "cruiseLine":{
                "id":982 //Here Cruiseline Id is mandatory
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
Date: Wed, 01 Feb 2023 09:46:10 GMT
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
      "requestId": "805b1aec-8840-4e48-b9db-5f102e04b539",
      "timeStamp": "01-Feb-2023 04:46:10"
    },
    "cruiseReservation": {
      "cruise": {
        "cruiseline": {
          "id": 982
        }
      },
      "pointOfSales": [
        {
          "id": 2119,
          "name": "NitroAPI Sandbox - USD | O100US6797",
          "priority": 5,
          "apiId": "MSC",
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
