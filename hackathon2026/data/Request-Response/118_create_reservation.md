# Create Reservation

**Path:** Create Reservation > Create Reservation With Grats For Carnival > Create Reservation

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
            "packageId": 1281377,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "6C",
                "fare": {
                    "fareCode": {
                        "code": "PNS"
                    }
                },
                "cabins": [
                    {
                        "number": "2280"
                    }
                ]
            }
        ],
        "dinings": [
            {
                "id": 22,
                "code": "1",
                "name": "Early",
                "status": 1
            }
        ],
        "services": [
            {
                "code": "GRATS",
                "Type": "PREPAIDGRATUITIES"
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
Date: Mon, 24 Apr 2023 10:05:45 GMT
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
  "advisories": [
    {
      "code": "1217",
      "message": "This is a vaccinated voyage available for guests who have received their final dose of an approved COVID-19 vaccine at least 14 days prior to embarkation day and have proof of vaccination. Unvaccinated guests can apply for a vaccine exemption.",
      "description": "CCL-",
      "type": "Warning"
    }
  ],
  "data": {
    "trackingInfo": {
      "requestId": "7be74502-d48b-476a-9ac1-53b339f81336",
      "timeStamp": "24-Apr-2023 06:05:22",
      "token": "EQTEMPKEN"
    },
    "id": 69314,
    "agencyConfirmation": "C9UQKFY",
    "cruiseReservation": {
      "id": 117294,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "4JCHM2"
      },
      "pos": {
        "id": 2220,
        "apiId": "Carnival",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "Any"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 57895,
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1281377,
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
