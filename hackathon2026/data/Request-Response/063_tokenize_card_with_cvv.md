# Tokenize Card with CVV

**Path:** Tokenized Card > Tokenize Card with CVV

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
  "Number": "4111111111111111",
  "cvv": "123",
  "type": "VI",
  "expiration": "12/26",
  "cardHolderName": "John Doe",
  "amount": 1237.2,
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
Date: Wed, 01 Feb 2023 11:31:23 GMT
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
    "token": "830f95ec-868d-4f23-a3c5-2615a5ffc2c5"
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
