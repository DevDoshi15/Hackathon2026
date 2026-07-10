# Cruise Search With CruiseTour Only

**Path:** Cruise Search > Cruise Search With CruiseTour Only

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
Date: Wed, 01 Feb 2023 09:39:49 GMT
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
    "total": 5057,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
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
        "id": 1334121,
        "code": "WUAY|30203",
        "name": "Taste Of Egypt",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "12-Feb-2023",
        "itinerary": {
          "id": 347099,
          "duration": 9,
          "departure": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "portsOfCalls": "CAIRO EGYPT|CAIRO|CAIRO|CAIROLUXOR (EMBARKATION)|LUXORESNA|EDFUKOM OMBO|ASWAN|ASWAN (DISEMBARKATION)CAIRO|CAIRO|CAIRO"
        },
        "uniqueItineraryId": "347099_14740__9_30203",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 4149
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:35:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 31,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          31,
          94
        ],
        "ship": {
          "id": 14740,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8121/14740/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8121/14740/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8121/14740/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8121,
            "priority": 100,
            "logoPath": "/content/images/cruise/8121/logo_190.png"
          }
        },
        "shipIds": [
          14740
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "12-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "12-Feb-2023",
        "cruiseTourCode": "30203",
        "voyageId": "WUAY",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_31.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 9,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "riverIds": [
          94
        ],
        "destinationIds": [
          31
        ]
      },
      {
        "id": 1239138,
        "code": "WAMQ|30203",
        "name": "From The Inca Empire To The Peruvian Amazon With The Nazca Lines",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "15-Feb-2023",
        "itinerary": {
          "id": 342114,
          "duration": 12,
          "departure": {
            "code": "LIM",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "LIM",
            "type": "CruisePort"
          },
          "portsOfCalls": "ARRIVE IN LIMA PERU|LIMAPISCOPARACAS & NAZCA LINES|PARACASBALLESTAS ISLAND CRUISELIMA|LIMA|SACRED VALLEY|SACRED VALLEY|MACHU PICCHU|CUSCO|CUSCOLIMAIQUITOSNAUTAPERUVIAN AMAZON RIVER (EMBARKATION)|PERUVIAN AMAZON|PERUVIAN AMAZON|IQUITOS (DISEMBARKATION)|LIMA",
          "mapPath": "/content/images/Itineraries/LIM_PIO_PRCS_IBST_LIM_SACV_MFT_CSCO_IQT_LIM.jpg",
          "fallbackMapPath": "/content/images/Itineraries/LIM_PIO_PRCS_IBST_LIM_SACV_MFT_CSCO_IQT_LIM.jpg"
        },
        "uniqueItineraryId": "342114_14088__12_30203",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 6456
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:35:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 32,
          "type": "Destination",
          "priority": 82
        },
        "parentDestinationIds": [
          32
        ],
        "ship": {
          "id": 14088,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8121/14088/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8121/14088/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8121/14088/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8121,
            "priority": 100,
            "logoPath": "/content/images/cruise/8121/logo_190.png"
          }
        },
        "shipIds": [
          14088
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "15-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "15-Feb-2023",
        "cruiseTourCode": "30203",
        "voyageId": "WAMQ",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_32.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 12,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "riverIds": [
          99
        ],
        "destinationIds": [
          32
        ],
        "packageDescription": "From the Inca Empire to the Peruvian Amazon with the Nazca Lines"
      },
      {
        "id": 1334074,
        "code": "WUAE|30203",
        "name": "Taste Of Egypt With Jordan",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "16-Feb-2023",
        "itinerary": {
          "id": 347097,
          "duration": 13,
          "departure": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "AMM",
            "type": "CruisePort"
          },
          "portsOfCalls": "CAIRO EGYPT|CAIRO|CAIRO|CAIROLUXOR (EMBARKATION)|LUXORESNA|EDFUKOM OMBO|ASWAN|ASWAN (DISEMBARKATION)CAIRO|CAIRO|CAIROAMMAN JORDAN|AMMANPETRA|PETRADEAD SEA|DEAD SEA EXCURSION TO JERASH RUINS|DEAD SEAAMMAN"
        },
        "uniqueItineraryId": "347097_14740__13_30203",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 6348
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:35:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 2,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          2,
          31
        ],
        "ship": {
          "id": 14740,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8121/14740/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8121/14740/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8121/14740/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8121,
            "priority": 100,
            "logoPath": "/content/images/cruise/8121/logo_190.png"
          }
        },
        "shipIds": [
          14740
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "16-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "16-Feb-2023",
        "cruiseTourCode": "30203",
        "voyageId": "WUAE",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_2.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          2,
          31
        ]
      },
      {
        "id": 1290707,
        "code": "802642802661|OSNOR2223WI",
        "name": "Norway Winter Expedition Cruise From Hamburg",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "17-Feb-2023",
        "itinerary": {
          "id": 342553,
          "duration": 14,
          "departure": {
            "code": "HAM",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "HAM",
            "type": "CruisePort"
          },
          "portsOfCalls": "Hamburg|Cuxhaven|Cuxhaven|Bergen|Mount Hoven (Loen)|Svolvr|Alta|Alta|Honningsvg|Troms|Reine|Lesund|Hardangerfjord|Hamburg",
          "normalizedPortsOfCall": "HAM|FCN|BGO|LOF|SVJ|ALF|HVG|TOS|RENE|AES|HDNG|HAM"
        },
        "uniqueItineraryId": "342553_14714__14_osnor2223wi",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 6066
              },
              {
                "name": "Outside",
                "value": 6430
              },
              {
                "name": "Suite",
                "value": 11707
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 10:44:53"
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
          "id": 14714,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/14714/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/14714/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/14714/ship_520.jpg",
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
          14714
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "17-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "17-Feb-2023",
        "cruiseTourCode": "OSNOR2223WI",
        "voyageId": "802642802661",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Outside",
          "Suite"
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
        "id": 1230128,
        "code": "SAI230208T",
        "name": "Magnificent Mekong",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "17-Feb-2023",
        "itinerary": {
          "id": 360328,
          "duration": 14,
          "departure": {
            "code": "HAN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SGN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Magnificent Mekong|Lotte Hotel Hanoi|Lotte Hotel Hanoi|Sofitel Phokeethra Royal Angkor Resort|Sofitel Phokeethra Royal Angkor Resort|Sofitel Phokeethra Royal Angkor Resort|Kampong Cham|Kampong Cham|Phnom Penh|Phnom Penh|Scenic Sailing Mekong River|Tan Chau|Sa Dec|Cai Be|Ho Chi Minh City|The Reverie Saigon|The Reverie Saigon"
        },
        "uniqueItineraryId": "360328_14949__14_sai230208t",
        "prices": [
          {
            "items": [
              {
                "name": "Balcony",
                "value": 6799
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "03-Jun-2022 22:04:31"
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
          "id": 19,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          19
        ],
        "ship": {
          "id": 14949,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8112/14949/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8112/14949/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8112/14949/ship_520.jpg",
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
          14949
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "08-Feb-2023",
        "arrivalDateTime": "15-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "17-Feb-2023",
        "cruiseTourCode": "SAI230208T",
        "voyageId": "SAI230208T",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_19.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          19
        ]
      },
      {
        "id": 1239149,
        "code": "WAMY|30203",
        "name": "From The Inca Empire To The Peruvian Amazon With The Nazca Lines & Galápagos Cruise",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "22-Feb-2023",
        "itinerary": {
          "id": 342122,
          "duration": 19,
          "departure": {
            "code": "LIM",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "UIO",
            "type": "CruisePort"
          },
          "portsOfCalls": "ARRIVE IN LIMA PERU|LIMAPISCOPARACAS & NAZCA LINES|PARACASBALLESTAS ISLAND CRUISELIMA|LIMA|SACRED VALLEY|SACRED VALLEY|MACHU PICCHU|CUSCO|CUSCOLIMAIQUITOSNAUTAPERUVIAN AMAZON RIVER (EMBARKATION)|PERUVIAN AMAZON|PERUVIAN AMAZON|IQUITOS (DISEMBARKATION)|LIMAQUITO|QUITO|BALTRAGALPAGOS ISLANDS (EMBARKATION)SANTA CRUZ ISLAND|SANTIAGO ISLAND|NORTH SEYMOUR ISLAND|SOUTH PLAZA ISLAND|GALPAGOS ISLANDS (DISEMBARKATION)SAN CRISTOBALQUITO|QUITO"
        },
        "uniqueItineraryId": "342122_14088__19_30203",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 11368
              },
              {
                "code": "PortCharge",
                "value": 120
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:35:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 32,
          "type": "Destination",
          "priority": 82
        },
        "parentDestinationIds": [
          32
        ],
        "ship": {
          "id": 14088,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8121/14088/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8121/14088/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8121/14088/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8121,
            "priority": 100,
            "logoPath": "/content/images/cruise/8121/logo_190.png"
          }
        },
        "shipIds": [
          14088
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "22-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "22-Feb-2023",
        "cruiseTourCode": "30203",
        "voyageId": "WAMY",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_32.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 19,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          32
        ],
        "packageDescription": "From the Inca Empire to the Peruvian Amazon with the Nazca Lines & Galápagos Cruise"
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
        "id": 1239123,
        "code": "WAME|30205",
        "name": "From The Inca Empire To The Peruvian Amazon With Galápagos Cruise",
        "startDateTime": "05-Feb-2023",
        "endDateTime": "22-Feb-2023",
        "itinerary": {
          "id": 342106,
          "duration": 17,
          "departure": {
            "code": "LIM",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "UIO",
            "type": "CruisePort"
          },
          "portsOfCalls": "LIMA PERU|LIMA|SACRED VALLEY|SACRED VALLEY|MACHU PICCHU|CUSCO|CUSCOLIMAIQUITOSNAUTAPERUVIAN AMAZON RIVER (EMBARKATION)|PERUVIAN AMAZON|PERUVIAN AMAZON|IQUITOS (DISEMBARKATION)|LIMAQUITO|QUITO|BALTRAGALPAGOS ISLANDS (EMBARKATION)SANTA CRUZ ISLAND|SANTIAGO ISLAND|NORTH SEYMOUR ISLAND|SOUTH PLAZA ISLAND|GALPAGOS ISLANDS (DISEMBARKATION)SAN CRISTOBALQUITO|QUITO"
        },
        "uniqueItineraryId": "342106_14088__17_30205",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 10378
              },
              {
                "code": "PortCharge",
                "value": 120
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:35:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 32,
          "type": "Destination",
          "priority": 82
        },
        "parentDestinationIds": [
          32
        ],
        "ship": {
          "id": 14088,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8121/14088/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8121/14088/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8121/14088/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8121,
            "priority": 100,
            "logoPath": "/content/images/cruise/8121/logo_190.png"
          }
        },
        "shipIds": [
          14088
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "05-Feb-2023",
        "arrivalDateTime": "22-Feb-2023",
        "cruisePackageDepartureDateTime": "05-Feb-2023",
        "cruisePackageArrivalDateTime": "22-Feb-2023",
        "cruiseTourCode": "30205",
        "voyageId": "WAME",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_32.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 17,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          32
        ],
        "packageDescription": "From the Inca Empire to the Peruvian Amazon with Galápagos Cruise"
      },
      {
        "id": 1276345,
        "code": "760021760034|UKFNANT2222IGR",
        "name": "Antarctic Circle Expedition",
        "startDateTime": "06-Feb-2023",
        "endDateTime": "23-Feb-2023",
        "itinerary": {
          "id": 320136,
          "duration": 17,
          "departure": {
            "code": "BUE",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BUE",
            "type": "CruisePort"
          },
          "portsOfCalls": "Buenos Aires|Ushuaia|South Shetland|Orne Harbour|Orne Harbour|Petermann Island|Crystal Sound|Marguerite Bay|Marguerite Bay|Penola Strait|Ushuaia",
          "mapPath": "/content/images/Itineraries/BUE_USH_SSTL_ORNE_PRMN_USH.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BUE_USH_SSTL_ORNE_PRMN_USH.jpg"
        },
        "uniqueItineraryId": "320136_14110__17_fnant2222",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 13770
              },
              {
                "name": "Suite",
                "value": 19193
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 10:45:02"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 65,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          65
        ],
        "ship": {
          "id": 14110,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/14110/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/14110/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/14110/ship_520.jpg",
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
          14110
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "07-Feb-2023",
        "arrivalDateTime": "23-Feb-2023",
        "cruisePackageDepartureDateTime": "06-Feb-2023",
        "cruisePackageArrivalDateTime": "23-Feb-2023",
        "cruiseTourCode": "FNANT2222",
        "voyageId": "760021760034",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_65.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 17,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          65
        ]
      },
      {
        "id": 1319892,
        "code": "859203859218|SCGAL2324W",
        "name": "Galápagos Islands Expedition Cruise – Iconic Wildlife & Sublime Scenery",
        "startDateTime": "07-Feb-2023",
        "endDateTime": "13-Feb-2023",
        "itinerary": {
          "id": 363640,
          "duration": 6,
          "departure": {
            "code": "UIO",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GYE",
            "type": "CruisePort"
          },
          "portsOfCalls": "Quito|Quito|Capitania Seymour Baltra|Dragon Hill|Punta Vicente Roca|Fernandina|Puerto Ayora|Puerto Ayora|Post Office Bay|Champion Islet|Punta Cormorant|Capitania Seymour Baltra"
        },
        "uniqueItineraryId": "363640_15108__6_scgal2324w",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 7096
              },
              {
                "name": "Suite",
                "value": 9474
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 10:44:57"
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
        "departureDateTime": "09-Feb-2023",
        "arrivalDateTime": "13-Feb-2023",
        "cruisePackageDepartureDateTime": "07-Feb-2023",
        "cruisePackageArrivalDateTime": "13-Feb-2023",
        "cruiseTourCode": "SCGAL2324W",
        "voyageId": "859203859218",
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
        "cruiseDuration": 6,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          48
        ]
      },
      {
        "id": 1315583,
        "code": "859203860032|APSCGAL2324WN",
        "name": "Galapagos Islands Expedition Cruise - Nine Of The Best Isles",
        "startDateTime": "07-Feb-2023",
        "endDateTime": "17-Feb-2023",
        "itinerary": {
          "id": 363641,
          "duration": 10,
          "departure": {
            "code": "UIO",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "GYE",
            "type": "CruisePort"
          },
          "portsOfCalls": "Quito|Quito|Capitania Seymour Baltra|Dragon Hill|Punta Vicente Roca|Fernandina|Puerto Ayora|Puerto Ayora|Post Office Bay|Champion Islet|Punta Cormorant|Capitania Seymour Baltra|Las Bachas|Las Bachas|Buccaneer Cove|Puerto Egas|Puerto Egas|Rabida|Bartolome|Bartolome|Prince Philip Steps Genovesa|Darwin Bay Genovesa|Capitania Seymour Baltra"
        },
        "uniqueItineraryId": "363641_15108__10_scgal2324wn",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 11392
              },
              {
                "name": "Suite",
                "value": 15661
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 10:44:57"
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
        "departureDateTime": "09-Feb-2023",
        "arrivalDateTime": "17-Feb-2023",
        "cruisePackageDepartureDateTime": "07-Feb-2023",
        "cruisePackageArrivalDateTime": "17-Feb-2023",
        "cruiseTourCode": "SCGAL2324WN",
        "voyageId": "859203860032",
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
        "id": 1230129,
        "code": "OSR230211T",
        "name": "Pharaohs & Pyramids",
        "startDateTime": "08-Feb-2023",
        "endDateTime": "19-Feb-2023",
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
        "uniqueItineraryId": "276726_14512__11_osr230211t",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 6999
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "03-Jun-2022 22:04:31"
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
        "departureDateTime": "11-Feb-2023",
        "arrivalDateTime": "18-Feb-2023",
        "cruisePackageDepartureDateTime": "08-Feb-2023",
        "cruisePackageArrivalDateTime": "19-Feb-2023",
        "cruiseTourCode": "OSR230211T",
        "voyageId": "OSR230211T",
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
        "id": 1300762,
        "code": "808923808938|SBCIS2215MAD",
        "name": "Wonders Of Madeira And The Canary Islands - Atlantic Expedition Cruise",
        "startDateTime": "09-Feb-2023",
        "endDateTime": "19-Feb-2023",
        "itinerary": {
          "id": 363608,
          "duration": 10,
          "departure": {
            "code": "LPA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "LPA",
            "type": "CruisePort"
          },
          "portsOfCalls": "Las Palmas|Funchal|Funchal|Porto Santo|Arrecife (Lanzarote)|Santa Cruz De Tenerife|Santa Cruz De La Palma|Puerto De La Estaca El Hierro|La Gomera|Las Palmas",
          "normalizedPortsOfCall": "LPS1|FNC|PXO|ARRE|SCDT|SPC|PDLE|LGMR|LPS1",
          "mapPath": "/content/images/Itineraries/LPS1_FNC_PXO_ARR_TFN_PLP_PDLE_HRRO_DLG_LPS1.jpg",
          "fallbackMapPath": "/content/images/Itineraries/LPS1_FNC_PXO_ARR_TFN_PLP_PDLE_HRRO_DLG_LPS1.jpg"
        },
        "uniqueItineraryId": "363608_15087__10_sbcis2215",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 4524
              },
              {
                "name": "Outside",
                "value": 5293
              },
              {
                "name": "Suite",
                "value": 7690
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 10:45:01"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 68,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          68
        ],
        "ship": {
          "id": 15087,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/9191/15087/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/9191/15087/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/9191/15087/ship_520.jpg",
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
          15087
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "09-Feb-2023",
        "arrivalDateTime": "19-Feb-2023",
        "cruisePackageDepartureDateTime": "09-Feb-2023",
        "cruisePackageArrivalDateTime": "19-Feb-2023",
        "cruiseTourCode": "SBCIS2215",
        "voyageId": "808923808938",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
          "Outside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_68.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          68
        ]
      },
      {
        "id": 1334122,
        "code": "WUAY|30210",
        "name": "Taste Of Egypt",
        "startDateTime": "10-Feb-2023",
        "endDateTime": "19-Feb-2023",
        "itinerary": {
          "id": 347099,
          "duration": 9,
          "departure": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "portsOfCalls": "CAIRO EGYPT|CAIRO|CAIRO|CAIROLUXOR (EMBARKATION)|LUXORESNA|EDFUKOM OMBO|ASWAN|ASWAN (DISEMBARKATION)CAIRO|CAIRO|CAIRO"
        },
        "uniqueItineraryId": "347099_14740__9_30210",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 4149
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:35:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 31,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          31,
          94
        ],
        "ship": {
          "id": 14740,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8121/14740/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8121/14740/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8121/14740/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8121,
            "priority": 100,
            "logoPath": "/content/images/cruise/8121/logo_190.png"
          }
        },
        "shipIds": [
          14740
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "10-Feb-2023",
        "arrivalDateTime": "19-Feb-2023",
        "cruisePackageDepartureDateTime": "10-Feb-2023",
        "cruisePackageArrivalDateTime": "19-Feb-2023",
        "cruiseTourCode": "30210",
        "voyageId": "WUAY",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_31.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 9,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "riverIds": [
          94
        ],
        "destinationIds": [
          31
        ]
      },
      {
        "id": 1334075,
        "code": "WUAE|30210",
        "name": "Taste Of Egypt With Jordan",
        "startDateTime": "10-Feb-2023",
        "endDateTime": "23-Feb-2023",
        "itinerary": {
          "id": 347097,
          "duration": 13,
          "departure": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "AMM",
            "type": "CruisePort"
          },
          "portsOfCalls": "CAIRO EGYPT|CAIRO|CAIRO|CAIROLUXOR (EMBARKATION)|LUXORESNA|EDFUKOM OMBO|ASWAN|ASWAN (DISEMBARKATION)CAIRO|CAIRO|CAIROAMMAN JORDAN|AMMANPETRA|PETRADEAD SEA|DEAD SEA EXCURSION TO JERASH RUINS|DEAD SEAAMMAN"
        },
        "uniqueItineraryId": "347097_14740__13_30210",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 6348
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:35:13"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 2,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          2,
          31
        ],
        "ship": {
          "id": 14740,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8121/14740/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8121/14740/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8121/14740/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8121,
            "priority": 100,
            "logoPath": "/content/images/cruise/8121/logo_190.png"
          }
        },
        "shipIds": [
          14740
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "10-Feb-2023",
        "arrivalDateTime": "23-Feb-2023",
        "cruisePackageDepartureDateTime": "10-Feb-2023",
        "cruisePackageArrivalDateTime": "23-Feb-2023",
        "cruiseTourCode": "30210",
        "voyageId": "WUAE",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Outside"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_2.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          2,
          31
        ]
      },
      {
        "id": 1306080,
        "code": "20306",
        "name": "3-Night Cairo Pre-Cruise, 7-Night Cruise Roundtrip Luxor, 1-Night Cairo Post-Cruise",
        "startDateTime": "10-Feb-2023",
        "endDateTime": "24-Feb-2023",
        "itinerary": {
          "id": 330592,
          "duration": 14,
          "departure": {
            "code": "LXR",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "LXR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Luxor|Luxor|Aswan|Aswan|Luxor|Luxor",
          "mapPath": "/content/images/Itineraries/LXR_ASW_LXR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/LXR_ASW_LXR.jpg"
        },
        "uniqueItineraryId": "330592_14829__14_20306",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 5899
              },
              {
                "name": "Balcony",
                "value": 7798
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "05-Jun-2022 00:01:31"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 51,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          51
        ],
        "ship": {
          "id": 14829,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8138/14829/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8138/14829/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8138/14829/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8138,
            "priority": 100,
            "logoPath": "/content/images/cruise/8138/logo_190.png"
          }
        },
        "shipIds": [
          14829
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "10-Feb-2023",
        "arrivalDateTime": "21-Feb-2023",
        "cruisePackageDepartureDateTime": "10-Feb-2023",
        "cruisePackageArrivalDateTime": "24-Feb-2023",
        "cruiseTourCode": "20306",
        "voyageId": "20306",
        "packageTourId": -1,
        "categoryTypes": [
          "Outside",
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_51.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          51
        ]
      },
      {
        "id": 1280456,
        "code": "WSHH|30210",
        "name": "Fascinating Vietnam, Cambodia & The Mekong River With Hanoi & Ha Long Bay (Southbound)",
        "startDateTime": "10-Feb-2023",
        "endDateTime": "25-Feb-2023",
        "itinerary": {
          "id": 342071,
          "duration": 15,
          "departure": {
            "code": "HAN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SGN",
            "type": "CruisePort"
          },
          "portsOfCalls": "HANOI VIETNAM|HANOI|HANOIHA LONG BAY|HA LONG BAYHANOISIEM REAP|SIEM REAP|SIEM REAP|PHNOM PENH (EMBARKATION)|WAT HANCHEYANGKOR BAN|KAMPONG TRALACHKONPONG LOUANG|PHNOM PENH|BORDER CROSSINGCHAU DOC VIETNAM|LONG KHANH ACU LAO GIENG|VINH LONG|HO CHI MINH CITY (DISEMBARKATION)|HO CHI MINH CITY EXCURSION TO CU CHI TUNNELS|HO CHI MINH CITY",
          "mapPath": "/content/images/Itineraries/HAN_HLG_REP_PNH_HNCH_AKGB_KPTR_KZLN_CHAU_CLGN_XVL_PHU.jpg",
          "fallbackMapPath": "/content/images/Itineraries/HAN_HLG_REP_PNH_HNCH_AKGB_KPTR_KZLN_CHAU_CLGN_XVL_PHU.jpg"
        },
        "uniqueItineraryId": "342071_14086__15_30210",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 7009
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 08:35:13"
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
          19,
          178
        ],
        "ship": {
          "id": 14086,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8121/14086/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8121/14086/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8121/14086/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://my.matterport.com/show/?m=aKfLj9NqLFC&hl=1&wh=0",
          "cruiseline": {
            "id": 8121,
            "priority": 100,
            "logoPath": "/content/images/cruise/8121/logo_190.png"
          }
        },
        "shipIds": [
          14086
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "10-Feb-2023",
        "arrivalDateTime": "25-Feb-2023",
        "cruisePackageDepartureDateTime": "10-Feb-2023",
        "cruisePackageArrivalDateTime": "25-Feb-2023",
        "cruiseTourCode": "30210",
        "voyageId": "WSHH",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_19.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 15,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "riverIds": [
          86
        ],
        "destinationIds": [
          19
        ],
        "packageDescription": "Fascinating Vietnam, Cambodia & the Mekong River with Hanoi & Ha Long Bay (Southbound)"
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
