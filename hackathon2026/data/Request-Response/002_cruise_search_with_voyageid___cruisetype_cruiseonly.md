# Cruise Search with VoyageId & CruiseType CruiseOnly

**Path:** Cruise Search > Cruise Only Search > Viking Ocean Cruises > Cruise Search with VoyageId & CruiseType CruiseOnly

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
                "OSK230414C"
            ]
        },
        {
            "key": "cruiseType",
            "values": [
                "CruiseOnly"
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
Date: Thu, 30 Mar 2023 15:50:38 GMT
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
    "total": 1,
    "pageStart": 1,
    "pageSize": 20,
    "list": [
      {
        "id": 1234358,
        "code": "OSK230414C",
        "name": "Mediterranean's Iconic Shores",
        "startDateTime": "14-Apr-2023",
        "endDateTime": "12-May-2023",
        "itinerary": {
          "id": 340759,
          "duration": 28,
          "departure": {
            "code": "BCN",
            "type": "CruisePort"
          },
          "arrival": {
            "code": "IST",
            "type": "CruisePort"
          },
          "portsOfCalls": "Barcelona|Barcelona|Montpellier (Sete)|Marseille|Monte Carlo|Florencepisa (Livorno)|Florencepisa (Livorno)|Rome (Civitavecchia)|Naples|Sicily (Messina)|Crotone|Bari|Sibenik|Venice|Venice|Venice|Split|Dubrovnik|Kotor|Corfu (Kerkyra)|Katakolon (Olympia)|Athens (Piraeus)|Athens (Piraeus)|Crete (Heraklion)|Rhodes|Ephesus (Kusadasi)|Troy (Canakkale)|Istanbul|Istanbul",
          "normalizedPortsOfCall": "BCN|SETE|MRS|MCM|LIV1|CIV|NAP|QME|CRV|BRI|SIBN|VCE|SPU|DBV|KOTO|CFU|KAR1|PIRA|HER|RHO|KUSA|CKZ|IST",
          "mapPath": "/content/images/Itineraries/BCN_MPL_MRS_MCM_LIV_ROM_NAP_QME_CRV_BRI_SIB_VCE_SPU_DBV_KOTO_CFU_KAK_ATH_HER_RHO_KUSA_CKZ_IST.jpg",
          "fallbackMapPath": "/content/images/Itineraries/BCN_MPL_MRS_MCM_LIV_ROM_NAP_QME_CRV_BRI_SIB_VCE_SPU_DBV_KOTO_CFU_KAK_ATH_HER_RHO_KUSA_CKZ_IST.jpg"
        },
        "uniqueItineraryId": "340759_13710__28",
        "prices": [
          {
            "items": [
              {
                "name": "Balcony",
                "value": 15396
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
          "id": 57,
          "type": "Destination",
          "priority": 61
        },
        "parentDestinationIds": [
          75
        ],
        "ship": {
          "id": 13710,
          "priority": 100,
          "images": [
            {
              "path": "/content/images/cruise/8175/13710/ship_150.jpg",
              "type": "Image",
              "imageType": "Small"
            },
            {
              "path": "/content/images/cruise/8175/13710/ship_375.jpg",
              "type": "Image",
              "imageType": "Medium"
            },
            {
              "path": "/content/images/cruise/8175/13710/ship_520.jpg",
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
          13710
        ],
        "cruiseType": "CruiseOnly",
        "departureDateTime": "14-Apr-2023",
        "arrivalDateTime": "12-May-2023",
        "cruisePackageDepartureDateTime": "14-Apr-2023",
        "cruisePackageArrivalDateTime": "12-May-2023",
        "voyageId": "OSK230414C",
        "stnExternalId": "1411076",
        "packageTourId": -1,
        "categoryTypes": [
          "Balcony",
          "Suite"
        ],
        "bookingSettings": {
          "bookingMode": "Online"
        },
        "destinationImagePath": "/content/images/Itineraries/itinerary_57.jpg",
        "maxOccupancy": 2,
        "minOccupancy": 1,
        "cruiseDuration": 28,
        "minGuestAge": 0,
        "alternateItineraryInfo": [],
        "destinationIds": [
          57
        ],
        "cruiseTourName": "Mediterranean's Iconic Shores",
        "cruiseName": "Mediterranean's Iconic Shores"
      }
    ],
    "rules": []
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
