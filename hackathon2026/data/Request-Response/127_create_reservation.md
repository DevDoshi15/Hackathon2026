# Create Reservation

**Path:** Create Reservation > Create Reservation With Grats/AddOns For NCL > Create Reservation

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/create`

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
            "packageId": 1238898,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "OC",
                "fare": {
                    "fareCode": {
                        "code": "DISC50"
                    }
                },
                "cabins": [
                    {
                        "number": "8031"
                    }
                ]
            }
        ],
        "dinings": [
            {
                "id": 4,
                "code": "FREEST",
                "name": "Freestyle",
                "status": 1,
                "tableSizeOptions": []
            }
        ],
        "addOns": [
            {
                "code": "PPSRVCHG"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970",
            "ContactInfo": {
                "Email": "john@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "416-555-4566"
                }
            },
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "ContactInfo": {
                "Email": "maria@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "4165554566"
                }
            }
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
Date: Fri, 17 Feb 2023 15:36:58 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "0ce0e4a3-fd73-4884-ab28-e57967be322c",
      "timeStamp": "17-Feb-2023 10:36:32",
      "token": "EQTEMPKEN"
    },
    "id": 66095,
    "agencyConfirmation": "JC891BZ",
    "cruiseReservation": {
      "id": 114075,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "52015286"
      },
      "pos": {
        "id": 2112,
        "apiId": "NCL",
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
        "packageId": 1238898,
        "packageTourId": -1
      }
    },
    "customers": [
      {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "address": {
          "country": {
            "id": "US"
          }
        },
        "contactInfo": {
          "email": "john@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "416-555-4566"
          }
        }
      },
      {
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "contactInfo": {
          "email": "maria@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "4165554566"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
