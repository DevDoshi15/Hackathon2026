# Cruise Sailing Availability (Live)

**Path:** Cruise Sailing Availability (Live) > Cruise Sailing Availability (Live)

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/SearchPackageWithSupplier`

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
    "filters": [
        {
            "key": "departureDateTime",
            "ranges": [
                {
                    "from": "01-Dec-2024",
                    "to": "30-Dec-2024"
                }
            ]
        },
        {
            "key": "duration",
            "ranges": [
                {
                    "from": "7",
                    "to": "9"
                }
            ]
        },
        {
            "key": "destinationId",
            "value": "10"
        },
        {
            "key": "cruiselineId",
            "value": "8"
        },
        {
            "key": "shipId",
            "value": "13825"
        },
        {
            "key": "departurePortCode",
            "value": "MIA"
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Fri, 19 Jan 2024 13:41:36 GMT
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
    "total": 5,
    "list": [
      {
        "id": 1384472,
        "destination": {
          "id": 10,
          "type": "Destination"
        },
        "ship": {
          "id": 13825,
          "name": "",
          "cruiseline": {
            "id": 8,
            "name": "Royal Caribbean"
          }
        },
        "shipIds": [
          13825
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "01-Dec-2024",
        "arrivalDateTime": "08-Dec-2024",
        "cruisePackageDepartureDateTime": "01-Dec-2024",
        "cruisePackageArrivalDateTime": "08-Dec-2024",
        "cruiseTourCode": "SY07E392",
        "voyageId": "SY07E392",
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "cruiseDuration": 7,
        "destinationIds": [
          10
        ],
        "code": "SY07E392",
        "startDateTime": "01-Dec-2024",
        "endDateTime": "08-Dec-2024",
        "itinerary": {
          "duration": 7,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          }
        },
        "isActive": true
      },
      {
        "id": 1384604,
        "destination": {
          "id": 10,
          "type": "Destination"
        },
        "ship": {
          "id": 13825,
          "name": "",
          "cruiseline": {
            "id": 8,
            "name": "Royal Caribbean"
          }
        },
        "shipIds": [
          13825
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "08-Dec-2024",
        "arrivalDateTime": "15-Dec-2024",
        "cruisePackageDepartureDateTime": "08-Dec-2024",
        "cruisePackageArrivalDateTime": "15-Dec-2024",
        "cruiseTourCode": "SY07E386",
        "voyageId": "SY07E386",
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "cruiseDuration": 7,
        "destinationIds": [
          10
        ],
        "code": "SY07E386",
        "startDateTime": "08-Dec-2024",
        "endDateTime": "15-Dec-2024",
        "itinerary": {
          "duration": 7,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          }
        },
        "isActive": true
      },
      {
        "id": 1383312,
        "destination": {
          "id": 14,
          "type": "Destination"
        },
        "ship": {
          "id": 13825,
          "name": "",
          "cruiseline": {
            "id": 8,
            "name": "Royal Caribbean"
          }
        },
        "shipIds": [
          13825
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "15-Dec-2024",
        "arrivalDateTime": "22-Dec-2024",
        "cruisePackageDepartureDateTime": "15-Dec-2024",
        "cruisePackageArrivalDateTime": "22-Dec-2024",
        "cruiseTourCode": "SY07W583",
        "voyageId": "SY07W583",
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "cruiseDuration": 7,
        "destinationIds": [
          14
        ],
        "code": "SY07W583",
        "startDateTime": "15-Dec-2024",
        "endDateTime": "22-Dec-2024",
        "itinerary": {
          "duration": 7,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          }
        },
        "isActive": true
      },
      {
        "id": 1384467,
        "destination": {
          "id": 10,
          "type": "Destination"
        },
        "ship": {
          "id": 13825,
          "name": "",
          "cruiseline": {
            "id": 8,
            "name": "Royal Caribbean"
          }
        },
        "shipIds": [
          13825
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "22-Dec-2024",
        "arrivalDateTime": "29-Dec-2024",
        "cruisePackageDepartureDateTime": "22-Dec-2024",
        "cruisePackageArrivalDateTime": "29-Dec-2024",
        "cruiseTourCode": "SY07E388",
        "voyageId": "SY07E388",
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "cruiseDuration": 7,
        "destinationIds": [
          10
        ],
        "code": "SY07E388",
        "startDateTime": "22-Dec-2024",
        "endDateTime": "29-Dec-2024",
        "itinerary": {
          "duration": 7,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          }
        },
        "isActive": true
      },
      {
        "id": 1384098,
        "destination": {
          "id": 10,
          "type": "Destination"
        },
        "ship": {
          "id": 13825,
          "name": "",
          "cruiseline": {
            "id": 8,
            "name": "Royal Caribbean"
          }
        },
        "shipIds": [
          13825
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "29-Dec-2024",
        "arrivalDateTime": "05-Jan-2025",
        "cruisePackageDepartureDateTime": "29-Dec-2024",
        "cruisePackageArrivalDateTime": "05-Jan-2025",
        "cruiseTourCode": "SY07E393",
        "voyageId": "SY07E393",
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "cruiseDuration": 7,
        "destinationIds": [
          10
        ],
        "code": "SY07E393",
        "startDateTime": "29-Dec-2024",
        "endDateTime": "05-Jan-2025",
        "itinerary": {
          "duration": 7,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          }
        },
        "isActive": true
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
