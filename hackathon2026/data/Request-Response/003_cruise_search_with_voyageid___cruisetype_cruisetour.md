# Cruise Search with VoyageId & CruiseType CruiseTour

**Path:** Cruise Search > Cruise Tour Search > Norwegian Cruiseline > Cruise Search with VoyageId & CruiseType CruiseTour

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
Date: Fri, 14 Apr 2023 13:48:07 GMT
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
    "total": 2,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1295842,
        "code": "16559601",
        "name": "11-Day O'ahu Explorer Hyatt Waikiki Standard View Cruisetour",
        "startDateTime": "04-Oct-2023",
        "endDateTime": "14-Oct-2023",
        "itinerary": {
          "id": 312210,
          "duration": 10,
          "departure": {
            "code": "HNL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "HNL",
            "type": "CruisePort"
          },
          "portsOfCalls": "At Hotel|At Hotel|At Hotel|Honolulu Hi|Kahului  Maui Hi|Kahului  Maui Hi|Hilo Hi|Kona Hi|Nawiliwili  Kauai Hi|Cruise Napali Coast Hi|Nawiliwili  Kauai Hi|Honolulu Hi",
          "normalizedPortsOfCall": "HNL|OGG|ITO|KOA|HPV|NPLH|HPV|HNL",
          "mapPath": "/content/images/Itineraries/HNL_OGG_HIL_KOA_HPV_NPLA_HPV_HNL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/HNL_OGG_HIL_KOA_HPV_NPLA_HPV_HNL.jpg"
        },
        "uniqueItineraryId": "312210_56__10_18432281",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 3274
              },
              {
                "name": "Outside",
                "value": 3580
              },
              {
                "name": "Balcony",
                "value": 4366
              },
              {
                "name": "Suite",
                "value": 5939
              },
              {
                "code": "PortCharge",
                "value": 273
              },
              {
                "code": "CruiseTax",
                "value": 812.29
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 22:35:16"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
            "KIDSFREE",
            "SHOREX",
            "WIFI"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "SHOREX",
              "subFareDetailsPromoCodes": [
                "SHOREX"
              ]
            },
            {
              "fareDetailsPromoCode": "KidsFree",
              "subFareDetailsPromoCodes": [
                "KidsFree"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
              ]
            },
            {
              "fareDetailsPromoCode": "BEV",
              "subFareDetailsPromoCodes": [
                "BEV"
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
        "cruiseType": "CruiseTour",
        "departureDateTime": "07-Oct-2023",
        "arrivalDateTime": "14-Oct-2023",
        "cruisePackageDepartureDateTime": "04-Oct-2023",
        "cruisePackageArrivalDateTime": "14-Oct-2023",
        "cruiseTourCode": "18432281",
        "voyageId": "16559601",
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
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          21
        ],
        "cruiseTourName": "11-Day O'ahu Explorer Hyatt Waikiki Standard View Cruisetour",
        "cruiseName": "Hawaii Hnl Inter Island"
      },
      {
        "id": 1295841,
        "code": "16559601",
        "name": "11-Day O'ahu Explorer Hyatt Waikiki Ocean View Cruisetour",
        "startDateTime": "04-Oct-2023",
        "endDateTime": "14-Oct-2023",
        "itinerary": {
          "id": 312210,
          "duration": 10,
          "departure": {
            "code": "HNL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "HNL",
            "type": "CruisePort"
          },
          "portsOfCalls": "At Hotel|At Hotel|At Hotel|Honolulu Hi|Kahului  Maui Hi|Kahului  Maui Hi|Hilo Hi|Kona Hi|Nawiliwili  Kauai Hi|Cruise Napali Coast Hi|Nawiliwili  Kauai Hi|Honolulu Hi",
          "normalizedPortsOfCall": "HNL|OGG|ITO|KOA|HPV|NPLH|HPV|HNL",
          "mapPath": "/content/images/Itineraries/HNL_OGG_HIL_KOA_HPV_NPLA_HPV_HNL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/HNL_OGG_HIL_KOA_HPV_NPLA_HPV_HNL.jpg"
        },
        "uniqueItineraryId": "312210_56__10_18432333",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 3574.35
              },
              {
                "name": "Outside",
                "value": 3879.85
              },
              {
                "name": "Balcony",
                "value": 4666.35
              },
              {
                "name": "Suite",
                "value": 6239.35
              },
              {
                "code": "PortCharge",
                "value": 273
              },
              {
                "code": "CruiseTax",
                "value": 302.87
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 05:23:51"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
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
        "cruiseType": "CruiseTour",
        "departureDateTime": "07-Oct-2023",
        "arrivalDateTime": "14-Oct-2023",
        "cruisePackageDepartureDateTime": "04-Oct-2023",
        "cruisePackageArrivalDateTime": "14-Oct-2023",
        "cruiseTourCode": "18432333",
        "voyageId": "16559601",
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
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          21
        ],
        "cruiseTourName": "11-Day O'ahu Explorer Hyatt Waikiki Ocean View Cruisetour",
        "cruiseName": "Hawaii Hnl Inter Island"
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
