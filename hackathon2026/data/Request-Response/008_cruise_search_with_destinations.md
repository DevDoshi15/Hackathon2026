# Cruise Search With Destinations

**Path:** Cruise Search > Cruise Search With Destinations

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
            "key": "destinationId",
            "values": [
                1,
                8
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
Date: Wed, 01 Feb 2023 09:28:15 GMT
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
    "total": 2134,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1316356,
        "code": "18720962",
        "name": "Bermuda - New York",
        "startDateTime": "26-Mar-2023",
        "endDateTime": "05-Apr-2023",
        "itinerary": {
          "id": 363263,
          "duration": 10,
          "departure": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "portsOfCalls": "New York City Ny|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Nassau Bahamas|Great Stirrup Cay Bahamas|Orlando-Beaches-Port Canaveral Fl|Virginia Beach (Norfolk) Va|New York City Ny",
          "normalizedPortsOfCall": "NYC|RNDB|NAS|GSCB|XPC|ORF|NYC"
        },
        "uniqueItineraryId": "363263_13608__10",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 679
              },
              {
                "name": "Outside",
                "value": 889
              },
              {
                "name": "Balcony",
                "value": 1069
              },
              {
                "name": "Suite",
                "value": 1259
              },
              {
                "code": "PortCharge",
                "value": 410
              },
              {
                "code": "CruiseTax",
                "value": 272.39
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:16:45"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
            "GRATSI",
            "OBC",
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
              "fareDetailsPromoCode": "BEV",
              "subFareDetailsPromoCodes": [
                "BEV"
              ]
            },
            {
              "fareDetailsPromoCode": "SHOREX",
              "subFareDetailsPromoCodes": [
                "SHOREX"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
              ]
            },
            {
              "fareDetailsPromoCode": "GRATSI",
              "subFareDetailsPromoCodes": [
                "GRATSI"
              ]
            },
            {
              "fareDetailsPromoCode": "OBC",
              "subFareDetailsPromoCodes": [
                "OBC"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 13608,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/13608/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/13608/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/13608/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/brochure.aspx?did=3719&brochureid=ICE17468&mtype=3718",
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          13608
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "26-Mar-2023",
        "arrivalDateTime": "05-Apr-2023",
        "cruisePackageDepartureDateTime": "26-Mar-2023",
        "cruisePackageArrivalDateTime": "05-Apr-2023",
        "voyageId": "18720962",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Outside",
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 6,
        "minOccupancy": 1,
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1284117,
        "code": "18126043",
        "name": "Bermuda - New York",
        "startDateTime": "28-Mar-2023",
        "endDateTime": "02-Apr-2023",
        "itinerary": {
          "id": 363255,
          "duration": 5,
          "departure": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "portsOfCalls": "New York City Ny|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|New York City Ny",
          "normalizedPortsOfCall": "NYC|RNDB|NYC",
          "mapPath": "/content/images/Itineraries/NYC_RND_NYC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/NYC_RND_NYC.jpg"
        },
        "uniqueItineraryId": "363255_15089__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 798.85
              },
              {
                "name": "Outside",
                "value": 1028.95
              },
              {
                "name": "Balcony",
                "value": 1199
              },
              {
                "name": "Suite",
                "value": 2826.85
              },
              {
                "code": "PortCharge",
                "value": 230
              },
              {
                "code": "CruiseTax",
                "value": 266.29
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
              "fareDetailsPromoCode": "SHOREX",
              "subFareDetailsPromoCodes": [
                "SHOREX"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
              ]
            },
            {
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "OBC",
              "subFareDetailsPromoCodes": [
                "OBC"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 15089,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/15089/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          15089
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "28-Mar-2023",
        "arrivalDateTime": "02-Apr-2023",
        "cruisePackageDepartureDateTime": "28-Mar-2023",
        "cruisePackageArrivalDateTime": "02-Apr-2023",
        "voyageId": "18126043",
        "stnExternalId": "1423099",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1250101,
        "code": "17225543",
        "name": "Bermuda - Boston",
        "startDateTime": "31-Mar-2023",
        "endDateTime": "07-Apr-2023",
        "itinerary": {
          "id": 363057,
          "duration": 7,
          "departure": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Boston Ma|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Boston Ma",
          "normalizedPortsOfCall": "BOS|RNDB|BOS",
          "mapPath": "/content/images/Itineraries/BOS_RND_BOS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BOS_RND_BOS.jpg"
        },
        "uniqueItineraryId": "363057_1097__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 438.75
              },
              {
                "name": "Outside",
                "value": 538
              },
              {
                "name": "Balcony",
                "value": 839
              },
              {
                "name": "Suite",
                "value": 1039
              },
              {
                "code": "PortCharge",
                "value": 260
              },
              {
                "code": "CruiseTax",
                "value": 259.4
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
            "GRATSI",
            "KIDSFREE",
            "SHOREX",
            "WIFI"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "GRATSI",
              "subFareDetailsPromoCodes": [
                "GRATSI"
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
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 1097,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/1097/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/brochure.aspx?did=3719&brochureid=ICE4782&mtype=4280&type=vr&browser_popup=700x450",
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          1097
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "31-Mar-2023",
        "arrivalDateTime": "07-Apr-2023",
        "cruisePackageDepartureDateTime": "31-Mar-2023",
        "cruisePackageArrivalDateTime": "07-Apr-2023",
        "voyageId": "17225543",
        "stnExternalId": "1408701",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1284121,
        "code": "18126044",
        "name": "Bermuda - New York",
        "startDateTime": "02-Apr-2023",
        "endDateTime": "09-Apr-2023",
        "itinerary": {
          "id": 363326,
          "duration": 7,
          "departure": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "portsOfCalls": "New York City Ny|Virginia Beach (Norfolk) Va|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|New York City Ny",
          "normalizedPortsOfCall": "NYC|ORF|RNDB|NYC",
          "mapPath": "/content/images/Itineraries/NYC_NOF_RND_NYC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/NYC_NOF_RND_NYC.jpg"
        },
        "uniqueItineraryId": "363326_15089__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 915.85
              },
              {
                "name": "Outside",
                "value": 1097.85
              },
              {
                "name": "Balcony",
                "value": 1617.85
              },
              {
                "name": "Suite",
                "value": 2566.85
              },
              {
                "code": "PortCharge",
                "value": 300
              },
              {
                "code": "CruiseTax",
                "value": 291.29
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
            "GRATSI",
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
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "OBC",
              "subFareDetailsPromoCodes": [
                "OBC"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
              ]
            },
            {
              "fareDetailsPromoCode": "GRATSI",
              "subFareDetailsPromoCodes": [
                "GRATSI"
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
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 15089,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/15089/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          15089
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Apr-2023",
        "arrivalDateTime": "09-Apr-2023",
        "cruisePackageDepartureDateTime": "02-Apr-2023",
        "cruisePackageArrivalDateTime": "09-Apr-2023",
        "voyageId": "18126044",
        "stnExternalId": "1423102",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1316357,
        "code": "18720963",
        "name": "Bermuda - New York",
        "startDateTime": "05-Apr-2023",
        "endDateTime": "15-Apr-2023",
        "itinerary": {
          "id": 363264,
          "duration": 10,
          "departure": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "portsOfCalls": "New York City Ny|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Nassau Bahamas|Great Stirrup Cay Bahamas|Orlando-Beaches-Port Canaveral Fl|Virginia Beach (Norfolk) Va|New York City Ny",
          "normalizedPortsOfCall": "NYC|RNDB|NAS|GSCB|XPC|ORF|NYC"
        },
        "uniqueItineraryId": "363264_13608__10",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 719
              },
              {
                "name": "Outside",
                "value": 929
              },
              {
                "name": "Balcony",
                "value": 1119
              },
              {
                "name": "Suite",
                "value": 1299
              },
              {
                "code": "PortCharge",
                "value": 410
              },
              {
                "code": "CruiseTax",
                "value": 272.39
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 23:02:41"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
            "GRATSI",
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
              "fareDetailsPromoCode": "SHOREX",
              "subFareDetailsPromoCodes": [
                "SHOREX"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
              ]
            },
            {
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "GRATSI",
              "subFareDetailsPromoCodes": [
                "GRATSI"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 13608,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/13608/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/13608/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/13608/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/brochure.aspx?did=3719&brochureid=ICE17468&mtype=3718",
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          13608
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "05-Apr-2023",
        "arrivalDateTime": "15-Apr-2023",
        "cruisePackageDepartureDateTime": "05-Apr-2023",
        "cruisePackageArrivalDateTime": "15-Apr-2023",
        "voyageId": "18720963",
        "stnExternalId": "1460215",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Outside",
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 6,
        "minOccupancy": 1,
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1250102,
        "code": "17225544",
        "name": "Bermuda - Boston",
        "startDateTime": "07-Apr-2023",
        "endDateTime": "14-Apr-2023",
        "itinerary": {
          "id": 363057,
          "duration": 7,
          "departure": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Boston Ma|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Boston Ma",
          "normalizedPortsOfCall": "BOS|RNDB|BOS",
          "mapPath": "/content/images/Itineraries/BOS_RND_BOS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BOS_RND_BOS.jpg"
        },
        "uniqueItineraryId": "363057_1097__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 549.25
              },
              {
                "name": "Outside",
                "value": 648.7
              },
              {
                "name": "Balcony",
                "value": 999.05
              },
              {
                "name": "Suite",
                "value": 1298.7
              },
              {
                "code": "PortCharge",
                "value": 260
              },
              {
                "code": "CruiseTax",
                "value": 259.4
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
            "SHOREX",
            "WIFI"
          ],
          "fareDetailsPromoCodesInfo": [
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
            },
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
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 1097,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/1097/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/brochure.aspx?did=3719&brochureid=ICE4782&mtype=4280&type=vr&browser_popup=700x450",
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          1097
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "07-Apr-2023",
        "arrivalDateTime": "14-Apr-2023",
        "cruisePackageDepartureDateTime": "07-Apr-2023",
        "cruisePackageArrivalDateTime": "14-Apr-2023",
        "voyageId": "17225544",
        "stnExternalId": "1408702",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1284122,
        "code": "18126045",
        "name": "Bermuda - New York",
        "startDateTime": "09-Apr-2023",
        "endDateTime": "16-Apr-2023",
        "itinerary": {
          "id": 363326,
          "duration": 7,
          "departure": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "portsOfCalls": "New York City Ny|Virginia Beach (Norfolk) Va|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|New York City Ny",
          "normalizedPortsOfCall": "NYC|ORF|RNDB|NYC",
          "mapPath": "/content/images/Itineraries/NYC_NOF_RND_NYC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/NYC_NOF_RND_NYC.jpg"
        },
        "uniqueItineraryId": "363326_15089__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 948
              },
              {
                "name": "Outside",
                "value": 1150
              },
              {
                "name": "Balcony",
                "value": 1546
              },
              {
                "name": "Suite",
                "value": 2476
              },
              {
                "code": "PortCharge",
                "value": 300
              },
              {
                "code": "CruiseTax",
                "value": 291.29
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 16:48:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
            "OBC",
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
              "fareDetailsPromoCode": "OBC",
              "subFareDetailsPromoCodes": [
                "OBC"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
              ]
            },
            {
              "fareDetailsPromoCode": "SHOREX",
              "subFareDetailsPromoCodes": [
                "SHOREX"
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
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 15089,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/15089/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          15089
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "09-Apr-2023",
        "arrivalDateTime": "16-Apr-2023",
        "cruisePackageDepartureDateTime": "09-Apr-2023",
        "cruisePackageArrivalDateTime": "16-Apr-2023",
        "voyageId": "18126045",
        "stnExternalId": "1423103",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1310801,
        "code": "SM230412C30",
        "name": "",
        "startDateTime": "12-Apr-2023",
        "endDateTime": "11-May-2023",
        "itinerary": {
          "id": 327177,
          "duration": 29,
          "departure": {
            "code": "UKB",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SWD",
            "type": "CruisePort"
          },
          "portsOfCalls": "Kobe|Kagoshima|Nagasaki|Busan|Kanazawa|Niigata|Sakata|Hakodate|Aomori|Yokohama|Osaka|Osaka|Tokyo|Miyako|Hakodate|Kushiro|Petropavlovsk Kamchatsky|Dutch Harbor|Kodiak Island|Seward (Anchorage",
          "normalizedPortsOfCall": "UKB|KOJ|NGS|PUS|KZW|KIJ|SKTA|HKD|AOJ|YOK|OSA|TYO|MMY|HKD|KUH|PKC|DUT|ADQ|SWD"
        },
        "uniqueItineraryId": "327177_13761__29_sm230412c30",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 17800
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 07:12:08"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 19,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48,
          19
        ],
        "ship": {
          "id": 13761,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8115/13761/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8115/13761/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8115/13761/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8115,
            "priority": 100,
            "logoPath": "/content/images/cruise/8115/logo_190.png"
          }
        },
        "shipIds": [
          13761
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "12-Apr-2023",
        "arrivalDateTime": "11-May-2023",
        "cruisePackageDepartureDateTime": "12-Apr-2023",
        "cruisePackageArrivalDateTime": "11-May-2023",
        "cruiseTourCode": "SM230412C30",
        "voyageId": "SM230412C30",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_19.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 29,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          19,
          1
        ],
        "packageDescription": ""
      },
      {
        "id": 1250105,
        "code": "17225545",
        "name": "Bermuda - Boston",
        "startDateTime": "14-Apr-2023",
        "endDateTime": "21-Apr-2023",
        "itinerary": {
          "id": 363057,
          "duration": 7,
          "departure": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Boston Ma|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Boston Ma",
          "normalizedPortsOfCall": "BOS|RNDB|BOS",
          "mapPath": "/content/images/Itineraries/BOS_RND_BOS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BOS_RND_BOS.jpg"
        },
        "uniqueItineraryId": "363057_1097__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 499
              },
              {
                "name": "Outside",
                "value": 599
              },
              {
                "name": "Balcony",
                "value": 1099
              },
              {
                "name": "Suite",
                "value": 1299
              },
              {
                "code": "PortCharge",
                "value": 260
              },
              {
                "code": "CruiseTax",
                "value": 259.4
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 20:08:33"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
            "GRATSI",
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
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "GRATSI",
              "subFareDetailsPromoCodes": [
                "GRATSI"
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
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 1097,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/1097/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/brochure.aspx?did=3719&brochureid=ICE4782&mtype=4280&type=vr&browser_popup=700x450",
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          1097
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "14-Apr-2023",
        "arrivalDateTime": "21-Apr-2023",
        "cruisePackageDepartureDateTime": "14-Apr-2023",
        "cruisePackageArrivalDateTime": "21-Apr-2023",
        "voyageId": "17225545",
        "stnExternalId": "1408703",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1310166,
        "code": "18506285",
        "name": "Alaska - Seattle",
        "startDateTime": "15-Apr-2023",
        "endDateTime": "22-Apr-2023",
        "itinerary": {
          "id": 363174,
          "duration": 7,
          "departure": {
            "code": "SEA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SEA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Seattle Wa|Juneau Ak|Skagway Ak|Cruise Glacier Bay Ak|Ketchikan (Ward Cove) Ak|Victoria  Bc  Canada|Seattle Wa",
          "normalizedPortsOfCall": "SEA|JNU|SGY|GBY|KTN|YYJ|SEA",
          "mapPath": "/content/images/Itineraries/SEA_JNU_SGY_KTN_YYJ_SEA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SEA_JNU_SGY_KTN_YYJ_SEA.jpg"
        },
        "uniqueItineraryId": "363174_13670__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 599
              },
              {
                "name": "Outside",
                "value": 999
              },
              {
                "name": "Balcony",
                "value": 1199
              },
              {
                "name": "Suite",
                "value": 1349
              },
              {
                "code": "PortCharge",
                "value": 370
              },
              {
                "code": "CruiseTax",
                "value": 320.32
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 10:54:52"
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
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 13670,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/13670/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/13670/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/13670/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/Brochure.aspx?did=8778&brochureid=ICE116257",
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          13670
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "15-Apr-2023",
        "arrivalDateTime": "22-Apr-2023",
        "cruisePackageDepartureDateTime": "15-Apr-2023",
        "cruisePackageArrivalDateTime": "22-Apr-2023",
        "voyageId": "18506285",
        "stnExternalId": "1449712",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Outside",
          "Suite",
          "Balcony"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ]
      },
      {
        "id": 1312480,
        "code": "DF2304158S",
        "name": "",
        "startDateTime": "15-Apr-2023",
        "endDateTime": "23-Apr-2023",
        "itinerary": {
          "id": 349513,
          "duration": 8,
          "departure": {
            "code": "XPC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "XPC",
            "type": "CruisePort"
          },
          "portsOfCalls": "PORT CANAVERAL|KINGS WHARF|NASSAU|CASTAWAY CAY|PORT CANAVERAL",
          "mapPath": "/content/images/Itineraries/XPC_KWF_NAS_CWC_XPC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/XPC_KWF_NAS_CWC_XPC.jpg"
        },
        "uniqueItineraryId": "349513_13372__8",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2024
              },
              {
                "name": "Outside",
                "value": 2272
              },
              {
                "name": "Balcony",
                "value": 2552
              },
              {
                "code": "PortCharge",
                "value": 240
              },
              {
                "code": "CruiseTax",
                "value": 201.74
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "02-Jun-2022 01:01:33"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 50,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          8,
          9
        ],
        "ship": {
          "id": 13372,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/4/13372/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/4/13372/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/4/13372/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 4,
            "priority": 100,
            "logoPath": "/content/images/cruise/4/logo_190.png"
          }
        },
        "shipIds": [
          13372
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "15-Apr-2023",
        "arrivalDateTime": "23-Apr-2023",
        "cruisePackageDepartureDateTime": "15-Apr-2023",
        "cruisePackageArrivalDateTime": "23-Apr-2023",
        "voyageId": "DF2304158S",
        "stnExternalId": "1448738",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Outside",
          "Inside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_50.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 8,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          50
        ]
      },
      {
        "id": 1284123,
        "code": "18126046",
        "name": "Bermuda - New York",
        "startDateTime": "16-Apr-2023",
        "endDateTime": "23-Apr-2023",
        "itinerary": {
          "id": 363326,
          "duration": 7,
          "departure": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "portsOfCalls": "New York City Ny|Virginia Beach (Norfolk) Va|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|New York City Ny",
          "normalizedPortsOfCall": "NYC|ORF|RNDB|NYC",
          "mapPath": "/content/images/Itineraries/NYC_NOF_RND_NYC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/NYC_NOF_RND_NYC.jpg"
        },
        "uniqueItineraryId": "363326_15089__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1195.35
              },
              {
                "name": "Outside",
                "value": 1630.85
              },
              {
                "name": "Balcony",
                "value": 1747.85
              },
              {
                "name": "Suite",
                "value": 2300.35
              },
              {
                "code": "PortCharge",
                "value": 300
              },
              {
                "code": "CruiseTax",
                "value": 291.29
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
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "OBC",
              "subFareDetailsPromoCodes": [
                "OBC"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
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
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 15089,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/15089/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          15089
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "16-Apr-2023",
        "arrivalDateTime": "23-Apr-2023",
        "cruisePackageDepartureDateTime": "16-Apr-2023",
        "cruisePackageArrivalDateTime": "23-Apr-2023",
        "voyageId": "18126046",
        "stnExternalId": "1423104",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1310802,
        "code": "WH230419C30",
        "name": "",
        "startDateTime": "19-Apr-2023",
        "endDateTime": "18-May-2023",
        "itinerary": {
          "id": 327178,
          "duration": 29,
          "departure": {
            "code": "TYO",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SWD",
            "type": "CruisePort"
          },
          "portsOfCalls": "Tokyo|Tokyo|Kobe|Kobe|Hiroshima|Incheon|Incheon|Busan|Sokcho|Akita|Aomori|Hakodate|Tokyo|Tokyo|Miyako|Hakodate|Kushiro|Petropavlovsk Kamchatsky|Dutch Harbor|Kodiak Island|Seward (Anchorage",
          "normalizedPortsOfCall": "TYO|UKB|HIJ|JCN|PUS|SKCH|AXT|AOJ|HKD|TYO|MMY|HKD|KUH|PKC|DUT|ADQ|SWD"
        },
        "uniqueItineraryId": "327178_13288__29_wh230419c30",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 14800
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 07:12:08"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 19,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48,
          19
        ],
        "ship": {
          "id": 13288,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8115/13288/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8115/13288/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8115/13288/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8115,
            "priority": 100,
            "logoPath": "/content/images/cruise/8115/logo_190.png"
          }
        },
        "shipIds": [
          13288
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "19-Apr-2023",
        "arrivalDateTime": "18-May-2023",
        "cruisePackageDepartureDateTime": "19-Apr-2023",
        "cruisePackageArrivalDateTime": "18-May-2023",
        "cruiseTourCode": "WH230419C30",
        "voyageId": "WH230419C30",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_19.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 29,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          19,
          1
        ],
        "packageDescription": ""
      },
      {
        "id": 1250112,
        "code": "17225546",
        "name": "Bermuda - Boston",
        "startDateTime": "21-Apr-2023",
        "endDateTime": "28-Apr-2023",
        "itinerary": {
          "id": 363057,
          "duration": 7,
          "departure": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Boston Ma|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Boston Ma",
          "normalizedPortsOfCall": "BOS|RNDB|BOS",
          "mapPath": "/content/images/Itineraries/BOS_RND_BOS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BOS_RND_BOS.jpg"
        },
        "uniqueItineraryId": "363057_1097__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 489.45
              },
              {
                "name": "Outside",
                "value": 668.85
              },
              {
                "name": "Balcony",
                "value": 1118.65
              },
              {
                "name": "Suite",
                "value": 1288.95
              },
              {
                "code": "PortCharge",
                "value": 260
              },
              {
                "code": "CruiseTax",
                "value": 259.4
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
            "OBC",
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
              "fareDetailsPromoCode": "BEV",
              "subFareDetailsPromoCodes": [
                "BEV"
              ]
            },
            {
              "fareDetailsPromoCode": "OBC",
              "subFareDetailsPromoCodes": [
                "OBC"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
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
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 1097,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/1097/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/brochure.aspx?did=3719&brochureid=ICE4782&mtype=4280&type=vr&browser_popup=700x450",
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          1097
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "21-Apr-2023",
        "arrivalDateTime": "28-Apr-2023",
        "cruisePackageDepartureDateTime": "21-Apr-2023",
        "cruisePackageArrivalDateTime": "28-Apr-2023",
        "voyageId": "17225546",
        "stnExternalId": "1408704",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1310168,
        "code": "18506286",
        "name": "Alaska - Seattle",
        "startDateTime": "22-Apr-2023",
        "endDateTime": "29-Apr-2023",
        "itinerary": {
          "id": 363174,
          "duration": 7,
          "departure": {
            "code": "SEA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SEA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Seattle Wa|Juneau Ak|Skagway Ak|Cruise Glacier Bay Ak|Ketchikan (Ward Cove) Ak|Victoria  Bc  Canada|Seattle Wa",
          "normalizedPortsOfCall": "SEA|JNU|SGY|GBY|KTN|YYJ|SEA",
          "mapPath": "/content/images/Itineraries/SEA_JNU_SGY_KTN_YYJ_SEA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SEA_JNU_SGY_KTN_YYJ_SEA.jpg"
        },
        "uniqueItineraryId": "363174_13670__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 648.7
              },
              {
                "name": "Outside",
                "value": 1049.1
              },
              {
                "name": "Balcony",
                "value": 1248.65
              },
              {
                "name": "Suite",
                "value": 1398.8
              },
              {
                "code": "PortCharge",
                "value": 370
              },
              {
                "code": "CruiseTax",
                "value": 320.32
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
            "SHOREX",
            "WIFI"
          ],
          "fareDetailsPromoCodesInfo": [
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
            },
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
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 13670,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/13670/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/13670/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/13670/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/Brochure.aspx?did=8778&brochureid=ICE116257",
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          13670
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "22-Apr-2023",
        "arrivalDateTime": "29-Apr-2023",
        "cruisePackageDepartureDateTime": "22-Apr-2023",
        "cruisePackageArrivalDateTime": "29-Apr-2023",
        "voyageId": "18506286",
        "stnExternalId": "1449730",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Outside",
          "Suite",
          "Balcony"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ]
      },
      {
        "id": 1284124,
        "code": "18126047",
        "name": "Bermuda - New York",
        "startDateTime": "23-Apr-2023",
        "endDateTime": "30-Apr-2023",
        "itinerary": {
          "id": 363326,
          "duration": 7,
          "departure": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "NYC",
            "type": "CruisePort"
          },
          "portsOfCalls": "New York City Ny|Virginia Beach (Norfolk) Va|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|New York City Ny",
          "normalizedPortsOfCall": "NYC|ORF|RNDB|NYC",
          "mapPath": "/content/images/Itineraries/NYC_NOF_RND_NYC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/NYC_NOF_RND_NYC.jpg"
        },
        "uniqueItineraryId": "363326_15089__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1091
              },
              {
                "name": "Outside",
                "value": 1397
              },
              {
                "name": "Balcony",
                "value": 1650
              },
              {
                "name": "Suite",
                "value": 2346
              },
              {
                "code": "PortCharge",
                "value": 300
              },
              {
                "code": "CruiseTax",
                "value": 308.88
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 20:00:16"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
            "GRATSI",
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
              "fareDetailsPromoCode": "GRATSI",
              "subFareDetailsPromoCodes": [
                "GRATSI"
              ]
            },
            {
              "fareDetailsPromoCode": "SHOREX",
              "subFareDetailsPromoCodes": [
                "SHOREX"
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
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 15089,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/15089/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/15089/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          15089
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "23-Apr-2023",
        "arrivalDateTime": "30-Apr-2023",
        "cruisePackageDepartureDateTime": "23-Apr-2023",
        "cruisePackageArrivalDateTime": "30-Apr-2023",
        "voyageId": "18126047",
        "stnExternalId": "1423105",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1285391,
        "code": "20230423MI14",
        "name": "Carnival Journeys - Alaska Cruise",
        "startDateTime": "23-Apr-2023",
        "endDateTime": "07-May-2023",
        "itinerary": {
          "id": 354102,
          "duration": 14,
          "departure": {
            "code": "LAX",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "LAX",
            "type": "CruisePort"
          },
          "portsOfCalls": "LOS ANGELES (LONG BEACH) CA|SITKA AK|JUNEAU AK|SKAGWAY AK|ICY STRAIT POINT AK|CRUISE TRACY ARM FJORD|KETCHIKAN AK|VICTORIA BC CANADA|LOS ANGELES (LONG BEACH) CA",
          "mapPath": "/content/images/Itineraries/LAX_LGB_SIT_JNU_SGY_ISPS_TRAC_KTN_YYJ_LGB_LAX.jpg",
          "fallbackMapPath": "/content/images/Itineraries/LAX_LGB_SIT_JNU_SGY_ISPS_TRAC_KTN_YYJ_LGB_LAX.jpg"
        },
        "uniqueItineraryId": "354102_5__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1099
              },
              {
                "name": "Outside",
                "value": 1333
              },
              {
                "name": "Balcony",
                "value": 1648
              },
              {
                "code": "PortCharge",
                "value": 299
              },
              {
                "code": "CruiseTax",
                "value": 268.86
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 20:25:22",
            "fareTypes": [
              "ML"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NR"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NR",
              "subFareDetailsPromoCodes": [
                "NR"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 5,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/5/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/5/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/5/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Orchestra/en-gl/index.html",
          "hasVrForActivity": true,
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 1,
            "priority": 100,
            "logoPath": "/content/images/cruise/1/logo_190.png"
          }
        },
        "shipIds": [
          5
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "23-Apr-2023",
        "arrivalDateTime": "07-May-2023",
        "cruisePackageDepartureDateTime": "23-Apr-2023",
        "cruisePackageArrivalDateTime": "07-May-2023",
        "voyageId": "20230423MI14",
        "stnExternalId": "1427699",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Outside",
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ]
      },
      {
        "id": 1250116,
        "code": "17225547",
        "name": "Bermuda - Boston",
        "startDateTime": "28-Apr-2023",
        "endDateTime": "05-May-2023",
        "itinerary": {
          "id": 363058,
          "duration": 7,
          "departure": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BOS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Boston Ma|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Royal Naval Dockyard Bermuda|Bar Harbor Me|Boston Ma",
          "normalizedPortsOfCall": "BOS|RNDB|BHB|BOS",
          "mapPath": "/content/images/Itineraries/BOS_RND_BHB_BOS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BOS_RND_BHB_BOS.jpg"
        },
        "uniqueItineraryId": "363058_1097__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 509
              },
              {
                "name": "Outside",
                "value": 659
              },
              {
                "name": "Balcony",
                "value": 1249
              },
              {
                "name": "Suite",
                "value": 1339
              },
              {
                "code": "PortCharge",
                "value": 260
              },
              {
                "code": "CruiseTax",
                "value": 259.4
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 20:01:56"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
            "GRATSI",
            "KIDSFREE",
            "SHOREX",
            "WIFI"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "GRATSI",
              "subFareDetailsPromoCodes": [
                "GRATSI"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
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
          "id": 8,
          "type": "Destination",
          "priority": 40
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 1097,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/1097/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/1097/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/brochure.aspx?did=3719&brochureid=ICE4782&mtype=4280&type=vr&browser_popup=700x450",
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          1097
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "28-Apr-2023",
        "arrivalDateTime": "05-May-2023",
        "cruisePackageDepartureDateTime": "28-Apr-2023",
        "cruisePackageArrivalDateTime": "05-May-2023",
        "voyageId": "17225547",
        "stnExternalId": "1408705",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_8.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          8
        ]
      },
      {
        "id": 1310170,
        "code": "18506287",
        "name": "Alaska - Seattle",
        "startDateTime": "29-Apr-2023",
        "endDateTime": "06-May-2023",
        "itinerary": {
          "id": 363174,
          "duration": 7,
          "departure": {
            "code": "SEA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SEA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Seattle Wa|Juneau Ak|Skagway Ak|Cruise Glacier Bay Ak|Ketchikan (Ward Cove) Ak|Victoria  Bc  Canada|Seattle Wa",
          "normalizedPortsOfCall": "SEA|JNU|SGY|GBY|KTN|YYJ|SEA",
          "mapPath": "/content/images/Itineraries/SEA_JNU_SGY_KTN_YYJ_SEA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SEA_JNU_SGY_KTN_YYJ_SEA.jpg"
        },
        "uniqueItineraryId": "363174_13670__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 698.75
              },
              {
                "name": "Outside",
                "value": 1098.5
              },
              {
                "name": "Balcony",
                "value": 1298.7
              },
              {
                "name": "Suite",
                "value": 1448.85
              },
              {
                "code": "PortCharge",
                "value": 370
              },
              {
                "code": "CruiseTax",
                "value": 320.32
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
            },
            {
              "fareDetailsPromoCode": "BEV",
              "subFareDetailsPromoCodes": [
                "BEV"
              ]
            },
            {
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "OBC",
              "subFareDetailsPromoCodes": [
                "OBC"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 13670,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/13670/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/13670/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/13670/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.iceportal.com/brochures/ice/Brochure.aspx?did=8778&brochureid=ICE116257",
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 6,
            "priority": 100,
            "logoPath": "/content/images/cruise/6/logo_190.png"
          }
        },
        "shipIds": [
          13670
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "29-Apr-2023",
        "arrivalDateTime": "06-May-2023",
        "cruisePackageDepartureDateTime": "29-Apr-2023",
        "cruisePackageArrivalDateTime": "06-May-2023",
        "voyageId": "18506287",
        "stnExternalId": "1449731",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Outside",
          "Suite",
          "Balcony"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ]
      },
      {
        "id": 1298881,
        "code": "K332",
        "name": "7-Day Alaskan Inside Passage",
        "startDateTime": "29-Apr-2023",
        "endDateTime": "06-May-2023",
        "itinerary": {
          "id": 269207,
          "duration": 7,
          "departure": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Vancouver BC Ca|Tracy Arm Inlet|Juneau Alaska Us|Skagway Alaska Us|Glacier Bay|Ketchikan Alaska Us|Vancouver BC Ca",
          "normalizedPortsOfCall": "YVR|TRAC|JNU|SGY|GCB|KTN|YVR",
          "mapPath": "/content/images/Itineraries/YVR_TRA_JNU_SGY_GLB_KTN_YVR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/YVR_TRA_JNU_SGY_GLB_KTN_YVR.jpg"
        },
        "uniqueItineraryId": "269207_13708__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 784
              },
              {
                "name": "Outside",
                "value": 1384
              },
              {
                "name": "Balcony",
                "value": 1434
              },
              {
                "name": "Suite",
                "value": 1784
              },
              {
                "code": "PortCharge",
                "value": 235
              },
              {
                "code": "CruiseTax",
                "value": 250
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:49:51"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
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
              "fareDetailsPromoCode": "Dining",
              "subFareDetailsPromoCodes": [
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "WiFi",
              "subFareDetailsPromoCodes": [
                "WiFi"
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
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 13708,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/13708/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/13708/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/13708/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 5,
            "priority": 100,
            "logoPath": "/content/images/cruise/5/logo_190.png"
          }
        },
        "shipIds": [
          13708
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "29-Apr-2023",
        "arrivalDateTime": "06-May-2023",
        "cruisePackageDepartureDateTime": "29-Apr-2023",
        "cruisePackageArrivalDateTime": "06-May-2023",
        "voyageId": "K332",
        "stnExternalId": "1436035",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ]
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
