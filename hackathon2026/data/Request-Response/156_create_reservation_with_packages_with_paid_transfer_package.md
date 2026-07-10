# Create Reservation With Packages With Paid Transfer Package

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with Paid Transfer Package > Create Reservation With Packages With Paid Transfer Package

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
            "packageId": 1298928
        },
        "Packages": [ // packages to be included for the reservation
            {
                "Type": "PrePackage",
                "Code": "B11YVRPAN"
            },
            {
                "Type": "PostPackage",
                "Code": "A22YVRPAN"
            }
        ],
        "Dinings": [
            {
                "id": 8,
                "code": "3",
                "name": "Early Seating Upper Level 5:45 PM",
                "status": 1
            }
        ],
        "categories": [
            {
                "code": "MM",
                "fare": {
                    "fareCode": {
                        "code": "NH1"
                    }
                },
                "cabins": [
                    {
                        "number": "GUAR"
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "title": "Mr",
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970", // Here Date of Birth is mandatory for all travellers
            "gender": "Male",
            "age": 52,
            "address": {
                "city": {
                    "id": "MIA"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
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
            "title": "Mrs",
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "gender": "Female",
            "age": 57,
            "address": {
                "city": {
                    "id": "MIA"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            },
            "ContactInfo": {
                "Email": "maria@domain.com",
                "Phone1": {
                    "CountryCode": "1",
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
Date: Thu, 09 Mar 2023 12:31:18 GMT
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
  "advisories": [],
  "data": {
    "trackingInfo": {
      "requestId": "f807179d-d61b-463a-b6b6-0dc53a9c61a5",
      "timeStamp": "09-Mar-2023 07:31:10"
    },
    "id": 66395,
    "agencyConfirmation": "6JA5D8G",
    "cruiseReservation": {
      "id": 114375,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "XTWC3R"
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
        "packageId": 1298928
      }
    },
    "customers": [
      {
        "title": "MR",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1970",
        "age": 52,
        "address": {
          "city": {
            "id": "MIA"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
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
        "title": "MRS",
        "gender": "Female",
        "rph": 2,
        "firstName": "Maria",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1965",
        "age": 57,
        "address": {
          "city": {
            "id": "MIA"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        },
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
