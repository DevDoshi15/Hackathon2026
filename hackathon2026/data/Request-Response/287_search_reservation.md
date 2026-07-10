# Search Reservation

**Path:** Search Reservation (Odysseus Only) > Search Reservation

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/Search`

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
    "Pagination": {
        "pageSize": 20,
        "pageIndex": 1
    },
    "packageId": 1269600,
    "CreatedOn": {
        "from": "01-Dec-2022",
        "to": "30-Dec-2022"
    },
    "ModifiedOn": {
        "from": "01-Dec-2022",
        "to": "30-Dec-2022"
    },
    "TravelDate": {
        "from": "30-Jan-2023",
        "to": "25-Feb-2023"
    },
    "cruiselineIds": "6,8",
    "bookingStatusIds": "7",
    "confirmationNumbers": "345652",
    "agencyConfirmationNumbers": "1FOO7J7",
    "firstName": "John",
    "lastName": "Doe"
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Thu, 16 Mar 2023 08:04:01 GMT
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
    "totalRecords": 1,
    "pageSize": 20,
    "pageIndex": 1,
    "reservations": [
      {
        "siteItemId": 130386,
        "id": 63565,
        "agencyConfirmation": "1FOO7J7",
        "cruiseReservation": {
          "departureArrivalInfo": {
            "departureDateTime": "30-Jan-2023 00:00:00",
            "arrivalDateTime": "03-Feb-2023 00:00:00",
            "departureCityId": "FLL",
            "arrivalCityId": "FLL"
          },
          "id": 111545,
          "status": 7,
          "reservationReferences": {
            "confirmationNumber": "345652",
            "pnrNumber": ""
          },
          "cruise": {
            "packageId": 1269600,
            "cruiseline": {
              "id": 8,
              "ships": [
                {
                  "id": 1093
                }
              ]
            }
          },
          "categories": [
            {
              "code": "2D",
              "type": 3,
              "cabins": [
                {
                  "number": "7260"
                }
              ],
              "fares": [
                {
                  "upgradeFrom": "2D",
                  "fareCode": {
                    "code": "I7522610",
                    "type": 0
                  }
                }
              ]
            }
          ]
        },
        "statusId": 7,
        "createdOn": "06-Dec-2022 04:37:32",
        "modifiedOn": "06-Dec-2022 04:37:37",
        "primaryCustomer": {
          "firstName": "John",
          "middleName": "",
          "lastName": "Doe"
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
