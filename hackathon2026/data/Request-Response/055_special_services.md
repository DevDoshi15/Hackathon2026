# Special Services

**Path:** Special Services > Special Services

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listSpecialservices`

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
//This request contains only mandatory elements
{
  "cruiseReservation": {
    "pos": {
      "currency": "USD"
    },
    "customerReferences": [
      {
        "rph": 1,
        "isPrimaryContact": true
      },
      {
        "rph": 2
      }
    ],
    "cruise": {
      "packageId": 1269434,
      "packageTourId": -1
    },
    "categories": [
      {
        "code": "2B",
        "fare": {
          "fareCode": {
            "code": "G0737880"
          }
        },
        "cabins": [
          {
            "number": "9330"
          }
        ]
      }
    ]
  },
  "customers": [
    {
      "rph": 1,
      "age": 52
    },
    {
      "rph": 2,     
      "age": 57
    }
  ],
  "trackingInfo": {
    "token": "EQTEMPKEN"
  }
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 01 Feb 2023 11:07:57 GMT
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
    "trackingInfo": {
      "requestId": "e70ff201-ca92-4336-ac68-442ee181a2e4",
      "timeStamp": "01-Feb-2023 06:07:56",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 4
      },
      "pos": {
        "id": 2114,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2C"
      },
      "customerReferences": [
        {
          "rph": 1,
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 311051,
          "destination": {
            "id": 7
          }
        },
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
        },
        "transportationType": 29
      },
      "serviceCollection": {
        "maxSelection": 4,
        "services": [
          {
            "code": "ANV",
            "name": "ANNIVERSARY",
            "description": "ANNIVERSARY",
            "type": "Celebration",
            "associationType": "PAX",
            "dateRequired": true,
            "numberOfYearsRequired": true
          },
          {
            "code": "BDY",
            "name": "BIRTHDAY",
            "description": "BIRTHDAY",
            "type": "Celebration",
            "dateRequired": true
          },
          {
            "code": "CAK",
            "name": "HONEYMOON",
            "description": "HONEYMOON",
            "type": "Celebration",
            "associationType": "PAX"
          },
          {
            "code": "CAL",
            "name": "RETIREMENT",
            "description": "RETIREMENT",
            "type": "Celebration"
          },
          {
            "code": "CRI",
            "name": "CRIBS",
            "description": "CRIBS",
            "type": "Children"
          },
          {
            "code": "ENG",
            "name": "ENGAGEMENT",
            "description": "ENGAGEMENT",
            "type": "Celebration",
            "associationType": "PAX"
          },
          {
            "code": "GRD",
            "name": "GRADUATION",
            "description": "GRADUATION",
            "type": "Celebration"
          },
          {
            "code": "HIG",
            "name": "HIGHCHAIR",
            "description": "HIGH CHAIR",
            "type": "Children"
          },
          {
            "code": "HND",
            "name": "DISABLED",
            "description": "DISABLED",
            "type": "Medical"
          },
          {
            "code": "REU",
            "name": "REUNION",
            "description": "REUNION",
            "type": "Celebration"
          },
          {
            "code": "SBE",
            "name": "SOFABED",
            "description": "SOFA BED",
            "type": "Housekeeping"
          },
          {
            "code": "af-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Afrikaans",
            "type": "Language"
          },
          {
            "code": "ar-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Arabic Standard",
            "type": "Language"
          },
          {
            "code": "bg-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Bulgarian",
            "type": "Language"
          },
          {
            "code": "ca-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Catalan",
            "type": "Language"
          },
          {
            "code": "zh-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Chinese Mandari",
            "type": "Language"
          },
          {
            "code": "cs-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Czech",
            "type": "Language"
          },
          {
            "code": "da-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Danish",
            "type": "Language"
          },
          {
            "code": "nl-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Dutch",
            "type": "Language"
          },
          {
            "code": "en-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "English",
            "type": "Language"
          },
          {
            "code": "fi-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Finnish",
            "type": "Language"
          },
          {
            "code": "fr-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "French",
            "type": "Language"
          },
          {
            "code": "de-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "German",
            "type": "Language"
          },
          {
            "code": "el-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Greek",
            "type": "Language"
          },
          {
            "code": "kl-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Greenlandic",
            "type": "Language"
          },
          {
            "code": "he-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Hebrew",
            "type": "Language"
          },
          {
            "code": "hi-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Hindi",
            "type": "Language"
          },
          {
            "code": "hu-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Hungarian",
            "type": "Language"
          },
          {
            "code": "is-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Icelandic",
            "type": "Language"
          },
          {
            "code": "id-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Indonesian",
            "type": "Language"
          },
          {
            "code": "it-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Italian",
            "type": "Language"
          },
          {
            "code": "ja-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Japanese",
            "type": "Language"
          },
          {
            "code": "ko-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Korean",
            "type": "Language"
          },
          {
            "code": "ky-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "KYRGYZ",
            "type": "Language"
          },
          {
            "code": "ms-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Malay",
            "type": "Language"
          },
          {
            "code": "no-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Norwegian",
            "type": "Language"
          },
          {
            "code": "pl-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Polish",
            "type": "Language"
          },
          {
            "code": "pt-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Portuguese",
            "type": "Language"
          },
          {
            "code": "ro-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Romanian",
            "type": "Language"
          },
          {
            "code": "ru-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Russian",
            "type": "Language"
          },
          {
            "code": "hr-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Serbo-Croatian",
            "type": "Language"
          },
          {
            "code": "sk-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Slovak",
            "type": "Language"
          },
          {
            "code": "sl-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Slovenian",
            "type": "Language"
          },
          {
            "code": "es-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Spanish",
            "type": "Language"
          },
          {
            "code": "sw-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Swahili",
            "type": "Language"
          },
          {
            "code": "sv-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Swedish",
            "type": "Language"
          },
          {
            "code": "th-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Thai",
            "type": "Language"
          },
          {
            "code": "tr-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Turkish",
            "type": "Language"
          },
          {
            "code": "uk-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Ukrainian",
            "type": "Language"
          },
          {
            "code": "vi-LNP",
            "name": "PREFERREDLANGUAGE",
            "description": "Vietnamese",
            "type": "Language"
          },
          {
            "code": "en-LND",
            "name": "DOCUMENTLANGUAGE",
            "description": "English",
            "type": "Language"
          },
          {
            "code": "es-LND",
            "name": "DOCUMENTLANGUAGE",
            "description": "Spanish",
            "type": "Language"
          },
          {
            "code": "fr-LND",
            "name": "DOCUMENTLANGUAGE",
            "description": "French",
            "type": "Language"
          },
          {
            "code": "zh-LND",
            "name": "DOCUMENTLANGUAGE",
            "description": "Chinese Mandari",
            "type": "Language"
          },
          {
            "code": "pt-LND",
            "name": "DOCUMENTLANGUAGE",
            "description": "Portuguese",
            "type": "Language"
          }
        ]
      }
    },
    "customers": [
      {
        "rph": 1,
        "age": 52
      },
      {
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
