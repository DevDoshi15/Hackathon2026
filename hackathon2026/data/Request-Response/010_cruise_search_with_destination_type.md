# Cruise Search With Destination type

**Path:** Cruise Search > Cruise Search With Destination type

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
            "key": "destinationType",
            "value": "River" // Possible Values - Ocean/River/All
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 01 Feb 2023 09:30:09 GMT
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
    "total": 9830,
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
        "id": 1280425,
        "code": "WSH|30202",
        "name": "Mekong Discovery (Southbound)",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 342051,
          "duration": 7,
          "departure": {
            "code": "PNH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SGN",
            "type": "CruisePort"
          },
          "portsOfCalls": "PHNOM PENH CAMBODIA (EMBARKATION)|WAT HANCHEYANGKOR BAN|KAMPONG TRALACHKONPONG LOUANGPHNOM PENH|PHNOM PENH|BORDER CROSSINGCHAU DOC VIETNAM|LONG KHANH ACU LAO GIENG|VINH LONG|HO CHI MINH CITY (DISEMBARKATION)",
          "mapPath": "/content/images/Itineraries/PNH_HNCH_AKGB_KPTR_KZLN_PNH_CHAU_CLGN_XVL_PHU.jpg",
          "fallbackMapPath": "/content/images/Itineraries/PNH_HNCH_AKGB_KPTR_KZLN_PNH_CHAU_CLGN_XVL_PHU.jpg"
        },
        "uniqueItineraryId": "342051_14086__7",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 4439
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
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "voyageId": "WSH",
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
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "riverIds": [
          86
        ],
        "destinationIds": [
          19
        ],
        "packageDescription": "Mekong Discovery (Southbound)"
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
        "id": 1325270,
        "code": "46607|9",
        "name": "Timeless Wonders Of Vietnam, Cambodia & The Mekong (2023)",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "17-Feb-2023",
        "itinerary": {
          "id": 339143,
          "duration": 14,
          "departure": {
            "code": "SGN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "HAN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Ho Chi Minh City Vietnam|Ho Chi Minh City|Ho Chi Minh City Transfer to My Tho (Embark) Tien Loi (Ben Tre)|Tien Loi (Ben Tre) Vinh Long Sa Dec|Phnom Penh|Angkor Ban Wat Hanchey Kampong Cham|Kampong Cham (Disembark) Transfer to Siem Reap|Siem Reap|Siem Reap|Siem Reap Fly to Hanoi|Hanoi|Hanoi"
        },
        "uniqueItineraryId": "339143_14473__14",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 7499
              },
              {
                "code": "PortCharge",
                "value": 210
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 03:00:15"
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
          "id": 14473,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8149/14473/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8149/14473/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8149/14473/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8149,
            "priority": 100,
            "logoPath": "/content/images/cruise/8149/logo_190.png"
          }
        },
        "shipIds": [
          14473
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "17-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "17-Feb-2023",
        "voyageId": "46607",
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
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "riverIds": [
          86
        ],
        "destinationIds": [
          19
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
        "id": 1282169,
        "code": "X306",
        "name": "Mexican Riviera",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 308583,
          "duration": 7,
          "departure": {
            "code": "LAX",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "LAX",
            "type": "CruisePort"
          },
          "portsOfCalls": "Los Angeles California|Cabo San Lucas Mexico|Mazatlan Mexico|Puerto Vallarta Mexico|Los Angeles California",
          "normalizedPortsOfCall": "LAX|SJD|MZT|PVR|LAX",
          "mapPath": "/content/images/Itineraries/LAX_CSL_MZT_PVR_LAX.jpg",
          "fallbackMapPath": "/content/images/Itineraries/LAX_CSL_MZT_PVR_LAX.jpg"
        },
        "uniqueItineraryId": "308583_14718__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 558
              },
              {
                "name": "Outside",
                "value": 796
              },
              {
                "name": "Balcony",
                "value": 801
              },
              {
                "name": "Suite",
                "value": 1168
              },
              {
                "code": "PortCharge",
                "value": 189
              },
              {
                "code": "CruiseTax",
                "value": 145
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
          "id": 24,
          "type": "Destination",
          "priority": 80
        },
        "parentDestinationIds": [
          42
        ],
        "ship": {
          "id": 14718,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14718/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14718/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14718/ship_520.jpg",
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
          14718
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "X306",
        "stnExternalId": "1422887",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_24.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          24
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
        "id": 1276915,
        "code": "8318",
        "name": "7-Day Classic Caribbean Yacht Harbors",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 345677,
          "duration": 7,
          "departure": {
            "code": "BGI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SXM",
            "type": "CruisePort"
          },
          "portsOfCalls": "Bridgetown Barbados|Port Elizabeth Bequia St Vincent and the Grenadines|Trois Ilets Martinique|Basse-Terre Guadeloupe|Charlestown Nevis St Kitts and Nevis|St Johns Antigua and Barbuda|Carambola Beach Saint Kitts and Nevis|Philipsburg Sint Maarten",
          "normalizedPortsOfCall": "BGI|BQU|TRIS|BBR|CHST|SJOH|CRMB|PSB",
          "mapPath": "/content/images/Itineraries/BGI_BQU_TIL_GLP_CHST_SJN_CRB_PSB.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BGI_BQU_TIL_GLP_CHST_SJN_CRB_PSB.jpg"
        },
        "uniqueItineraryId": "345677_13824__7",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 3839
              },
              {
                "code": "PortCharge",
                "value": 476
              },
              {
                "code": "CruiseTax",
                "value": 160
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:15:16"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
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
          "id": 13824,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/11/13824/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/11/13824/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/11/13824/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasVrForStateRoom": true,
          "cruiseline": {
            "id": 11,
            "priority": 100,
            "logoPath": "/content/images/cruise/11/logo_190.png"
          }
        },
        "shipIds": [
          13824
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "8318",
        "stnExternalId": "1417637",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_13.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          13,
          9
        ]
      },
      {
        "id": 1208143,
        "code": "MSP230204",
        "name": "Heart Of The Delta",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 346411,
          "duration": 7,
          "departure": {
            "code": "MSY",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MEM",
            "type": "CruisePort"
          },
          "portsOfCalls": "New Orleans|Darrow|Baton Rouge|St Francisville|Natchez|Vicksburg|Memphis",
          "mapPath": "/content/images/Itineraries/MSY_DRRW_BTR_STFR_HEZ_VKS_MEM.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MSY_DRRW_BTR_STFR_HEZ_VKS_MEM.jpg"
        },
        "uniqueItineraryId": "346411_14835__7",
        "prices": [
          {
            "items": [
              {
                "name": "Balcony",
                "value": 3999
              },
              {
                "name": "Suite",
                "value": 5799
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 15:30:13"
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
          "id": 112,
          "type": "Destination",
          "priority": 100
        },
        "parentDestinationIds": [
          180,
          48
        ],
        "ship": {
          "id": 14835,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8112/14835/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8112/14835/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8112/14835/ship_520.jpg",
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
          14835
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "MSP230204",
        "stnExternalId": "1384894",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_112.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "riverIds": [
          112
        ],
        "destinationIds": [
          112
        ]
      },
      {
        "id": 1292217,
        "code": "46367|8",
        "name": "Splendors Of Egypt & The Nile (2023)",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "15-Feb-2023",
        "itinerary": {
          "id": 240452,
          "duration": 11,
          "departure": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "portsOfCalls": "Cairo|Cairo|Aswan|Luxor (Disembark) Fly to Cairo|Cairo|Depart Cairo",
          "mapPath": "/content/images/Itineraries/CAI_LXR_DNDR_OMBO_ASW_EDFU_ESN_LXR_CAI.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CAI_LXR_DNDR_OMBO_ASW_EDFU_ESN_LXR_CAI.jpg"
        },
        "uniqueItineraryId": "240452_13477__11",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 8799
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 03:00:15"
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
          "id": 13477,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8149/13477/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8149/13477/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8149/13477/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8149,
            "priority": 100,
            "logoPath": "/content/images/cruise/8149/logo_190.png"
          }
        },
        "shipIds": [
          13477
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "15-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "15-Feb-2023",
        "voyageId": "46367",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_31.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 11,
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
        "id": 1292184,
        "code": "46298|8",
        "name": "Splendors Of Egypt & The Nile (2023)",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "15-Feb-2023",
        "itinerary": {
          "id": 240452,
          "duration": 11,
          "departure": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CAI",
            "type": "CruisePort"
          },
          "portsOfCalls": "Cairo|Cairo|Aswan|Luxor (Disembark) Fly to Cairo|Cairo|Depart Cairo",
          "mapPath": "/content/images/Itineraries/CAI_LXR_DNDR_OMBO_ASW_EDFU_ESN_LXR_CAI.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CAI_LXR_DNDR_OMBO_ASW_EDFU_ESN_LXR_CAI.jpg"
        },
        "uniqueItineraryId": "240452_14479__11",
        "prices": [
          {
            "items": [
              {
                "name": "Balcony",
                "value": 6999
              },
              {
                "name": "Suite",
                "value": 8799
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 03:00:15"
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
          "id": 14479,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8149/14479/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8149/14479/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8149/14479/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8149,
            "priority": 100,
            "logoPath": "/content/images/cruise/8149/logo_190.png"
          }
        },
        "shipIds": [
          14479
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "15-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "15-Feb-2023",
        "voyageId": "46298",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_31.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 11,
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
        "id": 1276916,
        "code": "8318A",
        "name": "14-Day Exotic Caribbean In Depth",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "18-Feb-2023",
        "itinerary": {
          "id": 345678,
          "duration": 14,
          "departure": {
            "code": "BGI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BGI",
            "type": "CruisePort"
          },
          "portsOfCalls": "Bridgetown Barbados|Port Elizabeth Bequia St Vincent and the Grenadines|Trois Ilets Martinique|Basse-Terre Guadeloupe|Charlestown Nevis St Kitts and Nevis|St Johns Antigua and Barbuda|Carambola Beach Saint Kitts and Nevis|Philipsburg Sint Maarten|Sopers Hole (Frenchmans Cay) BVI|Basseterre St Kitts and Nevis|Gustavia Saint Barthelemy|Terre-de-Haut Iles des Saintes Guadeloupe|Rodney Bay Saint Lucia|Saline Bay Mayreau St Vincent and the Grenadines|Bridgetown Barbados",
          "normalizedPortsOfCall": "BGI|BQU|TRIS|BBR|CHST|SJOH|CRMB|PSB|SPHL|BASS|GUST|LSS|RDNB|SLNB|BGI",
          "mapPath": "/content/images/Itineraries/BGI_BEQ_TIL_BBR_CHST_SJN_CRB_PSB_SOP_BBR_GUS_LSS_MRU_BGI.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BGI_BEQ_TIL_BBR_CHST_SJN_CRB_PSB_SOP_BBR_GUS_LSS_MRU_BGI.jpg"
        },
        "uniqueItineraryId": "345678_13824__14",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 7219
              },
              {
                "code": "PortCharge",
                "value": 952
              },
              {
                "code": "CruiseTax",
                "value": 280
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:15:16"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
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
          "id": 13824,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/11/13824/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/11/13824/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/11/13824/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasVrForStateRoom": true,
          "cruiseline": {
            "id": 11,
            "priority": 100,
            "logoPath": "/content/images/cruise/11/logo_190.png"
          }
        },
        "shipIds": [
          13824
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "18-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "18-Feb-2023",
        "voyageId": "8318A",
        "stnExternalId": "1417665",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_13.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 14,
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
