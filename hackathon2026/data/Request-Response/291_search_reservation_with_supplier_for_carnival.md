# Search Reservation With Supplier For Carnival

**Path:** Search Reservation With Supplier > Search Reservation With Supplier For Carnival

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
    "supplierId": 1,
    "pos": {
        "currency": "USD"
    },
    "SearchPreferences": {
        "ConfirmationNumber": "4HQWW8",
        "lastName":"Doe"
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Thu, 16 Mar 2023 08:12:57 GMT
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
      "requestId": "56533e38-528e-4797-a732-dca43ce73672",
      "timeStamp": "16-Mar-2023 04:12:47"
    },
    "reservations": [
      {
        "id": 65888,
        "cruiseReservation": {
          "id": 113868,
          "status": 14,
          "reservationReferences": {
            "confirmationNumber": "4HQWW8"
          },
          "cruise": {
            "cruiseline": {
              "id": 1,
              "code": "CCL",
              "name": "Carnival Cruise Lines",
              "ships": [
                {
                  "id": 13797,
                  "name": "Carnival Horizon"
                }
              ]
            }
          },
          "categories": [
            {
              "id": 62897,
              "code": "SS",
              "type": 4,
              "cabins": [
                {
                  "number": "11206",
                  "deck": {
                    "id": 6660,
                    "name": "Deck 11",
                    "description": "Camp Ocean, Cucina del Capitano, Dr. Seuss Bookville, Ji Ji Asian Kitchen, Reception, Bandstand, Staterooms. "
                  }
                }
              ],
              "details": {
                "styleClass": "#03A09B"
              }
            }
          ]
        },
        "statusId": 14,
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
