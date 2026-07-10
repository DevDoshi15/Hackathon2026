# Past Passenger Lookup (Using Past Pax Number)

**Path:** Past Passenger Lookup > Past Passenger Lookup (Using Past Pax Number)

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/GetPastPaxDetails`

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
    "cruiseReservation": {
        "cruise": {
            "cruiseLine": {
                "id": 982
            }
        },
        // Send ReservationPreferences.PastPaxLookupByNumber as true to retrieve the past passenger details using the past passenger number. 
        // If it's true and other details of the customer is sent, it will be ignored and search will occur only on the basis of past pax number.
        "reservationPreferences": [
            {
                "type": "PastPaxLookupByNumber",
                "value": true
            }
        ]
    },
    "customers": [
        {
            "pastPaxNumber": "240945" //We will always need the past passenger number, if ReservationPreferences.PastPaxLookupByNumber is true
        }
    ],
    "trackingInfo": {
        "token": "EQTEMPKEN"
    }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Mon, 28 Oct 2024 11:55:10 GMT
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
      "requestId": "e9e7d3c0-5bb6-4889-84fe-9b69e829de72",
      "timeStamp": "28-Oct-2024 07:54:59",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {},
      "pos": {
        "id": 2527,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "B2B",
        "system": "Test",
        "apiId": "MSC"
      },
      "customerReferences": [
        {
          "ageGroup": "Adult",
          "isPrimaryContact": true
        }
      ],
      "currencyInfo": {
        "currencyId": "USD"
      },
      "cruise": {
        "cruiseline": {
          "id": 982,
          "ships": [
            {}
          ]
        }
      }
    },
    "customers": [
      {
        "gender": "Male",
        "firstName": "Alberto",
        "middleName": "",
        "lastName": "Peluso",
        "dateOfBirth": "22-May-1935",
        "age": 89,
        "pastPaxNumber": "240945",
        "address": {
          "city": {
            "name": "Capilla del SeÂ¤or"
          },
          "addressline1": "Sin Nombre Sin numero",
          "postalCode": "2812"
        },
        "nationality": {},
        "contactInfo": {
          "email": "test@test.com",
          "phone1": {
            "number": "1234568790"
          }
        },
        "details": {
          "externalType": "MSCCLU55"
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
