# FareCode Details

**Path:** Farecode Details > FareCode Details

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/GetFareCodeDetails`

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
        "pos": { //Either id or currency is mandatory
            //"id": 1,
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
            "packageId": 1269434
        },
        "categories": [
            {
                "fare": {
                    "fareCode": {
                        "code": "I7522610" // To Fetch farecode details, code is required 
                    }
                }
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        },
        {
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
Date: Thu, 02 Feb 2023 10:06:59 GMT
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
      "requestId": "e236771c-6cd5-48e5-9339-dc362bf950b5",
      "timeStamp": "02-Feb-2023 05:06:58",
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
      "fareCodes": [
        {
          "code": "I7522610",
          "name": "PRICE CODE - I7522610<br>PROMO ID - WOW Sale<br>DESCRIPTION - 5N or Less Balcony<br>OFFERED FROM - 08/12/21<br>ELIGIBILITY - GUEST 1 Y 2 N 3 N 4 N 5+ N Sgl Y Child N Infant N<br>AGENCY RESTRICTION - NO<br>ALLOW BOOKINGS TO BE CONVERTED - YES<br>BASED ON PRICE TYPE - STANDARD<br>REFUNDABLE<br>BOOKING CHANNEL RESTRICTION - NO<br>PROMOTION COMMISSIONABLE - YES<br>COUNTRY RESTRICTION - YES<br>COUNTRY CODE - CAN AFG AGO ALB ARE ARM ATA AZE BDI BEL BEN BFA<br>COUNTRY CODE - BGR BHR BIH BLR BWA CAF CIV CMR COG COM CPV CYP C<br>BOOKING VALID FOR BOTH CRUISE AND AIR/SEA BOOKINGS<br>PROMOTION DEEP DISCOUNT - NO<br>ELIGIBLE FOR GAP - YES<br>ELIGIBLE FOR TC - YES<br>GATEWAY RESTRICTION - NO<br>GUEST AGE RESTRICTION - NO<br>INCLUDE IN BEST RATE - YES<br>LOYALTY TIER RESTRICTION - NO<br>SINGLE SUPPLEMENT - 200.00%<br>SINGLE SUPPLEMENT NCCF - 200.00%<br>OFFICE RESTRICTION - NO<br>PACKAGE CODE RESTRICTION - YES<br>PACKAGE CODE - FR4BH098<br>PUBLIC SERVICE CODE RESTRICTION - NO<br>RATE CATEGORY RESTRICTION - YES<br>RATE CATEGORY CODE - 4G 6B D1 2G S2 D4 2H VA 1B 4C VL D5<br>RATE CATEGORY CODE - 2B E2 D 7D 4B 5D 4D D6 B1 2E DA B2 3H<br>RESIDENT STATE/PROVINCE RESTRICTION - NO<br>OCCUPANCY RESTRICTION - YES<br>OCCUPANCY CODE - S D T Q<br>SOURCE TYPE - C<br>SOURCE REFUND TYPE - X<br>REDEEM START DATETIME -<br>REDEEM END DATETIME -",
          "type": 0,
          "refundableType": 1,
          "status": 1,
          "details": {},
          "groups": [
            {}
          ]
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 52,
        "address": {
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      },
      {
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
