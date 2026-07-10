# Cruise Search With Cruise Only

**Path:** Cruise Search > Cruise Search With Cruise Only

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
            "values": ["CruiseOnly"]
        }       
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 01 Feb 2023 09:38:51 GMT
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
    "total": 15995,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
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
      },
      {
        "id": 1267209,
        "code": "O311",
        "name": "22-Day South America & Antarctica",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "24-Feb-2023",
        "itinerary": {
          "id": 325809,
          "duration": 22,
          "departure": {
            "code": "BUE",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SCL",
            "type": "CruisePort"
          },
          "portsOfCalls": "Buenos Aires Argentina|Buenos Aires Argentina|Montevideo Uruguay|Punta Del Este Uruguay|Puerto Madryn Argentina|Stanley/Falkland Is/Islas Malvinas|Ushuaia Argentina|Punta Arenas Chile|Strait Of Magellan|Puerto Chacabuco Chile|Puerto Montt Chile|San Antonio (Santiago) Chile",
          "normalizedPortsOfCall": "BUE|MVD|PDP|PMY|PSY|USH|PUQ|MGLN|CHBC|PMC|SCL",
          "mapPath": "/content/images/Itineraries/BUE_MVD_PDP_PMY_PSY_CPHN_USH_PUQ_AMG_PCH_PMC_SAAN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BUE_MVD_PDP_PMY_PSY_CPHN_USH_PUQ_AMG_PCH_PMC_SAAN.jpg"
        },
        "uniqueItineraryId": "325809_37__22",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 3319
              },
              {
                "name": "Outside",
                "value": 3619
              },
              {
                "name": "Balcony",
                "value": 5819
              },
              {
                "name": "Suite",
                "value": 8419
              },
              {
                "code": "PortCharge",
                "value": 550
              },
              {
                "code": "CruiseTax",
                "value": 505
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:51:45"
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
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 32,
          "type": "Destination",
          "priority": 82
        },
        "parentDestinationIds": [
          32,
          65
        ],
        "ship": {
          "id": 37,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/37/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/37/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/37/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Grandiosa/en-gl/index.html",
          "hasVrForStateRoom": true,
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 5,
            "priority": 100,
            "logoPath": "/content/images/cruise/5/logo_190.png"
          }
        },
        "shipIds": [
          37
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "02-Feb-2023",
        "arrivalDateTime": "24-Feb-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "24-Feb-2023",
        "voyageId": "O311",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_32.jpg",
        "maxOccupancy": 6,
        "minOccupancy": 1,
        "cruiseDuration": 22,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          32,
          65
        ]
      },
      {
        "id": 1271908,
        "code": "M304B",
        "name": "Dubai To Sydney",
        "startDateTime": "02-Feb-2023",
        "endDateTime": "12-Mar-2023",
        "itinerary": {
          "id": 350615,
          "duration": 38,
          "departure": {
            "code": "DXB",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SYD",
            "type": "CruisePort"
          },
          "portsOfCalls": "Dubai United Arab Emirates|Muscat Oman|Colombo Sri Lanka|Kuala Lumpur (Tours From Port Kelang) Malaysia|Singapore|Singapore|Ho Chi Minh City (Tours From  Phu My) Vietnam|Nha Trang Vietnam|Hue Or Da Nang (Tours From    Chan May) Vietnam|Hong Kong China|Hong Kong China|Bitung Indonesia|Darwin Nt Australia|Whitsunday Island (Tours From Airlie Beach) Qld Australia|Brisbane Qld Australia|Sydney Nsw Australia|Sydney Nsw Australia"
        },
        "uniqueItineraryId": "350615_118__38",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 7499
              },
              {
                "name": "Outside",
                "value": 9299
              },
              {
                "name": "Balcony",
                "value": 9799
              },
              {
                "name": "Suite",
                "value": 26999
              },
              {
                "code": "PortCharge",
                "value": 1330
              },
              {
                "code": "CruiseTax",
                "value": 366.34
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:00:13"
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
          "id": 36,
          "type": "Destination",
          "priority": 200
        },
        "parentDestinationIds": [
          36
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
        "arrivalDateTime": "12-Mar-2023",
        "cruisePackageDepartureDateTime": "02-Feb-2023",
        "cruisePackageArrivalDateTime": "12-Mar-2023",
        "voyageId": "M304B",
        "stnExternalId": "1417121",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_36.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 38,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          36
        ]
      },
      {
        "id": 1333859,
        "code": "OR20230203DURDUR",
        "name": "South Africa, 3 Nights",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 361438,
          "duration": 3,
          "departure": {
            "code": "DUR",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "DUR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Durban South Africa|Portuguese Island (Inhaca Archipelago) Mozambique|Portuguese Island (Inhaca Archipelago) Mozambique|Durban South Africa",
          "normalizedPortsOfCall": "DUR|PTGS|DUR",
          "mapPath": "/content/images/Itineraries/DUR_PGI_DUR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/DUR_PGI_DUR.jpg"
        },
        "uniqueItineraryId": "361438_1110__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 109
              },
              {
                "name": "Outside",
                "value": 169
              },
              {
                "name": "Balcony",
                "value": 249
              },
              {
                "name": "Suite",
                "value": 549
              },
              {
                "code": "PortCharge",
                "value": 60
              },
              {
                "code": "CruiseTax",
                "value": 20.87
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
          "id": 2,
          "type": "Destination",
          "priority": 1000
        },
        "parentDestinationIds": [
          2
        ],
        "ship": {
          "id": 1110,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/1110/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/1110/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/1110/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Orchestra/en-gl/index.html",
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
          1110
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "OR20230203DURDUR",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_2.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 3,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          2
        ]
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
