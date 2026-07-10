# Get Cruise Itinerary from Supplier

**Path:** Get Cruise Itinerary from Supplier > Get Cruise Itinerary from Supplier

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/getitineraryfromsupplier`

### Headers

```
SiteItemId: {{Nitro.Sandbox.SiteItemId}}
```

### Authentication

**Type:** basic

```
username: {{Nitro.Sandbox.ClientId}}
password: {{Nitro.Sandbox.ClientSecret}}
```

### Request Body

```json
{
  "cruiseReservation": {
    "cruise": {
      "packageId": 1330761
    }
  },
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
Date: Wed, 17 Jan 2024 08:55:00 GMT
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
    "id": 353818,
    "nodes": [
      {
        "departureTime": "16:30:00",
        "description": "MIAMI, FLORIDA"
      },
      {
        "departureTime": "17:00:00",
        "arrivalTime": "07:00:00",
        "dayOffSet": 1,
        "description": "PERFECT DAY COCOCAY, BAHAMAS"
      },
      {
        "departureTime": "17:00:00",
        "arrivalTime": "08:00:00",
        "dayOffSet": 2,
        "description": "NASSAU, BAHAMAS"
      },
      {
        "arrivalTime": "06:00:00",
        "dayOffSet": 3,
        "description": "MIAMI, FLORIDA"
      }
    ],
    "portsOfCalls": "MIAMI, FLORIDA|PERFECT DAY COCOCAY, BAHAMAS|NASSAU, BAHAMAS|MIAMI, FLORIDA",
    "normalizedPortsOfCall": ""
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
