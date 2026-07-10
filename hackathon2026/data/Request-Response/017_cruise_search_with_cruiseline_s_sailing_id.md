# Cruise Search With Cruiseline's Sailing Id

**Path:** Cruise Search > Cruise Search With Cruiseline's Sailing Id

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
            "key": "voyageId",
            "values": [
                "RH07D356",
                "*1408",
                "8325*",
                "*N31*" // wild card character support
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
Date: Fri, 14 Apr 2023 14:20:29 GMT
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
    "total": 35,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1293898,
        "code": "N310",
        "name": "Mediterranean With France & Italy",
        "startDateTime": "15-Apr-2023",
        "endDateTime": "22-Apr-2023",
        "itinerary": {
          "id": 318213,
          "duration": 7,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy",
          "normalizedPortsOfCall": "BCN|GIB|MRS|GOA|LIV1|CIV",
          "mapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_CVV.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_CVV.jpg"
        },
        "uniqueItineraryId": "318213_14304__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 779
              },
              {
                "name": "Outside",
                "value": 1190
              },
              {
                "name": "Balcony",
                "value": 1180
              },
              {
                "name": "Suite",
                "value": 1429
              },
              {
                "code": "PortCharge",
                "value": 175
              },
              {
                "code": "CruiseTax",
                "value": 125
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "15-Apr-2023",
        "arrivalDateTime": "22-Apr-2023",
        "cruisePackageDepartureDateTime": "15-Apr-2023",
        "cruisePackageArrivalDateTime": "22-Apr-2023",
        "voyageId": "N310",
        "stnExternalId": "1434548",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "Mediterranean With France & Italy",
        "cruiseName": "Mediterranean With France & Italy"
      },
      {
        "id": 1294016,
        "code": "N310A",
        "name": "Mediterranean With Greek Isles, France & Turkey",
        "startDateTime": "15-Apr-2023",
        "endDateTime": "29-Apr-2023",
        "itinerary": {
          "id": 350162,
          "duration": 14,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece",
          "normalizedPortsOfCall": "BCN|GIB|MRS|GOA|LIV1|CIV|NAP|HER|KUSA|IST|JMK|ATH",
          "mapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS.jpg"
        },
        "uniqueItineraryId": "350162_14304__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1777
              },
              {
                "name": "Outside",
                "value": 2623
              },
              {
                "name": "Balcony",
                "value": 2606
              },
              {
                "name": "Suite",
                "value": 3109
              },
              {
                "code": "PortCharge",
                "value": 350
              },
              {
                "code": "CruiseTax",
                "value": 245
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "15-Apr-2023",
        "arrivalDateTime": "29-Apr-2023",
        "cruisePackageDepartureDateTime": "15-Apr-2023",
        "cruisePackageArrivalDateTime": "29-Apr-2023",
        "voyageId": "N310A",
        "stnExternalId": "1434393",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles, France & Turkey",
        "cruiseName": "Mediterranean With Greek Isles, France & Turkey"
      },
      {
        "id": 1294017,
        "code": "N310B",
        "name": "The Best Of The Mediterranean",
        "startDateTime": "15-Apr-2023",
        "endDateTime": "06-May-2023",
        "itinerary": {
          "id": 350163,
          "duration": 21,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain",
          "mapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS_JTR_KOTO_QME_NAP_PRJ_BCN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS_JTR_KOTO_QME_NAP_PRJ_BCN.jpg"
        },
        "uniqueItineraryId": "350163_14304__21",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2735
              },
              {
                "name": "Outside",
                "value": 4038
              },
              {
                "name": "Balcony",
                "value": 4043
              },
              {
                "name": "Suite",
                "value": 4809
              },
              {
                "code": "PortCharge",
                "value": 525
              },
              {
                "code": "CruiseTax",
                "value": 335
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "15-Apr-2023",
        "arrivalDateTime": "06-May-2023",
        "cruisePackageDepartureDateTime": "15-Apr-2023",
        "cruisePackageArrivalDateTime": "06-May-2023",
        "voyageId": "N310B",
        "stnExternalId": "1434399",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 21,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "The Best Of The Mediterranean",
        "cruiseName": "The Best Of The Mediterranean"
      },
      {
        "id": 1293899,
        "code": "N311",
        "name": "Mediterranean With Greek Isles & Turkey",
        "startDateTime": "22-Apr-2023",
        "endDateTime": "29-Apr-2023",
        "itinerary": {
          "id": 350154,
          "duration": 7,
          "departure": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece",
          "normalizedPortsOfCall": "CIV|NAP|HER|KUSA|IST|JMK|ATH",
          "mapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_ATH.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_ATH.jpg"
        },
        "uniqueItineraryId": "350154_14304__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 879
              },
              {
                "name": "Outside",
                "value": 1433
              },
              {
                "name": "Balcony",
                "value": 1426
              },
              {
                "name": "Suite",
                "value": 1679
              },
              {
                "code": "PortCharge",
                "value": 175
              },
              {
                "code": "CruiseTax",
                "value": 130
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "22-Apr-2023",
        "arrivalDateTime": "29-Apr-2023",
        "cruisePackageDepartureDateTime": "22-Apr-2023",
        "cruisePackageArrivalDateTime": "29-Apr-2023",
        "voyageId": "N311",
        "stnExternalId": "1434382",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles & Turkey",
        "cruiseName": "Mediterranean With Greek Isles & Turkey"
      },
      {
        "id": 1294018,
        "code": "N311A",
        "name": "Mediterranean With Greek Isles, Italy & Turkey",
        "startDateTime": "22-Apr-2023",
        "endDateTime": "06-May-2023",
        "itinerary": {
          "id": 350155,
          "duration": 14,
          "departure": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain",
          "mapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_ATH_JTR_KOTO_QME_NAP_BCN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_ATH_JTR_KOTO_QME_NAP_BCN.jpg"
        },
        "uniqueItineraryId": "350155_14304__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1809
              },
              {
                "name": "Outside",
                "value": 2778
              },
              {
                "name": "Balcony",
                "value": 2763
              },
              {
                "name": "Suite",
                "value": 3259
              },
              {
                "code": "PortCharge",
                "value": 350
              },
              {
                "code": "CruiseTax",
                "value": 220
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
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
          "id": 15,
          "type": "Destination",
          "priority": 50
        },
        "parentDestinationIds": [
          15
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "22-Apr-2023",
        "arrivalDateTime": "06-May-2023",
        "cruisePackageDepartureDateTime": "22-Apr-2023",
        "cruisePackageArrivalDateTime": "06-May-2023",
        "voyageId": "N311A",
        "stnExternalId": "1434384",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles, Italy & Turkey",
        "cruiseName": "Mediterranean With Greek Isles, Italy & Turkey"
      },
      {
        "id": 1294019,
        "code": "N311B",
        "name": "The Best Of The Mediterranean",
        "startDateTime": "22-Apr-2023",
        "endDateTime": "13-May-2023",
        "itinerary": {
          "id": 350164,
          "duration": 21,
          "departure": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "portsOfCalls": "Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy",
          "mapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_PIRS_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_PSA_CVV.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_PIRS_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_PSA_CVV.jpg"
        },
        "uniqueItineraryId": "350164_14304__21",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2759
              },
              {
                "name": "Balcony",
                "value": 4111
              },
              {
                "name": "Suite",
                "value": 4859
              },
              {
                "code": "PortCharge",
                "value": 525
              },
              {
                "code": "CruiseTax",
                "value": 320
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "22-Apr-2023",
        "arrivalDateTime": "13-May-2023",
        "cruisePackageDepartureDateTime": "22-Apr-2023",
        "cruisePackageArrivalDateTime": "13-May-2023",
        "voyageId": "N311B",
        "stnExternalId": "1434401",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 21,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "The Best Of The Mediterranean",
        "cruiseName": "The Best Of The Mediterranean"
      },
      {
        "id": 1294000,
        "code": "N312",
        "name": "Mediterranean With Greek Isles & Italy",
        "startDateTime": "29-Apr-2023",
        "endDateTime": "06-May-2023",
        "itinerary": {
          "id": 308372,
          "duration": 7,
          "departure": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain",
          "mapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN.jpg"
        },
        "uniqueItineraryId": "308372_14304__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 888
              },
              {
                "name": "Outside",
                "value": 1345
              },
              {
                "name": "Balcony",
                "value": 1337
              },
              {
                "name": "Suite",
                "value": 1579
              },
              {
                "code": "PortCharge",
                "value": 175
              },
              {
                "code": "CruiseTax",
                "value": 110
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "29-Apr-2023",
        "arrivalDateTime": "06-May-2023",
        "cruisePackageDepartureDateTime": "29-Apr-2023",
        "cruisePackageArrivalDateTime": "06-May-2023",
        "voyageId": "N312",
        "stnExternalId": "1434383",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles & Italy",
        "cruiseName": "Mediterranean With Greek Isles & Italy"
      },
      {
        "id": 1294020,
        "code": "N312A",
        "name": "Mediterranean With Greek Isles, France & Italy",
        "startDateTime": "29-Apr-2023",
        "endDateTime": "13-May-2023",
        "itinerary": {
          "id": 318320,
          "duration": 14,
          "departure": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "portsOfCalls": "Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy",
          "mapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_LIV_ROM.jpg",
          "fallbackMapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_LIV_ROM.jpg"
        },
        "uniqueItineraryId": "318320_14304__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1776
              },
              {
                "name": "Outside",
                "value": 2603
              },
              {
                "name": "Balcony",
                "value": 2585
              },
              {
                "name": "Suite",
                "value": 3059
              },
              {
                "code": "PortCharge",
                "value": 350
              },
              {
                "code": "CruiseTax",
                "value": 210
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "29-Apr-2023",
        "arrivalDateTime": "13-May-2023",
        "cruisePackageDepartureDateTime": "29-Apr-2023",
        "cruisePackageArrivalDateTime": "13-May-2023",
        "voyageId": "N312A",
        "stnExternalId": "1434391",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles, France & Italy",
        "cruiseName": "Mediterranean With Greek Isles, France & Italy"
      },
      {
        "id": 1294021,
        "code": "N312B",
        "name": "The Best Of The Mediterranean",
        "startDateTime": "29-Apr-2023",
        "endDateTime": "20-May-2023",
        "itinerary": {
          "id": 350165,
          "duration": 21,
          "departure": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece",
          "mapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_LIV_ROM_NAP_HER_KUSA_IST_JMK_ATH.jpg",
          "fallbackMapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_LIV_ROM_NAP_HER_KUSA_IST_JMK_ATH.jpg"
        },
        "uniqueItineraryId": "350165_14304__21",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2835
              },
              {
                "name": "Outside",
                "value": 4154
              },
              {
                "name": "Balcony",
                "value": 4160
              },
              {
                "name": "Suite",
                "value": 4919
              },
              {
                "code": "PortCharge",
                "value": 525
              },
              {
                "code": "CruiseTax",
                "value": 325
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "29-Apr-2023",
        "arrivalDateTime": "20-May-2023",
        "cruisePackageDepartureDateTime": "29-Apr-2023",
        "cruisePackageArrivalDateTime": "20-May-2023",
        "voyageId": "N312B",
        "stnExternalId": "1434402",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 21,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "cruiseTourName": "The Best Of The Mediterranean",
        "cruiseName": "The Best Of The Mediterranean"
      },
      {
        "id": 1293900,
        "code": "N313",
        "name": "Mediterranean With France & Italy",
        "startDateTime": "06-May-2023",
        "endDateTime": "13-May-2023",
        "itinerary": {
          "id": 318213,
          "duration": 7,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy",
          "normalizedPortsOfCall": "BCN|GIB|MRS|GOA|LIV1|CIV",
          "mapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_CVV.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_CVV.jpg"
        },
        "uniqueItineraryId": "318213_14304__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 879
              },
              {
                "name": "Outside",
                "value": 1258
              },
              {
                "name": "Balcony",
                "value": 1248
              },
              {
                "name": "Suite",
                "value": 1479
              },
              {
                "code": "PortCharge",
                "value": 175
              },
              {
                "code": "CruiseTax",
                "value": 130
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "06-May-2023",
        "arrivalDateTime": "13-May-2023",
        "cruisePackageDepartureDateTime": "06-May-2023",
        "cruisePackageArrivalDateTime": "13-May-2023",
        "voyageId": "N313",
        "stnExternalId": "1434549",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "Mediterranean With France & Italy",
        "cruiseName": "Mediterranean With France & Italy"
      },
      {
        "id": 1294022,
        "code": "N313A",
        "name": "Mediterranean With Greek Isles, France & Turkey",
        "startDateTime": "06-May-2023",
        "endDateTime": "20-May-2023",
        "itinerary": {
          "id": 350162,
          "duration": 14,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece",
          "normalizedPortsOfCall": "BCN|GIB|MRS|GOA|LIV1|CIV|NAP|HER|KUSA|IST|JMK|ATH",
          "mapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS.jpg"
        },
        "uniqueItineraryId": "350162_14304__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1859
              },
              {
                "name": "Balcony",
                "value": 2723
              },
              {
                "name": "Suite",
                "value": 3219
              },
              {
                "code": "PortCharge",
                "value": 350
              },
              {
                "code": "CruiseTax",
                "value": 245
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "06-May-2023",
        "arrivalDateTime": "20-May-2023",
        "cruisePackageDepartureDateTime": "06-May-2023",
        "cruisePackageArrivalDateTime": "20-May-2023",
        "voyageId": "N313A",
        "stnExternalId": "1434564",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles, France & Turkey",
        "cruiseName": "Mediterranean With Greek Isles, France & Turkey"
      },
      {
        "id": 1294023,
        "code": "N313B",
        "name": "The Best Of The Mediterranean",
        "startDateTime": "06-May-2023",
        "endDateTime": "27-May-2023",
        "itinerary": {
          "id": 350163,
          "duration": 21,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain",
          "mapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS_JTR_KOTO_QME_NAP_PRJ_BCN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS_JTR_KOTO_QME_NAP_PRJ_BCN.jpg"
        },
        "uniqueItineraryId": "350163_14304__21",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2859
              },
              {
                "name": "Outside",
                "value": 4193
              },
              {
                "name": "Balcony",
                "value": 4200
              },
              {
                "name": "Suite",
                "value": 4989
              },
              {
                "code": "PortCharge",
                "value": 525
              },
              {
                "code": "CruiseTax",
                "value": 335
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [
            "BEV",
            "DINING",
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
            }
          ]
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "06-May-2023",
        "arrivalDateTime": "27-May-2023",
        "cruisePackageDepartureDateTime": "06-May-2023",
        "cruisePackageArrivalDateTime": "27-May-2023",
        "voyageId": "N313B",
        "stnExternalId": "1434586",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 21,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "The Best Of The Mediterranean",
        "cruiseName": "The Best Of The Mediterranean"
      },
      {
        "id": 1293901,
        "code": "N314",
        "name": "Mediterranean With Greek Isles & Turkey",
        "startDateTime": "13-May-2023",
        "endDateTime": "20-May-2023",
        "itinerary": {
          "id": 350154,
          "duration": 7,
          "departure": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece",
          "normalizedPortsOfCall": "CIV|NAP|HER|KUSA|IST|JMK|ATH",
          "mapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_ATH.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_ATH.jpg"
        },
        "uniqueItineraryId": "350154_14304__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 979
              },
              {
                "name": "Balcony",
                "value": 1475
              },
              {
                "name": "Suite",
                "value": 1739
              },
              {
                "code": "PortCharge",
                "value": 175
              },
              {
                "code": "CruiseTax",
                "value": 130
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
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
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "13-May-2023",
        "arrivalDateTime": "20-May-2023",
        "cruisePackageDepartureDateTime": "13-May-2023",
        "cruisePackageArrivalDateTime": "20-May-2023",
        "voyageId": "N314",
        "stnExternalId": "1434525",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_15.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          15
        ],
        "groupInfo": [
          {
            "isAgency": true
          }
        ],
        "cruiseTourName": "Mediterranean With Greek Isles & Turkey",
        "cruiseName": "Mediterranean With Greek Isles & Turkey"
      },
      {
        "id": 1294024,
        "code": "N314A",
        "name": "Mediterranean With Greek Isles, Italy & Turkey",
        "startDateTime": "13-May-2023",
        "endDateTime": "27-May-2023",
        "itinerary": {
          "id": 350155,
          "duration": 14,
          "departure": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain",
          "mapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_ATH_JTR_KOTO_QME_NAP_BCN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_ATH_JTR_KOTO_QME_NAP_BCN.jpg"
        },
        "uniqueItineraryId": "350155_14304__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1928
              },
              {
                "name": "Balcony",
                "value": 2852
              },
              {
                "name": "Suite",
                "value": 3460
              },
              {
                "code": "PortCharge",
                "value": 350
              },
              {
                "code": "CruiseTax",
                "value": 220
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "13-May-2023",
        "arrivalDateTime": "27-May-2023",
        "cruisePackageDepartureDateTime": "13-May-2023",
        "cruisePackageArrivalDateTime": "27-May-2023",
        "voyageId": "N314A",
        "stnExternalId": "1434541",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles, Italy & Turkey",
        "cruiseName": "Mediterranean With Greek Isles, Italy & Turkey"
      },
      {
        "id": 1294025,
        "code": "N314B",
        "name": "The Best Of The Mediterranean",
        "startDateTime": "13-May-2023",
        "endDateTime": "03-Jun-2023",
        "itinerary": {
          "id": 350164,
          "duration": 21,
          "departure": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "portsOfCalls": "Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy",
          "mapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_PIRS_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_PSA_CVV.jpg",
          "fallbackMapPath": "/content/images/Itineraries/CVV_NAP_HER_KUSA_IST_JMK_PIRS_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_PSA_CVV.jpg"
        },
        "uniqueItineraryId": "350164_14304__21",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2859
              },
              {
                "name": "Balcony",
                "value": 4260
              },
              {
                "name": "Suite",
                "value": 5059
              },
              {
                "code": "PortCharge",
                "value": 525
              },
              {
                "code": "CruiseTax",
                "value": 320
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "13-May-2023",
        "arrivalDateTime": "03-Jun-2023",
        "cruisePackageDepartureDateTime": "13-May-2023",
        "cruisePackageArrivalDateTime": "03-Jun-2023",
        "voyageId": "N314B",
        "stnExternalId": "1434580",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 21,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "The Best Of The Mediterranean",
        "cruiseName": "The Best Of The Mediterranean"
      },
      {
        "id": 1293902,
        "code": "N315",
        "name": "Mediterranean With Greek Isles & Italy",
        "startDateTime": "20-May-2023",
        "endDateTime": "27-May-2023",
        "itinerary": {
          "id": 308372,
          "duration": 7,
          "departure": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "portsOfCalls": "Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain",
          "mapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN.jpg",
          "fallbackMapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN.jpg"
        },
        "uniqueItineraryId": "308372_14304__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 929
              },
              {
                "name": "Balcony",
                "value": 1377
              },
              {
                "name": "Suite",
                "value": 1649
              },
              {
                "code": "PortCharge",
                "value": 175
              },
              {
                "code": "CruiseTax",
                "value": 110
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "20-May-2023",
        "arrivalDateTime": "27-May-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "27-May-2023",
        "voyageId": "N315",
        "stnExternalId": "1434534",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles & Italy",
        "cruiseName": "Mediterranean With Greek Isles & Italy"
      },
      {
        "id": 1294026,
        "code": "N315A",
        "name": "Mediterranean With Greek Isles, France & Italy",
        "startDateTime": "20-May-2023",
        "endDateTime": "03-Jun-2023",
        "itinerary": {
          "id": 318320,
          "duration": 14,
          "departure": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "portsOfCalls": "Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy",
          "mapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_LIV_ROM.jpg",
          "fallbackMapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_LIV_ROM.jpg"
        },
        "uniqueItineraryId": "318320_14304__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 1809
              },
              {
                "name": "Outside",
                "value": 2700
              },
              {
                "name": "Balcony",
                "value": 2685
              },
              {
                "name": "Suite",
                "value": 3209
              },
              {
                "code": "PortCharge",
                "value": 350
              },
              {
                "code": "CruiseTax",
                "value": 210
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "20-May-2023",
        "arrivalDateTime": "03-Jun-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "03-Jun-2023",
        "voyageId": "N315A",
        "stnExternalId": "1434558",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles, France & Italy",
        "cruiseName": "Mediterranean With Greek Isles, France & Italy"
      },
      {
        "id": 1294027,
        "code": "N315B",
        "name": "The Best Of The Mediterranean",
        "startDateTime": "20-May-2023",
        "endDateTime": "10-Jun-2023",
        "itinerary": {
          "id": 350165,
          "duration": 21,
          "departure": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Athens (Piraeus) Greece|Santorini Greece|Kotor Montenegro|Sicily (Messina) Italy|Naples Italy (For Capri & Pompeii)|Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece",
          "mapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_LIV_ROM_NAP_HER_KUSA_IST_JMK_ATH.jpg",
          "fallbackMapPath": "/content/images/Itineraries/ATH_JTR_KOTO_QME_NAP_BCN_GIB_MRS_GOA_LIV_ROM_NAP_HER_KUSA_IST_JMK_ATH.jpg"
        },
        "uniqueItineraryId": "350165_14304__21",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2999
              },
              {
                "name": "Balcony",
                "value": 4427
              },
              {
                "name": "Suite",
                "value": 5279
              },
              {
                "code": "PortCharge",
                "value": 525
              },
              {
                "code": "CruiseTax",
                "value": 325
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "20-May-2023",
        "arrivalDateTime": "10-Jun-2023",
        "cruisePackageDepartureDateTime": "20-May-2023",
        "cruisePackageArrivalDateTime": "10-Jun-2023",
        "voyageId": "N315B",
        "stnExternalId": "1434574",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 21,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "The Best Of The Mediterranean",
        "cruiseName": "The Best Of The Mediterranean"
      },
      {
        "id": 1293903,
        "code": "N316",
        "name": "Mediterranean With France & Italy",
        "startDateTime": "27-May-2023",
        "endDateTime": "03-Jun-2023",
        "itinerary": {
          "id": 318213,
          "duration": 7,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "CIV",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy",
          "normalizedPortsOfCall": "BCN|GIB|MRS|GOA|LIV1|CIV",
          "mapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_CVV.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_CVV.jpg"
        },
        "uniqueItineraryId": "318213_14304__7",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 879
              },
              {
                "name": "Outside",
                "value": 1316
              },
              {
                "name": "Balcony",
                "value": 1308
              },
              {
                "name": "Suite",
                "value": 1559
              },
              {
                "code": "PortCharge",
                "value": 175
              },
              {
                "code": "CruiseTax",
                "value": 125
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "27-May-2023",
        "arrivalDateTime": "03-Jun-2023",
        "cruisePackageDepartureDateTime": "27-May-2023",
        "cruisePackageArrivalDateTime": "03-Jun-2023",
        "voyageId": "N316",
        "stnExternalId": "1434550",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 7,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "Mediterranean With France & Italy",
        "cruiseName": "Mediterranean With France & Italy"
      },
      {
        "id": 1294028,
        "code": "N316A",
        "name": "Mediterranean With Greek Isles, France & Turkey",
        "startDateTime": "27-May-2023",
        "endDateTime": "10-Jun-2023",
        "itinerary": {
          "id": 350162,
          "duration": 14,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "ATH",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona Spain|Gibraltar|Marseille (Provence) France|Genoa Italy|Florence/Pisa (Livorno) Italy|Rome (Civitavecchia) Italy|Naples Italy (For Capri & Pompeii)|Crete (Heraklion) Greece|Kusadasi Turkey (For Ephesus)|Istanbul Turkey|Mykonos Greece|Athens (Piraeus) Greece",
          "normalizedPortsOfCall": "BCN|GIB|MRS|GOA|LIV1|CIV|NAP|HER|KUSA|IST|JMK|ATH",
          "mapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_GIB_MRS_GOA_LIV_PSA_CVV_NAP_PRJ_HER_KUSA_IST_JMK_PIRS.jpg"
        },
        "uniqueItineraryId": "350162_14304__14",
        "prices": [
          {
            "items": [
              {
                "name": "Inside",
                "value": 2019
              },
              {
                "name": "Outside",
                "value": 2962
              },
              {
                "name": "Balcony",
                "value": 2950
              },
              {
                "name": "Suite",
                "value": 3509
              },
              {
                "code": "PortCharge",
                "value": 350
              },
              {
                "code": "CruiseTax",
                "value": 245
              }
            ],
            "currencyCode": "USD",
            "modifiedOn": "04-Jun-2022 21:40:11",
            "fareTypes": [
              "RE"
            ]
          }
        ],
        "contentInfo": {},
        "dynamicRule": {
          "fareDetailsPromoCodes": [],
          "fareDetailsPromoCodesInfo": []
        },
        "status": "Publish",
        "isActive": true,
        "destination": {
          "id": 75,
          "type": "Destination",
          "priority": 60
        },
        "parentDestinationIds": [
          15,
          75
        ],
        "ship": {
          "id": 14304,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/7/14304/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/7/14304/ship_520.jpg",
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
          14304
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "27-May-2023",
        "arrivalDateTime": "10-Jun-2023",
        "cruisePackageDepartureDateTime": "27-May-2023",
        "cruisePackageArrivalDateTime": "10-Jun-2023",
        "voyageId": "N316A",
        "stnExternalId": "1434565",
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
        "destinationImagePath": "/content/images/Itineraries/itinerary_75.jpg",
        "maxOccupancy": 8,
        "minOccupancy": 1,
        "cruiseDuration": 14,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          75,
          15
        ],
        "cruiseTourName": "Mediterranean With Greek Isles, France & Turkey",
        "cruiseName": "Mediterranean With Greek Isles, France & Turkey"
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
