# Cruise Search With Departure Port

**Path:** Cruise Search > Cruise Search With Departure Port

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
            "key": "departurePortCode",
            "values": ["MIA","LON"]
        }     
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 01 Feb 2023 09:38:06 GMT
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
    "total": 2062,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1228193,
        "code": "20230202SN04",
        "name": "Bahamas From Miami, Fl",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 309533,
          "duration": 4,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "MIAMI FL|PRINCESS CAYS THE BAHAMAS|NASSAU THE BAHAMAS|MIAMI FL",
          "mapPath": "/content/images/Itineraries/MIA_PRC_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_PRC_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "309533_14270__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 189
              },
              {
                "name": "Outside",
                "value": 229
              },
              {
                "name": "Balcony",
                "value": 359
              },
              {
                "name": "Suite",
                "value": 609
              },
              {
                "code": "PortCharge",
                "value": 99
              },
              {
                "code": "CruiseTax",
                "value": 138.86
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
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 14270,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/14270/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/14270/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/14270/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 1,
            "priority": 100,
            "logoPath": "/content/images/cruise/1/logo_190.png"
          }
        },
        "shipIds": [
          14270
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "20230202SN04",
        "stnExternalId": "1393851",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1329485,
        "code": "19244685",
        "name": "Bahamas - Short",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 363195,
          "duration": 3,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami Fl|Grand Bahama Island Bahamas|Great Stirrup Cay Bahamas|Miami Fl",
          "normalizedPortsOfCall": "MIA|GBI|GSCB|MIA"
        },
        "uniqueItineraryId": "363195_1179__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 248.95
              },
              {
                "name": "Outside",
                "value": 299
              },
              {
                "name": "Balcony",
                "value": 449.15
              },
              {
                "name": "Suite",
                "value": 1099.15
              },
              {
                "code": "PortCharge",
                "value": 110
              },
              {
                "code": "CruiseTax",
                "value": 189.92
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
          "id": 1179,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/6/1179/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/6/1179/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/6/1179/ship_520.jpg",
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
          1179
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "19244685",
        "stnExternalId": "1456983",
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
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ],
        "groupInfo": [
          {
            "isAgency": true
          }
        ]
      },
      {
        "id": 1269601,
        "code": "LB3BH045",
        "name": "3 Night Bahamas & Perfect Day Cruise",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 349022,
          "duration": 3,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fort Lauderdale -  Florida|Perfect Day Cococay -  Bahamas|Nassau -  Bahamas|Fort Lauderdale -  Florida",
          "normalizedPortsOfCall": "FLL|COCY|NAS|FLL",
          "mapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_CCY_NAS_MIA.jpg"
        },
        "uniqueItineraryId": "349022_1093__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 259
              },
              {
                "name": "Outside",
                "value": 319
              },
              {
                "name": "Balcony",
                "value": 359
              },
              {
                "name": "Suite",
                "value": 569
              },
              {
                "code": "PortCharge",
                "value": 90
              },
              {
                "code": "CruiseTax",
                "value": 107.85
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
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 1093,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/1093/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/1093/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/1093/ship_520.jpg",
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
          1093
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "LB3BH045",
        "stnExternalId": "1413714",
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
        "id": 1226527,
        "code": "20230203CQ03",
        "name": "Bahamas From Miami, Fl",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 309351,
          "duration": 3,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "MIAMI FL|NASSAU THE BAHAMAS|MIAMI FL",
          "mapPath": "/content/images/Itineraries/MIA_NAS_MIA.JPG",
          "fallbackMapPath": "/content/images/Itineraries/MIA_NAS_MIA.JPG"
        },
        "uniqueItineraryId": "309351_1__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 139
              },
              {
                "name": "Outside",
                "value": 179
              },
              {
                "name": "Balcony",
                "value": 251
              },
              {
                "name": "Suite",
                "value": 272
              },
              {
                "code": "PortCharge",
                "value": 89
              },
              {
                "code": "CruiseTax",
                "value": 128.86
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
              "fareDetailsPromoCode": "NR",
              "subFareDetailsPromoCodes": [
                "NR"
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
          "id": 1,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/1/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/1/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/1/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Armonia/en-gl/index.html",
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
          1
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "20230203CQ03",
        "stnExternalId": "1392707",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1290319,
        "code": "SC2302035NPP",
        "name": "Dominican Daze",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "08-Feb-2023",
        "itinerary": {
          "id": 333294,
          "duration": 5,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami|Puerto Plata|The Beach Club at Bimini|Miami",
          "mapPath": "/content/images/Itineraries/MIA_POP_BIM_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_POP_BIM_MIA.jpg"
        },
        "uniqueItineraryId": "333294_14477__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 904.75
              },
              {
                "name": "Outside",
                "value": 1020.25
              },
              {
                "name": "Balcony",
                "value": 1135.75
              },
              {
                "name": "Suite",
                "value": 1713.25
              },
              {
                "code": "CruiseTax",
                "value": 192
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 07:09:48"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "DINING",
            "FIT",
            "GRATSI",
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
              "fareDetailsPromoCode": "FIT",
              "subFareDetailsPromoCodes": [
                "FIT"
              ]
            },
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
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 9,
          "type": "Destination",
          "priority": 2
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 14477,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8807/14477/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8807/14477/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8807/14477/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8807,
            "priority": 100,
            "logoPath": "/content/images/cruise/8807/logo_190.png"
          }
        },
        "shipIds": [
          14477
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "08-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "08-Feb-2023",
        "voyageId": "SC2302035NPP",
        "stnExternalId": "1429063",
        "packageTourId": -1,
        "categoryTypes": [
          "Outside",
          "Inside",
          "Suite",
          "Balcony"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_9.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          9
        ]
      },
      {
        "id": 1327345,
        "code": "PR20230203SOUSOU",
        "name": "Northern Europe, 7 Nights",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 362899,
          "duration": 7,
          "departure": {
            "code": "SOU",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SOU",
            "type": "CruisePort"
          },
          "portsOfCalls": "Southampton (London)United Kingdom|HamburgGermany|Zeebrugge (Bruges) Belgium|Rotterdam (Amsterdam) Netherlands|Le Havre (Paris) France|Southampton (London)United Kingdom",
          "normalizedPortsOfCall": "SOU|HAM|ZBR1|RTM|LEH|SOU",
          "mapPath": "/content/images/Itineraries/SOU_HAM_ZBR_RTM_LEH_SOU.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SOU_HAM_ZBR_RTM_LEH_SOU.jpg"
        },
        "uniqueItineraryId": "362899_13510__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 419
              },
              {
                "name": "Outside",
                "value": 619
              },
              {
                "name": "Balcony",
                "value": 669
              },
              {
                "name": "Suite",
                "value": 939
              },
              {
                "code": "PortCharge",
                "value": 159
              },
              {
                "code": "CruiseTax",
                "value": 98
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 09:10:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 39,
          "type": "Destination",
          "priority": 54
        },
        "parentDestinationIds": [
          15
        ],
        "ship": {
          "id": 13510,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/13510/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/13510/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/13510/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Preziosa/en-gl/index.html",
          "hasVrForActivity": true,
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 982,
            "priority": 100,
            "logoPath": "/content/images/cruise/982/logo_190.png"
          }
        },
        "shipIds": [
          13510
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "10-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "voyageId": "PR20230203SOUSOU",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Inside",
          "Outside",
          "Balcony"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_39.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          39
        ]
      },
      {
        "id": 1259895,
        "code": "EG10D048",
        "name": "10 Night Ultimate Southern Caribbean",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "13-Feb-2023",
        "itinerary": {
          "id": 239009,
          "duration": 10,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fort Lauderdale -  Florida|Philipsburg -  St Maarten|Castries -  St Lucia|Bridgetown -  Barbados|St Johns -  Antigua|Basseterre -  St Kitts & Nevis|Fort Lauderdale -  Florida",
          "normalizedPortsOfCall": "FLL|SXM|UVF|BGI|ANU|BASS|FLL",
          "mapPath": "/content/images/Itineraries/MIA_PSB_SLU_BGI_ANU_BBR_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_PSB_SLU_BGI_ANU_BBR_MIA.jpg"
        },
        "uniqueItineraryId": "239009_13858__10",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1391.5
              },
              {
                "name": "Outside",
                "value": 1540.5
              },
              {
                "name": "Balcony",
                "value": 2307
              },
              {
                "name": "Suite",
                "value": 5460.5
              },
              {
                "code": "PortCharge",
                "value": 275
              },
              {
                "code": "CruiseTax",
                "value": 127.99
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "ML"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "ALWAYS",
            "BOGO",
            "DISCOUNT",
            "ELEVATE",
            "INDULGE",
            "NRD",
            "RETREAT"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "BOGO",
              "subFareDetailsPromoCodes": [
                "BOGO"
              ]
            },
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
              "fareDetailsPromoCode": "RETREAT",
              "subFareDetailsPromoCodes": [
                "RETREAT",
                "WiFi",
                "BEV",
                "GRATS",
                "SHOREX",
                "OBC",
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "ALWAYS",
              "subFareDetailsPromoCodes": [
                "ALWAYS",
                "WiFi",
                "BEV",
                "GRATS"
              ]
            },
            {
              "fareDetailsPromoCode": "ELEVATE",
              "subFareDetailsPromoCodes": [
                "ELEVATE",
                "WiFi",
                "BEV",
                "GRATS",
                "SHOREX"
              ]
            },
            {
              "fareDetailsPromoCode": "INDULGE",
              "subFareDetailsPromoCodes": [
                "INDULGE",
                "WiFi",
                "BEV",
                "GRATS",
                "SHOREX",
                "OBC"
              ]
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 13,
          "type": "Destination",
          "priority": 28
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 13858,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/2/13858/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/2/13858/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/2/13858/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 2,
            "priority": 100,
            "logoPath": "/content/images/cruise/2/logo_190.png"
          }
        },
        "shipIds": [
          13858
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "13-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "13-Feb-2023",
        "voyageId": "EG10D048",
        "stnExternalId": "1409559",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_13.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          13,
          9
        ],
        "groupInfo": [
          {
            "isHeadQuarter": true,
            "isAgency": true
          }
        ]
      },
      {
        "id": 1312438,
        "code": "DD2302045SI",
        "name": "",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 349436,
          "duration": 5,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "PORT OF MIAMI|GEORGE TOWN GRAND CAYMAN|CASTAWAY CAY|PORT OF MIAMI",
          "mapPath": "/content/images/Itineraries/MIA_GCM_CWC_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_GCM_CWC_MIA.jpg"
        },
        "uniqueItineraryId": "349436_13259__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1150
              },
              {
                "name": "Outside",
                "value": 1220
              },
              {
                "name": "Balcony",
                "value": 1375
              },
              {
                "name": "Suite",
                "value": 2835
              },
              {
                "code": "PortCharge",
                "value": 125
              },
              {
                "code": "CruiseTax",
                "value": 121.68
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "02-Jun-2022 12:29:12"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
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
          "id": 13259,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/4/13259/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/4/13259/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/4/13259/ship_520.jpg",
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
          13259
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "voyageId": "DD2302045SI",
        "stnExternalId": "1448717",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14
        ]
      },
      {
        "id": 1277446,
        "code": "J316",
        "name": "7-Day Eastern Caribbean",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 283766,
          "duration": 7,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fort Lauderdale Florida Us|Grand Turk Turks And Caicos|San Juan Puerto Rico|St Thomas USVI|Half Moon Cay Bahamas|Fort Lauderdale Florida Us",
          "normalizedPortsOfCall": "FLL|GDT|SJU|STT|HAFC|FLL",
          "mapPath": "/content/images/Itineraries/FLL_HAF_FLL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FLL_HAF_FLL.jpg"
        },
        "uniqueItineraryId": "283766_13993__7",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 10,
          "type": "Destination",
          "priority": 24
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 13993,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/13993/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/13993/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/13993/ship_520.jpg",
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
          13993
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "J316",
        "stnExternalId": "1419617",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_10.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          10,
          9
        ]
      },
      {
        "id": 1276663,
        "code": "Y306",
        "name": "Eastern Caribbean With Puerto Rico",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 308601,
          "duration": 7,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Ft Lauderdale Florida|Princess Cays Bahamas|San Juan Puerto Rico|Amber Cove Dominican Republic|Grand Turk Turks & Caicos|Ft Lauderdale Florida",
          "mapPath": "/content/images/Itineraries/MIA_PRC_SJU_AMB_GDT_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_PRC_SJU_AMB_GDT_MIA.jpg"
        },
        "uniqueItineraryId": "308601_14053__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 668
              },
              {
                "name": "Outside",
                "value": 1049
              },
              {
                "name": "Balcony",
                "value": 988
              },
              {
                "name": "Suite",
                "value": 1298
              },
              {
                "code": "PortCharge",
                "value": 189
              },
              {
                "code": "CruiseTax",
                "value": 185
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 9,
          "type": "Destination",
          "priority": 2
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 14053,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14053/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14053/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14053/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 7,
            "priority": 100,
            "logoPath": "/content/images/cruise/7/logo_190.png"
          }
        },
        "shipIds": [
          14053
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "Y306",
        "stnExternalId": "1422198",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_9.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          9
        ]
      },
      {
        "id": 1270863,
        "code": "SY07E307",
        "name": "7 Night Eastern Caribbean & Perfect Day",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 311479,
          "duration": 7,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Miami -  Florida|Philipsburg -  St Maarten|Charlotte Amalie -  St Thomas|Perfect Day Cococay -  Bahamas|Miami -  Florida",
          "normalizedPortsOfCall": "MIA|SXM|SPB|COCY|MIA",
          "mapPath": "/content/images/Itineraries/MIA_PSB_SPB_CCY_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_PSB_SPB_CCY_MIA.jpg"
        },
        "uniqueItineraryId": "311479_13825__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 750
              },
              {
                "name": "Outside",
                "value": 850
              },
              {
                "name": "Balcony",
                "value": 883
              },
              {
                "name": "Suite",
                "value": 1923
              },
              {
                "code": "PortCharge",
                "value": 225
              },
              {
                "code": "CruiseTax",
                "value": 142.82
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
          "id": 10,
          "type": "Destination",
          "priority": 24
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 13825,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/13825/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/13825/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/13825/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://my.matterport.com/show/?m=uSSjUz8gXAG",
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          13825
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "SY07E307",
        "stnExternalId": "1416309",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Suite",
          "Inside",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_10.jpg",
        "maxOccupancy": 14,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          10,
          9
        ]
      },
      {
        "id": 1259856,
        "code": "AX07W462",
        "name": "7 Night Key West, Belize & Grand Cayman",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 298161,
          "duration": 7,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fort Lauderdale -  Florida|Key West -  Florida|Belize City -  Belize|Cozumel -  Mexico|George Town -  Grand Cayman|Fort Lauderdale -  Florida",
          "normalizedPortsOfCall": "FLL|EYW|BZE|CZM|GCM|FLL",
          "mapPath": "/content/images/Itineraries/MIA_EYW_BZE_CZM_GCM_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_EYW_BZE_CZM_GCM_MIA.jpg"
        },
        "uniqueItineraryId": "298161_14393__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 873.5
              },
              {
                "name": "Outside",
                "value": 951
              },
              {
                "name": "Balcony",
                "value": 1410.5
              },
              {
                "name": "Suite",
                "value": 3115.5
              },
              {
                "code": "PortCharge",
                "value": 225
              },
              {
                "code": "CruiseTax",
                "value": 164.09
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:30:15",
            "fareTypes": [
              "ML"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "ALWAYS",
            "BOGO",
            "DISCOUNT",
            "ELEVATE",
            "INDULGE",
            "NRD",
            "RETREAT"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "ALWAYS",
              "subFareDetailsPromoCodes": [
                "ALWAYS",
                "WiFi",
                "BEV",
                "GRATS"
              ]
            },
            {
              "fareDetailsPromoCode": "INDULGE",
              "subFareDetailsPromoCodes": [
                "INDULGE",
                "WiFi",
                "BEV",
                "GRATS",
                "SHOREX",
                "OBC"
              ]
            },
            {
              "fareDetailsPromoCode": "BOGO",
              "subFareDetailsPromoCodes": [
                "BOGO"
              ]
            },
            {
              "fareDetailsPromoCode": "NRD",
              "subFareDetailsPromoCodes": [
                "NRD"
              ]
            },
            {
              "fareDetailsPromoCode": "RETREAT",
              "subFareDetailsPromoCodes": [
                "RETREAT",
                "WiFi",
                "BEV",
                "GRATS",
                "SHOREX",
                "OBC",
                "Dining"
              ]
            },
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
              ]
            },
            {
              "fareDetailsPromoCode": "ELEVATE",
              "subFareDetailsPromoCodes": [
                "ELEVATE",
                "WiFi",
                "BEV",
                "GRATS",
                "SHOREX"
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
          "id": 14393,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/2/14393/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/2/14393/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/2/14393/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 2,
            "priority": 100,
            "logoPath": "/content/images/cruise/2/logo_190.png"
          }
        },
        "shipIds": [
          14393
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "AX07W462",
        "stnExternalId": "1409515",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_14.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14,
          9
        ]
      },
      {
        "id": 1222191,
        "code": "20230204HZ08",
        "name": "Southern Caribbean From Miami, Fl",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "12-Feb-2023",
        "itinerary": {
          "id": 346169,
          "duration": 8,
          "departure": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "MIAMI FL|ARUBA|BONAIRE|LA ROMANA DOMINICAN REPUBLIC|AMBER COVE DOMINICAN REPUBLIC|MIAMI FL",
          "mapPath": "/content/images/Itineraries/MIA_AUA_BON_LAR_AMB_MIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MIA_AUA_BON_LAR_AMB_MIA.jpg"
        },
        "uniqueItineraryId": "346169_13797__8",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 759
              },
              {
                "name": "Balcony",
                "value": 1099
              },
              {
                "name": "Suite",
                "value": 1646
              },
              {
                "code": "PortCharge",
                "value": 159
              },
              {
                "code": "CruiseTax",
                "value": 156.86
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
          "id": 13,
          "type": "Destination",
          "priority": 28
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 13797,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/13797/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/13797/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/13797/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 1,
            "priority": 100,
            "logoPath": "/content/images/cruise/1/logo_190.png"
          }
        },
        "shipIds": [
          13797
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "12-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "12-Feb-2023",
        "voyageId": "20230204HZ08",
        "stnExternalId": "1390897",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_13.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 8,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          13
        ]
      },
      {
        "id": 1277494,
        "code": "Y315",
        "name": "11-Day Southern Caribbean Wayfarer",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "15-Feb-2023",
        "itinerary": {
          "id": 326066,
          "duration": 11,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fort Lauderdale Florida Us|Philipsburg Sint Maarten|Castries Saint Lucia|Bridgetown Barbados|Fort-De-France Martinique|Basseterre St Kitts And Nevis|St Thomas USVI|Half Moon Cay Bahamas|Fort Lauderdale Florida Us",
          "normalizedPortsOfCall": "FLL|PSB|SLU|BGI|FDF|BASS|STT|HAFC|FLL",
          "mapPath": "/content/images/Itineraries/FLL_PSB_SLU_BGI_FDF_BBR_SPB_HAF_FLL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FLL_PSB_SLU_BGI_FDF_BBR_SPB_HAF_FLL.jpg"
        },
        "uniqueItineraryId": "326066_14723__11",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1559
              },
              {
                "name": "Outside",
                "value": 1859
              },
              {
                "name": "Balcony",
                "value": 2059
              },
              {
                "name": "Suite",
                "value": 3059
              },
              {
                "code": "PortCharge",
                "value": 295
              },
              {
                "code": "CruiseTax",
                "value": 190
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:54:37"
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
          "id": 13,
          "type": "Destination",
          "priority": 28
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 14723,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/14723/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/14723/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/14723/ship_520.jpg",
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
          14723
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "15-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "15-Feb-2023",
        "voyageId": "Y315",
        "stnExternalId": "1419572",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_13.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 11,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          13,
          9
        ]
      },
      {
        "id": 1290705,
        "code": "800965800984|MANOR2223WI",
        "name": "Fjords Expedition Cruise From Dover",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "18-Feb-2023",
        "itinerary": {
          "id": 348069,
          "duration": 14,
          "departure": {
            "code": "QQD",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "QQD",
            "type": "CruisePort"
          },
          "portsOfCalls": "Dover|Harwich|Harwich|Nordfjord|Reine|Alta|Alta|Troms|Narvik|Bergen|Egersund|Dover"
        },
        "uniqueItineraryId": "348069_14713__14_manor2223wi",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 6708
              },
              {
                "name": "Outside",
                "value": 7245
              },
              {
                "name": "Suite",
                "value": 14087
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 10:44:56"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 39,
          "type": "Destination",
          "priority": 54
        },
        "parentDestinationIds": [
          15
        ],
        "ship": {
          "id": 14713,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/14713/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/14713/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/14713/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 9191,
            "priority": 100,
            "logoPath": "/content/images/cruise/9191/logo_190.png"
          }
        },
        "shipIds": [
          14713
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "18-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "18-Feb-2023",
        "cruiseTourCode": "MANOR2223WI",
        "voyageId": "800965800984",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_39.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          39
        ]
      },
      {
        "id": 1290563,
        "code": "800965800984|MANOR2223WI",
        "name": "Northern Lights Expedition Cruise From Dover",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "18-Feb-2023",
        "itinerary": {
          "id": 348069,
          "duration": 14,
          "departure": {
            "code": "QQD",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "QQD",
            "type": "CruisePort"
          },
          "portsOfCalls": "Dover|Harwich|Harwich|Nordfjord|Reine|Alta|Alta|Troms|Narvik|Bergen|Egersund|Dover"
        },
        "uniqueItineraryId": "348069_14713__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 6708
              },
              {
                "name": "Outside",
                "value": 7245
              },
              {
                "name": "Suite",
                "value": 14087
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 09:55:10"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 39,
          "type": "Destination",
          "priority": 54
        },
        "parentDestinationIds": [
          15
        ],
        "ship": {
          "id": 14713,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/14713/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/14713/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/14713/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 9191,
            "priority": 100,
            "logoPath": "/content/images/cruise/9191/logo_190.png"
          }
        },
        "shipIds": [
          14713
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "18-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "18-Feb-2023",
        "voyageId": "800965800984",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside",
          "Inside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_39.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          39
        ]
      },
      {
        "id": 1282192,
        "code": "Y306A",
        "name": "Caribbean East/West Adventurer",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "18-Feb-2023",
        "itinerary": {
          "id": 330814,
          "duration": 14,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Ft Lauderdale Florida|Princess Cays Bahamas|San Juan Puerto Rico|Amber Cove Dominican Republic|Grand Turk Turks & Caicos|Ft Lauderdale Florida|Cozumel Mexico|Roatan Honduras|Belize City Belize|Costa Maya (Mahahual) Mexico|Ft Lauderdale Florida"
        },
        "uniqueItineraryId": "330814_14053__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1338
              },
              {
                "name": "Outside",
                "value": 2070
              },
              {
                "name": "Balcony",
                "value": 1950
              },
              {
                "name": "Suite",
                "value": 2598
              },
              {
                "code": "PortCharge",
                "value": 378
              },
              {
                "code": "CruiseTax",
                "value": 305
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 9,
          "type": "Destination",
          "priority": 2
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 14053,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14053/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14053/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14053/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 7,
            "priority": 100,
            "logoPath": "/content/images/cruise/7/logo_190.png"
          }
        },
        "shipIds": [
          14053
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "18-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "18-Feb-2023",
        "voyageId": "Y306A",
        "stnExternalId": "1427647",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_9.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          9
        ]
      },
      {
        "id": 1277447,
        "code": "J316A",
        "name": "14-Day Eastern / Tropical Caribbean",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "18-Feb-2023",
        "itinerary": {
          "id": 311700,
          "duration": 14,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fort Lauderdale Florida Us|Grand Turk Turks And Caicos|San Juan Puerto Rico|St Thomas USVI|Half Moon Cay Bahamas|Fort Lauderdale Florida Us|Key West Florida Us|Amber Cove Dominican Republic|Grand Turk Turks And Caicos|Half Moon Cay Bahamas|Fort Lauderdale Florida Us",
          "normalizedPortsOfCall": "FLL|GDT|SJU|STT|HAFC|FLL|EYW|AMBE|GDT|HAFC|FLL",
          "mapPath": "/content/images/Itineraries/FLL_GDT_SJU_STT_HAF_FLL_EYW_AMB_GDT_HAF_FLL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FLL_GDT_SJU_STT_HAF_FLL_EYW_AMB_GDT_HAF_FLL.jpg"
        },
        "uniqueItineraryId": "311700_13993__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1559
              },
              {
                "name": "Outside",
                "value": 2129
              },
              {
                "name": "Balcony",
                "value": 2319
              },
              {
                "name": "Suite",
                "value": 3269
              },
              {
                "code": "PortCharge",
                "value": 380
              },
              {
                "code": "CruiseTax",
                "value": 315
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:49:01"
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
          "id": 9,
          "type": "Destination",
          "priority": 2
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 13993,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/13993/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/13993/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/13993/ship_520.jpg",
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
          13993
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "18-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "18-Feb-2023",
        "voyageId": "J316A",
        "stnExternalId": "1419618",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_9.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          9
        ]
      },
      {
        "id": 1277495,
        "code": "Y315A",
        "name": "21-Day Southern Caribbean Wayfarer / Seafarer",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "25-Feb-2023",
        "itinerary": {
          "id": 326073,
          "duration": 21,
          "departure": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "FLL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fort Lauderdale Florida Us|Philipsburg Sint Maarten|Castries Saint Lucia|Bridgetown Barbados|Fort-De-France Martinique|Basseterre St Kitts And Nevis|St Thomas USVI|Half Moon Cay Bahamas|Fort Lauderdale Florida Us|Half Moon Cay Bahamas|Grand Turk Turks And Caicos|Amber Cove Dominican Republic|Kralendijk Bonaire|Willemstad Curacao|Oranjestad Aruba|Fort Lauderdale Florida Us",
          "normalizedPortsOfCall": "FLL|PSB|SLU|BGI|FDF|BASS|STT|HAFC|FLL|HAFC|GDT|AMBE|KRLD|CUR|ORAN|FLL",
          "mapPath": "/content/images/Itineraries/FLL_PSB_SLU_BGI_FDF_BBR_SPB_HAF_FLL_HAF_GDT_AMB_KRA_WIL_ORA_FLL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FLL_PSB_SLU_BGI_FDF_BBR_SPB_HAF_FLL_HAF_GDT_AMB_KRA_WIL_ORA_FLL.jpg"
        },
        "uniqueItineraryId": "326073_14723__21",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2599
              },
              {
                "name": "Outside",
                "value": 3169
              },
              {
                "name": "Balcony",
                "value": 3549
              },
              {
                "name": "Suite",
                "value": 5549
              },
              {
                "code": "PortCharge",
                "value": 565
              },
              {
                "code": "CruiseTax",
                "value": 340
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:54:37"
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
          "id": 13,
          "type": "Destination",
          "priority": 28
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 14723,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/14723/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/14723/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/14723/ship_520.jpg",
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
          14723
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "25-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "25-Feb-2023",
        "voyageId": "Y315A",
        "stnExternalId": "1419573",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_13.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 21,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          13,
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
