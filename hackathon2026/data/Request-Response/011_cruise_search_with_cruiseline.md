# Cruise Search With CruiseLine

**Path:** Cruise Search > Cruise Search With CruiseLine

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
            "key": "cruiselineId",
            "values": [
                6,
                8,
                982
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
Date: Wed, 01 Feb 2023 09:31:01 GMT
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
    "total": 3963,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
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
      },
      {
        "id": 1333843,
        "code": "SX20230203CPTCPT",
        "name": "South Africa, 3 Nights",
        "startDateTime": "03-Feb-2023",
        "endDateTime": "06-Feb-2023",
        "itinerary": {
          "id": 350280,
          "duration": 3,
          "departure": {
            "code": "CPT",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CPT",
            "type": "CruisePort"
          },
          "portsOfCalls": "Cape Town South Africa|Mossel Bay South Africa|Mossel Bay South Africa|Cape Town South Africa",
          "normalizedPortsOfCall": "CPT|MZY|CPT",
          "mapPath": "/content/images/Itineraries/CPT_MZY_CPT.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CPT_MZY_CPT.jpg"
        },
        "uniqueItineraryId": "350280_1112__3",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 109
              },
              {
                "name": "Outside",
                "value": 179
              },
              {
                "name": "Balcony",
                "value": 329
              },
              {
                "name": "Suite",
                "value": 509
              },
              {
                "code": "PortCharge",
                "value": 60
              },
              {
                "code": "CruiseTax",
                "value": 23.48
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
          "id": 1112,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/1112/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/1112/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/1112/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Sinfonia/en-gl/index.html",
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
          1112
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "03-Feb-2023",
        "arrivalDateTime": "06-Feb-2023",
        "cruisePackageDepartureDateTime": "03-Feb-2023",
        "cruisePackageArrivalDateTime": "06-Feb-2023",
        "voyageId": "SX20230203CPTCPT",
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
        "id": 1327927,
        "code": "VI20230204BCNBCN",
        "name": "Mediterranean, 7 Nights",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 362199,
          "duration": 7,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Marseille (Provence) France|Genoa (Portofino) Italy|La Spezia (Cinque Terre) Italy|Naples (Pompeii) Italy|Palma De Mallorca (Baleari Is) Spain|Barcelona Spain",
          "normalizedPortsOfCall": "BCN|MRS|GOA|LPZ|NAP|PMI|BCN",
          "mapPath": "/content/images/Itineraries/BCN_MRS_GOA_LPZ_NAP_PMI_BCN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_MRS_GOA_LPZ_NAP_PMI_BCN.jpg"
        },
        "uniqueItineraryId": "362199_14390__7",
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
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "VI20230204BCNBCN",
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
        "id": 1327611,
        "code": "SP20230204JEDJED",
        "name": "Saudi Arabia & Red Sea, 7 Nights",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 362628,
          "duration": 7,
          "departure": {
            "code": "JED",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "JED",
            "type": "CruisePort"
          },
          "portsOfCalls": "Jeddah Saudi Arabia|Yanbu Al Bahr Saudi Arabia|Al Wajh Saudi Arabia|Aqaba (Petra) Jordan|Safaga Egypt|Jeddah Saudi Arabia",
          "normalizedPortsOfCall": "JED|YNB|ALWJ|AQJ|SAF1|JED",
          "mapPath": "/content/images/Itineraries/JED_YNAL_WAJH_AQJ_SAF_JED.jpg",
          "fallbackMapPath": "/content/images/Itineraries/JED_YNAL_WAJH_AQJ_SAF_JED.jpg"
        },
        "uniqueItineraryId": "362628_13239__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 299
              },
              {
                "name": "Outside",
                "value": 409
              },
              {
                "name": "Balcony",
                "value": 519
              },
              {
                "name": "Suite",
                "value": 949
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
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "SP20230204JEDJED",
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
        "id": 1327519,
        "code": "SH20230204SSZSSZ",
        "name": "South America, 7 Nights",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 361471,
          "duration": 7,
          "departure": {
            "code": "SSZ",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "SSZ",
            "type": "CruisePort"
          },
          "portsOfCalls": "Santos (Sao Paolo) Brazil|Maceio Brazil|Salvador Brazil|Buzios Brazil|Santos (Sao Paolo) Brazil",
          "normalizedPortsOfCall": "SSZ|MCZ|SSA|BZC|SSZ",
          "mapPath": "/content/images/Itineraries/SSZ_MCZ_SSA_BZC_SSZ.jpg",
          "fallbackMapPath": "/content/images/Itineraries/SSZ_MCZ_SSA_BZC_SSZ.jpg"
        },
        "uniqueItineraryId": "361471_14538__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 798
              },
              {
                "name": "Balcony",
                "value": 1018
              },
              {
                "name": "Suite",
                "value": 1138
              },
              {
                "code": "PortCharge",
                "value": 159
              },
              {
                "code": "CruiseTax",
                "value": 115.65
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
          "id": 32,
          "type": "Destination",
          "priority": 82
        },
        "parentDestinationIds": [
          32
        ],
        "ship": {
          "id": 14538,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/14538/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/14538/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/14538/ship_520.jpg",
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
          14538
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "SH20230204SSZSSZ",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_32.jpg",
        "maxOccupancy": 6,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          32
        ]
      },
      {
        "id": 1327346,
        "code": "AX20230204ITJITJ",
        "name": "South America, 7 Nights",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 361472,
          "duration": 7,
          "departure": {
            "code": "ITJ",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ITJ",
            "type": "CruisePort"
          },
          "portsOfCalls": "Itajai (Balneario Camboriu) Brazil|Punta Del Este Uruguay|Buenos Aires Argentina|Ilhabela Brazil|Itajai (Balneario Camboriu) Brazil",
          "normalizedPortsOfCall": "ITJ|PDP|BUE|ILLH|ITJ",
          "mapPath": "/content/images/Itineraries/ITA_PDP_BUE_IIH_ITA.jpg",
          "fallbackMapPath": "/content/images/Itineraries/ITA_PDP_BUE_IIH_ITA.jpg"
        },
        "uniqueItineraryId": "361472_1104__7",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 589
              },
              {
                "name": "Suite",
                "value": 969
              },
              {
                "code": "PortCharge",
                "value": 60
              },
              {
                "code": "CruiseTax",
                "value": 157.9
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
          "id": 32,
          "type": "Destination",
          "priority": 82
        },
        "parentDestinationIds": [
          32
        ],
        "ship": {
          "id": 1104,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/982/1104/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/982/1104/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/982/1104/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://virtual-tours.msccruises.com/MSC-Armonia/en-gl/index.html",
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
          1104
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "AX20230204ITJITJ",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_32.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          32
        ]
      },
      {
        "id": 1324781,
        "code": "GR20230204MRSMRS",
        "name": "Mediterranean, 7 Nights",
        "startDateTime": "04-Feb-2023",
        "endDateTime": "11-Feb-2023",
        "itinerary": {
          "id": 362627,
          "duration": 7,
          "departure": {
            "code": "MRS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MRS",
            "type": "CruisePort"
          },
          "portsOfCalls": "Marseille (Provence) France|Genoa (Portofino) Italy|Civitavecchia (Rome) Italy|Palermo (Monreale) Italy|Valletta Malta|Barcelona Spain|Marseille (Provence) France",
          "normalizedPortsOfCall": "MRS|GOA|CIV|PMO|VLT|BCN|MRS",
          "mapPath": "/content/images/Itineraries/MRS_GOA_CVV_PMO_VLT_BCN_MRS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/MRS_GOA_CVV_PMO_VLT_BCN_MRS.jpg"
        },
        "uniqueItineraryId": "362627_14091__7",
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
                "value": 70.33
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
        "departureDateTime": "04-Feb-2023",
        "arrivalDateTime": "11-Feb-2023",
        "cruisePackageDepartureDateTime": "04-Feb-2023",
        "cruisePackageArrivalDateTime": "11-Feb-2023",
        "voyageId": "GR20230204MRSMRS",
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
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
