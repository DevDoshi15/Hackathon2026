# Dining Availability

**Path:** Dining Availability > Dining Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/ListDinings`

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
//This request contains only mandatory elements
{
  "cruiseReservation": {
    "pos": {
      "currency": "USD"
    },
    "customerReferences": [
      {
        "rph": 1,
        "isPrimaryContact": true
      },
      {
        "rph": 2
      }
    ],
    "cruise": {
      "packageId": 1269434,
      "packageTourId": -1
    },
    "categories": [
      {
        "code": "2B",
        "fare": {
          "fareCode": {
            "code": "G0737880"
          }
        },
        "cabins": [
          {
            "number": "9330"
          }
        ]
      }
    ]
  },
  "customers": [
    {
      "rph": 1,      
      "age": 52
    },
    {
      "rph": 2,      
      "age": 57      
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
Date: Wed, 01 Feb 2023 11:10:09 GMT
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
      "requestId": "fbaf041d-a554-46f9-adcf-83a46d01cd72",
      "timeStamp": "01-Feb-2023 06:10:08",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 4
      },
      "pos": {
        "id": 2114,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2C"
      },
      "customerReferences": [
        {
          "rph": 1,
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 311051,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
        },
        "transportationType": 29
      },
      "dinings": [
        {
          "id": 1,
          "code": "M",
          "name": "05:15 PM",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 2,
          "code": "2",
          "name": "08:00 PM",
          "status": 1,
          "tableSizeOptions": []
        },
        {
          "id": 24,
          "code": "O",
          "name": "MY TIME",
          "status": 1,
          "tableSizeOptions": []
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 52
      },
      {
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
