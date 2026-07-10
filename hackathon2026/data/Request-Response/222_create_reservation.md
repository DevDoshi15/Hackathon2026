# Create Reservation

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 3 (2 Adults + 1 Child) Kids Special Package (RCCL) > Create Reservation

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
//This request contains only mandatory elements
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1269434
        },
        "categories": [
            {
                "code": "VP",
                "fare": {
                    "fareCode": {
                        "code": "I9610792"
                    }
                },
                "cabins": [
                    {
                        "number": "1854"
                    }
                ]
            }
        ],
        "dinings": [
            {
                "id": 1,
                "code": "M",
                "name": "05:15 PM",
                "status": 1,
                "tableSizeOptions": []
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1992",
            "age": 31,
            "address": {
                "country": {
                    "id": "US"
                }
            },
            "ContactInfo": {
                "Email": "john@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "416-555-4566"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1993",
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 3,
            "firstName": "Johny",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-2013",
            "age": 10,
            "address": {
                "country": {
                    "id": "US"
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
Date: Mon, 27 Mar 2023 11:13:11 GMT
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
      "requestId": "a9550476-27a8-40ef-8184-6446d8f409ae",
      "timeStamp": "27-Mar-2023 07:12:59",
      "token": "EQTEMPKEN"
    },
    "id": 66743,
    "agencyConfirmation": "6HLM3D9",
    "cruiseReservation": {
      "id": 114723,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "388506"
      },
      "pos": {
        "id": 2227,
        "apiId": "RCCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2B"
      },
      "customerReferences": [
        {
          "rph": 1,
          "ageGroup": "Adult",
          "odyCustomerRef": 60846,
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult",
          "odyCustomerRef": 60826
        },
        {
          "rph": 3,
          "ageGroup": "Child",
          "odyCustomerRef": 60838
        }
      ],
      "cruise": {
        "packageId": 1269434
      }
    },
    "customers": [
      {
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1992",
        "age": 31,
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
        "dateOfBirth": "02-Jan-1993",
        "age": 30,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 3,
        "firstName": "Johny",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-2013",
        "age": 10,
        "address": {
          "country": {
            "id": "US"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
