# Past Passenger Lookup (Using cruiseline)

**Path:** Past Passenger Lookup > Past Passenger Lookup (Using cruiseline)

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
        "pos": {
            "currency": "USD"
        },
        "cruise": {
            "cruiseLine": {
                "id": 8 //Cruiseline Id is mandatory
            }
        }
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "Daniel",
            "lastName": "Florence",
            "dateOfBirth": "17-Sep-1981",
            "contactInfo": {
                "email": "dflorence21@hotmail.com"
            }
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
Date: Wed, 01 Feb 2023 11:36:23 GMT
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
      "requestId": "ae856776-2d9e-41cd-8077-40ff46f0b05f",
      "timeStamp": "01-Feb-2023 06:36:22",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {},
      "pos": {
        "id": 2114,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2C"
      },
      "cruise": {
        "cruiseline": {
          "id": 8,
          "ships": [
            {}
          ]
        },
        "itinerary": {
          "destination": {}
        }
      }
    },
    "customers": [
      {
        "rph": 1,
        "firstName": "Daniel",
        "lastName": "Florence",
        "dateOfBirth": "17-Sep-1981",
        "pastPaxNumber": "351962538",
        "contactInfo": {
          "email": "dflorence21@hotmail.com"
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
