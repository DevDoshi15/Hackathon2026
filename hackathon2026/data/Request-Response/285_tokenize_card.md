# Tokenize Card

**Path:** Apply Payment - After Reservation is Created > Tokenize Card

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/payment/TokenizeCard`

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
  "Number": "4387751111111111",
  "cvv": "123",
  "type": "VI",
  "expiration": "12/26",
  "cardHolderName": "John Doe",
  "amount": 1053.46,
  "currency": "USD",
  "BillingDetails": {
    "Address": {
      "Addressline1": "NE 4th Avenue",
      "Country": {
        "id": "US"
      },
      "City": {
        "name": "MIAMI"
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
Date: Mon, 20 Feb 2023 10:30:55 GMT
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
    "token": "f5d94630-61d8-4bf5-811d-1ca43a2882dd"
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
