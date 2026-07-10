# Tokenize Card without CVV

**Path:** Create Reservation > Create Reservation - Payment Pending Confirmation Flag > Tokenize Card without CVV

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
    "Number": "4035529900007013",
    "type": "VI",
    "expiration": "12/26",
    "cardHolderName": "John Doe",
    "amount": 1220,
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
Date: Mon, 25 Sep 2023 11:26:28 GMT
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
    "token": "78f3a706-8e91-425f-8ed5-63b6a0102f4a"
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
