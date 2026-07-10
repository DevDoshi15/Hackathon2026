# Package Availability

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with No Transfer Package > Package Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listPackages`

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
    "cruiseReservation": {
        "pos": {
            "id": "0",
            "currency": "USD"
        },
        "cruise": {
            "packageId": 1277420,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "MM",
                "fare": {
                    "fareCode": {
                        "code": "NH1"
                    }
                }
            }
        ],
        "customerReferences": [
            {
                "RPH": "1",
                "isPrimaryContact": true
            },
            {
                "RPH": "2"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "firstName": "John",
            "lastName": "Doe"
        },
        {
            "rph": 2,
            "age": 57,
            "firstName": "Maria",
            "lastName": "Doe"
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Mon, 06 Mar 2023 08:39:27 GMT
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
      "requestId": "9932ad05-ed78-484f-933a-2fd987b4fd95",
      "timeStamp": "06-Mar-2023 03:39:25"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "02-Apr-2023 00:00:00",
        "arrivalDateTime": "09-Apr-2023 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 7
      },
      "pos": {
        "id": 2111,
        "apiId": "Carnival",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2C"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
        }
      ],
      "cruise": {
        "packageId": 1277420,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 13250
            }
          ]
        },
        "itinerary": {
          "id": 311682,
          "destination": {
            "id": 14
          }
        },
        "voyage": {
          "departureDateTime": "02-Apr-2023 00:00:00",
          "arrivalDateTime": "09-Apr-2023 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "I330"
        },
        "transportationType": 29
      },
      "packages": [
        {
          "code": "B0TNOXFR",
          "description": "NO TRANSFER",
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ],
          "packageType": "PrePackage"
        },
        {
          "code": "B0MMIAFLL-AS",
          "description": "TRANSFER MIA AIRPORT/FT LAUDERDALE",
          "prices": [
            {
              "id": 41,
              "amount": 29,
              "type": "AVGPP"
            }
          ],
          "packageType": "PrePackage"
        },
        {
          "code": "B0TFLL-AS",
          "description": "TRANSFER FLL AIRPORT/SHIP",
          "prices": [
            {
              "id": 41,
              "amount": 19,
              "type": "AVGPP"
            }
          ],
          "packageType": "PrePackage"
        },
        {
          "code": "B11FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 1 NT",
          "prices": [
            {
              "id": 41,
              "amount": 219,
              "type": "AVGPP"
            }
          ],
          "duration": 1,
          "packageType": "PrePackage"
        },
        {
          "code": "B11FLLHAM",
          "description": "HARBOR BEACH MARRIOTT RESOR - 1 NT",
          "prices": [
            {
              "id": 41,
              "amount": 229,
              "type": "AVGPP"
            }
          ],
          "duration": 1,
          "packageType": "PrePackage"
        },
        {
          "code": "B11FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 1 NT",
          "prices": [
            {
              "id": 41,
              "amount": 189,
              "type": "AVGPP"
            }
          ],
          "duration": 1,
          "packageType": "PrePackage"
        },
        {
          "code": "B11MIAFLLGEN",
          "description": "FLY/CRUISE - MIAMI HOTEL    - 1 NT",
          "prices": [
            {
              "id": 41,
              "amount": 9999,
              "type": "AVGPP"
            }
          ],
          "duration": 1,
          "packageType": "PrePackage"
        },
        {
          "code": "B21FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 2 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 388,
              "type": "AVGPP"
            }
          ],
          "duration": 2,
          "packageType": "PrePackage"
        },
        {
          "code": "B21FLLHAM",
          "description": "HARBOR BEACH MARRIOTT RESOR - 2 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 388,
              "type": "AVGPP"
            }
          ],
          "duration": 2,
          "packageType": "PrePackage"
        },
        {
          "code": "B21FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 2 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 318,
              "type": "AVGPP"
            }
          ],
          "duration": 2,
          "packageType": "PrePackage"
        },
        {
          "code": "B21MIAFLLGEN",
          "description": "FLY/CRUISE - MIAMI HOTEL    - 2 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 19998,
              "type": "AVGPP"
            }
          ],
          "duration": 2,
          "packageType": "PrePackage"
        },
        {
          "code": "B31FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 3 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 557,
              "type": "AVGPP"
            }
          ],
          "duration": 3,
          "packageType": "PrePackage"
        },
        {
          "code": "B31FLLHAM",
          "description": "HARBOR BEACH MARRIOTT RESOR - 3 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 547,
              "type": "AVGPP"
            }
          ],
          "duration": 3,
          "packageType": "PrePackage"
        },
        {
          "code": "B31FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 3 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 447,
              "type": "AVGPP"
            }
          ],
          "duration": 3,
          "packageType": "PrePackage"
        },
        {
          "code": "B31MIAFLLGEN",
          "description": "FLY/CRUISE - MIAMI HOTEL    - 3 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 29997,
              "type": "AVGPP"
            }
          ],
          "duration": 3,
          "packageType": "PrePackage"
        },
        {
          "code": "A0TNOXFR",
          "description": "NO TRANSFER",
          "prices": [
            {
              "id": 41,
              "amount": 0,
              "type": "AVGPP"
            }
          ],
          "packageType": "PostPackage"
        },
        {
          "code": "A0MFLLMIA-SA",
          "description": "TRANSFER FT LAUDERDALE SHIP/MIA AIR",
          "prices": [
            {
              "id": 41,
              "amount": 29,
              "type": "AVGPP"
            }
          ],
          "packageType": "PostPackage"
        },
        {
          "code": "A0TFLL-SA",
          "description": "TRANSFER FLL SHIP/AIRPORT",
          "prices": [
            {
              "id": 41,
              "amount": 19,
              "type": "AVGPP"
            }
          ],
          "packageType": "PostPackage"
        },
        {
          "code": "A12FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 1 NT",
          "prices": [
            {
              "id": 41,
              "amount": 219,
              "type": "AVGPP"
            }
          ],
          "duration": 1,
          "packageType": "PostPackage"
        },
        {
          "code": "A12FLLHAM",
          "description": "HARBOR BEACH MARRIOTT RESOR - 1 NT",
          "prices": [
            {
              "id": 41,
              "amount": 229,
              "type": "AVGPP"
            }
          ],
          "duration": 1,
          "packageType": "PostPackage"
        },
        {
          "code": "A12FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 1 NT",
          "prices": [
            {
              "id": 41,
              "amount": 189,
              "type": "AVGPP"
            }
          ],
          "duration": 1,
          "packageType": "PostPackage"
        },
        {
          "code": "A22FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 2 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 388,
              "type": "AVGPP"
            }
          ],
          "duration": 2,
          "packageType": "PostPackage"
        },
        {
          "code": "A22FLLHAM",
          "description": "HARBOR BEACH MARRIOTT RESOR - 2 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 388,
              "type": "AVGPP"
            }
          ],
          "duration": 2,
          "packageType": "PostPackage"
        },
        {
          "code": "A22FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 2 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 318,
              "type": "AVGPP"
            }
          ],
          "duration": 2,
          "packageType": "PostPackage"
        },
        {
          "code": "A32FLLELM",
          "description": "ELEMENT FORT LAUDERDALE     - 3 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 557,
              "type": "AVGPP"
            }
          ],
          "duration": 3,
          "packageType": "PostPackage"
        },
        {
          "code": "A32FLLHAM",
          "description": "HARBOR BEACH MARRIOTT RESOR - 3 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 547,
              "type": "AVGPP"
            }
          ],
          "duration": 3,
          "packageType": "PostPackage"
        },
        {
          "code": "A32FLLRFP",
          "description": "RENAISSANCE FT LAUDERDALE W - 3 NTS",
          "prices": [
            {
              "id": 41,
              "amount": 447,
              "type": "AVGPP"
            }
          ],
          "duration": 3,
          "packageType": "PostPackage"
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "age": 52
      },
      {
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
