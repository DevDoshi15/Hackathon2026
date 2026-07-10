# SilverSea Cruiseline

**Path:** List Cruise Line Airports > SilverSea Cruiseline

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
// for SilverSea we receive departure city code, air category code, air category type and prices as well etc., from the cruiseline
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1295367
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
Date: Fri, 26 May 2023 12:02:01 GMT
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
    "airGateways": [
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ABQ"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ATL"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "AUS"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BHM"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BNA"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BOS"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "BWI"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CHS"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CLE"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CLT"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CMH"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "CVG"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DEN"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DFW"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "DTW"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "EWR"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 698,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 3998,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "FLL"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "IAH"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "IND"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "JAX"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 698,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 3998,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LAS"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LAX"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "LIT"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MCI"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MCO"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MEM"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MIA"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MSP"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "MSY"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "NYC"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "OKC"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "OMA"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "ORD"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PDX"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PHL"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PHX"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PIT"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "PSP"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 698,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 3998,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RDU"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 698,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 3998,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "RSW"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 698,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 3998,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SAN"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SAT"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SAV"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 698,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 3998,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SDF"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SEA"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "SLC"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "STL"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TPA"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TUL"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "TUS"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "WAS"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YEG"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 698,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 3998,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YUL"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YVR"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YYC"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 698,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 3998,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      },
      {
        "outboundFlightInfo": {
          "departureArrivalInfo": {
            "departureCityId": "YYZ"
          }
        },
        "categories": [
          {
            "code": "1",
            "type": "Economy",
            "prices": [
              {
                "id": 1,
                "amount": 0,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          },
          {
            "code": "P",
            "type": "Business",
            "prices": [
              {
                "id": 1,
                "amount": 1598,
                "currencyId": "USD",
                "type": "ADULT"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
