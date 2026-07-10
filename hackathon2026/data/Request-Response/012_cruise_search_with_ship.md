# Cruise Search With Ship

**Path:** Cruise Search > Cruise Search With Ship

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
            "key": "shipId",
            "values": [
                71,
                116
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
Date: Wed, 01 Feb 2023 09:43:22 GMT
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
    "total": 227,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1269280,
        "code": "AD04W115",
        "name": "4 Night Western Caribbean Cruise",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 310922,
          "duration": 4,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310922_71__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 209
              },
              {
                "name": "Outside",
                "value": 279
              },
              {
                "name": "Balcony",
                "value": 368
              },
              {
                "name": "Suite",
                "value": 819
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 101.81
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "AD04W115",
        "stnExternalId": "1413697",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ],
        "groupInfo": [
          {
            "isHeadQuarter": true,
            "consolidatorId": 33
          }
        ]
      },
      {
        "id": 1269411,
        "code": "FR3BH038",
        "name": "3 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 350358,
          "duration": 3,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Nassau -  Bahamas|Perfect Day Cococay -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|NAS|COCY|MIA",
          "mapPath": "/content/images/Itineraries/MIA_NAS_CCY_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_NAS_CCY_MIA.jpg"
        },
        "uniqueItineraryId": "350358_116__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 278
              },
              {
                "name": "Outside",
                "value": 339
              },
              {
                "name": "Balcony",
                "value": 419
              },
              {
                "name": "Suite",
                "value": 648
              },
              {
                "code": "PortCharge",
                "value": 90
              },
              {
                "code": "CruiseTax",
                "value": 118.65
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "ML",
              "PF"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "FR3BH038",
        "stnExternalId": "1413934",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269412,
        "code": "FR4BH098",
        "name": "4 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "06-Feb-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 311051,
          "duration": 4,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|COCY|NAS|MIA",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "311051_116__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 319
              },
              {
                "name": "Outside",
                "value": 389
              },
              {
                "name": "Balcony",
                "value": 438
              },
              {
                "name": "Suite",
                "value": 679
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 118.6
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "ML",
              "PF"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "KIDSFREE",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
            {
              "fareDetailsPromoCode": "KidsFree",
              "subFareDetailsPromoCodes": [
                "KidsFree"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "06-Feb-2023",
        "arrivalDateTime": "10-Feb-2023",
        "cruisePackageDepartureDateTime": "06-Feb-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "voyageId": "FR4BH098",
        "stnExternalId": "1413967",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269281,
        "code": "AD05W358",
        "name": "5 Night Western Caribbean Cruise",
        "startDateTime": "06-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 310923,
          "duration": 5,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Puerto Costa Maya -  Mexico|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310923_71__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 258
              },
              {
                "name": "Outside",
                "value": 309
              },
              {
                "name": "Balcony",
                "value": 468
              },
              {
                "name": "Suite",
                "value": 828
              },
              {
                "code": "PortCharge",
                "value": 135
              },
              {
                "code": "CruiseTax",
                "value": 116.5
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "06-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "06-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "AD05W358",
        "stnExternalId": "1413698",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ]
      },
      {
        "id": 1269413,
        "code": "FR3BH037",
        "name": "3 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "10-Feb-2023",
        "endDateTime": "13-Feb-2023",
        "itinerary": {
          "id": 302950,
          "duration": 3,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|COCY|NAS|MIA",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "302950_116__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 268
              },
              {
                "name": "Outside",
                "value": 329
              },
              {
                "name": "Balcony",
                "value": 408
              },
              {
                "name": "Suite",
                "value": 628
              },
              {
                "code": "PortCharge",
                "value": 90
              },
              {
                "code": "CruiseTax",
                "value": 118.5
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "ML",
              "PF"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "10-Feb-2023",
        "arrivalDateTime": "13-Feb-2023",
        "cruisePackageDepartureDateTime": "10-Feb-2023",
        "cruisePackageArrivalDateTime": "13-Feb-2023",
        "voyageId": "FR3BH037",
        "stnExternalId": "1413935",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269282,
        "code": "AD05W359",
        "name": "5 Night Western Caribbean Cruise",
        "startDateTime": "11-Feb-2023",
        "endDateTime": "16-Feb-2023",
        "itinerary": {
          "id": 310923,
          "duration": 5,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Puerto Costa Maya -  Mexico|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310923_71__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 288
              },
              {
                "name": "Outside",
                "value": 368
              },
              {
                "name": "Balcony",
                "value": 528
              },
              {
                "name": "Suite",
                "value": 878
              },
              {
                "code": "PortCharge",
                "value": 135
              },
              {
                "code": "CruiseTax",
                "value": 116.61
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "11-Feb-2023",
        "arrivalDateTime": "16-Feb-2023",
        "cruisePackageDepartureDateTime": "11-Feb-2023",
        "cruisePackageArrivalDateTime": "16-Feb-2023",
        "voyageId": "AD05W359",
        "stnExternalId": "1413701",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ]
      },
      {
        "id": 1269414,
        "code": "FR4BH098",
        "name": "4 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "13-Feb-2023",
        "endDateTime": "17-Feb-2023",
        "itinerary": {
          "id": 311051,
          "duration": 4,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|COCY|NAS|MIA",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "311051_116__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 329
              },
              {
                "name": "Outside",
                "value": 379
              },
              {
                "name": "Balcony",
                "value": 489
              },
              {
                "name": "Suite",
                "value": 729
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 118.6
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "ML",
              "PF"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "13-Feb-2023",
        "arrivalDateTime": "17-Feb-2023",
        "cruisePackageDepartureDateTime": "13-Feb-2023",
        "cruisePackageArrivalDateTime": "17-Feb-2023",
        "voyageId": "FR4BH098",
        "stnExternalId": "1413968",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269283,
        "code": "AD04W115",
        "name": "4 Night Western Caribbean Cruise",
        "startDateTime": "16-Feb-2023",
        "endDateTime": "20-Feb-2023",
        "itinerary": {
          "id": 310922,
          "duration": 4,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310922_71__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 219
              },
              {
                "name": "Outside",
                "value": 279
              },
              {
                "name": "Balcony",
                "value": 408
              },
              {
                "name": "Suite",
                "value": 919
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 101.81
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "16-Feb-2023",
        "arrivalDateTime": "20-Feb-2023",
        "cruisePackageDepartureDateTime": "16-Feb-2023",
        "cruisePackageArrivalDateTime": "20-Feb-2023",
        "voyageId": "AD04W115",
        "stnExternalId": "1413700",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "arePackageToursAvailable": true,
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ],
        "groupInfo": [
          {
            "isHeadQuarter": true,
            "isAgency": true,
            "consolidatorId": 33
          }
        ]
      },
      {
        "id": 1269415,
        "code": "FR3BH038",
        "name": "3 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "17-Feb-2023",
        "endDateTime": "20-Feb-2023",
        "itinerary": {
          "id": 350358,
          "duration": 3,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Nassau -  Bahamas|Perfect Day Cococay -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|NAS|COCY|MIA",
          "mapPath": "/content/images/Itineraries/MIA_NAS_CCY_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_NAS_CCY_MIA.jpg"
        },
        "uniqueItineraryId": "350358_116__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 289
              },
              {
                "name": "Outside",
                "value": 368
              },
              {
                "name": "Balcony",
                "value": 438
              },
              {
                "name": "Suite",
                "value": 688
              },
              {
                "code": "PortCharge",
                "value": 90
              },
              {
                "code": "CruiseTax",
                "value": 118.65
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "PF",
              "ML"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "17-Feb-2023",
        "arrivalDateTime": "20-Feb-2023",
        "cruisePackageDepartureDateTime": "17-Feb-2023",
        "cruisePackageArrivalDateTime": "20-Feb-2023",
        "voyageId": "FR3BH038",
        "stnExternalId": "1413936",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ],
        "groupInfo": [
          {
            "isHeadQuarter": true
          }
        ]
      },
      {
        "id": 1269416,
        "code": "FR4BH105",
        "name": "4 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "20-Feb-2023",
        "endDateTime": "24-Feb-2023",
        "itinerary": {
          "id": 360634,
          "duration": 4,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|COCY|NAS|MIA",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "360634_116__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 338
              },
              {
                "name": "Outside",
                "value": 408
              },
              {
                "name": "Balcony",
                "value": 499
              },
              {
                "name": "Suite",
                "value": 709
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 118.57
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "PF",
              "ML"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "20-Feb-2023",
        "arrivalDateTime": "24-Feb-2023",
        "cruisePackageDepartureDateTime": "20-Feb-2023",
        "cruisePackageArrivalDateTime": "24-Feb-2023",
        "voyageId": "FR4BH105",
        "stnExternalId": "1413969",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269284,
        "code": "AD05W358",
        "name": "5 Night Western Caribbean Cruise",
        "startDateTime": "20-Feb-2023",
        "endDateTime": "25-Feb-2023",
        "itinerary": {
          "id": 310923,
          "duration": 5,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Puerto Costa Maya -  Mexico|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310923_71__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 268
              },
              {
                "name": "Outside",
                "value": 320
              },
              {
                "name": "Balcony",
                "value": 568
              },
              {
                "name": "Suite",
                "value": 928
              },
              {
                "code": "PortCharge",
                "value": 135
              },
              {
                "code": "CruiseTax",
                "value": 116.5
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "20-Feb-2023",
        "arrivalDateTime": "25-Feb-2023",
        "cruisePackageDepartureDateTime": "20-Feb-2023",
        "cruisePackageArrivalDateTime": "25-Feb-2023",
        "voyageId": "AD05W358",
        "stnExternalId": "1413699",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ]
      },
      {
        "id": 1269417,
        "code": "FR3BH037",
        "name": "3 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "24-Feb-2023",
        "endDateTime": "27-Feb-2023",
        "itinerary": {
          "id": 302950,
          "duration": 3,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|COCY|NAS|MIA",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "302950_116__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 268
              },
              {
                "name": "Outside",
                "value": 338
              },
              {
                "name": "Balcony",
                "value": 419
              },
              {
                "name": "Suite",
                "value": 618
              },
              {
                "code": "PortCharge",
                "value": 90
              },
              {
                "code": "CruiseTax",
                "value": 118.5
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "PF",
              "ML"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "24-Feb-2023",
        "arrivalDateTime": "27-Feb-2023",
        "cruisePackageDepartureDateTime": "24-Feb-2023",
        "cruisePackageArrivalDateTime": "27-Feb-2023",
        "voyageId": "FR3BH037",
        "stnExternalId": "1413937",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269285,
        "code": "AD05W359",
        "name": "5 Night Western Caribbean Cruise",
        "startDateTime": "25-Feb-2023",
        "endDateTime": "02-Mar-2023",
        "itinerary": {
          "id": 310923,
          "duration": 5,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Puerto Costa Maya -  Mexico|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310923_71__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 278
              },
              {
                "name": "Outside",
                "value": 348
              },
              {
                "name": "Balcony",
                "value": 538
              },
              {
                "name": "Suite",
                "value": 828
              },
              {
                "code": "PortCharge",
                "value": 135
              },
              {
                "code": "CruiseTax",
                "value": 116.61
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "KIDSFREE",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "KidsFree",
              "subFareDetailsPromoCodes": [
                "KidsFree"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "25-Feb-2023",
        "arrivalDateTime": "02-Mar-2023",
        "cruisePackageDepartureDateTime": "25-Feb-2023",
        "cruisePackageArrivalDateTime": "02-Mar-2023",
        "voyageId": "AD05W359",
        "stnExternalId": "1413702",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ]
      },
      {
        "id": 1269418,
        "code": "FR4BH104",
        "name": "4 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "27-Feb-2023",
        "endDateTime": "03-Mar-2023",
        "itinerary": {
          "id": 311050,
          "duration": 4,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|COCY|NAS|MIA",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "311050_116__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 309
              },
              {
                "name": "Outside",
                "value": 368
              },
              {
                "name": "Balcony",
                "value": 428
              },
              {
                "name": "Suite",
                "value": 688
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 118.57
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "PF",
              "ML"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "27-Feb-2023",
        "arrivalDateTime": "03-Mar-2023",
        "cruisePackageDepartureDateTime": "27-Feb-2023",
        "cruisePackageArrivalDateTime": "03-Mar-2023",
        "voyageId": "FR4BH104",
        "stnExternalId": "1413970",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269286,
        "code": "AD04W115",
        "name": "4 Night Western Caribbean Cruise",
        "startDateTime": "02-Mar-2023",
        "endDateTime": "06-Mar-2023",
        "itinerary": {
          "id": 310922,
          "duration": 4,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310922_71__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 228
              },
              {
                "name": "Outside",
                "value": 289
              },
              {
                "name": "Balcony",
                "value": 399
              },
              {
                "name": "Suite",
                "value": 788
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 101.81
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Mar-2023",
        "arrivalDateTime": "06-Mar-2023",
        "cruisePackageDepartureDateTime": "02-Mar-2023",
        "cruisePackageArrivalDateTime": "06-Mar-2023",
        "voyageId": "AD04W115",
        "stnExternalId": "1413703",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ],
        "groupInfo": [
          {
            "isHeadQuarter": true,
            "consolidatorId": 33
          }
        ]
      },
      {
        "id": 1269419,
        "code": "FR3BH038",
        "name": "3 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "03-Mar-2023",
        "endDateTime": "06-Mar-2023",
        "itinerary": {
          "id": 350358,
          "duration": 3,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Nassau -  Bahamas|Perfect Day Cococay -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|NAS|COCY|MIA",
          "mapPath": "/content/images/Itineraries/MIA_NAS_CCY_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_NAS_CCY_MIA.jpg"
        },
        "uniqueItineraryId": "350358_116__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 309
              },
              {
                "name": "Outside",
                "value": 378
              },
              {
                "name": "Balcony",
                "value": 439
              },
              {
                "name": "Suite",
                "value": 679
              },
              {
                "code": "PortCharge",
                "value": 90
              },
              {
                "code": "CruiseTax",
                "value": 118.65
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "ML",
              "PF"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Mar-2023",
        "arrivalDateTime": "06-Mar-2023",
        "cruisePackageDepartureDateTime": "03-Mar-2023",
        "cruisePackageArrivalDateTime": "06-Mar-2023",
        "voyageId": "FR3BH038",
        "stnExternalId": "1413938",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269420,
        "code": "FR4BH101",
        "name": "4 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "06-Mar-2023",
        "endDateTime": "10-Mar-2023",
        "itinerary": {
          "id": 360634,
          "duration": 4,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|COCY|NAS|MIA",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "360634_116__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 368
              },
              {
                "name": "Outside",
                "value": 449
              },
              {
                "name": "Balcony",
                "value": 508
              },
              {
                "name": "Suite",
                "value": 769
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 126.4
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "ML",
              "PF"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "06-Mar-2023",
        "arrivalDateTime": "10-Mar-2023",
        "cruisePackageDepartureDateTime": "06-Mar-2023",
        "cruisePackageArrivalDateTime": "10-Mar-2023",
        "voyageId": "FR4BH101",
        "stnExternalId": "1414007",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269287,
        "code": "AD05W358",
        "name": "5 Night Western Caribbean Cruise",
        "startDateTime": "06-Mar-2023",
        "endDateTime": "11-Mar-2023",
        "itinerary": {
          "id": 310923,
          "duration": 5,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Puerto Costa Maya -  Mexico|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310923_71__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 428
              },
              {
                "name": "Outside",
                "value": 518
              },
              {
                "name": "Balcony",
                "value": 658
              },
              {
                "name": "Suite",
                "value": 1178
              },
              {
                "code": "PortCharge",
                "value": 135
              },
              {
                "code": "CruiseTax",
                "value": 116.5
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
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
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "06-Mar-2023",
        "arrivalDateTime": "11-Mar-2023",
        "cruisePackageDepartureDateTime": "06-Mar-2023",
        "cruisePackageArrivalDateTime": "11-Mar-2023",
        "voyageId": "AD05W358",
        "stnExternalId": "1413750",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ]
      },
      {
        "id": 1269421,
        "code": "FR3BH037",
        "name": "3 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "10-Mar-2023",
        "endDateTime": "13-Mar-2023",
        "itinerary": {
          "id": 302950,
          "duration": 3,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|COCY|NAS|MIA",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "302950_116__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 298
              },
              {
                "name": "Outside",
                "value": 389
              },
              {
                "name": "Balcony",
                "value": 438
              },
              {
                "name": "Suite",
                "value": 658
              },
              {
                "code": "PortCharge",
                "value": 90
              },
              {
                "code": "CruiseTax",
                "value": 118.5
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "PF",
              "ML"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 116,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/116/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/116/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/116/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          116
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "10-Mar-2023",
        "arrivalDateTime": "13-Mar-2023",
        "cruisePackageDepartureDateTime": "10-Mar-2023",
        "cruisePackageArrivalDateTime": "13-Mar-2023",
        "voyageId": "FR3BH037",
        "stnExternalId": "1413939",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1269288,
        "code": "AD05W359",
        "name": "5 Night Western Caribbean Cruise",
        "startDateTime": "11-Mar-2023",
        "endDateTime": "16-Mar-2023",
        "itinerary": {
          "id": 310923,
          "duration": 5,
          "departure": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GLS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Galveston -  Texas|Puerto Costa Maya -  Mexico|Cozumel -  Mexico|Galveston -  Texas",
          "mapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/GLS_CST_CZM_GLS.jpg"
        },
        "uniqueItineraryId": "310923_71__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 500.5
              },
              {
                "name": "Outside",
                "value": 602.5
              },
              {
                "name": "Balcony",
                "value": 778
              },
              {
                "name": "Suite",
                "value": 1358
              },
              {
                "code": "PortCharge",
                "value": 135
              },
              {
                "code": "CruiseTax",
                "value": 116.61
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DISCOUNT",
            "NRD"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 71,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/71/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/71/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/71/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          71
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "11-Mar-2023",
        "arrivalDateTime": "16-Mar-2023",
        "cruisePackageDepartureDateTime": "11-Mar-2023",
        "cruisePackageArrivalDateTime": "16-Mar-2023",
        "voyageId": "AD05W359",
        "stnExternalId": "1413751",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ]
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
