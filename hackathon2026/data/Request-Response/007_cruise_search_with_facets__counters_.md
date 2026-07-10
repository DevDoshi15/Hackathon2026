# Cruise Search With Facets (Counters)

**Path:** Cruise Search > Cruise Search With Facets (Counters)

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/cruise?fetchFacets=true`

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
// pass fetchFacets=true in the Query String param, to fetch facets along with cruise details
{
    "filters": [
        {
            "key": "departureDate",
            "ranges": []
        },
        {
            "key": "duration",
            "ranges": []
        },
        {
            "key": "destinationId",
            "values": []
        },
        {
            "key": "destinationType",
            "value": "All"
        },
        {
            "key": "cruiselineId",
            "values": []
        },
        {
            "key": "shipId",
            "values": []
        },
        {
            "key": "departurePortCode",
            "values": []
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 01 Feb 2023 09:27:40 GMT
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
    "total": 21052,
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
        "id": 1324056,
        "code": "MR20230202CPVCP1",
        "name": "Caribbean And Antilles, 10 Nights",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "12-Feb-2023",
        "itinerary": {
          "id": 361528,
          "duration": 10,
          "departure": {
            "code": "XPC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "XPC",
            "type": "CruisePort"
          },
          "portsOfCalls": "Port Canaveral (Orlando) United States|Ocean Cay Msc Marine ReserveBahamas|Ocean Cay Msc Marine ReserveBahamas|Port Canaveral (Orlando) United States|NassauBahamas|Ocean Cay Msc Marine ReserveBahamas|Belize City Belize|Cozumel Mexico|Port Canaveral (Orlando) United States",
          "normalizedPortsOfCall": "XPC|OCAY|XPC|NAS|OCAY|BZE|CZM|XPC",
          "mapPath": "/content/images/Itineraries/XPC_OCC_XPC_NAS_OCC_BZE_CZM_XPC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/XPC_OCC_XPC_NAS_OCC_BZE_CZM_XPC.jpg"
        },
        "uniqueItineraryId": "361528_13725__10",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 759
              },
              {
                "name": "Outside",
                "value": 919
              },
              {
                "name": "Balcony",
                "value": 979
              },
              {
                "name": "Suite",
                "value": 3179
              },
              {
                "code": "PortCharge",
                "value": 200
              },
              {
                "code": "CruiseTax",
                "value": 253.15
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
        "arrivalDateTime": "12-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "12-Feb-2023",
        "voyageId": "MR20230202CPVCP1",
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
        "cruiseDuration": 10,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          7
        ]
      },
      {
        "id": 1270895,
        "code": "793086793215",
        "name": "The Roundtrip Voyage",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "13-Feb-2023",
        "itinerary": {
          "id": 342635,
          "duration": 11,
          "departure": {
            "code": "BGO",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BGO",
            "type": "CruisePort"
          },
          "portsOfCalls": "Bergen|Flor|Maly|Torvik|Lesund|Molde|Kristiansund|Trondheim|Rrvik|Brnnysund|Sandnessjen|Nesna|Rnes|Bod|Stamsund|Svolvr|Stokmarknes|Sortland|Risyhamn|Harstad|Finnsnes|Troms|Skjervy|Ksfjord|Hammerfest|Havysund|Honningsvg|Kjllefjord|Mehamn|Berlevg|Btsfjord|Vard|Vads|Kirkenes|Vard|Btsfjord|Berlevg|Mehamn|Kjllefjord|Honningsvg|Havysund|Hammerfest|Ksfjord|Skjervy|Troms|Troms|Finnsnes|Harstad|Risyhamn|Sortland|Stokmarknes|Svolvr|Stamsund|Bod|Rnes|Nesna|Sandnessjen|Brnnysund|Rrvik|Trondheim|Kristiansund|Molde|Lesund|Torvik|Maly|Flor|Bergen"
        },
        "uniqueItineraryId": "342635_13441__11",
        "prices": [],
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
        "arrivalDateTime": "13-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "13-Feb-2023",
        "voyageId": "793086793215",
        "stnExternalId": "1430058",
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
        "cruiseDuration": 11,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          39
        ]
      },
      {
        "id": 1330412,
        "code": "M304",
        "name": "Dubai To Singapore",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "14-Feb-2023",
        "itinerary": {
          "id": 348831,
          "duration": 12,
          "departure": {
            "code": "DXB",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SIN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Dubai United Arab Emirates|Muscat Oman|Colombo Sri Lanka|Kuala Lumpur (Tours From Port Kelang) Malaysia|Singapore|Singapore",
          "normalizedPortsOfCall": "DXB|MCT|CMB|XPQ|SIN"
        },
        "uniqueItineraryId": "348831_118__12",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2899
              },
              {
                "name": "Outside",
                "value": 3799
              },
              {
                "name": "Balcony",
                "value": 4099
              },
              {
                "code": "PortCharge",
                "value": 490
              },
              {
                "code": "CruiseTax",
                "value": 110
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
          "id": 19,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          2,
          19
        ],
        "ship": {
          "id": 118,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/12/118/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/12/118/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/12/118/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 12,
            "priority": 100,
            "logoPath": "/content/images/cruise/12/logo_190.png"
          }
        },
        "shipIds": [
          118
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "14-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "14-Feb-2023",
        "voyageId": "M304",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_19.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 12,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          19,
          2
        ]
      },
      {
        "id": 1234324,
        "code": "OOR230202",
        "name": "Australia & New Zealand",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "16-Feb-2023",
        "itinerary": {
          "id": 357326,
          "duration": 14,
          "departure": {
            "code": "SYD",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "AKL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Sydney|Sydney|Melbourne|Tasmania (Hobart)|Dunedin|Christchurch|Wellington|Napier|Rotorua (Tauranga)|Auckland|Auckland",
          "normalizedPortsOfCall": "SYD|MLB|HBA|DUD|CHC|WLG|NPE|TRG|AKL",
          "mapPath": "/content/images/Itineraries/SYD_MEL_HBA_DUD_CHC_WLG_NPE_TRG_AKL.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SYD_MEL_HBA_DUD_CHC_WLG_NPE_TRG_AKL.jpg"
        },
        "uniqueItineraryId": "357326_13785__14",
        "prices": [
          {
            "items": [
              {
                "name": "Balcony",
                "value": 7499
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 15:15:14"
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
          "id": 29,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          29
        ],
        "ship": {
          "id": 13785,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8175/13785/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8175/13785/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8175/13785/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8175,
            "priority": 100,
            "logoPath": "/content/images/cruise/8175/logo_190.png"
          }
        },
        "shipIds": [
          13785
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "16-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "16-Feb-2023",
        "voyageId": "OOR230202",
        "stnExternalId": "1397477",
        "packageTourId": -1,
        "categoryTypes": [
          "Suite",
          "Balcony"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_29.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          29
        ]
      },
      {
        "id": 1271907,
        "code": "M304A",
        "name": "Dubai To Hong Kong",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "23-Feb-2023",
        "itinerary": {
          "id": 350614,
          "duration": 21,
          "departure": {
            "code": "DXB",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "HKG",
            "type": "CruisePort"
          },
          "portsOfCalls": "Dubai United Arab Emirates|Muscat Oman|Colombo Sri Lanka|Kuala Lumpur (Tours From Port Kelang) Malaysia|Singapore|Singapore|Ho Chi Minh City (Tours From  Phu My) Vietnam|Nha Trang Vietnam|Hue Or Da Nang (Tours From    Chan May) Vietnam|Hong Kong China|Hong Kong China"
        },
        "uniqueItineraryId": "350614_118__21",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 4499
              },
              {
                "name": "Outside",
                "value": 5899
              },
              {
                "name": "Balcony",
                "value": 6199
              },
              {
                "code": "PortCharge",
                "value": 735
              },
              {
                "code": "CruiseTax",
                "value": 180.25
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
          "id": 19,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          2,
          19
        ],
        "ship": {
          "id": 118,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/12/118/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/12/118/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/12/118/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 12,
            "priority": 100,
            "logoPath": "/content/images/cruise/12/logo_190.png"
          }
        },
        "shipIds": [
          118
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "23-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "23-Feb-2023",
        "voyageId": "M304A",
        "stnExternalId": "1417120",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_19.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 21,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          19,
          2
        ]
      }
    ],
    "facets": [
      {
        "key": "duration",
        "isRangeFilter": true,
        "values": [
          {
            "count": 702,
            "from": 1,
            "to": 3
          },
          {
            "count": 2736,
            "from": 4,
            "to": 6
          },
          {
            "count": 8899,
            "from": 7,
            "to": 9
          },
          {
            "count": 5009,
            "from": 10,
            "to": 13
          },
          {
            "count": 3706,
            "from": 14
          }
        ]
      },
      {
        "key": "maxOccupancy",
        "isRangeFilter": true,
        "values": [
          {
            "count": 8988,
            "from": 2,
            "to": 2
          },
          {
            "count": 6640,
            "from": 4,
            "to": 4
          },
          {
            "count": 5424,
            "from": 5
          }
        ]
      },
      {
        "key": "packageTour",
        "values": [
          {
            "count": 21052,
            "value": "nonTourPackage"
          }
        ]
      },
      {
        "key": "StnExternalId",
        "values": [
          {
            "count": 12166
          }
        ]
      },
      {
        "key": "hasVrUrl",
        "values": [
          {
            "count": 8450
          }
        ]
      },
      {
        "key": "hasShipVideoUrl",
        "values": [
          {
            "count": 10802
          }
        ]
      },
      {
        "key": "isKidsFriendly",
        "values": [
          {
            "count": 8493
          }
        ]
      },
      {
        "key": "destinationId",
        "values": [
          {
            "count": 5168,
            "value": "15"
          },
          {
            "count": 1992,
            "value": "1"
          },
          {
            "count": 1401,
            "value": "51"
          },
          {
            "count": 1102,
            "value": "41"
          },
          {
            "count": 1029,
            "value": "39"
          },
          {
            "count": 959,
            "value": "9"
          },
          {
            "count": 924,
            "value": "19"
          },
          {
            "count": 913,
            "value": "16"
          },
          {
            "count": 901,
            "value": "7"
          },
          {
            "count": 849,
            "value": "18"
          },
          {
            "count": 750,
            "value": "2"
          },
          {
            "count": 584,
            "value": "10"
          },
          {
            "count": 406,
            "value": "14"
          },
          {
            "count": 385,
            "value": "32"
          },
          {
            "count": 346,
            "value": "38"
          },
          {
            "count": 307,
            "value": "57"
          },
          {
            "count": 238,
            "value": "60"
          },
          {
            "count": 231,
            "value": "29"
          },
          {
            "count": 193,
            "value": "48"
          },
          {
            "count": 185,
            "value": "75"
          },
          {
            "count": 169,
            "value": "13"
          },
          {
            "count": 167,
            "value": "55"
          },
          {
            "count": 133,
            "value": "8"
          },
          {
            "count": 127,
            "value": "56"
          },
          {
            "count": 125,
            "value": "31"
          },
          {
            "count": 123,
            "value": "44"
          },
          {
            "count": 120,
            "value": "26"
          },
          {
            "count": 116,
            "value": "65"
          },
          {
            "count": 113,
            "value": "36"
          },
          {
            "count": 113,
            "value": "40"
          },
          {
            "count": 107,
            "value": "67"
          },
          {
            "count": 96,
            "value": "104"
          },
          {
            "count": 70,
            "value": "73"
          },
          {
            "count": 68,
            "value": "112"
          },
          {
            "count": 67,
            "value": "49"
          },
          {
            "count": 63,
            "value": "34"
          },
          {
            "count": 53,
            "value": "54"
          },
          {
            "count": 49,
            "value": "42"
          },
          {
            "count": 37,
            "value": "47"
          },
          {
            "count": 35,
            "value": "52"
          },
          {
            "count": 35,
            "value": "121"
          },
          {
            "count": 32,
            "value": "74"
          },
          {
            "count": 25,
            "value": "24"
          },
          {
            "count": 25,
            "value": "58"
          },
          {
            "count": 24,
            "value": "68"
          },
          {
            "count": 23,
            "value": "63"
          },
          {
            "count": 21,
            "value": "45"
          },
          {
            "count": 19,
            "value": "21"
          },
          {
            "count": 10,
            "value": "61"
          },
          {
            "count": 7,
            "value": "124"
          },
          {
            "count": 6,
            "value": "105"
          },
          {
            "count": 5,
            "value": "50"
          },
          {
            "count": 3,
            "value": "171"
          },
          {
            "count": 1,
            "value": "53"
          },
          {
            "count": 1,
            "value": "142"
          },
          {
            "count": 1,
            "value": "185"
          }
        ]
      },
      {
        "key": "riverId",
        "values": [
          {
            "count": 1348,
            "value": "76"
          },
          {
            "count": 1170,
            "value": "77"
          },
          {
            "count": 482,
            "value": "78"
          },
          {
            "count": 334,
            "value": "83"
          },
          {
            "count": 276,
            "value": "79"
          },
          {
            "count": 254,
            "value": "86"
          },
          {
            "count": 193,
            "value": "84"
          },
          {
            "count": 146,
            "value": "80"
          },
          {
            "count": 128,
            "value": "81"
          },
          {
            "count": 128,
            "value": "82"
          },
          {
            "count": 96,
            "value": "94"
          },
          {
            "count": 79,
            "value": "85"
          },
          {
            "count": 68,
            "value": "112"
          },
          {
            "count": 54,
            "value": "88"
          },
          {
            "count": 54,
            "value": "99"
          },
          {
            "count": 35,
            "value": "95"
          },
          {
            "count": 25,
            "value": "93"
          },
          {
            "count": 11,
            "value": "102"
          },
          {
            "count": 1,
            "value": "142"
          }
        ]
      },
      {
        "key": "cruiseType",
        "values": [
          {
            "count": 15995,
            "value": "CruiseOnly"
          },
          {
            "count": 5057,
            "value": "CruiseTour"
          }
        ]
      },
      {
        "key": "cruiselineId",
        "values": [
          {
            "count": 2127,
            "value": "8112"
          },
          {
            "count": 2016,
            "value": "982"
          },
          {
            "count": 1840,
            "value": "8121"
          },
          {
            "count": 1696,
            "value": "9155"
          },
          {
            "count": 1589,
            "value": "1"
          },
          {
            "count": 1580,
            "value": "8138"
          },
          {
            "count": 1300,
            "value": "7"
          },
          {
            "count": 1045,
            "value": "8"
          },
          {
            "count": 963,
            "value": "5"
          },
          {
            "count": 902,
            "value": "6"
          },
          {
            "count": 691,
            "value": "2"
          },
          {
            "count": 619,
            "value": "8149"
          },
          {
            "count": 615,
            "value": "8175"
          },
          {
            "count": 507,
            "value": "9191"
          },
          {
            "count": 454,
            "value": "8115"
          },
          {
            "count": 404,
            "value": "11"
          },
          {
            "count": 376,
            "value": "8146"
          },
          {
            "count": 344,
            "value": "8224"
          },
          {
            "count": 325,
            "value": "12"
          },
          {
            "count": 296,
            "value": "3"
          },
          {
            "count": 237,
            "value": "8156"
          },
          {
            "count": 225,
            "value": "8807"
          },
          {
            "count": 208,
            "value": "4"
          },
          {
            "count": 208,
            "value": "8116"
          },
          {
            "count": 198,
            "value": "9"
          },
          {
            "count": 147,
            "value": "1043"
          },
          {
            "count": 61,
            "value": "9204"
          },
          {
            "count": 49,
            "value": "8829"
          },
          {
            "count": 30,
            "value": "8119"
          }
        ]
      },
      {
        "key": "shipId",
        "values": [
          {
            "count": 472,
            "value": "62"
          },
          {
            "count": 451,
            "value": "13762"
          },
          {
            "count": 303,
            "value": "36"
          },
          {
            "count": 296,
            "value": "13250"
          },
          {
            "count": 287,
            "value": "14086"
          },
          {
            "count": 224,
            "value": "14064"
          },
          {
            "count": 195,
            "value": "14998"
          },
          {
            "count": 182,
            "value": "13308"
          },
          {
            "count": 177,
            "value": "14997"
          },
          {
            "count": 172,
            "value": "14304"
          },
          {
            "count": 172,
            "value": "14964"
          },
          {
            "count": 171,
            "value": "13708"
          },
          {
            "count": 165,
            "value": "14538"
          },
          {
            "count": 163,
            "value": "13393"
          },
          {
            "count": 157,
            "value": "13788"
          },
          {
            "count": 147,
            "value": "15044"
          },
          {
            "count": 143,
            "value": "1109"
          },
          {
            "count": 138,
            "value": "13392"
          },
          {
            "count": 134,
            "value": "13528"
          },
          {
            "count": 130,
            "value": "116"
          },
          {
            "count": 130,
            "value": "118"
          },
          {
            "count": 130,
            "value": "14383"
          },
          {
            "count": 128,
            "value": "15108"
          },
          {
            "count": 123,
            "value": "1"
          },
          {
            "count": 121,
            "value": "1108"
          },
          {
            "count": 120,
            "value": "14065"
          },
          {
            "count": 120,
            "value": "14085"
          },
          {
            "count": 119,
            "value": "1110"
          },
          {
            "count": 116,
            "value": "13757"
          },
          {
            "count": 114,
            "value": "15045"
          },
          {
            "count": 111,
            "value": "1116"
          },
          {
            "count": 108,
            "value": "14088"
          },
          {
            "count": 106,
            "value": "13231"
          },
          {
            "count": 106,
            "value": "13710"
          },
          {
            "count": 105,
            "value": "14047"
          },
          {
            "count": 104,
            "value": "1093"
          },
          {
            "count": 103,
            "value": "13299"
          },
          {
            "count": 103,
            "value": "14478"
          },
          {
            "count": 100,
            "value": "1112"
          },
          {
            "count": 100,
            "value": "13510"
          },
          {
            "count": 99,
            "value": "13239"
          },
          {
            "count": 99,
            "value": "13496"
          },
          {
            "count": 99,
            "value": "13670"
          },
          {
            "count": 99,
            "value": "13714"
          },
          {
            "count": 98,
            "value": "17"
          },
          {
            "count": 98,
            "value": "13307"
          },
          {
            "count": 98,
            "value": "14090"
          },
          {
            "count": 97,
            "value": "71"
          },
          {
            "count": 97,
            "value": "13487"
          },
          {
            "count": 97,
            "value": "13824"
          },
          {
            "count": 97,
            "value": "14270"
          },
          {
            "count": 95,
            "value": "14477"
          },
          {
            "count": 94,
            "value": "14060"
          },
          {
            "count": 93,
            "value": "13306"
          },
          {
            "count": 93,
            "value": "14014"
          },
          {
            "count": 92,
            "value": "1105"
          },
          {
            "count": 91,
            "value": "13509"
          },
          {
            "count": 90,
            "value": "13490"
          },
          {
            "count": 89,
            "value": "13233"
          },
          {
            "count": 89,
            "value": "13649"
          },
          {
            "count": 88,
            "value": "13309"
          },
          {
            "count": 88,
            "value": "13786"
          },
          {
            "count": 87,
            "value": "1096"
          },
          {
            "count": 86,
            "value": "14740"
          },
          {
            "count": 85,
            "value": "14084"
          },
          {
            "count": 84,
            "value": "13825"
          },
          {
            "count": 83,
            "value": "14091"
          },
          {
            "count": 82,
            "value": "13653"
          },
          {
            "count": 81,
            "value": "13867"
          },
          {
            "count": 80,
            "value": "135"
          },
          {
            "count": 80,
            "value": "13627"
          },
          {
            "count": 80,
            "value": "13669"
          },
          {
            "count": 79,
            "value": "13237"
          },
          {
            "count": 78,
            "value": "13507"
          },
          {
            "count": 78,
            "value": "13734"
          },
          {
            "count": 78,
            "value": "14045"
          },
          {
            "count": 75,
            "value": "13696"
          },
          {
            "count": 74,
            "value": "13695"
          },
          {
            "count": 74,
            "value": "13772"
          },
          {
            "count": 74,
            "value": "15087"
          },
          {
            "count": 74,
            "value": "15127"
          },
          {
            "count": 72,
            "value": "13697"
          },
          {
            "count": 71,
            "value": "1163"
          },
          {
            "count": 70,
            "value": "13522"
          },
          {
            "count": 69,
            "value": "5"
          },
          {
            "count": 69,
            "value": "1104"
          },
          {
            "count": 69,
            "value": "13523"
          },
          {
            "count": 68,
            "value": "14533"
          },
          {
            "count": 68,
            "value": "14535"
          },
          {
            "count": 68,
            "value": "14835"
          },
          {
            "count": 68,
            "value": "15090"
          },
          {
            "count": 67,
            "value": "13256"
          },
          {
            "count": 67,
            "value": "13650"
          },
          {
            "count": 66,
            "value": "1181"
          },
          {
            "count": 65,
            "value": "1191"
          },
          {
            "count": 65,
            "value": "13380"
          },
          {
            "count": 65,
            "value": "13712"
          },
          {
            "count": 65,
            "value": "13797"
          },
          {
            "count": 65,
            "value": "14073"
          },
          {
            "count": 65,
            "value": "14471"
          },
          {
            "count": 65,
            "value": "14965"
          },
          {
            "count": 64,
            "value": "3"
          },
          {
            "count": 64,
            "value": "13716"
          },
          {
            "count": 64,
            "value": "14046"
          },
          {
            "count": 64,
            "value": "14472"
          },
          {
            "count": 64,
            "value": "14719"
          },
          {
            "count": 63,
            "value": "1182"
          },
          {
            "count": 63,
            "value": "13385"
          },
          {
            "count": 63,
            "value": "13387"
          },
          {
            "count": 62,
            "value": "1100"
          },
          {
            "count": 62,
            "value": "13500"
          },
          {
            "count": 62,
            "value": "13773"
          },
          {
            "count": 61,
            "value": "13437"
          },
          {
            "count": 61,
            "value": "13441"
          },
          {
            "count": 61,
            "value": "13785"
          },
          {
            "count": 61,
            "value": "14803"
          },
          {
            "count": 61,
            "value": "15110"
          },
          {
            "count": 60,
            "value": "4"
          },
          {
            "count": 60,
            "value": "14109"
          },
          {
            "count": 60,
            "value": "14475"
          },
          {
            "count": 59,
            "value": "13439"
          },
          {
            "count": 59,
            "value": "14512"
          },
          {
            "count": 59,
            "value": "14712"
          },
          {
            "count": 58,
            "value": "6"
          },
          {
            "count": 58,
            "value": "13240"
          },
          {
            "count": 58,
            "value": "13386"
          },
          {
            "count": 58,
            "value": "13796"
          },
          {
            "count": 58,
            "value": "14713"
          },
          {
            "count": 58,
            "value": "14714"
          },
          {
            "count": 57,
            "value": "13236"
          },
          {
            "count": 57,
            "value": "13443"
          },
          {
            "count": 57,
            "value": "13608"
          },
          {
            "count": 57,
            "value": "13645"
          },
          {
            "count": 57,
            "value": "13993"
          },
          {
            "count": 57,
            "value": "14504"
          },
          {
            "count": 57,
            "value": "14532"
          },
          {
            "count": 57,
            "value": "14698"
          },
          {
            "count": 57,
            "value": "15089"
          },
          {
            "count": 56,
            "value": "13281"
          },
          {
            "count": 56,
            "value": "13486"
          },
          {
            "count": 56,
            "value": "14006"
          },
          {
            "count": 56,
            "value": "14110"
          },
          {
            "count": 56,
            "value": "14155"
          },
          {
            "count": 56,
            "value": "15026"
          },
          {
            "count": 56,
            "value": "15035"
          },
          {
            "count": 56,
            "value": "15058"
          },
          {
            "count": 55,
            "value": "13646"
          },
          {
            "count": 55,
            "value": "13725"
          },
          {
            "count": 55,
            "value": "13731"
          },
          {
            "count": 55,
            "value": "14089"
          },
          {
            "count": 54,
            "value": "1179"
          },
          {
            "count": 54,
            "value": "13288"
          },
          {
            "count": 54,
            "value": "13658"
          },
          {
            "count": 54,
            "value": "13732"
          },
          {
            "count": 54,
            "value": "14087"
          },
          {
            "count": 54,
            "value": "14476"
          },
          {
            "count": 54,
            "value": "15159"
          },
          {
            "count": 53,
            "value": "1097"
          },
          {
            "count": 53,
            "value": "13711"
          },
          {
            "count": 53,
            "value": "14390"
          },
          {
            "count": 53,
            "value": "15031"
          },
          {
            "count": 52,
            "value": "13383"
          },
          {
            "count": 52,
            "value": "13717"
          },
          {
            "count": 52,
            "value": "14393"
          },
          {
            "count": 51,
            "value": "37"
          },
          {
            "count": 51,
            "value": "1117"
          },
          {
            "count": 51,
            "value": "14328"
          },
          {
            "count": 51,
            "value": "14723"
          },
          {
            "count": 51,
            "value": "15014"
          },
          {
            "count": 51,
            "value": "15065"
          },
          {
            "count": 50,
            "value": "14717"
          },
          {
            "count": 50,
            "value": "15021"
          },
          {
            "count": 49,
            "value": "13232"
          },
          {
            "count": 49,
            "value": "13442"
          },
          {
            "count": 49,
            "value": "13761"
          },
          {
            "count": 49,
            "value": "14106"
          },
          {
            "count": 49,
            "value": "14492"
          },
          {
            "count": 49,
            "value": "15020"
          },
          {
            "count": 48,
            "value": "1159"
          },
          {
            "count": 47,
            "value": "1176"
          },
          {
            "count": 47,
            "value": "13713"
          },
          {
            "count": 46,
            "value": "18"
          },
          {
            "count": 46,
            "value": "32"
          },
          {
            "count": 46,
            "value": "13289"
          },
          {
            "count": 46,
            "value": "13858"
          },
          {
            "count": 46,
            "value": "14948"
          },
          {
            "count": 45,
            "value": "1190"
          },
          {
            "count": 45,
            "value": "13672"
          },
          {
            "count": 45,
            "value": "13673"
          },
          {
            "count": 45,
            "value": "15022"
          },
          {
            "count": 44,
            "value": "13449"
          },
          {
            "count": 44,
            "value": "13471"
          },
          {
            "count": 44,
            "value": "15174"
          },
          {
            "count": 43,
            "value": "21"
          },
          {
            "count": 43,
            "value": "24"
          },
          {
            "count": 43,
            "value": "58"
          },
          {
            "count": 43,
            "value": "13768"
          },
          {
            "count": 43,
            "value": "15071"
          },
          {
            "count": 43,
            "value": "15130"
          },
          {
            "count": 41,
            "value": "13255"
          },
          {
            "count": 41,
            "value": "13633"
          },
          {
            "count": 41,
            "value": "13760"
          },
          {
            "count": 41,
            "value": "14534"
          },
          {
            "count": 40,
            "value": "33"
          },
          {
            "count": 40,
            "value": "13472"
          },
          {
            "count": 40,
            "value": "13630"
          },
          {
            "count": 40,
            "value": "13660"
          },
          {
            "count": 40,
            "value": "13661"
          },
          {
            "count": 40,
            "value": "13766"
          },
          {
            "count": 40,
            "value": "15008"
          },
          {
            "count": 40,
            "value": "15041"
          },
          {
            "count": 39,
            "value": "31"
          },
          {
            "count": 39,
            "value": "13616"
          },
          {
            "count": 39,
            "value": "13722"
          },
          {
            "count": 39,
            "value": "13765"
          },
          {
            "count": 39,
            "value": "14508"
          },
          {
            "count": 39,
            "value": "15015"
          },
          {
            "count": 38,
            "value": "1098"
          },
          {
            "count": 38,
            "value": "13537"
          },
          {
            "count": 38,
            "value": "13539"
          },
          {
            "count": 38,
            "value": "13614"
          },
          {
            "count": 38,
            "value": "13681"
          },
          {
            "count": 38,
            "value": "13682"
          },
          {
            "count": 38,
            "value": "13719"
          },
          {
            "count": 38,
            "value": "13767"
          },
          {
            "count": 38,
            "value": "14058"
          },
          {
            "count": 38,
            "value": "14511"
          },
          {
            "count": 37,
            "value": "30"
          },
          {
            "count": 37,
            "value": "13465"
          },
          {
            "count": 37,
            "value": "14038"
          },
          {
            "count": 37,
            "value": "14056"
          },
          {
            "count": 37,
            "value": "15004"
          },
          {
            "count": 36,
            "value": "13758"
          },
          {
            "count": 36,
            "value": "14053"
          },
          {
            "count": 36,
            "value": "14718"
          },
          {
            "count": 35,
            "value": "1187"
          },
          {
            "count": 35,
            "value": "13286"
          },
          {
            "count": 35,
            "value": "13372"
          },
          {
            "count": 35,
            "value": "13538"
          },
          {
            "count": 35,
            "value": "13613"
          },
          {
            "count": 35,
            "value": "13615"
          },
          {
            "count": 35,
            "value": "13736"
          },
          {
            "count": 35,
            "value": "13769"
          },
          {
            "count": 35,
            "value": "13774"
          },
          {
            "count": 35,
            "value": "13775"
          },
          {
            "count": 35,
            "value": "14059"
          },
          {
            "count": 34,
            "value": "1161"
          },
          {
            "count": 34,
            "value": "13296"
          },
          {
            "count": 34,
            "value": "13618"
          },
          {
            "count": 34,
            "value": "13621"
          },
          {
            "count": 34,
            "value": "13622"
          },
          {
            "count": 34,
            "value": "15011"
          },
          {
            "count": 34,
            "value": "15024"
          },
          {
            "count": 33,
            "value": "13623"
          },
          {
            "count": 33,
            "value": "13624"
          },
          {
            "count": 33,
            "value": "13723"
          },
          {
            "count": 33,
            "value": "14055"
          },
          {
            "count": 33,
            "value": "14072"
          },
          {
            "count": 33,
            "value": "14509"
          },
          {
            "count": 33,
            "value": "14510"
          },
          {
            "count": 33,
            "value": "15012"
          },
          {
            "count": 32,
            "value": "1188"
          },
          {
            "count": 32,
            "value": "13294"
          },
          {
            "count": 32,
            "value": "13542"
          },
          {
            "count": 32,
            "value": "13543"
          },
          {
            "count": 32,
            "value": "13675"
          },
          {
            "count": 32,
            "value": "13793"
          },
          {
            "count": 32,
            "value": "14516"
          },
          {
            "count": 32,
            "value": "14517"
          },
          {
            "count": 32,
            "value": "14829"
          },
          {
            "count": 32,
            "value": "15019"
          },
          {
            "count": 31,
            "value": "1183"
          },
          {
            "count": 31,
            "value": "13440"
          },
          {
            "count": 31,
            "value": "13674"
          },
          {
            "count": 31,
            "value": "15043"
          },
          {
            "count": 31,
            "value": "15112"
          },
          {
            "count": 30,
            "value": "13297"
          },
          {
            "count": 30,
            "value": "13447"
          },
          {
            "count": 30,
            "value": "13721"
          },
          {
            "count": 30,
            "value": "15029"
          },
          {
            "count": 29,
            "value": "13448"
          },
          {
            "count": 29,
            "value": "14514"
          },
          {
            "count": 29,
            "value": "14949"
          },
          {
            "count": 29,
            "value": "15037"
          },
          {
            "count": 29,
            "value": "15040"
          },
          {
            "count": 28,
            "value": "13444"
          },
          {
            "count": 28,
            "value": "13477"
          },
          {
            "count": 27,
            "value": "13576"
          },
          {
            "count": 27,
            "value": "14295"
          },
          {
            "count": 27,
            "value": "15023"
          },
          {
            "count": 26,
            "value": "114"
          },
          {
            "count": 26,
            "value": "1162"
          },
          {
            "count": 26,
            "value": "13295"
          },
          {
            "count": 26,
            "value": "13469"
          },
          {
            "count": 26,
            "value": "13617"
          },
          {
            "count": 25,
            "value": "13287"
          },
          {
            "count": 25,
            "value": "13470"
          },
          {
            "count": 25,
            "value": "14302"
          },
          {
            "count": 25,
            "value": "14479"
          },
          {
            "count": 25,
            "value": "15010"
          },
          {
            "count": 24,
            "value": "52"
          },
          {
            "count": 24,
            "value": "13575"
          },
          {
            "count": 22,
            "value": "13536"
          },
          {
            "count": 22,
            "value": "15027"
          },
          {
            "count": 22,
            "value": "15188"
          },
          {
            "count": 21,
            "value": "13541"
          },
          {
            "count": 21,
            "value": "14040"
          },
          {
            "count": 21,
            "value": "14054"
          },
          {
            "count": 21,
            "value": "14057"
          },
          {
            "count": 21,
            "value": "15005"
          },
          {
            "count": 21,
            "value": "15016"
          },
          {
            "count": 21,
            "value": "15141"
          },
          {
            "count": 20,
            "value": "13290"
          },
          {
            "count": 20,
            "value": "13577"
          },
          {
            "count": 20,
            "value": "13612"
          },
          {
            "count": 20,
            "value": "13679"
          },
          {
            "count": 20,
            "value": "13680"
          },
          {
            "count": 20,
            "value": "14043"
          },
          {
            "count": 20,
            "value": "14528"
          },
          {
            "count": 20,
            "value": "15002"
          },
          {
            "count": 20,
            "value": "15109"
          },
          {
            "count": 19,
            "value": "13259"
          },
          {
            "count": 19,
            "value": "13678"
          },
          {
            "count": 19,
            "value": "14435"
          },
          {
            "count": 19,
            "value": "15042"
          },
          {
            "count": 18,
            "value": "13540"
          },
          {
            "count": 18,
            "value": "13676"
          },
          {
            "count": 18,
            "value": "13823"
          },
          {
            "count": 18,
            "value": "15017"
          },
          {
            "count": 18,
            "value": "15030"
          },
          {
            "count": 18,
            "value": "15182"
          },
          {
            "count": 17,
            "value": "13619"
          },
          {
            "count": 17,
            "value": "14275"
          },
          {
            "count": 16,
            "value": "13720"
          },
          {
            "count": 16,
            "value": "13822"
          },
          {
            "count": 16,
            "value": "14118"
          },
          {
            "count": 16,
            "value": "14473"
          },
          {
            "count": 15,
            "value": "13677"
          },
          {
            "count": 15,
            "value": "13685"
          },
          {
            "count": 14,
            "value": "13735"
          },
          {
            "count": 14,
            "value": "15036"
          },
          {
            "count": 14,
            "value": "15126"
          },
          {
            "count": 13,
            "value": "15003"
          },
          {
            "count": 12,
            "value": "15018"
          },
          {
            "count": 12,
            "value": "15032"
          },
          {
            "count": 12,
            "value": "15063"
          },
          {
            "count": 9,
            "value": "15168"
          },
          {
            "count": 8,
            "value": "14759"
          },
          {
            "count": 7,
            "value": "14994"
          },
          {
            "count": 5,
            "value": "15039"
          },
          {
            "count": 3,
            "value": "13573"
          },
          {
            "count": 3,
            "value": "15034"
          },
          {
            "count": 2,
            "value": "15025"
          },
          {
            "count": 1,
            "value": "15013"
          },
          {
            "count": 1,
            "value": "15038"
          }
        ]
      },
      {
        "key": "departurePortCode",
        "values": [
          {
            "count": 1192,
            "value": "AMS"
          },
          {
            "count": 1190,
            "value": "MIA"
          },
          {
            "count": 896,
            "value": "YVR"
          },
          {
            "count": 775,
            "value": "BUD"
          },
          {
            "count": 635,
            "value": "XPC"
          },
          {
            "count": 605,
            "value": "PAR"
          },
          {
            "count": 502,
            "value": "BCN"
          },
          {
            "count": 484,
            "value": "BSL"
          },
          {
            "count": 479,
            "value": "FLL"
          },
          {
            "count": 433,
            "value": "GLS"
          },
          {
            "count": 417,
            "value": "SEA"
          },
          {
            "count": 394,
            "value": "CIV"
          },
          {
            "count": 381,
            "value": "BGO"
          },
          {
            "count": 381,
            "value": "FAI"
          },
          {
            "count": 374,
            "value": "ATH"
          },
          {
            "count": 366,
            "value": "CAI"
          },
          {
            "count": 352,
            "value": "VCE"
          },
          {
            "count": 346,
            "value": "LAX"
          },
          {
            "count": 321,
            "value": "PRG"
          },
          {
            "count": 288,
            "value": "LIS"
          },
          {
            "count": 268,
            "value": "SYD"
          },
          {
            "count": 264,
            "value": "SXB"
          },
          {
            "count": 260,
            "value": "ANC"
          },
          {
            "count": 254,
            "value": "SOU"
          },
          {
            "count": 246,
            "value": "REP"
          },
          {
            "count": 234,
            "value": "CPT"
          },
          {
            "count": 223,
            "value": "NYC"
          },
          {
            "count": 207,
            "value": "VIE"
          },
          {
            "count": 193,
            "value": "GOA"
          },
          {
            "count": 193,
            "value": "KUSA"
          },
          {
            "count": 187,
            "value": "JNB"
          },
          {
            "count": 184,
            "value": "OPO"
          },
          {
            "count": 182,
            "value": "SGN"
          },
          {
            "count": 181,
            "value": "BA1"
          },
          {
            "count": 177,
            "value": "BUH"
          },
          {
            "count": 176,
            "value": "BOD"
          },
          {
            "count": 166,
            "value": "TPA"
          },
          {
            "count": 163,
            "value": "HAN"
          },
          {
            "count": 149,
            "value": "UIO"
          },
          {
            "count": 141,
            "value": "MRS"
          },
          {
            "count": 139,
            "value": "IST"
          },
          {
            "count": 136,
            "value": "REK"
          },
          {
            "count": 135,
            "value": "HAM"
          },
          {
            "count": 134,
            "value": "LIM"
          },
          {
            "count": 134,
            "value": "MSY"
          },
          {
            "count": 118,
            "value": "CPH"
          },
          {
            "count": 113,
            "value": "PIRA"
          },
          {
            "count": 109,
            "value": "AVN"
          },
          {
            "count": 109,
            "value": "ZPM"
          },
          {
            "count": 102,
            "value": "NCE"
          },
          {
            "count": 100,
            "value": "VILS"
          },
          {
            "count": 98,
            "value": "BUE"
          },
          {
            "count": 97,
            "value": "ZRH"
          },
          {
            "count": 96,
            "value": "SJU"
          },
          {
            "count": 91,
            "value": "CHS"
          },
          {
            "count": 91,
            "value": "EWR"
          },
          {
            "count": 87,
            "value": "BGI"
          },
          {
            "count": 87,
            "value": "ZPF"
          },
          {
            "count": 86,
            "value": "LYS"
          },
          {
            "count": 81,
            "value": "BRI"
          },
          {
            "count": 81,
            "value": "LAVR"
          },
          {
            "count": 78,
            "value": "BER"
          },
          {
            "count": 78,
            "value": "SIN"
          },
          {
            "count": 73,
            "value": "NUE"
          },
          {
            "count": 67,
            "value": "PSLR"
          },
          {
            "count": 67,
            "value": "QQD"
          },
          {
            "count": 64,
            "value": "DEG"
          },
          {
            "count": 63,
            "value": "BWI"
          },
          {
            "count": 61,
            "value": "AKL"
          },
          {
            "count": 61,
            "value": "MUC"
          },
          {
            "count": 60,
            "value": "KKN"
          },
          {
            "count": 60,
            "value": "LYR"
          },
          {
            "count": 60,
            "value": "NAP"
          },
          {
            "count": 60,
            "value": "PMO"
          },
          {
            "count": 60,
            "value": "STO"
          },
          {
            "count": 57,
            "value": "BNE"
          },
          {
            "count": 57,
            "value": "SC1"
          },
          {
            "count": 56,
            "value": "PPT"
          },
          {
            "count": 55,
            "value": "BOS"
          },
          {
            "count": 55,
            "value": "MEL"
          },
          {
            "count": 52,
            "value": "DXB"
          },
          {
            "count": 52,
            "value": "HKG"
          },
          {
            "count": 47,
            "value": "HFA"
          },
          {
            "count": 47,
            "value": "SWD"
          },
          {
            "count": 46,
            "value": "TYO"
          },
          {
            "count": 45,
            "value": "MAD"
          },
          {
            "count": 44,
            "value": "BKK"
          },
          {
            "count": 43,
            "value": "GIUR"
          },
          {
            "count": 43,
            "value": "USH"
          },
          {
            "count": 42,
            "value": "SFO"
          },
          {
            "count": 42,
            "value": "TRS"
          },
          {
            "count": 41,
            "value": "FRA"
          },
          {
            "count": 41,
            "value": "PMI"
          },
          {
            "count": 41,
            "value": "QCM"
          },
          {
            "count": 40,
            "value": "KEL"
          },
          {
            "count": 38,
            "value": "SAN"
          },
          {
            "count": 37,
            "value": "WH1"
          },
          {
            "count": 36,
            "value": "DEL"
          },
          {
            "count": 35,
            "value": "LMAS"
          },
          {
            "count": 34,
            "value": "NTS"
          },
          {
            "count": 34,
            "value": "SKG"
          },
          {
            "count": 33,
            "value": "SVQ"
          },
          {
            "count": 32,
            "value": "BIO"
          },
          {
            "count": 32,
            "value": "LXR"
          },
          {
            "count": 30,
            "value": "LON"
          },
          {
            "count": 29,
            "value": "LEH"
          },
          {
            "count": 29,
            "value": "MIL"
          },
          {
            "count": 29,
            "value": "REM"
          },
          {
            "count": 29,
            "value": "WPU"
          },
          {
            "count": 29,
            "value": "YOK"
          },
          {
            "count": 28,
            "value": "GNW"
          },
          {
            "count": 28,
            "value": "QME"
          },
          {
            "count": 28,
            "value": "RIO"
          },
          {
            "count": 28,
            "value": "SJDL"
          },
          {
            "count": 28,
            "value": "YQB"
          },
          {
            "count": 27,
            "value": "AGP"
          },
          {
            "count": 27,
            "value": "VLC"
          },
          {
            "count": 26,
            "value": "AOI"
          },
          {
            "count": 26,
            "value": "CEQ"
          },
          {
            "count": 26,
            "value": "MOB"
          },
          {
            "count": 25,
            "value": "BDS"
          },
          {
            "count": 25,
            "value": "FDF"
          },
          {
            "count": 25,
            "value": "PNH"
          },
          {
            "count": 25,
            "value": "SXM"
          },
          {
            "count": 24,
            "value": "DKR"
          },
          {
            "count": 24,
            "value": "LPA"
          },
          {
            "count": 22,
            "value": "COK"
          },
          {
            "count": 22,
            "value": "DPS"
          },
          {
            "count": 22,
            "value": "SSZ"
          },
          {
            "count": 22,
            "value": "VAP"
          },
          {
            "count": 22,
            "value": "ZAF"
          },
          {
            "count": 21,
            "value": "ALC"
          },
          {
            "count": 21,
            "value": "AUH"
          },
          {
            "count": 21,
            "value": "DRW"
          },
          {
            "count": 21,
            "value": "MEM"
          },
          {
            "count": 21,
            "value": "TAR"
          },
          {
            "count": 20,
            "value": "DBV"
          },
          {
            "count": 19,
            "value": "VLT"
          },
          {
            "count": 19,
            "value": "YYC"
          },
          {
            "count": 18,
            "value": "PTP"
          },
          {
            "count": 18,
            "value": "RAN"
          },
          {
            "count": 17,
            "value": "ANR"
          },
          {
            "count": 17,
            "value": "GLA"
          },
          {
            "count": 17,
            "value": "JFM"
          },
          {
            "count": 17,
            "value": "LRM"
          },
          {
            "count": 17,
            "value": "MYTH"
          },
          {
            "count": 17,
            "value": "RTM"
          },
          {
            "count": 17,
            "value": "SCL"
          },
          {
            "count": 16,
            "value": "CHSS"
          },
          {
            "count": 16,
            "value": "KZCH"
          },
          {
            "count": 16,
            "value": "LMK"
          },
          {
            "count": 16,
            "value": "SYR1"
          },
          {
            "count": 16,
            "value": "ZWD"
          },
          {
            "count": 15,
            "value": "DOJ"
          },
          {
            "count": 15,
            "value": "SEZ"
          },
          {
            "count": 15,
            "value": "YMQ"
          },
          {
            "count": 14,
            "value": "GVA"
          },
          {
            "count": 14,
            "value": "OLB"
          },
          {
            "count": 14,
            "value": "TILB"
          },
          {
            "count": 14,
            "value": "VDT"
          },
          {
            "count": 13,
            "value": "BME"
          },
          {
            "count": 13,
            "value": "MANT"
          },
          {
            "count": 13,
            "value": "ZQF"
          },
          {
            "count": 12,
            "value": "BLB"
          },
          {
            "count": 12,
            "value": "DUR"
          },
          {
            "count": 12,
            "value": "JED"
          },
          {
            "count": 12,
            "value": "KRK"
          },
          {
            "count": 12,
            "value": "LUX"
          },
          {
            "count": 12,
            "value": "SAF1"
          },
          {
            "count": 11,
            "value": "AUA"
          },
          {
            "count": 11,
            "value": "BRU"
          },
          {
            "count": 11,
            "value": "CCU"
          },
          {
            "count": 11,
            "value": "OLT"
          },
          {
            "count": 11,
            "value": "ORF"
          },
          {
            "count": 11,
            "value": "ZBR1"
          },
          {
            "count": 10,
            "value": "CNS"
          },
          {
            "count": 10,
            "value": "DUB"
          },
          {
            "count": 10,
            "value": "LNZ"
          },
          {
            "count": 10,
            "value": "MCM"
          },
          {
            "count": 10,
            "value": "MSP"
          },
          {
            "count": 10,
            "value": "MVD"
          },
          {
            "count": 10,
            "value": "SFJ"
          },
          {
            "count": 10,
            "value": "TOS"
          },
          {
            "count": 9,
            "value": "BCON"
          },
          {
            "count": 9,
            "value": "DOH"
          },
          {
            "count": 9,
            "value": "ONX"
          },
          {
            "count": 9,
            "value": "OSL"
          },
          {
            "count": 9,
            "value": "SIG"
          },
          {
            "count": 8,
            "value": "BOM"
          },
          {
            "count": 8,
            "value": "HNL"
          },
          {
            "count": 8,
            "value": "MAO"
          },
          {
            "count": 8,
            "value": "MCZ"
          },
          {
            "count": 8,
            "value": "OSA"
          },
          {
            "count": 7,
            "value": "ADL"
          },
          {
            "count": 7,
            "value": "CHC"
          },
          {
            "count": 7,
            "value": "JNU"
          },
          {
            "count": 7,
            "value": "MDL"
          },
          {
            "count": 7,
            "value": "PTY"
          },
          {
            "count": 7,
            "value": "SZG"
          },
          {
            "count": 7,
            "value": "YHZ"
          },
          {
            "count": 6,
            "value": "ASHD"
          },
          {
            "count": 6,
            "value": "DUD"
          },
          {
            "count": 6,
            "value": "FNC"
          },
          {
            "count": 6,
            "value": "LACH"
          },
          {
            "count": 6,
            "value": "LHR"
          },
          {
            "count": 6,
            "value": "RAV"
          },
          {
            "count": 6,
            "value": "SCDT"
          },
          {
            "count": 6,
            "value": "SSA"
          },
          {
            "count": 6,
            "value": "STL"
          },
          {
            "count": 6,
            "value": "ZAG"
          },
          {
            "count": 6,
            "value": "ZCC"
          },
          {
            "count": 5,
            "value": "ARRE"
          },
          {
            "count": 5,
            "value": "SAAN"
          },
          {
            "count": 5,
            "value": "SPND"
          },
          {
            "count": 5,
            "value": "TRI"
          },
          {
            "count": 5,
            "value": "UKB"
          },
          {
            "count": 5,
            "value": "YBZ"
          },
          {
            "count": 4,
            "value": "AQJ"
          },
          {
            "count": 4,
            "value": "CALL"
          },
          {
            "count": 4,
            "value": "EDI"
          },
          {
            "count": 4,
            "value": "KEEL"
          },
          {
            "count": 4,
            "value": "KGIA"
          },
          {
            "count": 4,
            "value": "PAS"
          },
          {
            "count": 3,
            "value": "ITJ"
          },
          {
            "count": 3,
            "value": "MKE"
          },
          {
            "count": 3,
            "value": "NAN"
          },
          {
            "count": 3,
            "value": "OME"
          },
          {
            "count": 3,
            "value": "RAI"
          },
          {
            "count": 3,
            "value": "SINA"
          },
          {
            "count": 2,
            "value": "AMM"
          },
          {
            "count": 2,
            "value": "CGN"
          },
          {
            "count": 2,
            "value": "CMB"
          },
          {
            "count": 2,
            "value": "ETHA"
          },
          {
            "count": 2,
            "value": "HEL"
          },
          {
            "count": 2,
            "value": "HOFL"
          },
          {
            "count": 2,
            "value": "IQT"
          },
          {
            "count": 2,
            "value": "MCT"
          },
          {
            "count": 2,
            "value": "MRU"
          },
          {
            "count": 2,
            "value": "MTBD"
          },
          {
            "count": 2,
            "value": "ORAN"
          },
          {
            "count": 2,
            "value": "PDL"
          },
          {
            "count": 2,
            "value": "POVS"
          },
          {
            "count": 2,
            "value": "SHA"
          },
          {
            "count": 2,
            "value": "SJO"
          },
          {
            "count": 2,
            "value": "TCI"
          },
          {
            "count": 2,
            "value": "YUL"
          },
          {
            "count": 1,
            "value": "AMAD"
          },
          {
            "count": 1,
            "value": "AYT"
          },
          {
            "count": 1,
            "value": "BZC"
          },
          {
            "count": 1,
            "value": "CAS"
          },
          {
            "count": 1,
            "value": "CLL"
          },
          {
            "count": 1,
            "value": "CTG"
          },
          {
            "count": 1,
            "value": "DRS"
          },
          {
            "count": 1,
            "value": "DYR"
          },
          {
            "count": 1,
            "value": "FAIR"
          },
          {
            "count": 1,
            "value": "FBE"
          },
          {
            "count": 1,
            "value": "FLAM"
          },
          {
            "count": 1,
            "value": "GREE"
          },
          {
            "count": 1,
            "value": "HAB"
          },
          {
            "count": 1,
            "value": "HBA"
          },
          {
            "count": 1,
            "value": "HKT"
          },
          {
            "count": 1,
            "value": "JAP"
          },
          {
            "count": 1,
            "value": "MANA"
          },
          {
            "count": 1,
            "value": "MART"
          },
          {
            "count": 1,
            "value": "MBA"
          },
          {
            "count": 1,
            "value": "MMK"
          },
          {
            "count": 1,
            "value": "MNL"
          },
          {
            "count": 1,
            "value": "PME"
          },
          {
            "count": 1,
            "value": "PUQ"
          },
          {
            "count": 1,
            "value": "QOT"
          },
          {
            "count": 1,
            "value": "ROSY"
          },
          {
            "count": 1,
            "value": "SGT"
          },
          {
            "count": 1,
            "value": "TALC"
          },
          {
            "count": 1,
            "value": "TOKY"
          },
          {
            "count": 1,
            "value": "UAK"
          },
          {
            "count": 1,
            "value": "UKY"
          },
          {
            "count": 1,
            "value": "URO"
          },
          {
            "count": 1,
            "value": "VIF"
          },
          {
            "count": 1,
            "value": "ZAI"
          }
        ]
      },
      {
        "key": "arrivalPortCode",
        "values": [
          {
            "count": 1187,
            "value": "MIA"
          },
          {
            "count": 1034,
            "value": "YVR"
          },
          {
            "count": 1014,
            "value": "AMS"
          },
          {
            "count": 822,
            "value": "BUD"
          },
          {
            "count": 639,
            "value": "XPC"
          },
          {
            "count": 621,
            "value": "PAR"
          },
          {
            "count": 563,
            "value": "BSL"
          },
          {
            "count": 533,
            "value": "BCN"
          },
          {
            "count": 477,
            "value": "FLL"
          },
          {
            "count": 433,
            "value": "GLS"
          },
          {
            "count": 423,
            "value": "CIV"
          },
          {
            "count": 384,
            "value": "ATH"
          },
          {
            "count": 377,
            "value": "BGO"
          },
          {
            "count": 372,
            "value": "VFA"
          },
          {
            "count": 360,
            "value": "VCE"
          },
          {
            "count": 353,
            "value": "SEA"
          },
          {
            "count": 346,
            "value": "PRG"
          },
          {
            "count": 335,
            "value": "LAX"
          },
          {
            "count": 328,
            "value": "OPO"
          },
          {
            "count": 323,
            "value": "CAI"
          },
          {
            "count": 322,
            "value": "FAI"
          },
          {
            "count": 284,
            "value": "SOU"
          },
          {
            "count": 264,
            "value": "ANC"
          },
          {
            "count": 251,
            "value": "SXB"
          },
          {
            "count": 246,
            "value": "SYD"
          },
          {
            "count": 230,
            "value": "NYC"
          },
          {
            "count": 214,
            "value": "SGN"
          },
          {
            "count": 213,
            "value": "GOA"
          },
          {
            "count": 204,
            "value": "VIE"
          },
          {
            "count": 181,
            "value": "BA1"
          },
          {
            "count": 176,
            "value": "REP"
          },
          {
            "count": 166,
            "value": "TPA"
          },
          {
            "count": 150,
            "value": "LIS"
          },
          {
            "count": 148,
            "value": "LAVR"
          },
          {
            "count": 143,
            "value": "BOD"
          },
          {
            "count": 143,
            "value": "IST"
          },
          {
            "count": 143,
            "value": "MRS"
          },
          {
            "count": 137,
            "value": "REK"
          },
          {
            "count": 136,
            "value": "MSY"
          },
          {
            "count": 129,
            "value": "BUH"
          },
          {
            "count": 127,
            "value": "HAM"
          },
          {
            "count": 126,
            "value": "KUSA"
          },
          {
            "count": 122,
            "value": "CPH"
          },
          {
            "count": 118,
            "value": "ZRH"
          },
          {
            "count": 115,
            "value": "HAN"
          },
          {
            "count": 114,
            "value": "PIRA"
          },
          {
            "count": 112,
            "value": "GYE"
          },
          {
            "count": 111,
            "value": "AVN"
          },
          {
            "count": 109,
            "value": "ZPM"
          },
          {
            "count": 108,
            "value": "UIO"
          },
          {
            "count": 102,
            "value": "VILS"
          },
          {
            "count": 99,
            "value": "NCE"
          },
          {
            "count": 95,
            "value": "LYS"
          },
          {
            "count": 91,
            "value": "CHS"
          },
          {
            "count": 91,
            "value": "EWR"
          },
          {
            "count": 88,
            "value": "ZPF"
          },
          {
            "count": 87,
            "value": "BER"
          },
          {
            "count": 87,
            "value": "SJU"
          },
          {
            "count": 85,
            "value": "BKK"
          },
          {
            "count": 84,
            "value": "BGI"
          },
          {
            "count": 83,
            "value": "BUE"
          },
          {
            "count": 81,
            "value": "BRI"
          },
          {
            "count": 80,
            "value": "NUE"
          },
          {
            "count": 76,
            "value": "SIN"
          },
          {
            "count": 75,
            "value": "HALO"
          },
          {
            "count": 74,
            "value": "QCM"
          },
          {
            "count": 72,
            "value": "DEG"
          },
          {
            "count": 69,
            "value": "QQD"
          },
          {
            "count": 67,
            "value": "LIM"
          },
          {
            "count": 65,
            "value": "PSLR"
          },
          {
            "count": 63,
            "value": "BWI"
          },
          {
            "count": 63,
            "value": "KKN"
          },
          {
            "count": 62,
            "value": "LYR"
          },
          {
            "count": 61,
            "value": "NAP"
          },
          {
            "count": 60,
            "value": "PMO"
          },
          {
            "count": 59,
            "value": "BOS"
          },
          {
            "count": 59,
            "value": "LON"
          },
          {
            "count": 57,
            "value": "SC1"
          },
          {
            "count": 57,
            "value": "STO"
          },
          {
            "count": 56,
            "value": "WH1"
          },
          {
            "count": 54,
            "value": "BNE"
          },
          {
            "count": 54,
            "value": "MEL"
          },
          {
            "count": 53,
            "value": "TYO"
          },
          {
            "count": 51,
            "value": "PPT"
          },
          {
            "count": 50,
            "value": "AKL"
          },
          {
            "count": 50,
            "value": "SWD"
          },
          {
            "count": 47,
            "value": "CCU"
          },
          {
            "count": 47,
            "value": "HKG"
          },
          {
            "count": 46,
            "value": "HFA"
          },
          {
            "count": 46,
            "value": "TRS"
          },
          {
            "count": 45,
            "value": "AMM"
          },
          {
            "count": 45,
            "value": "DXB"
          },
          {
            "count": 43,
            "value": "CPT"
          },
          {
            "count": 43,
            "value": "SFO"
          },
          {
            "count": 42,
            "value": "ANR"
          },
          {
            "count": 41,
            "value": "PMI"
          },
          {
            "count": 39,
            "value": "GIUR"
          },
          {
            "count": 39,
            "value": "USH"
          },
          {
            "count": 38,
            "value": "BBU"
          },
          {
            "count": 36,
            "value": "KEL"
          },
          {
            "count": 34,
            "value": "LMAS"
          },
          {
            "count": 34,
            "value": "NTS"
          },
          {
            "count": 34,
            "value": "REM"
          },
          {
            "count": 34,
            "value": "SAN"
          },
          {
            "count": 34,
            "value": "SKG"
          },
          {
            "count": 33,
            "value": "FRA"
          },
          {
            "count": 33,
            "value": "SVQ"
          },
          {
            "count": 32,
            "value": "LXR"
          },
          {
            "count": 31,
            "value": "LEH"
          },
          {
            "count": 29,
            "value": "GNW"
          },
          {
            "count": 29,
            "value": "YQB"
          },
          {
            "count": 28,
            "value": "SJDL"
          },
          {
            "count": 28,
            "value": "VLC"
          },
          {
            "count": 27,
            "value": "AGP"
          },
          {
            "count": 27,
            "value": "QME"
          },
          {
            "count": 26,
            "value": "CEQ"
          },
          {
            "count": 26,
            "value": "LPA"
          },
          {
            "count": 26,
            "value": "MOB"
          },
          {
            "count": 26,
            "value": "YOK"
          },
          {
            "count": 25,
            "value": "AOI"
          },
          {
            "count": 25,
            "value": "DPS"
          },
          {
            "count": 24,
            "value": "BDS"
          },
          {
            "count": 24,
            "value": "RIO"
          },
          {
            "count": 23,
            "value": "DKR"
          },
          {
            "count": 23,
            "value": "VDT"
          },
          {
            "count": 23,
            "value": "ZAF"
          },
          {
            "count": 22,
            "value": "DBV"
          },
          {
            "count": 22,
            "value": "KTM"
          },
          {
            "count": 22,
            "value": "WPU"
          },
          {
            "count": 21,
            "value": "ALC"
          },
          {
            "count": 21,
            "value": "FDF"
          },
          {
            "count": 21,
            "value": "MEM"
          },
          {
            "count": 20,
            "value": "VAP"
          },
          {
            "count": 19,
            "value": "GLA"
          },
          {
            "count": 19,
            "value": "JFM"
          },
          {
            "count": 19,
            "value": "SSZ"
          },
          {
            "count": 19,
            "value": "SXM"
          },
          {
            "count": 19,
            "value": "TAR"
          },
          {
            "count": 19,
            "value": "VLT"
          },
          {
            "count": 19,
            "value": "ZWD"
          },
          {
            "count": 18,
            "value": "AUH"
          },
          {
            "count": 18,
            "value": "BCON"
          },
          {
            "count": 18,
            "value": "DRW"
          },
          {
            "count": 18,
            "value": "RAN"
          },
          {
            "count": 17,
            "value": "BME"
          },
          {
            "count": 17,
            "value": "PTP"
          },
          {
            "count": 17,
            "value": "RTM"
          },
          {
            "count": 17,
            "value": "SCL"
          },
          {
            "count": 17,
            "value": "SEZ"
          },
          {
            "count": 16,
            "value": "HOFL"
          },
          {
            "count": 16,
            "value": "LRM"
          },
          {
            "count": 16,
            "value": "MAD"
          },
          {
            "count": 16,
            "value": "PNH"
          },
          {
            "count": 16,
            "value": "SYR1"
          },
          {
            "count": 15,
            "value": "YMQ"
          },
          {
            "count": 14,
            "value": "CHSS"
          },
          {
            "count": 14,
            "value": "OLB"
          },
          {
            "count": 14,
            "value": "OLT"
          },
          {
            "count": 14,
            "value": "TILB"
          },
          {
            "count": 14,
            "value": "TOS"
          },
          {
            "count": 13,
            "value": "AUA"
          },
          {
            "count": 13,
            "value": "BLB"
          },
          {
            "count": 13,
            "value": "BRU"
          },
          {
            "count": 13,
            "value": "CNS"
          },
          {
            "count": 13,
            "value": "GVA"
          },
          {
            "count": 12,
            "value": "LNZ"
          },
          {
            "count": 12,
            "value": "MANT"
          },
          {
            "count": 11,
            "value": "ORF"
          },
          {
            "count": 11,
            "value": "SAF1"
          },
          {
            "count": 11,
            "value": "SFJ"
          },
          {
            "count": 11,
            "value": "ZBR1"
          },
          {
            "count": 10,
            "value": "BOM"
          },
          {
            "count": 10,
            "value": "DUB"
          },
          {
            "count": 10,
            "value": "JED"
          },
          {
            "count": 10,
            "value": "MCM"
          },
          {
            "count": 10,
            "value": "MSP"
          },
          {
            "count": 9,
            "value": "DUR"
          },
          {
            "count": 9,
            "value": "HNL"
          },
          {
            "count": 9,
            "value": "MAO"
          },
          {
            "count": 8,
            "value": "ADL"
          },
          {
            "count": 8,
            "value": "LUX"
          },
          {
            "count": 8,
            "value": "MVD"
          },
          {
            "count": 8,
            "value": "ONX"
          },
          {
            "count": 8,
            "value": "OSA"
          },
          {
            "count": 8,
            "value": "OSL"
          },
          {
            "count": 8,
            "value": "SIG"
          },
          {
            "count": 7,
            "value": "BRIA"
          },
          {
            "count": 7,
            "value": "CHC"
          },
          {
            "count": 7,
            "value": "DOH"
          },
          {
            "count": 7,
            "value": "DOJ"
          },
          {
            "count": 7,
            "value": "JNU"
          },
          {
            "count": 7,
            "value": "KRK"
          },
          {
            "count": 7,
            "value": "QMZ"
          },
          {
            "count": 7,
            "value": "SZG"
          },
          {
            "count": 7,
            "value": "ZQF"
          },
          {
            "count": 6,
            "value": "ASHD"
          },
          {
            "count": 6,
            "value": "CALL"
          },
          {
            "count": 6,
            "value": "COCM"
          },
          {
            "count": 6,
            "value": "FNC"
          },
          {
            "count": 6,
            "value": "KZCH"
          },
          {
            "count": 6,
            "value": "LACH"
          },
          {
            "count": 6,
            "value": "LHR"
          },
          {
            "count": 6,
            "value": "MCZ"
          },
          {
            "count": 6,
            "value": "MYTH"
          },
          {
            "count": 6,
            "value": "RAV"
          },
          {
            "count": 6,
            "value": "SCDT"
          },
          {
            "count": 6,
            "value": "STL"
          },
          {
            "count": 6,
            "value": "ZAG"
          },
          {
            "count": 6,
            "value": "ZCC"
          },
          {
            "count": 5,
            "value": "AQJ"
          },
          {
            "count": 5,
            "value": "ARRE"
          },
          {
            "count": 5,
            "value": "DUD"
          },
          {
            "count": 5,
            "value": "NVS"
          },
          {
            "count": 5,
            "value": "PAS"
          },
          {
            "count": 5,
            "value": "PTY"
          },
          {
            "count": 5,
            "value": "SAAN"
          },
          {
            "count": 5,
            "value": "SETE"
          },
          {
            "count": 5,
            "value": "SPND"
          },
          {
            "count": 5,
            "value": "YBZ"
          },
          {
            "count": 4,
            "value": "EDI"
          },
          {
            "count": 4,
            "value": "KEEL"
          },
          {
            "count": 4,
            "value": "KGIA"
          },
          {
            "count": 4,
            "value": "MDL"
          },
          {
            "count": 4,
            "value": "SSA"
          },
          {
            "count": 4,
            "value": "TRI"
          },
          {
            "count": 3,
            "value": "BPE"
          },
          {
            "count": 3,
            "value": "ITJ"
          },
          {
            "count": 3,
            "value": "JAP"
          },
          {
            "count": 3,
            "value": "MART"
          },
          {
            "count": 3,
            "value": "MIL"
          },
          {
            "count": 3,
            "value": "MKE"
          },
          {
            "count": 3,
            "value": "NAN"
          },
          {
            "count": 3,
            "value": "RUDE"
          },
          {
            "count": 3,
            "value": "SHA"
          },
          {
            "count": 3,
            "value": "UKB"
          },
          {
            "count": 3,
            "value": "YHZ"
          },
          {
            "count": 2,
            "value": "BREI"
          },
          {
            "count": 2,
            "value": "CGN"
          },
          {
            "count": 2,
            "value": "CMB"
          },
          {
            "count": 2,
            "value": "ETHA"
          },
          {
            "count": 2,
            "value": "GLC"
          },
          {
            "count": 2,
            "value": "HBA"
          },
          {
            "count": 2,
            "value": "HEL"
          },
          {
            "count": 2,
            "value": "IQT"
          },
          {
            "count": 2,
            "value": "MHG"
          },
          {
            "count": 2,
            "value": "MRU"
          },
          {
            "count": 2,
            "value": "OME"
          },
          {
            "count": 2,
            "value": "ORAN"
          },
          {
            "count": 2,
            "value": "PDL"
          },
          {
            "count": 2,
            "value": "POVS"
          },
          {
            "count": 2,
            "value": "RAI"
          },
          {
            "count": 2,
            "value": "ROSY"
          },
          {
            "count": 2,
            "value": "TCI"
          },
          {
            "count": 2,
            "value": "YUL"
          },
          {
            "count": 1,
            "value": "AVV"
          },
          {
            "count": 1,
            "value": "AYT"
          },
          {
            "count": 1,
            "value": "BBO"
          },
          {
            "count": 1,
            "value": "CLL"
          },
          {
            "count": 1,
            "value": "CTG"
          },
          {
            "count": 1,
            "value": "DRS"
          },
          {
            "count": 1,
            "value": "DYR"
          },
          {
            "count": 1,
            "value": "FAIR"
          },
          {
            "count": 1,
            "value": "FLAM"
          },
          {
            "count": 1,
            "value": "FUK"
          },
          {
            "count": 1,
            "value": "HAB"
          },
          {
            "count": 1,
            "value": "IJM"
          },
          {
            "count": 1,
            "value": "LIV1"
          },
          {
            "count": 1,
            "value": "MANA"
          },
          {
            "count": 1,
            "value": "MBA"
          },
          {
            "count": 1,
            "value": "MCT"
          },
          {
            "count": 1,
            "value": "MMK"
          },
          {
            "count": 1,
            "value": "PME"
          },
          {
            "count": 1,
            "value": "PUQ"
          },
          {
            "count": 1,
            "value": "PVR"
          },
          {
            "count": 1,
            "value": "SGT"
          },
          {
            "count": 1,
            "value": "SJO"
          },
          {
            "count": 1,
            "value": "SLSD"
          },
          {
            "count": 1,
            "value": "TALC"
          },
          {
            "count": 1,
            "value": "TOKY"
          },
          {
            "count": 1,
            "value": "UAK"
          },
          {
            "count": 1,
            "value": "UKY"
          },
          {
            "count": 1,
            "value": "URO"
          },
          {
            "count": 1,
            "value": "VIF"
          },
          {
            "count": 1,
            "value": "ZAI"
          },
          {
            "count": 1,
            "value": "ZNZ"
          }
        ]
      },
      {
        "key": "promoCode",
        "values": [
          {
            "count": 6377,
            "value": "DISCOUNT"
          },
          {
            "count": 2316,
            "value": "WIFI"
          },
          {
            "count": 2087,
            "value": "BEV"
          },
          {
            "count": 2087,
            "value": "DINING"
          },
          {
            "count": 2057,
            "value": "NR"
          },
          {
            "count": 1833,
            "value": "SHOREX"
          },
          {
            "count": 1560,
            "value": "NRD"
          },
          {
            "count": 528,
            "value": "BOGO"
          },
          {
            "count": 515,
            "value": "OBC"
          },
          {
            "count": 346,
            "value": "GRATSI"
          },
          {
            "count": 280,
            "value": "KIDSFREE"
          },
          {
            "count": 225,
            "value": "FIT"
          },
          {
            "count": 197,
            "value": "RETREAT"
          },
          {
            "count": 189,
            "value": "ALWAYS"
          },
          {
            "count": 185,
            "value": "ELEVATE"
          },
          {
            "count": 185,
            "value": "INDULGE"
          },
          {
            "count": 15,
            "value": "FREEUPG"
          },
          {
            "count": 9,
            "value": "EBB"
          },
          {
            "count": 2,
            "value": "ADDGSTDISC"
          }
        ]
      },
      {
        "key": "price",
        "isRangeFilter": true,
        "values": [
          {
            "count": 5701,
            "from": 0,
            "to": 1000
          },
          {
            "count": 2072,
            "from": 1001,
            "to": 2000
          },
          {
            "count": 2522,
            "from": 2001,
            "to": 3000
          },
          {
            "count": 2759,
            "from": 3001,
            "to": 4000
          },
          {
            "count": 1762,
            "from": 4001,
            "to": 5000
          },
          {
            "count": 1243,
            "from": 5001,
            "to": 6000
          },
          {
            "count": 3746,
            "from": 6001
          }
        ]
      },
      {
        "key": "departureDateTime",
        "isRangeFilter": true,
        "values": [
          {
            "count": 1,
            "from": "01-Jan-2023",
            "to": "31-Jan-2023"
          },
          {
            "count": 883,
            "from": "01-Feb-2023",
            "to": "28-Feb-2023"
          },
          {
            "count": 1306,
            "from": "01-Mar-2023",
            "to": "31-Mar-2023"
          },
          {
            "count": 1791,
            "from": "01-Apr-2023",
            "to": "30-Apr-2023"
          },
          {
            "count": 2018,
            "from": "01-May-2023",
            "to": "31-May-2023"
          },
          {
            "count": 2048,
            "from": "01-Jun-2023",
            "to": "30-Jun-2023"
          },
          {
            "count": 2270,
            "from": "01-Jul-2023",
            "to": "31-Jul-2023"
          },
          {
            "count": 2219,
            "from": "01-Aug-2023",
            "to": "31-Aug-2023"
          },
          {
            "count": 1943,
            "from": "01-Sep-2023",
            "to": "30-Sep-2023"
          },
          {
            "count": 1738,
            "from": "01-Oct-2023",
            "to": "31-Oct-2023"
          },
          {
            "count": 1035,
            "from": "01-Nov-2023",
            "to": "30-Nov-2023"
          },
          {
            "count": 938,
            "from": "01-Dec-2023",
            "to": "31-Dec-2023"
          },
          {
            "count": 595,
            "from": "01-Jan-2024",
            "to": "31-Jan-2024"
          },
          {
            "count": 543,
            "from": "01-Feb-2024",
            "to": "29-Feb-2024"
          },
          {
            "count": 618,
            "from": "01-Mar-2024",
            "to": "31-Mar-2024"
          },
          {
            "count": 362,
            "from": "01-Apr-2024",
            "to": "30-Apr-2024"
          },
          {
            "count": 139,
            "from": "01-May-2024",
            "to": "31-May-2024"
          },
          {
            "count": 117,
            "from": "01-Jun-2024",
            "to": "30-Jun-2024"
          },
          {
            "count": 102,
            "from": "01-Jul-2024",
            "to": "31-Jul-2024"
          },
          {
            "count": 117,
            "from": "01-Aug-2024",
            "to": "31-Aug-2024"
          },
          {
            "count": 115,
            "from": "01-Sep-2024",
            "to": "30-Sep-2024"
          },
          {
            "count": 88,
            "from": "01-Oct-2024",
            "to": "31-Oct-2024"
          },
          {
            "count": 39,
            "from": "01-Nov-2024",
            "to": "30-Nov-2024"
          },
          {
            "count": 25,
            "from": "01-Dec-2024",
            "to": "31-Dec-2024"
          },
          {
            "count": 2,
            "from": "01-Jan-2025",
            "to": "31-Jan-2025"
          }
        ]
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
