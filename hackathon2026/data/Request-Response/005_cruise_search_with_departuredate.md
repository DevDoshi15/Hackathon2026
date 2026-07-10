# Cruise Search with DepartureDate

**Path:** Cruise Search > Cruise Search with DepartureDate

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
            "key": "departureDate",
            "ranges": [
                {
                    "from": "23-May-2023",
                    "to": "23-Nov-2023"
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
Date: Fri, 17 Feb 2023 07:39:11 GMT
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
    "total": 13885,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1301292,
        "code": "V324",
        "name": "14-Day Yukon+Denali: Tour Y3l",
        "startDateTime": "17-May-2023",
        "endDateTime": "31-May-2023",
        "itinerary": {
          "id": 359103,
          "duration": 14,
          "departure": {
            "code": "ANC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "TRANSFER ANC AIRPORT/HOTEL|ANCHORAGE AREA HOTEL|MEET YOUR JOURNEY HOST|TRANSFER HOTEL/RAIL DEPOT|MCKINLEY EXPLORER ANCHORAGE/TALKEETNA|MCKINLEY EXPLORER TALKEETNA/DENALI|TRANSFER RAIL DEPOT/HOTEL|MCKINLEY CHALET RESORT|AM TUNDRA WILDERNESS TOUR|DENALI AFTERNOON AT LEISURE|DENALI DAY AT LEISURE|DENALI/FAIRBANKS COACH|PM GOLD DREDGE|WESTMARK FAIRBANKS HOTEL|TRANSFER HOTEL/FAI AIRPORT|AIR FAIRBANKS/DAWSON|TRANSFER YDA AIRPORT/HOTEL|ROUNDTRIP TRANSFERS KLONDIKE SPIRIT|KLONDIKE SPIRIT|WESTMARK INN DAWSON|DAWSON DAY AT LEISURE|DAWSON/WHITEHORSE COACH|LUNCH MINTO/KLONDIKE HWY|WHITEHORSE AREA HOTEL|WHITEHORSE/FRASER COACH|WPYR FRASER/SKAGWAY|TRANSFER RAIL/HOTEL|WESTMARK INN SKAGWAY|SKAGWAY DAY AT LEISURE|TRANSFER HOTEL/SHIP|GOODBYE TO YOUR JOURNEY HOST|SKAGWAY|GLACIER BAY|KETCHIKAN|VANCOUVER|ANCHORAGE AREA HOTEL"
        },
        "uniqueItineraryId": "359103_43__14_t3ay3l",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 3099
              },
              {
                "name": "Outside",
                "value": 3249
              },
              {
                "name": "Suite",
                "value": 3999
              },
              {
                "code": "PortCharge",
                "value": 381
              },
              {
                "code": "CruiseTax",
                "value": 270
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:27:06"
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
          "id": 43,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/43/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/43/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/43/ship_520.jpg",
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
          43
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "24-May-2023",
        "arrivalDateTime": "31-May-2023",
        "cruisePackageDepartureDateTime": "17-May-2023",
        "cruisePackageArrivalDateTime": "31-May-2023",
        "cruiseTourCode": "T3AY3L",
        "voyageId": "V324",
        "stnExternalId": "1454331",
        "packageTourId": -1,
        "categoryTypes": [
          "Outside",
          "Inside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseTourName": "14-Day Yukon+Denali: Tour Y3l"
      },
      {
        "id": 1300580,
        "code": "A317",
        "name": "Voyage Of The Glaciers With Glacier Bay (Southbound)",
        "startDateTime": "17-May-2023",
        "endDateTime": "03-Jun-2023",
        "itinerary": {
          "id": 354444,
          "duration": 17,
          "departure": {
            "code": "FAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fairbanks|Fairbanks|Denali Princess Wilderness Lodge|Denali Princess Wilderness Lodge|Mt Mckinley Princess Wilderness Lodge|Mt Mckinley Princess Wilderness Lodge|Kenai Princess Wilderness Lodge|Kenai Princess Wilderness Lodge|Copper River Princess Wilderness Lodge|Copper River Princess Wilderness Lodge|Whittier|Anchorage (Whittier) Alaska|Skagway Alaska|Juneau Alaska|Ketchikan Alaska|Vancouver Canada",
          "mapPath": "/content/images/Itineraries/FAI_DNL_MCL_KENI_CPPR_WH1_ANC_GBNP_SGY_JNU_KTN_YVR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FAI_DNL_MCL_KENI_CPPR_WH1_ANC_GBNP_SGY_JNU_KTN_YVR.jpg"
        },
        "uniqueItineraryId": "354444_62__17_t3atb1",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 4768
              },
              {
                "name": "Outside",
                "value": 4868
              },
              {
                "name": "Balcony",
                "value": 5468
              },
              {
                "name": "Suite",
                "value": 5868
              },
              {
                "code": "PortCharge",
                "value": 745
              },
              {
                "code": "CruiseTax",
                "value": 324.47
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:02:14"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
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
          "id": 62,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/62/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/62/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/62/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 7,
            "priority": 100,
            "logoPath": "/content/images/cruise/7/logo_190.png"
          }
        },
        "shipIds": [
          62
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "27-May-2023",
        "arrivalDateTime": "03-Jun-2023",
        "cruisePackageDepartureDateTime": "17-May-2023",
        "cruisePackageArrivalDateTime": "03-Jun-2023",
        "cruiseTourCode": "T3ATB1",
        "voyageId": "A317",
        "stnExternalId": "1438516",
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
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 17,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseName": "Voyage Of The Glaciers With Glacier Bay (Southbound)"
      },
      {
        "id": 1299008,
        "code": "I340",
        "name": "18-Day Yukon+Denali: Tour Y1l",
        "startDateTime": "17-May-2023",
        "endDateTime": "04-Jun-2023",
        "itinerary": {
          "id": 362994,
          "duration": 18,
          "departure": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "NO TRANSFER - HOTEL AT YVR AIRPORT|THE FAIRMONT VANCOUVER AIRPORT HOTEL|AIR VANCOUVER/WHITEHORSE|MEET YOUR JOURNEY HOST|TRANSFER YXY AIRPORT/HOTEL|WHITEHORSE AREA HOTEL|XFER WITH MUKTUK TOUR ENROUTE TO AIRPORT|AIR WHITEHORSE/DAWSON|TRANSFER YDA AIRPORT/HOTEL|WESTMARK INN DAWSON|DAWSON DAY AT LEISURE|TRANSFER HOTEL/YDA AIRPORT|AIR DAWSON/FAIRBANKS|TRANSFER FAI AIRPORT/HOTEL|WESTMARK FAIRBANKS HOTEL|AM GOLD DREDGE/PM RIVERBOAT - FAI|FAIRBANKS/DENALI COACH|DENALI AFTERNOON AT LEISURE|MCKINLEY CHALET RESORT|AM TUNDRA WILDERNESS TOUR|DENALI AFTERNOON AT LEISURE|DENALI DAY AT LEISURE|TRANSFER HOTEL/RAIL DEPOT|MCKINLEY EXPLORER DENALI/TALKEETNA|MCKINLEY EXPLORER TALKEETNA/ANCHORAGE|TRANSFER RAIL DEPOT/HOTEL|ANCHORAGE AREA HOTEL|ANCHORAGE DAY AT LEISURE|GOODBYE TO YOUR JOURNEY HOST|CRUISETRAIN ANCHORAGE/WHITTIER|WHITTIER|GLACIER BAY|SKAGWAY|JUNEAU|KETCHIKAN|VANCOUVER|WHITEHORSE AREA HOTEL"
        },
        "uniqueItineraryId": "362994_13250__18_t3ay1l",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 4604
              },
              {
                "name": "Outside",
                "value": 4954
              },
              {
                "name": "Balcony",
                "value": 5604
              },
              {
                "name": "Suite",
                "value": 6304
              },
              {
                "code": "PortCharge",
                "value": 513
              },
              {
                "code": "CruiseTax",
                "value": 530
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:10:33"
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
          "id": 13250,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/13250/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/13250/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/13250/ship_520.jpg",
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
          13250
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "28-May-2023",
        "arrivalDateTime": "04-Jun-2023",
        "cruisePackageDepartureDateTime": "17-May-2023",
        "cruisePackageArrivalDateTime": "04-Jun-2023",
        "cruiseTourCode": "T3AY1L",
        "voyageId": "I340",
        "stnExternalId": "1450796",
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
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 18,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseTourName": "18-Day Yukon+Denali: Tour Y1l"
      },
      {
        "id": 1301564,
        "code": "V324",
        "name": "13-Day Yukon+Denali: Tour R4l",
        "startDateTime": "18-May-2023",
        "endDateTime": "31-May-2023",
        "itinerary": {
          "id": 359110,
          "duration": 13,
          "departure": {
            "code": "SEA",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "HOTEL COURTESY TRANSFER SEA APT/HTL|HOTEL COURTESY TRANSFER HTL/SEA APT|AIR SEATTLE/ANCHORAGE|TRANSFER ANC AIRPORT/HOTEL|ANCHORAGE AREA HOTEL|MEET YOUR JOURNEY HOST|TRANSFER HOTEL/RAIL DEPOT|MCKINLEY EXPLORER ANCHORAGE/TALKEETNA|MCKINLEY EXPLORER TALKEETNA/DENALI|TRANSFER RAIL DEPOT/HOTEL|DENALI AREA HOTEL|AM TUNDRA WILDERNESS TOUR|DENALI AFTERNOON AT LEISURE|DENALI/FAIRBANKS COACH|PM GOLD DREDGE|WESTMARK FAIRBANKS HOTEL|TRANSFER HOTEL/FAI AIRPORT|AIR FAIRBANKS/DAWSON|TRANSFER YDA AIRPORT/HOTEL|WESTMARK INN DAWSON|DAWSON DAY AT LEISURE|ROUNDTRIP TRANSFERS KLONDIKE SPIRIT|KLONDIKE SPIRIT|DAWSON/WHITEHORSE COACH|LUNCH MINTO/KLONDIKE HWY|WHITEHORSE AREA HOTEL|WHITEHORSE/FRASER COACH|WPYR FRASER/SKAGWAY|TRANSFER RAIL/HOTEL|WESTMARK INN SKAGWAY|TRANSFER HOTEL/SHIP|GOODBYE TO YOUR JOURNEY HOST|SKAGWAY|GLACIER BAY|KETCHIKAN|VANCOUVER|AIR SEATTLE/ANCHORAGE"
        },
        "uniqueItineraryId": "359110_43__13_t3ar4l",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 3323
              },
              {
                "name": "Outside",
                "value": 3473
              },
              {
                "name": "Suite",
                "value": 4223
              },
              {
                "code": "PortCharge",
                "value": 327
              },
              {
                "code": "CruiseTax",
                "value": 295
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:27:05"
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
          "id": 43,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/43/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/43/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/43/ship_520.jpg",
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
          43
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "24-May-2023",
        "arrivalDateTime": "31-May-2023",
        "cruisePackageDepartureDateTime": "18-May-2023",
        "cruisePackageArrivalDateTime": "31-May-2023",
        "cruiseTourCode": "T3AR4L",
        "voyageId": "V324",
        "packageTourId": -1,
        "categoryTypes": [
          "Outside",
          "Inside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseTourName": "13-Day Yukon+Denali: Tour R4l"
      },
      {
        "id": 1301221,
        "code": "V324",
        "name": "12-Day Yukon+Denali: Tour Y4l",
        "startDateTime": "19-May-2023",
        "endDateTime": "31-May-2023",
        "itinerary": {
          "id": 359139,
          "duration": 12,
          "departure": {
            "code": "ANC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "TRANSFER ANC AIRPORT/HOTEL|ANCHORAGE AREA HOTEL|MEET YOUR JOURNEY HOST|TRANSFER HOTEL/RAIL DEPOT|MCKINLEY EXPLORER ANCHORAGE/TALKEETNA|MCKINLEY EXPLORER TALKEETNA/DENALI|TRANSFER RAIL DEPOT/HOTEL|DENALI AREA HOTEL|AM TUNDRA WILDERNESS TOUR|DENALI AFTERNOON AT LEISURE|DENALI/FAIRBANKS COACH|PM GOLD DREDGE|WESTMARK FAIRBANKS HOTEL|TRANSFER HOTEL/FAI AIRPORT|AIR FAIRBANKS/DAWSON|TRANSFER YDA AIRPORT/HOTEL|WESTMARK INN DAWSON|DAWSON DAY AT LEISURE|ROUNDTRIP TRANSFERS KLONDIKE SPIRIT|KLONDIKE SPIRIT|DAWSON/WHITEHORSE COACH|LUNCH MINTO/KLONDIKE HWY|WHITEHORSE AREA HOTEL|WHITEHORSE/FRASER COACH|WPYR FRASER/SKAGWAY|TRANSFER RAIL/HOTEL|WESTMARK INN SKAGWAY|TRANSFER HOTEL/SHIP|GOODBYE TO YOUR JOURNEY HOST|SKAGWAY|GLACIER BAY|KETCHIKAN|VANCOUVER|ANCHORAGE AREA HOTEL"
        },
        "uniqueItineraryId": "359139_43__12_t3ay4l",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2864
              },
              {
                "name": "Outside",
                "value": 3014
              },
              {
                "name": "Suite",
                "value": 3764
              },
              {
                "code": "PortCharge",
                "value": 327
              },
              {
                "code": "CruiseTax",
                "value": 255
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:27:08"
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
          "id": 43,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/43/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/43/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/43/ship_520.jpg",
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
          43
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "24-May-2023",
        "arrivalDateTime": "31-May-2023",
        "cruisePackageDepartureDateTime": "19-May-2023",
        "cruisePackageArrivalDateTime": "31-May-2023",
        "cruiseTourCode": "T3AY4L",
        "voyageId": "V324",
        "stnExternalId": "1451060",
        "packageTourId": -1,
        "categoryTypes": [
          "Outside",
          "Inside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 12,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseTourName": "12-Day Yukon+Denali: Tour Y4l"
      },
      {
        "id": 1300539,
        "code": "A317",
        "name": "Voyage Of The Glaciers With Glacier Bay (Southbound)",
        "startDateTime": "19-May-2023",
        "endDateTime": "03-Jun-2023",
        "itinerary": {
          "id": 354438,
          "duration": 15,
          "departure": {
            "code": "FAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fairbanks|Fairbanks|Denali Princess Wilderness Lodge|Denali Princess Wilderness Lodge|Mt Mckinley Princess Wilderness Lodge|Kenai Princess Wilderness Lodge|Kenai Princess Wilderness Lodge|Kenai Princess Wilderness Lodge|Whittier|Anchorage (Whittier) Alaska|Skagway Alaska|Juneau Alaska|Ketchikan Alaska|Vancouver Canada",
          "mapPath": "/content/images/Itineraries/FAI_DNL_MCL_KENI_WH1_ANC_GBNP_SGY_JNU_KTN_YVR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FAI_DNL_MCL_KENI_WH1_ANC_GBNP_SGY_JNU_KTN_YVR.jpg"
        },
        "uniqueItineraryId": "354438_62__15_t3asb8",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 4068
              },
              {
                "name": "Outside",
                "value": 4168
              },
              {
                "name": "Balcony",
                "value": 4768
              },
              {
                "name": "Suite",
                "value": 5168
              },
              {
                "code": "PortCharge",
                "value": 645
              },
              {
                "code": "CruiseTax",
                "value": 312.54
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:01:42"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
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
          "id": 62,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/62/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/62/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/62/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 7,
            "priority": 100,
            "logoPath": "/content/images/cruise/7/logo_190.png"
          }
        },
        "shipIds": [
          62
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "27-May-2023",
        "arrivalDateTime": "03-Jun-2023",
        "cruisePackageDepartureDateTime": "19-May-2023",
        "cruisePackageArrivalDateTime": "03-Jun-2023",
        "cruiseTourCode": "T3ASB8",
        "voyageId": "A317",
        "stnExternalId": "1438514",
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
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 15,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseName": "Voyage Of The Glaciers With Glacier Bay (Southbound)"
      },
      {
        "id": 1295520,
        "code": "G320",
        "name": "Scandinavia & Baltic (From Copenhagen)",
        "startDateTime": "19-May-2023",
        "endDateTime": "07-Jun-2023",
        "itinerary": {
          "id": 321471,
          "duration": 19,
          "departure": {
            "code": "BUD",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CPH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Budapest Hungary|Budapest Hungary|Vienna Austria|Vienna Austria|Prague Czech Republic|Prague Czech Republic|Berlin Germany|Berlin Germany|Copenhagen Denmark|Copenhagen Denmark|Skagen Denmark|Aarhus Denmark|Berlin (Warnemunde) Germany|Tallinn Estonia|St Petersburg Russia|St Petersburg Russia|Helsinki Finland|Stockholm (Nynashamn) Sweden|Copenhagen Denmark",
          "mapPath": "/content/images/Itineraries/BUD_VIE_PRG_BER_CPH_QJV_AAR_ZWD_BER_TLL_LED_HEL_NYN_STO_CPH.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BUD_VIE_PRG_BER_CPH_QJV_AAR_ZWD_BER_TLL_LED_HEL_NYN_STO_CPH.jpg"
        },
        "uniqueItineraryId": "321471_65__19_t3e01a",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 6089
              },
              {
                "name": "Balcony",
                "value": 6489
              },
              {
                "name": "Suite",
                "value": 7139
              },
              {
                "code": "PortCharge",
                "value": 675
              },
              {
                "code": "CruiseTax",
                "value": 235
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:02:55"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 15,
          "type": "Destination",
          "priority": 50
        },
        "parentDestinationIds": [
          15
        ],
        "ship": {
          "id": 65,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/65/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/65/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/65/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.fredolsencruises.com/virtual-tour/bolette/full-tour/",
          "cruiseline": {
            "id": 7,
            "priority": 100,
            "logoPath": "/content/images/cruise/7/logo_190.png"
          }
        },
        "shipIds": [
          65
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "27-May-2023",
        "arrivalDateTime": "07-Jun-2023",
        "cruisePackageDepartureDateTime": "19-May-2023",
        "cruisePackageArrivalDateTime": "07-Jun-2023",
        "cruiseTourCode": "T3E01A",
        "voyageId": "G320",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Inside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 4,
        "minOccupancy": 1,
        "cruiseDuration": 19,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseName": "Scandinavia & Baltic (From Copenhagen)"
      },
      {
        "id": 1301384,
        "code": "V324",
        "name": "11-Day Yukon+Denali: Tour Y5l",
        "startDateTime": "20-May-2023",
        "endDateTime": "31-May-2023",
        "itinerary": {
          "id": 359142,
          "duration": 11,
          "departure": {
            "code": "ANC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "TRANSFER ANC AIRPORT/HOTEL|ANCHORAGE AREA HOTEL|MEET YOUR JOURNEY HOST|TRANSFER HOTEL/RAIL DEPOT|MCKINLEY EXPLORER ANCHORAGE/TALKEETNA|MCKINLEY EXPLORER TALKEETNA/DENALI|TRANSFER RAIL DEPOT/HOTEL|DENALI AREA HOTEL|AM TUNDRA WILDERNESS TOUR|DENALI AFTERNOON AT LEISURE|DENALI/FAIRBANKS COACH|PM GOLD DREDGE|WESTMARK FAIRBANKS HOTEL|TRANSFER HOTEL/FAI AIRPORT|AIR FAIRBANKS/DAWSON|TRANSFER YDA AIRPORT/HOTEL|WESTMARK INN DAWSON|DAWSON DAY AT LEISURE|DAWSON/WHITEHORSE COACH|LUNCH MINTO/KLONDIKE HWY|WHITEHORSE AREA HOTEL|WHITEHORSE/FRASER COACH|WPYR FRASER/SKAGWAY|TRANSFER RAIL/SHIP|SKAGWAY|GLACIER BAY|KETCHIKAN|VANCOUVER|ANCHORAGE AREA HOTEL"
        },
        "uniqueItineraryId": "359142_43__11_t3ay5l",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2769
              },
              {
                "name": "Outside",
                "value": 2919
              },
              {
                "name": "Suite",
                "value": 3669
              },
              {
                "code": "PortCharge",
                "value": 300
              },
              {
                "code": "CruiseTax",
                "value": 250
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:27:09"
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
          "id": 43,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/5/43/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/5/43/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/5/43/ship_520.jpg",
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
          43
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "24-May-2023",
        "arrivalDateTime": "31-May-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "31-May-2023",
        "cruiseTourCode": "T3AY5L",
        "voyageId": "V324",
        "stnExternalId": "1454332",
        "packageTourId": -1,
        "categoryTypes": [
          "Outside",
          "Inside",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 11,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseTourName": "11-Day Yukon+Denali: Tour Y5l"
      },
      {
        "id": 1320359,
        "code": "19503",
        "name": "3 Nights Lisbon Pre-Cruise And 3 Nights Madrid Post-Cruise",
        "startDateTime": "20-May-2023",
        "endDateTime": "02-Jun-2023",
        "itinerary": {
          "id": 335874,
          "duration": 13,
          "departure": {
            "code": "LIS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "VDT",
            "type": "CruisePort"
          },
          "portsOfCalls": "Porto|Porto|Entre-os-Rios|Rgua|Rgua|Pinho|Pinho|Barca dAlva|Vega de Terrn|Vega de Terrn",
          "mapPath": "/content/images/Itineraries/OPO_EORS_REG_PIN_BAR_VDT.jpg",
          "fallbackMapPath": "/content/images/Itineraries/OPO_EORS_REG_PIN_BAR_VDT.jpg"
        },
        "uniqueItineraryId": "335874_13523__13_19503562679562696",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 5649
              },
              {
                "name": "Balcony",
                "value": 6748
              },
              {
                "name": "Suite",
                "value": 9348
              },
              {
                "code": "PortCharge",
                "value": 210
              },
              {
                "code": "CruiseTax",
                "value": 210
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:01:42"
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
          "id": 13523,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8138/13523/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8138/13523/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8138/13523/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8138,
            "priority": 100,
            "logoPath": "/content/images/cruise/8138/logo_190.png"
          }
        },
        "shipIds": [
          13523
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "23-May-2023",
        "arrivalDateTime": "30-May-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "02-Jun-2023",
        "cruiseTourCode": "19503-562679-562696",
        "voyageId": "19503",
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
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          51
        ],
        "cruiseTourName": "3 Nights Lisbon Pre-Cruise And 3 Nights Madrid Post-Cruise",
        "cruiseName": "Flavors Of Portugal & Spain"
      },
      {
        "id": 1317742,
        "code": "RD07A309",
        "name": "13Nt Alaska Wilderness Spectacular Ct 8B",
        "startDateTime": "20-May-2023",
        "endDateTime": "02-Jun-2023",
        "itinerary": {
          "id": 336445,
          "duration": 13,
          "departure": {
            "code": "FAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fairbanks - Alaska (PRE-CRUISE TOUR)|Fairbanks - Alaska (PRE-CRUISE TOUR)|Fairbanks - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Talkeetna - Alaska (PRE-CRUISE TOUR)|Talkeetna - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Seward -  Alaska|Juneau -  Alaska|Skagway -  Alaska|Icy Strait Point -  Alaska|Ketchikan -  Alaska|Vancouver -  British Columbia",
          "normalizedPortsOfCall": "FAI|DNLI|TKA|ANC|SWD|JNU|SGY|ICYS|KTN|YVR",
          "mapPath": "/content/images/Itineraries/FAI_DNL_TKA_ANC_SWD_JNU_SGY_ISPS_KTN_YVR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FAI_DNL_TKA_ANC_SWD_JNU_SGY_ISPS_KTN_YVR.jpg"
        },
        "uniqueItineraryId": "336445_83__13_rd13b308",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2960
              },
              {
                "name": "Outside",
                "value": 3260
              },
              {
                "name": "Balcony",
                "value": 3910
              },
              {
                "name": "Suite",
                "value": 4990
              },
              {
                "code": "PortCharge",
                "value": 235
              },
              {
                "code": "CruiseTax",
                "value": 257.83
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
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 83,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/83/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/83/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/83/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          83
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "26-May-2023",
        "arrivalDateTime": "02-Jun-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "02-Jun-2023",
        "cruiseTourCode": "RD13B308",
        "voyageId": "RD07A309",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "gratuitiesInfo": {
          "inside": 101.5,
          "outside": 101.5,
          "balcony": 101.5,
          "suite": 101.5
        },
        "cruiseTourName": "13Nt Alaska Wilderness Spectacular Ct 8B",
        "cruiseName": "13Nt Alaska Wilderness Spectacular Ct 8B"
      },
      {
        "id": 1317741,
        "code": "RD07A309",
        "name": "13Nt Grand Mountain Marvels Ct 7B",
        "startDateTime": "20-May-2023",
        "endDateTime": "02-Jun-2023",
        "itinerary": {
          "id": 336444,
          "duration": 13,
          "departure": {
            "code": "FAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fairbanks - Alaska (PRE-CRUISE TOUR)|Fairbanks - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Talkeetna - Alaska (PRE-CRUISE TOUR)|Talkeetna - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Seward - Alaska (PRE-CRUISE TOUR)|Seward - Alaska (PRE-CRUISE TOUR)|Seward -  Alaska|Juneau -  Alaska|Skagway -  Alaska|Icy Strait Point -  Alaska|Ketchikan -  Alaska|Vancouver -  British Columbia",
          "normalizedPortsOfCall": "FAI|DNLI|TKA|ANC|SWD|JNU|SGY|ICYS|KTN|YVR",
          "mapPath": "/content/images/Itineraries/FAI_DNL_TKA_ANC_SWD_JNU_SGY_ISPS_KTN_YVR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FAI_DNL_TKA_ANC_SWD_JNU_SGY_ISPS_KTN_YVR.jpg"
        },
        "uniqueItineraryId": "336444_83__13_rd13b307",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2831
              },
              {
                "name": "Outside",
                "value": 3130
              },
              {
                "name": "Balcony",
                "value": 3780
              },
              {
                "name": "Suite",
                "value": 4861
              },
              {
                "code": "PortCharge",
                "value": 235
              },
              {
                "code": "CruiseTax",
                "value": 257.83
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
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 83,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/83/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/83/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/83/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          83
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "26-May-2023",
        "arrivalDateTime": "02-Jun-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "02-Jun-2023",
        "cruiseTourCode": "RD13B307",
        "voyageId": "RD07A309",
        "stnExternalId": "1454959",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "gratuitiesInfo": {
          "inside": 101.5,
          "outside": 101.5,
          "balcony": 101.5,
          "suite": 101.5
        },
        "cruiseTourName": "13Nt Grand Mountain Marvels Ct 7B",
        "cruiseName": "13Nt Alaska Wilderness Spectacular Ct 8B"
      },
      {
        "id": 1274492,
        "code": "19551",
        "name": "3 Nights Prague Pre-Cruise And 2 Nights Reims (Champagne), 1 Night Paris Post-Cruise",
        "startDateTime": "20-May-2023",
        "endDateTime": "02-Jun-2023",
        "itinerary": {
          "id": 327482,
          "duration": 13,
          "departure": {
            "code": "PRG",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "PAR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Prague|Prague|Prague|Prague|Nuremberg|Bamberg|Wrzburg|Wertheim|Rdesheim|Rhine Gorge|Lahnstein|Cochem|Zell|Trier|Luxembourg|Reims|Reims|Reims|Paris|Paris",
          "mapPath": "/content/images/Itineraries/PRG_NUE_ZCD_WURZ_WERT_RUDE_LHNS_COCM_ZELL_ZQF_LUX_RHE_PAR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/PRG_NUE_ZCD_WURZ_WERT_RUDE_LHNS_COCM_ZELL_ZQF_LUX_RHE_PAR.jpg"
        },
        "uniqueItineraryId": "327482_13500__13_19551563011563013",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 6149
              },
              {
                "name": "Balcony",
                "value": 7248
              },
              {
                "name": "Suite",
                "value": 9748
              },
              {
                "code": "PortCharge",
                "value": 210
              },
              {
                "code": "CruiseTax",
                "value": 210
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:01:42"
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
          "id": 13500,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8138/13500/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8138/13500/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8138/13500/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8138,
            "priority": 100,
            "logoPath": "/content/images/cruise/8138/logo_190.png"
          }
        },
        "shipIds": [
          13500
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "23-May-2023",
        "arrivalDateTime": "30-May-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "02-Jun-2023",
        "cruiseTourCode": "19551-563011-563013",
        "voyageId": "19551",
        "stnExternalId": "1418491",
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
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          51
        ],
        "cruiseTourName": "3 Nights Prague Pre-Cruise And 2 Nights Reims (Champagne), 1 Night Paris Post-Cruise",
        "cruiseName": "Europe’S Rivers & Castles"
      },
      {
        "id": 1274491,
        "code": "19551",
        "name": "3 Nights Prague Pre-Cruise And 3 Nights Paris Post-Cruise",
        "startDateTime": "20-May-2023",
        "endDateTime": "02-Jun-2023",
        "itinerary": {
          "id": 327481,
          "duration": 13,
          "departure": {
            "code": "PRG",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "PAR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Prague|Prague|Prague|Prague|Nuremberg|Bamberg|Wrzburg|Wertheim|Rdesheim|Rhine Gorge|Lahnstein|Cochem|Zell|Trier|Luxembourg|Paris|Paris|Paris|Paris",
          "mapPath": "/content/images/Itineraries/PRG_NUE_ZCD_WURZ_WERT_RUDE_LHNS_COCM_ZELL_ZQF_LUX_PAR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/PRG_NUE_ZCD_WURZ_WERT_RUDE_LHNS_COCM_ZELL_ZQF_LUX_PAR.jpg"
        },
        "uniqueItineraryId": "327481_13500__13_19551563011563012",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 6179
              },
              {
                "name": "Balcony",
                "value": 7278
              },
              {
                "name": "Suite",
                "value": 9778
              },
              {
                "code": "PortCharge",
                "value": 210
              },
              {
                "code": "CruiseTax",
                "value": 210
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:01:42"
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
          "id": 13500,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8138/13500/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8138/13500/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8138/13500/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8138,
            "priority": 100,
            "logoPath": "/content/images/cruise/8138/logo_190.png"
          }
        },
        "shipIds": [
          13500
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "23-May-2023",
        "arrivalDateTime": "30-May-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "02-Jun-2023",
        "cruiseTourCode": "19551-563011-563012",
        "voyageId": "19551",
        "stnExternalId": "1418496",
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
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          51
        ],
        "cruiseTourName": "3 Nights Prague Pre-Cruise And 3 Nights Paris Post-Cruise",
        "cruiseName": "Europe’S Rivers & Castles"
      },
      {
        "id": 1274490,
        "code": "19503",
        "name": "3 Nights Lisbon Pre-Cruise And 3 Nights Madrid Post-Cruise",
        "startDateTime": "20-May-2023",
        "endDateTime": "02-Jun-2023",
        "itinerary": {
          "id": 285777,
          "duration": 13,
          "departure": {
            "code": "LIS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "MAD",
            "type": "CruisePort"
          },
          "portsOfCalls": "Lisbon|Lisbon|Lisbon|Lisbon|Porto|Porto|Entre-os-Rios|Rgua|Rgua|Pinho|Pinho|Barca dAlva|Vega de Terrn|Vega de Terrn|Salamanca|Madrid|Madrid|Madrid|Madrid",
          "mapPath": "/content/images/Itineraries/LIS_OPO_EORS_REG_PINH_BDAL_VDT_SLM_MAD.jpg",
          "fallbackMapPath": "/content/images/Itineraries/LIS_OPO_EORS_REG_PINH_BDAL_VDT_SLM_MAD.jpg"
        },
        "uniqueItineraryId": "285777_13523__13_19503562679562696",
        "prices": [
          {
            "items": [
              {
                "name": "Balcony",
                "value": 7348
              },
              {
                "code": "PortCharge",
                "value": 210
              },
              {
                "code": "CruiseTax",
                "value": 210
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 00:01:31"
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
          "id": 13523,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8138/13523/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8138/13523/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8138/13523/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "hasShipVideoUrl": true,
          "cruiseline": {
            "id": 8138,
            "priority": 100,
            "logoPath": "/content/images/cruise/8138/logo_190.png"
          }
        },
        "shipIds": [
          13523
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "23-May-2023",
        "arrivalDateTime": "30-May-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "02-Jun-2023",
        "cruiseTourCode": "19503-562679-562696",
        "voyageId": "19503",
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
        "cruiseDuration": 13,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          51
        ],
        "cruiseTourName": "3 Nights Lisbon Pre-Cruise And 3 Nights Madrid Post-Cruise",
        "cruiseName": "Flavors Of Portugal & Spain"
      },
      {
        "id": 1300600,
        "code": "8315",
        "name": "Calgary, Canada To Anchorage (Whittier), Alaska",
        "startDateTime": "20-May-2023",
        "endDateTime": "03-Jun-2023",
        "itinerary": {
          "id": 347531,
          "duration": 14,
          "departure": {
            "code": "YYC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "WH1",
            "type": "CruisePort"
          },
          "portsOfCalls": "Calgary Canada|Banff Canada|Banff Canada|Lake Louise Canada|Jasper Canada|Kamloops Canada|Vancouver British Columbia Canada|Vancouver British Columbia Canada|Vancouver Canada|Ketchikan Alaska|Juneau Alaska|Skagway Alaska|Anchorage (Whittier) Alaska",
          "mapPath": "/content/images/Itineraries/YYC_YBA_LOUI_YJA_KLOP_YVR_KTN_JNU_SGY_GBNP_CLF_ANC.jpg",
          "fallbackMapPath": "/content/images/Itineraries/YYC_YBA_LOUI_YJA_KLOP_YVR_KTN_JNU_SGY_GBNP_CLF_ANC.jpg"
        },
        "uniqueItineraryId": "347531_13762__14_t3a01a",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 7118
              },
              {
                "name": "Balcony",
                "value": 7768
              },
              {
                "name": "Suite",
                "value": 8218
              },
              {
                "code": "PortCharge",
                "value": 805
              },
              {
                "code": "CruiseTax",
                "value": 496.52
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 19:02:41"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
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
          "id": 13762,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/13762/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/13762/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/13762/ship_520.jpg",
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
          13762
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "27-May-2023",
        "arrivalDateTime": "03-Jun-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "03-Jun-2023",
        "cruiseTourCode": "T3A01A",
        "voyageId": "8315",
        "packageTourId": -1,
        "categoryTypes": [
          "Inside",
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
        ],
        "cruiseTourName": "Calgary, Canada To Anchorage (Whittier), Alaska",
        "cruiseName": "Voyage Of The Glaciers (Northbound)"
      },
      {
        "id": 1300384,
        "code": "A317",
        "name": "Voyage Of The Glaciers With Glacier Bay (Southbound)",
        "startDateTime": "20-May-2023",
        "endDateTime": "03-Jun-2023",
        "itinerary": {
          "id": 354410,
          "duration": 14,
          "departure": {
            "code": "FAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fairbanks|Fairbanks|Denali Princess Wilderness Lodge|Denali Princess Wilderness Lodge|Mt Mckinley Princess Wilderness Lodge|Kenai Princess Wilderness Lodge|Kenai Princess Wilderness Lodge|Whittier|Anchorage (Whittier) Alaska|Skagway Alaska|Juneau Alaska|Ketchikan Alaska|Vancouver Canada",
          "mapPath": "/content/images/Itineraries/FAI_DNL_MCL_KENI_WH1_ANC_GBNP_SGY_JNU_KTN_YVR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FAI_DNL_MCL_KENI_WH1_ANC_GBNP_SGY_JNU_KTN_YVR.jpg"
        },
        "uniqueItineraryId": "354410_62__14_t3anb7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2868
              },
              {
                "name": "Outside",
                "value": 2968
              },
              {
                "name": "Balcony",
                "value": 3568
              },
              {
                "name": "Suite",
                "value": 3968
              },
              {
                "code": "PortCharge",
                "value": 455
              },
              {
                "code": "CruiseTax",
                "value": 300.78
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 18:59:56"
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodesInfo": []
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
          "id": 62,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/62/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/62/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/62/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 7,
            "priority": 100,
            "logoPath": "/content/images/cruise/7/logo_190.png"
          }
        },
        "shipIds": [
          62
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "27-May-2023",
        "arrivalDateTime": "03-Jun-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "03-Jun-2023",
        "cruiseTourCode": "T3ANB7",
        "voyageId": "A317",
        "stnExternalId": "1438494",
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
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseName": "Voyage Of The Glaciers With Glacier Bay (Southbound)"
      },
      {
        "id": 1301293,
        "code": "K339",
        "name": "14-Day Yukon+Denali: Tour Y3l",
        "startDateTime": "20-May-2023",
        "endDateTime": "03-Jun-2023",
        "itinerary": {
          "id": 359104,
          "duration": 14,
          "departure": {
            "code": "ANC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "TRANSFER ANC AIRPORT/HOTEL|ANCHORAGE AREA HOTEL|MEET YOUR JOURNEY HOST|TRANSFER HOTEL/RAIL DEPOT|MCKINLEY EXPLORER ANCHORAGE/TALKEETNA|MCKINLEY EXPLORER TALKEETNA/DENALI|TRANSFER RAIL DEPOT/HOTEL|MCKINLEY CHALET RESORT|AM TUNDRA WILDERNESS TOUR|DENALI AFTERNOON AT LEISURE|DENALI DAY AT LEISURE|DENALI/FAIRBANKS COACH|PM GOLD DREDGE|WESTMARK FAIRBANKS HOTEL|TRANSFER HOTEL/FAI AIRPORT|AIR FAIRBANKS/DAWSON|TRANSFER YDA AIRPORT/HOTEL|ROUNDTRIP TRANSFERS KLONDIKE SPIRIT|KLONDIKE SPIRIT|WESTMARK INN DAWSON|DAWSON DAY AT LEISURE|DAWSON/WHITEHORSE COACH|LUNCH MINTO/KLONDIKE HWY|WHITEHORSE AREA HOTEL|WHITEHORSE/FRASER COACH|WPYR FRASER/SKAGWAY|TRANSFER RAIL/HOTEL|WESTMARK INN SKAGWAY|SKAGWAY DAY AT LEISURE|TRANSFER HOTEL/SHIP|GOODBYE TO YOUR JOURNEY HOST|SKAGWAY|GLACIER BAY|KETCHIKAN|VANCOUVER|ANCHORAGE AREA HOTEL"
        },
        "uniqueItineraryId": "359104_13708__14_t3ay3l",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 3184
              },
              {
                "name": "Outside",
                "value": 3534
              },
              {
                "name": "Balcony",
                "value": 3634
              },
              {
                "name": "Suite",
                "value": 3884
              },
              {
                "code": "PortCharge",
                "value": 381
              },
              {
                "code": "CruiseTax",
                "value": 235
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:16:27"
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
        "cruiseType": "CruiseTour",
        "departureDateTime": "27-May-2023",
        "arrivalDateTime": "03-Jun-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "03-Jun-2023",
        "cruiseTourCode": "T3AY3L",
        "voyageId": "K339",
        "stnExternalId": "1454199",
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
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "cruiseTourName": "14-Day Yukon+Denali: Tour Y3l"
      },
      {
        "id": 1230219,
        "code": "HGR230523",
        "name": "Portugal's River of Gold",
        "startDateTime": "21-May-2023",
        "endDateTime": "30-May-2023",
        "itinerary": {
          "id": 358212,
          "duration": 9,
          "departure": {
            "code": "LIS",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "OPO",
            "type": "CruisePort"
          },
          "portsOfCalls": "Porto|Regua|Pinhao|Scenic Sailing Douro River|Barca dAlva|Salamanca|Pinhao|Regua|Regua|Porto|Porto|Porto"
        },
        "uniqueItineraryId": "358212_14072__9_hgr230523t",
        "prices": [
          {
            "items": [
              {
                "name": "Outside",
                "value": 4499
              },
              {
                "name": "Balcony",
                "value": 6499
              },
              {
                "name": "Suite",
                "value": 7299
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "03-Jun-2022 22:05:17"
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
          "id": 15,
          "type": "Destination",
          "priority": 50
        },
        "parentDestinationIds": [
          15
        ],
        "ship": {
          "id": 14072,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8112/14072/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8112/14072/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8112/14072/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "vrUrl": "https://www.vikingrivercruises.com/content/douro/start.html?secure=true#.Xs-qI2hKhPY",
          "hasVrForStateRoom": true,
          "cruiseline": {
            "id": 8112,
            "priority": 100,
            "logoPath": "/content/images/cruise/8112/logo_190.png"
          }
        },
        "shipIds": [
          14072
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "23-May-2023",
        "arrivalDateTime": "30-May-2023",
        "cruisePackageDepartureDateTime": "21-May-2023",
        "cruisePackageArrivalDateTime": "30-May-2023",
        "cruiseTourCode": "HGR230523T",
        "voyageId": "HGR230523",
        "packageTourId": -1,
        "categoryTypes": [
          "Outside",
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 9,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "Portugal's River of Gold",
        "cruiseName": "Douro's Valleys & Vineyards"
      },
      {
        "id": 1317740,
        "code": "RD07A309",
        "name": "12Nt Katmai Bear Trek 12B",
        "startDateTime": "21-May-2023",
        "endDateTime": "02-Jun-2023",
        "itinerary": {
          "id": 336443,
          "duration": 12,
          "departure": {
            "code": "ANC",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Anchorage - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Talkeetna - Alaska (PRE-CRUISE TOUR)|Talkeetna - Alaska (PRE-CRUISE TOUR)|Seward - Alaska (PRE-CRUISE TOUR)|Alyeska (Girdwood) - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Seward -  Alaska|Juneau -  Alaska|Skagway -  Alaska|Icy Strait Point -  Alaska|Ketchikan -  Alaska|Vancouver -  British Columbia",
          "normalizedPortsOfCall": "ANC|DNLI|TKA|SWD|AQY|ANC|SWD|JNU|SGY|ICYS|KTN|YVR"
        },
        "uniqueItineraryId": "336443_83__12_rd12b312",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 3890
              },
              {
                "name": "Outside",
                "value": 4190
              },
              {
                "name": "Balcony",
                "value": 4840
              },
              {
                "name": "Suite",
                "value": 5920
              },
              {
                "code": "PortCharge",
                "value": 235
              },
              {
                "code": "CruiseTax",
                "value": 257.83
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
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 83,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/83/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/83/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/83/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          83
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "26-May-2023",
        "arrivalDateTime": "02-Jun-2023",
        "cruisePackageDepartureDateTime": "21-May-2023",
        "cruisePackageArrivalDateTime": "02-Jun-2023",
        "cruiseTourCode": "RD12B312",
        "voyageId": "RD07A309",
        "stnExternalId": "1454814",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 12,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "gratuitiesInfo": {
          "inside": 101.5,
          "outside": 101.5,
          "balcony": 101.5,
          "suite": 101.5
        },
        "cruiseTourName": "12Nt Katmai Bear Trek 12B",
        "cruiseName": "13Nt Alaska Wilderness Spectacular Ct 8B"
      },
      {
        "id": 1317739,
        "code": "RD07A309",
        "name": "12Nt Fjord&Tundra Nat'l Parks Explorer Ct 6B",
        "startDateTime": "21-May-2023",
        "endDateTime": "02-Jun-2023",
        "itinerary": {
          "id": 336442,
          "duration": 12,
          "departure": {
            "code": "FAI",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "YVR",
            "type": "CruisePort"
          },
          "portsOfCalls": "Fairbanks - Alaska (PRE-CRUISE TOUR)|Fairbanks - Alaska (PRE-CRUISE TOUR)|Fairbanks - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Denali - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Anchorage - Alaska (PRE-CRUISE TOUR)|Seward - Alaska (PRE-CRUISE TOUR)|Seward - Alaska (PRE-CRUISE TOUR)|Seward -  Alaska|Juneau -  Alaska|Skagway -  Alaska|Icy Strait Point -  Alaska|Ketchikan -  Alaska|Vancouver -  British Columbia",
          "normalizedPortsOfCall": "FAI|DNLI|ANC|SWD|JNU|SGY|ICYS|KTN|YVR",
          "mapPath": "/content/images/Itineraries/FAI_DNL_ANC_SWD_JNU_SGY_ISPS_KTN_YVR.jpg",
          "fallbackMapPath": "/content/images/Itineraries/FAI_DNL_ANC_SWD_JNU_SGY_ISPS_KTN_YVR.jpg"
        },
        "uniqueItineraryId": "336442_83__12_rd12b306",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2420
              },
              {
                "name": "Outside",
                "value": 2720
              },
              {
                "name": "Balcony",
                "value": 3370
              },
              {
                "name": "Suite",
                "value": 4450
              },
              {
                "code": "PortCharge",
                "value": 235
              },
              {
                "code": "CruiseTax",
                "value": 257.83
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
          "id": 1,
          "type": "Destination",
          "priority": 1
        },
        "parentDestinationIds": [
          48
        ],
        "ship": {
          "id": 83,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8/83/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8/83/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8/83/ship_520.jpg",
              "type": "Image",
              "imageType": "Large"
            }
          ],
          "cruiseline": {
            "id": 8,
            "priority": 100,
            "logoPath": "/content/images/cruise/8/logo_190.png"
          }
        },
        "shipIds": [
          83
        ],
        "cruiseType": "CruiseTour",
        "departureDateTime": "26-May-2023",
        "arrivalDateTime": "02-Jun-2023",
        "cruisePackageDepartureDateTime": "21-May-2023",
        "cruisePackageArrivalDateTime": "02-Jun-2023",
        "cruiseTourCode": "RD12B306",
        "voyageId": "RD07A309",
        "stnExternalId": "1454884",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_1.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 12,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          1
        ],
        "gratuitiesInfo": {
          "inside": 101.5,
          "outside": 101.5,
          "balcony": 101.5,
          "suite": 101.5
        },
        "cruiseTourName": "12Nt Fjord&Tundra Nat'l Parks Explorer Ct 6B",
        "cruiseName": "13Nt Alaska Wilderness Spectacular Ct 8B"
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
