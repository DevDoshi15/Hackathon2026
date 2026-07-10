# Search Reservation With Supplier For RCCL

**Path:** Search Reservation With Supplier > Search Reservation With Supplier For RCCL

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
    "supplierId": 8,
    "pos": {
        "currency": "USD"
    },
    "SearchPreferences": {
        "ConfirmationNumber": "345652",
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
Date: Thu, 16 Mar 2023 08:10:22 GMT
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
      "requestId": "9c5cd292-0239-425e-b881-1aece6439c74",
      "timeStamp": "16-Mar-2023 04:10:19"
    },
    "reservations": [
      {
        "id": 63565,
        "cruiseReservation": {
          "id": 111545,
          "status": 7,
          "reservationReferences": {
            "confirmationNumber": "345652"
          },
          "cruise": {
            "cruiseline": {
              "id": 8,
              "code": "RCC",
              "name": "Royal Caribbean",
              "ships": [
                {
                  "id": 1093,
                  "name": "Liberty of the Seas"
                }
              ]
            }
          },
          "categories": [
            {
              "id": 374133321,
              "code": "2D",
              "type": 3,
              "cabins": [
                {
                  "number": "7260",
                  "deck": {
                    "id": 10790,
                    "name": "Deck 7",
                    "description": "Staterooms."
                  }
                }
              ],
              "details": {
                "size": "188 sq. ft.",
                "styleClass": "#3cb5cf"
              }
            }
          ]
        },
        "statusId": 7,
        "primaryCustomer": {
          "firstName": "JOHN",
          "lastName": "DOE",
          "dateOfBirth": "02-Jan-1970",
          "age": 53
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
