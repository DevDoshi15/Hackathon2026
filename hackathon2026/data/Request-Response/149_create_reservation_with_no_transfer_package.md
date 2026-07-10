# Create Reservation With No Transfer Package

**Path:** Create Reservation > Create Reservation With Packages > Create Reservation with No Transfer Package > Create Reservation With No Transfer Package

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
            "packageId": 1277420
        },
        "Packages": [ // element to indicate Transfers are not required, if not sent, some cruiselines like Holland America will include that by default
            {
                "Type": "PrePackage",
                "Code": "B0TNOXFR"
            },
            {
                "Type": "PostPackage",
                "Code": "A0TNOXFR"
            }
        ],
        "Dinings": [
            {
                "id": 8,
                "code": "3",
                "name": "Early Seating Upper Level 5:45 PM",
                "status": 1,
                "tableSizeOptions": []
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
                        "number": "8146"
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
Date: Mon, 06 Mar 2023 08:51:46 GMT
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
      "requestId": "ec9ccb00-af05-4138-91f2-fb0508fda053",
      "timeStamp": "06-Mar-2023 03:51:38"
    },
    "id": 66312,
    "agencyConfirmation": "BIBUYET",
    "cruiseReservation": {
      "id": 114292,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "XTVDVT"
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
        "packageId": 1277420
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
