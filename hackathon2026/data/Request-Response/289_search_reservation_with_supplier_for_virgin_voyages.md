# Search Reservation With Supplier For Virgin Voyages

**Path:** Search Reservation With Supplier > Search Reservation With Supplier For Virgin Voyages

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
    "supplierId": 8807,
    "pos": {
        "currency": "USD"
    },
    "SearchPreferences": {
        "CustomerFirstName": "John",
        "CustomerLastName": "Doe"
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Thu, 16 Mar 2023 08:11:24 GMT
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
      "requestId": "68bb5961-6324-41b9-bbaa-1f32aee8335f",
      "timeStamp": "16-Mar-2023 04:11:06"
    },
    "reservations": [
      {
        "id": 66209,
        "cruiseReservation": {
          "id": 114189,
          "status": 14,
          "reservationReferences": {
            "confirmationNumber": "316607"
          },
          "cruise": {
            "cruiseline": {
              "id": 8807,
              "ships": [
                {
                  "id": 14477,
                  "name": "Scarlet Lady"
                }
              ]
            }
          },
          "categories": [
            {
              "id": 74065,
              "code": "IN",
              "type": 1,
              "cabins": [
                {
                  "isGuarantee": true
                }
              ],
              "details": {
                "styleClass": "#f04b24"
              }
            }
          ]
        },
        "statusId": 14,
        "primaryCustomer": {
          "firstName": "JOHN",
          "lastName": "DOE",
          "dateOfBirth": "03-Mar-1967",
          "age": 56
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
