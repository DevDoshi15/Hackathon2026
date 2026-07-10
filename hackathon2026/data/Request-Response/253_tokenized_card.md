# Tokenized Card

**Path:** Create Reservation > Create Reservation - Payment Declined Flag > Tokenized Card

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
//This request contains only mandatory elements
{
    "Number": "4387751111111111", // Here we are not using NCL Test Card to generate token, as we want the payment to fail, as this sample intends to show "PaymentDeclined" flag example
    "cvv": "123",
    "type": "VI",
    "expiration": "12/26",
    "cardHolderName": "John Doe",
    "BillingDetails": {
        "Address": {
            "Addressline1": "NE 4th Avenue",
            "Country": {
                "id": "US"
            },
            "State": {
                "id": "FL"
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
Date: Wed, 06 Sep 2023 09:49:18 GMT
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
    "token": "dfcc86da-f268-438c-8302-a5f9d57d92cf"
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
