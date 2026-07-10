# Cruise Search with VoyageId & CruiseType CruiseOnly

**Path:** Cruise Search > Cruise Only Search > Norwegian Cruiseline > Cruise Search with VoyageId & CruiseType CruiseOnly

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
                "16559601"
            ]
        },
        {
            "key": "cruiseType",
            "values": [
                "CruiseOnly"
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
Date: Fri, 14 Apr 2023 13:48:43 GMT
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
        "id": 1214823,
        "code": "16559601",
        "name": "Hawaii Hnl Inter Island",
        "startDateTime": "07-Oct-2023",
        "endDateTime": "14-Oct-2023",
        "itinerary": {
          "id": 363062,
          "duration": 7,
          "departure": {
            "code": "HNL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "HNL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Honolulu Hi|Kahului  Maui Hi|Kahului  Maui Hi|Hilo Hi|Kona Hi|Nawiliwili  Kauai Hi|Nawiliwili  Kauai Hi|Cruise Napali Coast Hi|Honolulu Hi",
          "normalizedPortsOfCall": "HNL|OGG|ITO|KOA|HPV|NPLH|HNL",
          "mapPath": "/content/images/Itineraries/HNL_OGG_HIL_KON_HPV_NPLA_HNL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/HNL_OGG_HIL_KON_HPV_NPLA_HNL.jpg"
        },
        "uniqueItineraryId": "363062_56__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1975.35
              },
              {
                "name": "Outside",
                "value": 2280.85
              },
              {
                "name": "Balcony",
                "value": 3067.35
              },
              {
                "name": "Suite",
                "value": 4640.35
              },
              {
                "code": "PortCharge",
                "value": 273
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:00:14"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
            "KIDSFREE",
            "OBC",
            "SHOREX",
            "WIFI"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "BEV",
              "subFareDetailsPromoCodes": [
                "BEV"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
              ]
            },
            {
              "fareDetailsPromoCode": "OBC",
              "subFareDetailsPromoCodes": [
                "OBC"
              ]
            },
            {
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "KidsFree",
              "subFareDetailsPromoCodes": [
                "KidsFree"
              ]
            },
            {
              "fareDetailsPromoCode": "SHOREX",
              "subFareDetailsPromoCodes": [
                "SHOREX"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 21,
          "type": "Destination",
          "priority": 70
        },
        "parentDestinationIds": [
          21
        ],
        "ship": {
          "id": 56,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/56/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/56/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/56/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          56
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "07-Oct-2023",
        "arrivalDateTime": "14-Oct-2023",
        "cruisePackageDepartureDateTime": "07-Oct-2023",
        "cruisePackageArrivalDateTime": "14-Oct-2023",
        "voyageId": "16559601",
        "stnExternalId": "1386732",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Suite",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_21.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          21
        ],
        "cruiseTourName": "Hawaii Hnl Inter Island",
        "cruiseName": "Hawaii Hnl Inter Island"
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
