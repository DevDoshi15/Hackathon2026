# Cruise Search With Duration

**Path:** Cruise Search > Cruise Search With Duration

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
            "key": "duration",
            "ranges": [
                {
                    "from": "4",
                    "to": "6"
                },
                {
                    "from": "7",
                    "to": "9"
                }
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
Date: Wed, 01 Feb 2023 09:29:48 GMT
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
    "total": 11635,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
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
        "id": 1270896,
        "code": "793086793151",
        "name": "The Voyage North",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "08-Feb-2023",
        "itinerary": {
          "id": 342639,
          "duration": 6,
          "departure": {
            "code": "BGO",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "KKN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Bergen|Flor|Maly|Torvik|Lesund|Molde|Kristiansund|Trondheim|Rrvik|Brnnysund|Sandnessjen|Nesna|Rnes|Bod|Stamsund|Svolvr|Stokmarknes|Sortland|Risyhamn|Harstad|Finnsnes|Troms|Skjervy|Ksfjord|Hammerfest|Havysund|Honningsvg|Kjllefjord|Mehamn|Berlevg|Btsfjord|Vard|Vads|Kirkenes"
        },
        "uniqueItineraryId": "342639_13441__6",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2102
              },
              {
                "name": "Outside",
                "value": 2459
              },
              {
                "name": "Suite",
                "value": 5570
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 09:50:09"
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
          "id": 13441,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8146/13441/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8146/13441/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8146/13441/ship_520.jpg",
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
          13441
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "08-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "08-Feb-2023",
        "voyageId": "793086793151",
        "stnExternalId": "1429955",
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
        "cruiseDuration": 6,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          39
        ]
      },
      {
        "id": 1327610,
        "code": "SP20230202SGASGA",
        "name": "Saudi Arabia & Red Sea, 7 Nights",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 362632,
          "duration": 7,
          "departure": {
            "code": "SAF1",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SAF1",
            "type": "CruisePort"
          },
          "portsOfCalls": "Safaga Egypt|Jeddah Saudi Arabia|Yanbu Al Bahr Saudi Arabia|Al Wajh Saudi Arabia|Aqaba (Petra) Jordan|Safaga Egypt",
          "normalizedPortsOfCall": "SAF1|JED|YNB|ALWJ|AQJ|SAF1",
          "mapPath": "/content/images/Itineraries/SAF_JED_YNAL_WAJH_AQJ_SAF.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SAF_JED_YNAL_WAJH_AQJ_SAF.jpg"
        },
        "uniqueItineraryId": "362632_13239__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 299
              },
              {
                "name": "Outside",
                "value": 439
              },
              {
                "name": "Balcony",
                "value": 519
              },
              {
                "name": "Suite",
                "value": 1189
              },
              {
                "code": "PortCharge",
                "value": 160
              },
              {
                "code": "CruiseTax",
                "value": 140
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
          "id": 31,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          31
        ],
        "ship": {
          "id": 13239,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/13239/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/13239/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/13239/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Splendida/en-gl/index.html",
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
          13239
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "voyageId": "SP20230202SGASGA",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_31.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          31
        ]
      },
      {
        "id": 1327344,
        "code": "PR20230202LEHLEH",
        "name": "Northern Europe, 7 Nights",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 361799,
          "duration": 7,
          "departure": {
            "code": "LEH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "LEH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Le Havre (Paris) France|Southampton (London)United Kingdom|HamburgGermany|Zeebrugge (Bruges) Belgium|Rotterdam (Amsterdam) Netherlands|Le Havre (Paris) France",
          "normalizedPortsOfCall": "LEH|SOU|HAM|ZBR1|RTM|LEH",
          "mapPath": "/content/images/Itineraries/LEH_SOU_HAM_ZBR_RTM_LEH.jpg",
          "fallbackMapPath": "/content/images/Itineraries/LEH_SOU_HAM_ZBR_RTM_LEH.jpg"
        },
        "uniqueItineraryId": "361799_13510__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 419
              },
              {
                "name": "Outside",
                "value": 549
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
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "voyageId": "PR20230202LEHLEH",
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
        "id": 1287671,
        "code": "EU20230202DOHDOH",
        "name": "Dubai, Abu Dhabi & Qatar, 7 Nights",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 319329,
          "duration": 7,
          "departure": {
            "code": "DOH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "DOH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Doha Qatar|DubaiUArab Emirates|DubaiUArab Emirates|Abu DhabiUArab Emirates|Sir Bani YasUArab Emirates|Dammam Saudi Arabia|Doha Qatar",
          "normalizedPortsOfCall": "DOH|DXB|AUH|XSB|DMM|DOH",
          "mapPath": "/content/images/Itineraries/DOH_DXB_AUH_XSB_DMMM_DOH.jpg",
          "fallbackMapPath": "/content/images/Itineraries/DOH_DXB_AUH_XSB_DMMM_DOH.jpg"
        },
        "uniqueItineraryId": "319329_14964__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 659
              },
              {
                "name": "Outside",
                "value": 759
              },
              {
                "name": "Balcony",
                "value": 799
              },
              {
                "name": "Suite",
                "value": 1239
              },
              {
                "code": "PortCharge",
                "value": 159
              },
              {
                "code": "CruiseTax",
                "value": 96.53
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 09:10:15"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
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
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 54,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          31
        ],
        "ship": {
          "id": 14964,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/14964/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/14964/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/14964/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 982,
            "priority": 100,
            "logoPath": "/content/images/cruise/982/logo_190.png"
          }
        },
        "shipIds": [
          14964
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "voyageId": "EU20230202DOHDOH",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_54.jpg",
        "maxOccupancy": 6,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          54
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
        "id": 1328084,
        "code": "VI20230203PMIPMI",
        "name": "Mediterranean, 7 Nights",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 362209,
          "duration": 7,
          "departure": {
            "code": "PMI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "PMI",
            "type": "CruisePort"
          },
          "portsOfCalls": "Palma De Mallorca (Baleari Is) Spain|Barcelona Spain|Marseille (Provence) France|Genoa (Portofino) Italy|La Spezia (Cinque Terre) Italy|Naples (Pompeii) Italy|Palma De Mallorca (Baleari Is) Spain",
          "normalizedPortsOfCall": "PMI|BCN|MRS|GOA|LPZ|NAP|PMI",
          "mapPath": "/content/images/Itineraries/PMI_BCN_MRS_GOA_LPZ_NAP_PMI.jpg",
          "fallbackMapPath": "/content/images/Itineraries/PMI_BCN_MRS_GOA_LPZ_NAP_PMI.jpg"
        },
        "uniqueItineraryId": "362209_14390__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 599
              },
              {
                "name": "Outside",
                "value": 719
              },
              {
                "name": "Balcony",
                "value": 859
              },
              {
                "name": "Suite",
                "value": 1239
              },
              {
                "code": "PortCharge",
                "value": 159
              },
              {
                "code": "CruiseTax",
                "value": 140
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
          "id": 18,
          "type": "Destination",
          "priority": 64
        },
        "parentDestinationIds": [
          75
        ],
        "ship": {
          "id": 14390,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/14390/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/14390/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/14390/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 982,
            "priority": 100,
            "logoPath": "/content/images/cruise/982/logo_190.png"
          }
        },
        "shipIds": [
          14390
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "10-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "voyageId": "VI20230203PMIPMI",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_18.jpg",
        "maxOccupancy": 6,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          18
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
        "id": 1324895,
        "code": "GR20230203BCNBCN",
        "name": "Mediterranean, 7 Nights",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "10-Feb-2023",
        "itinerary": {
          "id": 362626,
          "duration": 7,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Marseille (Provence) France|Genoa (Portofino) Italy|Civitavecchia (Rome) Italy|Palermo (Monreale) Italy|Valletta Malta|Barcelona Spain",
          "normalizedPortsOfCall": "BCN|MRS|GOA|CIV|PMO|VLT|BCN",
          "mapPath": "/content/images/Itineraries/BCN_MRS_GOA_CVV_PMO_VLT_BCN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_MRS_GOA_CVV_PMO_VLT_BCN.jpg"
        },
        "uniqueItineraryId": "362626_14091__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 599
              },
              {
                "name": "Outside",
                "value": 719
              },
              {
                "name": "Balcony",
                "value": 859
              },
              {
                "name": "Suite",
                "value": 1239
              },
              {
                "code": "PortCharge",
                "value": 159
              },
              {
                "code": "CruiseTax",
                "value": 72.49
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
          "id": 18,
          "type": "Destination",
          "priority": 64
        },
        "parentDestinationIds": [
          75
        ],
        "ship": {
          "id": 14091,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/14091/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/14091/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/14091/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Grandiosa/en-gl/index.html",
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 982,
            "priority": 100,
            "logoPath": "/content/images/cruise/982/logo_190.png"
          }
        },
        "shipIds": [
          14091
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "10-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "10-Feb-2023",
        "voyageId": "GR20230203BCNBCN",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_18.jpg",
        "maxOccupancy": 6,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          18
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
        "id": 1331121,
        "code": "20230204FD05",
        "name": "5 Day Exotic Eastern Caribbean Cruise",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 309361,
          "duration": 5,
          "departure": {
            "code": "XPC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "XPC",
            "type": "CruisePort"
          },
          "portsOfCalls": "PORT CANAVERAL (ORLANDO) FL|AMBER COVE DOMINICAN REPUBLIC|GRAND TURK|PORT CANAVERAL (ORLANDO) FL",
          "mapPath": "/content/images/Itineraries/XPC_AMB_GDT_XPC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/XPC_AMB_GDT_XPC.jpg"
        },
        "uniqueItineraryId": "309361_1096__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 239
              },
              {
                "name": "Outside",
                "value": 319
              },
              {
                "name": "Balcony",
                "value": 469
              },
              {
                "name": "Suite",
                "value": 844
              },
              {
                "code": "PortCharge",
                "value": 119
              },
              {
                "code": "CruiseTax",
                "value": 119.86
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
            "NR",
            "OBC",
            "WIFI"
          ],
          "fareDetailsPromoCodesInfo": [
            {
              "fareDetailsPromoCode": "Discount",
              "subFareDetailsPromoCodes": [
                "Discount"
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
          "id": 10,
          "type": "Destination",
          "priority": 24
        },
        "parentDestinationIds": [
          9
        ],
        "ship": {
          "id": 1096,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/1096/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/1096/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/1096/ship_520.jpg",
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
          1096
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "voyageId": "20230204FD05",
        "stnExternalId": "1458499",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_10.jpg",
        "maxOccupancy": 5,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          10
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
        "id": 1252564,
        "code": "E1230204005",
        "name": "King George Island To King George Island",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 327059,
          "duration": 5,
          "departure": {
            "code": "KGIA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "KGIA",
            "type": "CruisePort"
          },
          "portsOfCalls": "King George Island|Antarctic Peninsula|Antarctic Peninsula|South Shetland Islands|King George Island",
          "normalizedPortsOfCall": "KGIA|ANPE|SDZ|KGIA",
          "mapPath": "/content/images/Itineraries/KGIA_SSTL_KGIA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/KGIA_SSTL_KGIA.jpg"
        },
        "uniqueItineraryId": "327059_13290__5",
        "prices": [
          {
            "items": [
              {
                "name": "Suite",
                "value": 13950
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 15:05:11"
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
          "id": 13290,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8115/13290/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8115/13290/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8115/13290/ship_520.jpg",
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
          13290
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "voyageId": "E1230204005",
        "stnExternalId": "1405056",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_65.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          65
        ],
        "packageDescription": ""
      },
      {
        "id": 1225946,
        "code": "20230204SH05",
        "name": "Bahamas From Charleston, Sc",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "09-Feb-2023",
        "itinerary": {
          "id": 334358,
          "duration": 5,
          "departure": {
            "code": "CHS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CHS",
            "type": "CruisePort"
          },
          "portsOfCalls": "CHARLESTON SC|BIMINI THE BAHAMAS|NASSAU THE BAHAMAS|CHARLESTON SC",
          "mapPath": "/content/images/Itineraries/CHS_BIM_NAS_CHS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CHS_BIM_NAS_CHS.jpg"
        },
        "uniqueItineraryId": "334358_13509__5",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 309
              },
              {
                "name": "Outside",
                "value": 379
              },
              {
                "name": "Balcony",
                "value": 529
              },
              {
                "name": "Suite",
                "value": 909
              },
              {
                "code": "PortCharge",
                "value": 119
              },
              {
                "code": "CruiseTax",
                "value": 135.86
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
          "id": 13509,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/1/13509/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/1/13509/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/1/13509/ship_520.jpg",
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
          13509
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "09-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "09-Feb-2023",
        "voyageId": "20230204SH05",
        "stnExternalId": "1392199",
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
        "cruiseDuration": 5,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
