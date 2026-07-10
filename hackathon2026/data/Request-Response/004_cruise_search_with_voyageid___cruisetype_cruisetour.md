# Cruise Search with VoyageId & CruiseType CruiseTour

**Path:** Cruise Search > Cruise Tour Search > Viking Ocean Cruises > Cruise Search with VoyageId & CruiseType CruiseTour

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/cruise`

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
    "filters": [
        {
            "key": "voyageId",
            "values": [
                "HMM230703T"
            ]
        },
        {
            "key": "cruiseType",
            "values": [
                "CruiseTour"
            ]
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Tue, 04 Apr 2023 12:57:15 GMT
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
    "total": 1,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1289965,
        "code": "HMM230703T",
        "name": "Portugal's River of Gold",
        "startDateTime": "01-Jul-2023",
        "endDateTime": "10-Jul-2023",
        "itinerary": {
          "id": 357994,
          "duration": 9,
          "departure": {
            "code": "LIS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "OPO",
            "type": "CruisePort"
          },
          "portsOfCalls": "Portugals River of Gold|Lisbon Hotel|Lisbon Hotel|Porto|Regua|Pinhao|Scenic Sailing Douro River|Barca dAlva|Salamanca|Pinhao|Regua|Regua|Porto|Porto|Porto"
        },
        "uniqueItineraryId": "357994_13623__9_hmm230703t",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 3899
              },
              {
                "name": "Balcony",
                "value": 5499
              },
              {
                "name": "Suite",
                "value": 6299
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "03-Jun-2022 22:05:57"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 15,
          "type": "Destination",
          "priority": 50
        },
        "parentDestinationIds": [
          15
        ],
        "ship": {
          "id": 13623,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8112/13623/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8112/13623/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8112/13623/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.vikingrivercruises.com/content/douro/start.html?secure=true",
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8112,
            "priority": 100,
            "logoPath": "/content/images/cruise/8112/logo_190.png"
          }
        },
        "shipIds": [
          13623
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Jul-2023",
        "arrivalDateTime": "10-Jul-2023",
        "cruisePackageDepartureDateTime": "01-Jul-2023",
        "cruisePackageArrivalDateTime": "10-Jul-2023",
        "cruiseTourCode": "HMM230703T",
        "voyageId": "HMM230703T",
        "stnExternalId": "1429855",
        "packageTourId": -1,
        "categoryTypes": [
          "Outside",
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 9,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "Portugal's River of Gold"
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
