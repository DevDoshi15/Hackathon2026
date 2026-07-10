# Create Reservation With Gratuities

**Path:** Modify Reservation > Create Reservation With Gratuities then Modify By Adding Insurance > Create Reservation With Gratuities

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
        "cruise": {
            "packageId": 1307173
        },
        "categories": [
            {
                "code": "SL",
                "fare": {
                    "fareCode": {
                        "code": "BESTFARE"
                    }
                },
                "cabins": [
                    {
                        "number": "12702"
                    }
                ]
            }
        ],
        "addOns": [
            {
                "code": "PPSRVCHG" // Gratuties information can be found in FareCode Availability API
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
                    "Number": "416-555-4566"
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
Date: Thu, 04 May 2023 08:44:41 GMT
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
    "trackingInfo": {
      "requestId": "4f297d41-0d91-42e7-a92a-05d9fe219f30",
      "timeStamp": "04-May-2023 04:44:29",
      "token": "EQTEMPKEN"
    },
    "id": 69732,
    "agencyConfirmation": "INY5QBK",
    "cruiseReservation": {
      "id": 117712,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "52029814"
      },
      "pos": {
        "id": 2250,
        "apiId": "NCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2B"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 57895,
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 57894
        }
      ],
      "cruise": {
        "packageId": 1307173
      }
    },
    "customers": [
      {
        "gender": "Male",
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
        "gender": "Male",
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "contactInfo": {
          "email": "maria@domain.com",
          "phone1": {
            "countryCode": "1",
            "number": "416-555-4566"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
