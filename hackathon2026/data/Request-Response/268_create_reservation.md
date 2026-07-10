# Create Reservation

**Path:** Create Reservation > Create Reservation With Air For P&O Cruise line > Create Reservation

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
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": {
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "MAN"
            }
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
            "packageId": 1501519,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "B2",
                "fare": {
                    "farecode": {
                        "code": "KD1"
                    }
                },
                "cabins": [
                    {
                        "number": "R412"
                    }
                ]
            }
        ],
         "dinings": [
                {
                    "id": 22,
                    "code": "1",
                    "name": "Early",
                    "status": 1,
                    "diningRoom": {
                        "type": "FIRST SEATING"
                    }
                }]
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "middleName":"FA",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970",
            "age": 53,
            "address": {
                "country": {
                    "id": "GB"
                },
                "city": {
                    "name": "London"
                }
            },
            "ContactInfo": {
                "Email": "john@domain.com",
                "Phone1": {
                    "CountryCode": "44",
                    "Number": "416-555-4566"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "middleName":"FA",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "age": 58,
            "address": {
                "country": {
                    "id": "GB"
                }
            },
            "ContactInfo": {
                "Email": "maria@domain.com",
                "Phone1": {
                    "CountryCode": "44",
                    "Number": "416-555-4566"
                }
            }
        }
    ]
}
```

## Response

**Status:** OK (200)

### Response Headers

```
Server: nginx
Date: Wed, 08 Feb 2023 09:05:19 GMT
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
  "advisories": [
    {
      "code": "35",
      "message": "CONSUMER ADVICE",
      "description": "NON-COMMISSIONABLE FARE OF    109.00 GBP PER PERSON IS INCLUDED IN THE CRUISE FARE.",
      "type": "Information"
    }
  ],
  "data": {
    "trackingInfo": {
      "requestId": "7fbf5168-6c1f-4f68-8256-1c7a10e39831",
      "timeStamp": "23-Jun-2026 07:39:56",
      "token": "EQTEMPKEN"
    },
    "id": 142511,
    "agencyConfirmation": "SRP9UFA",
    "cruiseReservation": {
      "id": 191374,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "2D9J4H"
      },
      "pos": {
        "id": 3487,
        "officeId": "O212GBTP17",
        "currency": "GBP",
        "type": "B2B",
        "system": "Test",
        "apiId": "Carnival"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 133165,
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 133166
        }
      ],
      "currencyInfo": {
        "currencyId": "GBP",
        "countryId": "GB"
      },
      "externalSessionInfo": {
        "externalId": "a@#$A721"
      },
      "type": "Cruise",
      "cruise": {
        "packageId": 1501519
      },
      "categories": [
        {
          "id": 60438,
          "code": "B2",
          "fares": [
            {
              "fareCode": {
                "code": "KD1",
                "type": 0
              }
            }
          ]
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "firstName": "John",
        "middleName": "FA",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "age": 53,
        "address": {
          "city": {
            "name": "London"
          },
          "country": {
            "id": "GB"
          }
        },
        "contactInfo": {
          "email": "john@domain.com",
          "phone1": {
            "countryCode": "44",
            "number": "416-555-4566"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "firstName": "Maria",
        "middleName": "FA",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "age": 58,
        "address": {
          "country": {
            "id": "GB"
          }
        },
        "contactInfo": {
          "email": "maria@domain.com",
          "phone1": {
            "countryCode": "44",
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
