# Tokenize Card without CVV

**Path:** Tokenized Card > Tokenize Card without CVV

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
    "type": "VI",
    "expiration": "12/26",
    "cardHolderName": "John Doe",
    "amount": 1424.5,
    "currency": "USD",
    "BillingDetails": {
        "Address": {
            "Addressline1": "NE 4th Avenue",
            "Addressline2": "123",
            "Country": {
                "id": "US"
            },
            "State": {
                "id": "FL"
            },
            "City": {
                "name": "MIAMI"
            },
            "PostalCode": "33141"
        },
        "BankName": "HSBC",
        "ContactInfo": {
            "Phone1": {
                "CountryCode": "1",
                "Number": "123-456-7890",
                "Type": "Billing"
            },
            "Phone2": {
                "CountryCode": "1",
                "Number": "123-456-7890",
                "Type": "Bank"
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
Date: Wed, 01 Feb 2023 10:21:50 GMT
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
    "token": "58586142-31dd-4f17-bf5f-fbaa7a2cdca5"
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
