# List Cruise Line Airports

**Path:** Create Reservation > Create Reservation With Air For P&O Cruise line > List Cruise Line Airports

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/ListAirGateways`

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
// for P&O  we will receive departure city codes with Prices
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1501519
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
Date: Fri, 26 May 2023 12:03:49 GMT
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
    "airGateways": [
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "03-Jun-2027 00:00:00",
            "arrivalDateTime": "03-Jun-2027 00:00:00",
            "departureCityId": "BFS",
            "arrivalCityId": "VLT"
          }
        },
        "inboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "10-Jun-2027 00:00:00",
            "arrivalDateTime": "10-Jun-2027 00:00:00",
            "departureCityId": "VLT",
            "arrivalCityId": "BFS"
          }
        },
        "categories": [
          {
            "prices": [
              {
                "id": 1,
                "amount": 1979,
                "type": "ADULT"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "CHILD"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "INFANT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "03-Jun-2027 00:00:00",
            "arrivalDateTime": "03-Jun-2027 00:00:00",
            "departureCityId": "BHX",
            "arrivalCityId": "VLT"
          }
        },
        "inboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "10-Jun-2027 00:00:00",
            "arrivalDateTime": "10-Jun-2027 00:00:00",
            "departureCityId": "VLT",
            "arrivalCityId": "BHX"
          }
        },
        "categories": [
          {
            "prices": [
              {
                "id": 1,
                "amount": 1869,
                "type": "ADULT"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "CHILD"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "INFANT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "03-Jun-2027 00:00:00",
            "arrivalDateTime": "03-Jun-2027 00:00:00",
            "departureCityId": "BRS",
            "arrivalCityId": "VLT"
          }
        },
        "inboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "10-Jun-2027 00:00:00",
            "arrivalDateTime": "10-Jun-2027 00:00:00",
            "departureCityId": "VLT",
            "arrivalCityId": "BRS"
          }
        },
        "categories": [
          {
            "prices": [
              {
                "id": 1,
                "amount": 1839,
                "type": "ADULT"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "CHILD"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "INFANT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "03-Jun-2027 00:00:00",
            "arrivalDateTime": "03-Jun-2027 00:00:00",
            "departureCityId": "EMA",
            "arrivalCityId": "VLT"
          }
        },
        "inboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "10-Jun-2027 00:00:00",
            "arrivalDateTime": "10-Jun-2027 00:00:00",
            "departureCityId": "VLT",
            "arrivalCityId": "EMA"
          }
        },
        "categories": [
          {
            "prices": [
              {
                "id": 1,
                "amount": 1909,
                "type": "ADULT"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "CHILD"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "INFANT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "03-Jun-2027 00:00:00",
            "arrivalDateTime": "03-Jun-2027 00:00:00",
            "departureCityId": "GLA",
            "arrivalCityId": "VLT"
          }
        },
        "inboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "10-Jun-2027 00:00:00",
            "arrivalDateTime": "10-Jun-2027 00:00:00",
            "departureCityId": "VLT",
            "arrivalCityId": "GLA"
          }
        },
        "categories": [
          {
            "prices": [
              {
                "id": 1,
                "amount": 1929,
                "type": "ADULT"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "CHILD"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "INFANT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "03-Jun-2027 00:00:00",
            "arrivalDateTime": "03-Jun-2027 00:00:00",
            "departureCityId": "LON",
            "arrivalCityId": "VLT"
          }
        },
        "inboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "10-Jun-2027 00:00:00",
            "arrivalDateTime": "10-Jun-2027 00:00:00",
            "departureCityId": "VLT",
            "arrivalCityId": "LON"
          }
        },
        "categories": [
          {
            "prices": [
              {
                "id": 1,
                "amount": 1749,
                "type": "ADULT"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "CHILD"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "INFANT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "03-Jun-2027 00:00:00",
            "arrivalDateTime": "03-Jun-2027 00:00:00",
            "departureCityId": "MAN",
            "arrivalCityId": "VLT"
          }
        },
        "inboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "10-Jun-2027 00:00:00",
            "arrivalDateTime": "10-Jun-2027 00:00:00",
            "departureCityId": "VLT",
            "arrivalCityId": "MAN"
          }
        },
        "categories": [
          {
            "prices": [
              {
                "id": 1,
                "amount": 1829,
                "type": "ADULT"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "CHILD"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "INFANT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "03-Jun-2027 00:00:00",
            "arrivalDateTime": "03-Jun-2027 00:00:00",
            "departureCityId": "NCL",
            "arrivalCityId": "VLT"
          }
        },
        "inboundFlightInfo": {
          "departureArrivalInfo": {
            "departureDateTime": "10-Jun-2027 00:00:00",
            "arrivalDateTime": "10-Jun-2027 00:00:00",
            "departureCityId": "VLT",
            "arrivalCityId": "NCL"
          }
        },
        "categories": [
          {
            "prices": [
              {
                "id": 1,
                "amount": 1929,
                "type": "ADULT"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "CHILD"
              },
              {
                "id": 1,
                "amount": 0,
                "type": "INFANT"
              }
            ]
          }
        ]
      }
    ],
    "categoryTypePrices": [
      {
        "amount": 0,
        "type": "Inside"
      },
      {
        "amount": 0,
        "type": "Outside"
      },
      {
        "amount": 0,
        "type": "Suite"
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
