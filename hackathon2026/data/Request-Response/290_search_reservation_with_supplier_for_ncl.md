# Search Reservation With Supplier For NCL

**Path:** Search Reservation With Supplier > Search Reservation With Supplier For NCL

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/SearchWithSupplier`

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
    "supplierId": 6,
    "pos": {
        "currency": "USD"
    },
    "SearchPreferences": {
        "ConfirmationNumber": "52012988"
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Thu, 16 Mar 2023 08:11:46 GMT
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
      "requestId": "861a2fb4-c612-490c-83de-96d74d97cac4",
      "timeStamp": "16-Mar-2023 04:11:41"
    },
    "reservations": [
      {
        "id": 65946,
        "cruiseReservation": {
          "id": 113926,
          "status": 14,
          "reservationReferences": {
            "confirmationNumber": "52012988"
          },
          "cruise": {
            "cruiseline": {
              "id": 6,
              "code": "NCL",
              "name": "Norwegian Cruise Line",
              "ships": [
                {
                  "id": 52,
                  "name": "Norwegian Star"
                }
              ]
            }
          },
          "categories": [
            {
              "id": 54957,
              "code": "IX",
              "type": 1,
              "cabins": [
                {
                  "number": "GTY",
                  "isGuarantee": true
                }
              ],
              "details": {
                "styleClass": "#5A7CC1"
              }
            }
          ]
        },
        "statusId": 14,
        "primaryCustomer": {
          "firstName": "TAJAMMAL",
          "lastName": "AMIN",
          "dateOfBirth": "01-Jan-1999",
          "age": 24
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
