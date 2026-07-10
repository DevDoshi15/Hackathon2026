# Cruise Search With Including All Packages

**Path:** Cruise Search > Cruise Search With Including All Packages

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
// includeAllPackages:true. This will ignore the active/status/validity check and returns all sailings/packages even if they are inactive, and returns all custom packages even if they're not published or not valid for current date.
{
    "filters": [
        {
            "key": "includeAllPackages",
            "value": true
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 01 Feb 2023 09:43:51 GMT
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
    "total": 26899,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1320011,
        "code": "858199858220|SCGAL2324EMACCH",
        "name": "Galápagos Islands Expedition – In Darwin’S Footsteps",
        "startDateTime": "29-Jan-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 363750,
          "duration": 12,
          "departure": {
            "code": "ZRH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ZRH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Zurich|Zurich|Zurich|Zurich|Zurich|Capitania Seymour Baltra|Mosquera|Mosquera|Puerto Baquerizo Moreno|Punta Pitt San Cristobal|Punta Pitt San Cristobal|Santa Fe|Plaza Sur|Plaza Sur|Puerto Ayora|Puerto Ayora|Punta Suarez|Bahia Gardner|Islote Eden|Seymour Norte|Capitania Seymour Baltra|Zurich",
          "mapPath": "/content/images/Itineraries/SMRN_MSQR_PBMR_PNPT_STFI_PLZS_PT1_SARZ_GRDN_EEDN_SMRN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SMRN_MSQR_PBMR_PNPT_STFI_PLZS_PT1_SARZ_GRDN_EEDN_SMRN.jpg"
        },
        "uniqueItineraryId": "363750_15108__12_scgal2324emacch",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 48,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 15108,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/15108/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_520.jpg",
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
          15108
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "29-Jan-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "cruiseTourCode": "SCGAL2324EMACCH",
        "voyageId": "858199858220",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_48.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 12,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          48
        ]
      },
      {
        "id": 1320008,
        "code": "858199858220|SCGAL2324EMACCH",
        "name": "Galápagos Islands Expedition – In Darwin’S Footsteps",
        "startDateTime": "29-Jan-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 363747,
          "duration": 12,
          "departure": {
            "code": "AMS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "AMS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Amsterdam|Amsterdam|Amsterdam|Amsterdam|Amsterdam|Capitania Seymour Baltra|Mosquera|Mosquera|Puerto Baquerizo Moreno|Punta Pitt San Cristobal|Punta Pitt San Cristobal|Santa Fe|Plaza Sur|Plaza Sur|Puerto Ayora|Puerto Ayora|Punta Suarez|Bahia Gardner|Islote Eden|Seymour Norte|Capitania Seymour Baltra|Amsterdam",
          "mapPath": "/content/images/Itineraries/SMRN_MSQR_PBMR_PNPT_STFI_PLZS_PT1_SARZ_GRDN_EEDN_SMRN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SMRN_MSQR_PBMR_PNPT_STFI_PLZS_PT1_SARZ_GRDN_EEDN_SMRN.jpg"
        },
        "uniqueItineraryId": "363747_15108__12_scgal2324emacem",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 48,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 15108,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/15108/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_520.jpg",
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
          15108
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "29-Jan-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "cruiseTourCode": "SCGAL2324EMACEM",
        "voyageId": "858199858220",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_48.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 12,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          48
        ]
      },
      {
        "id": 1320007,
        "code": "858199858220|SCGAL2324EMACCH",
        "name": "Galápagos Islands Expedition – In Darwin’S Footsteps",
        "startDateTime": "29-Jan-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 363746,
          "duration": 12,
          "departure": {
            "code": "LHR",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "LHR",
            "type": "CruisePort"
          },
          "portsOfCalls": "London Heathrow|London Heathrow|London Heathrow|London Heathrow|London Heathrow|Capitania Seymour Baltra|Mosquera|Mosquera|Puerto Baquerizo Moreno|Punta Pitt San Cristobal|Punta Pitt San Cristobal|Santa Fe|Plaza Sur|Plaza Sur|Puerto Ayora|Puerto Ayora|Punta Suarez|Bahia Gardner|Islote Eden|Seymour Norte|Capitania Seymour Baltra|London Heathrow"
        },
        "uniqueItineraryId": "363746_15108__12_scgal2324emacuk",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 48,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 15108,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/15108/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_520.jpg",
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
          15108
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "29-Jan-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "cruiseTourCode": "SCGAL2324EMACUK",
        "voyageId": "858199858220",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_48.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 12,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          48
        ]
      },
      {
        "id": 1275242,
        "code": "ANT230202T",
        "name": "Pharaohs & Pyramids",
        "startDateTime": "30-Jan-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 276726,
          "duration": 11,
          "departure": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "portsOfCalls": "Pharaohs &amp Pyramids|Sheraton Cairo Hotel &amp Casino|Sheraton Cairo Hotel &amp Casino|Sheraton Cairo Hotel &amp Casino|Luxor|Luxor|Qena|Esna|Aswan|Aswan|Kom Ombo|Edfu|Luxor|Luxor|InterContinental Cairo Citystars",
          "mapPath": "/content/images/Itineraries/CAI_LXR_QENA_ESN_ASW_OMBO_EDFU_LXR_CAI.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CAI_LXR_QENA_ESN_ASW_OMBO_EDFU_LXR_CAI.jpg"
        },
        "uniqueItineraryId": "276726_14155__11_ant230202t",
        "prices": [
          {
            "items": [
              {
                "name": "Balcony",
                "value": 6999
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "03-Jun-2022 22:04:30"
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
          "id": 2,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          2
        ],
        "ship": {
          "id": 14155,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8112/14155/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8112/14155/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8112/14155/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8112,
            "priority": 100,
            "logoPath": "/content/images/cruise/8112/logo_190.png"
          }
        },
        "shipIds": [
          14155
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "30-Jan-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "cruiseTourCode": "ANT230202T",
        "voyageId": "ANT230202T",
        "stnExternalId": "1426169",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_2.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 11,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          2
        ]
      },
      {
        "id": 1320010,
        "code": "858199858220|SCGAL2324EMACCH",
        "name": "Galápagos Islands Expedition – In Darwin’S Footsteps",
        "startDateTime": "31-Jan-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 363749,
          "duration": 10,
          "departure": {
            "code": "ZRH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ZRH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Zurich|Zurich|Zurich|Capitania Seymour Baltra|Mosquera|Mosquera|Puerto Baquerizo Moreno|Punta Pitt San Cristobal|Punta Pitt San Cristobal|Santa Fe|Plaza Sur|Plaza Sur|Puerto Ayora|Puerto Ayora|Punta Suarez|Bahia Gardner|Islote Eden|Seymour Norte|Capitania Seymour Baltra|Zurich"
        },
        "uniqueItineraryId": "363749_15108__10_scgal2324euioch",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 48,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 15108,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/15108/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_520.jpg",
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
          15108
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "31-Jan-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "cruiseTourCode": "SCGAL2324EUIOCH",
        "voyageId": "858199858220",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_48.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          48
        ]
      },
      {
        "id": 1320009,
        "code": "858199858220|SCGAL2324EMACCH",
        "name": "Galápagos Islands Expedition – In Darwin’S Footsteps",
        "startDateTime": "31-Jan-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 363748,
          "duration": 10,
          "departure": {
            "code": "AMS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "AMS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Amsterdam|Amsterdam|Amsterdam|Capitania Seymour Baltra|Mosquera|Mosquera|Puerto Baquerizo Moreno|Punta Pitt San Cristobal|Punta Pitt San Cristobal|Santa Fe|Plaza Sur|Plaza Sur|Puerto Ayora|Puerto Ayora|Punta Suarez|Bahia Gardner|Islote Eden|Seymour Norte|Capitania Seymour Baltra|Amsterdam"
        },
        "uniqueItineraryId": "363748_15108__10_scgal2324euioem",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 48,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 15108,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/15108/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_520.jpg",
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
          15108
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "31-Jan-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "cruiseTourCode": "SCGAL2324EUIOEM",
        "voyageId": "858199858220",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_48.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          48
        ]
      },
      {
        "id": 1320006,
        "code": "858199858220|SCGAL2324EMACCH",
        "name": "Galápagos Islands Expedition – In Darwin’S Footsteps",
        "startDateTime": "31-Jan-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 363745,
          "duration": 10,
          "departure": {
            "code": "LHR",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "LHR",
            "type": "CruisePort"
          },
          "portsOfCalls": "London Heathrow|London Heathrow|London Heathrow|Capitania Seymour Baltra|Mosquera|Mosquera|Puerto Baquerizo Moreno|Punta Pitt San Cristobal|Punta Pitt San Cristobal|Santa Fe|Plaza Sur|Plaza Sur|Puerto Ayora|Puerto Ayora|Punta Suarez|Bahia Gardner|Islote Eden|Seymour Norte|Capitania Seymour Baltra|London Heathrow"
        },
        "uniqueItineraryId": "363745_15108__10_scgal2324euiouk",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 48,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 15108,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/15108/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_520.jpg",
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
          15108
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "31-Jan-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "cruiseTourCode": "SCGAL2324EUIOUK",
        "voyageId": "858199858220",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_48.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          48
        ]
      },
      {
        "id": 1319891,
        "code": "858199858220|SCGAL2324EMACCH",
        "name": "Galápagos Islands Expedition – In Darwin’S Footsteps",
        "startDateTime": "01-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 363639,
          "duration": 8,
          "departure": {
            "code": "UIO",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GYE",
            "type": "CruisePort"
          },
          "portsOfCalls": "Quito|Quito|Capitania Seymour Baltra|Mosquera|Mosquera|Puerto Baquerizo Moreno|Punta Pitt San Cristobal|Punta Pitt San Cristobal|Santa Fe|Plaza Sur|Plaza Sur|Puerto Ayora|Puerto Ayora|Punta Suarez|Bahia Gardner|Islote Eden|Seymour Norte|Capitania Seymour Baltra",
          "mapPath": "/content/images/Itineraries/UIO_SMRN_MSQR_MRNO_PNPT_STFI_PLZS_PT1_SARZ_GRDN_EEDN_SMRN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/UIO_SMRN_MSQR_MRNO_PNPT_STFI_PLZS_PT1_SARZ_GRDN_EEDN_SMRN.jpg"
        },
        "uniqueItineraryId": "363639_15108__8_scgal2324e",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 9062
              },
              {
                "name": "Suite",
                "value": 12306
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 10:44:51"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 48,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 15108,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/15108/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/15108/ship_520.jpg",
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
          15108
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "01-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "cruiseTourCode": "SCGAL2324E",
        "voyageId": "858199858220",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_48.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 8,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          48
        ]
      },
      {
        "id": 1230126,
        "code": "OSR230204T",
        "name": "Pharaohs & Pyramids",
        "startDateTime": "01-Feb-2023",
        "endDateTime": "12-Feb-2023",
        "itinerary": {
          "id": 276726,
          "duration": 11,
          "departure": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "portsOfCalls": "Pharaohs &amp Pyramids|Sheraton Cairo Hotel &amp Casino|Sheraton Cairo Hotel &amp Casino|Sheraton Cairo Hotel &amp Casino|Luxor|Luxor|Qena|Esna|Aswan|Aswan|Kom Ombo|Edfu|Luxor|Luxor|InterContinental Cairo Citystars",
          "mapPath": "/content/images/Itineraries/CAI_LXR_QENA_ESN_ASW_OMBO_EDFU_LXR_CAI.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CAI_LXR_QENA_ESN_ASW_OMBO_EDFU_LXR_CAI.jpg"
        },
        "uniqueItineraryId": "276726_14512__11_osr230204t",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 6999
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "03-Jun-2022 22:04:30"
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
          "id": 2,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          2
        ],
        "ship": {
          "id": 14512,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8112/14512/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8112/14512/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8112/14512/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8112,
            "priority": 100,
            "logoPath": "/content/images/cruise/8112/logo_190.png"
          }
        },
        "shipIds": [
          14512
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "01-Feb-2023",
        "cruisePackageArrivalDateTime": "12-Feb-2023",
        "cruiseTourCode": "OSR230204T",
        "voyageId": "OSR230204T",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_2.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 11,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          2
        ]
      },
      {
        "id": 1271948,
        "code": "Q306",
        "name": "Australia Short Break",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "04-Feb-2023",
        "itinerary": {
          "id": 355888,
          "duration": 2,
          "departure": {
            "code": "SYD",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MEL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Sydney Nsw Australia|Melbourne Vic Australia",
          "normalizedPortsOfCall": "SYD|MEL",
          "mapPath": "/content/images/Itineraries/SYD_MEL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SYD_MEL.jpg"
        },
        "uniqueItineraryId": "355888_13231__2",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 449
              },
              {
                "name": "Outside",
                "value": 499
              },
              {
                "name": "Balcony",
                "value": 549
              },
              {
                "name": "Suite",
                "value": 899
              },
              {
                "code": "PortCharge",
                "value": 70
              },
              {
                "code": "CruiseTax",
                "value": 74.44
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:00:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 29,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          29
        ],
        "ship": {
          "id": 13231,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/12/13231/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/12/13231/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/12/13231/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 12,
            "priority": 100,
            "logoPath": "/content/images/cruise/12/logo_190.png"
          }
        },
        "shipIds": [
          13231
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "04-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "04-Feb-2023",
        "voyageId": "Q306",
        "stnExternalId": "1417282",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony",
          "Inside",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_29.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 2,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          29
        ]
      },
      {
        "id": 1323250,
        "code": "MR20230202CPVCPV",
        "name": "Caribbean And Antilles, 3 Nights",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "05-Feb-2023",
        "itinerary": {
          "id": 361388,
          "duration": 3,
          "departure": {
            "code": "XPC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "XPC",
            "type": "CruisePort"
          },
          "portsOfCalls": "Port Canaveral (Orlando) United States|Ocean Cay Msc Marine ReserveBahamas|Ocean Cay Msc Marine ReserveBahamas|Port Canaveral (Orlando) United States",
          "normalizedPortsOfCall": "XPC|OCAY|XPC",
          "mapPath": "/content/images/Itineraries/XPC_OCC_XPC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/XPC_OCC_XPC.jpg"
        },
        "uniqueItineraryId": "361388_13725__3",
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
                "value": 279
              },
              {
                "name": "Suite",
                "value": 679
              },
              {
                "code": "PortCharge",
                "value": 60
              },
              {
                "code": "CruiseTax",
                "value": 117.12
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
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 13725,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/13725/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/13725/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/13725/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": " https://virtual-tours.msccruises.com/MSC-Meraviglia/en-gl/index.html",
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
          13725
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "05-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "05-Feb-2023",
        "voyageId": "MR20230202CPVCPV",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_7.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1234045,
        "code": "20230202SP03",
        "name": "Getaway From Brisbane, Australia",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "05-Feb-2023",
        "itinerary": {
          "id": 298598,
          "duration": 3,
          "departure": {
            "code": "BNE",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BNE",
            "type": "CruisePort"
          },
          "portsOfCalls": "BRISBANE AUSTRALIA|BRISBANE AUSTRALIA",
          "mapPath": "/content/images/Itineraries/BNE_BNE.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BNE_BNE.jpg"
        },
        "uniqueItineraryId": "298598_6__3",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 29,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          29
        ],
        "ship": {
          "id": 6,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/6/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/6/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/6/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Sinfonia/en-gl/index.html",
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
          6
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "05-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "05-Feb-2023",
        "voyageId": "20230202SP03",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_29.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          29
        ]
      },
      {
        "id": 1328605,
        "code": "DW2302024SD",
        "name": "",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 349420,
          "duration": 4,
          "departure": {
            "code": "SAN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SAN",
            "type": "CruisePort"
          },
          "portsOfCalls": "SAN DIEGO|CATALINA|ENSENADA|SAN DIEGO",
          "mapPath": "/content/images/Itineraries/SAN_AVX_ESE_SAN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SAN_AVX_ESE_SAN.jpg"
        },
        "uniqueItineraryId": "349420_33__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 576
              },
              {
                "name": "Outside",
                "value": 632
              },
              {
                "name": "Balcony",
                "value": 904
              },
              {
                "name": "Suite",
                "value": 1744
              },
              {
                "code": "PortCharge",
                "value": 100
              },
              {
                "code": "CruiseTax",
                "value": 121.51
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 01:06:56"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 56,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          42
        ],
        "ship": {
          "id": 33,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/4/33/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/4/33/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/4/33/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Bellissima/en-gl/index.html",
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 4,
            "priority": 100,
            "logoPath": "/content/images/cruise/4/logo_190.png"
          }
        },
        "shipIds": [
          33
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "DW2302024SD",
        "stnExternalId": "1462655",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_56.jpg",
        "maxOccupancy": 6,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          56
        ]
      },
      {
        "id": 1308065,
        "code": "SC04I741",
        "name": "4 Night Penang & Phuket Cruise",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 311513,
          "duration": 4,
          "departure": {
            "code": "SIN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SIN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Singapore -  Singapore|Penang -  Malaysia|Phuket -  Thailand|Singapore -  Singapore",
          "normalizedPortsOfCall": "SIN|PEN|HKT|SIN",
          "mapPath": "/content/images/Itineraries/SIN_PEN_HKT_SIN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SIN_PEN_HKT_SIN.jpg"
        },
        "uniqueItineraryId": "311513_14118__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 373
              },
              {
                "name": "Outside",
                "value": 438
              },
              {
                "name": "Balcony",
                "value": 579
              },
              {
                "name": "Suite",
                "value": 852
              },
              {
                "code": "PortCharge",
                "value": 100
              },
              {
                "code": "CruiseTax",
                "value": 57.81
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
          "id": 19,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          19
        ],
        "ship": {
          "id": 14118,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/14118/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/14118/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/14118/ship_520.jpg",
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
          14118
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "SC04I741",
        "stnExternalId": "1453328",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Balcony",
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_19.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          19
        ]
      },
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
        "id": 1226528,
        "code": "20230202EC04",
        "name": "Bahamas From Jacksonville, Fl",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 309394,
          "duration": 4,
          "departure": {
            "code": "JAX",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "JAX",
            "type": "CruisePort"
          },
          "portsOfCalls": "JACKSONVILLE FL|FREEPORT THE BAHAMAS|NASSAU THE BAHAMAS|JACKSONVILLE FL",
          "mapPath": "/content/images/Itineraries/JAX_FEP_JAX_838854.jpg",
          "fallbackMapPath": "/content/images/Itineraries/JAX_FEP_JAX_838854.jpg"
        },
        "uniqueItineraryId": "309394_10__4",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 7,
          "type": "Destination",
          "priority": 3
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 10,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/10/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/10/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/10/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 1,
            "priority": 100,
            "logoPath": "/content/images/cruise/1/logo_190.png"
          }
        },
        "shipIds": [
          10
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "20230202EC04",
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
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1222298,
        "code": "20230202PA04",
        "name": "Western Caribbean From Tampa, Fl",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 309395,
          "duration": 4,
          "departure": {
            "code": "TPA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "TPA",
            "type": "CruisePort"
          },
          "portsOfCalls": "TAMPA FL|COZUMEL MEXICO|TAMPA FL",
          "mapPath": "/content/images/Itineraries/TPA_CZM_TPA.JPG",
          "fallbackMapPath": "/content/images/Itineraries/TPA_CZM_TPA.JPG"
        },
        "uniqueItineraryId": "309395_17__4",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 207
              },
              {
                "name": "Outside",
                "value": 247
              },
              {
                "name": "Balcony",
                "value": 418
              },
              {
                "name": "Suite",
                "value": 544
              },
              {
                "code": "PortCharge",
                "value": 99
              },
              {
                "code": "CruiseTax",
                "value": 90.86
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
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 17,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/17/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/17/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/17/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Magnifica/en-gl/index.html",
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
          17
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "20230202PA04",
        "stnExternalId": "1390954",
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
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14
        ]
      },
      {
        "id": 1222169,
        "code": "20230202PA04",
        "name": "Western Caribbean From Tampa, Fl",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 309395,
          "duration": 4,
          "departure": {
            "code": "TPA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "TPA",
            "type": "CruisePort"
          },
          "portsOfCalls": "TAMPA FL|COZUMEL MEXICO|TAMPA FL",
          "mapPath": "/content/images/Itineraries/TPA_CZM_TPA.JPG",
          "fallbackMapPath": "/content/images/Itineraries/TPA_CZM_TPA.JPG"
        },
        "uniqueItineraryId": "309395_17__4",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 14,
          "type": "Destination",
          "priority": 26
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 17,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/17/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/17/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/17/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Magnifica/en-gl/index.html",
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
          17
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "20230202PA04",
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
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 4,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          14
        ]
      },
      {
        "id": 1307653,
        "code": "854432854495",
        "name": "The Voyage South",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "07-Feb-2023",
        "itinerary": {
          "id": 342640,
          "duration": 5,
          "departure": {
            "code": "KKN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BGO",
            "type": "CruisePort"
          },
          "portsOfCalls": "Kirkenes|Vard|Btsfjord|Berlevg|Mehamn|Kjllefjord|Honningsvg|Havysund|Hammerfest|Ksfjord|Skjervy|Troms|Troms|Finnsnes|Harstad|Risyhamn|Sortland|Stokmarknes|Svolvr|Stamsund|Bod|Rnes|Nesna|Sandnessjen|Brnnysund|Rrvik|Trondheim|Kristiansund|Molde|Lesund|Torvik|Maly|Flor|Bergen"
        },
        "uniqueItineraryId": "342640_13447__5",
        "prices": [],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "destination": {
          "id": 39,
          "type": "Destination",
          "priority": 54
        },
        "parentDestinationIds": [
          15
        ],
        "ship": {
          "id": 13447,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8146/13447/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8146/13447/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8146/13447/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8146,
            "priority": 100,
            "logoPath": "/content/images/cruise/8146/logo_190.png"
          }
        },
        "shipIds": [
          13447
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "07-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "07-Feb-2023",
        "voyageId": "854432854495",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Inside",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_39.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          39
        ]
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
