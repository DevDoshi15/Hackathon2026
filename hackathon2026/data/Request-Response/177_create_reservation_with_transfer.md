# Create Reservation With Transfer

**Path:** Create Reservation > Create Reservation With Transfer (Pre/Post Airport Transfer) > Create Reservation With Transfer

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
            "packageId": 1269292
        },
        "Packages": [
            {
                "Type": "RoundTransfer",
                "Code": "THOUPD",
                "AdditionalCode": "7"
            }
        ],
        "Dinings": [
            {
                "id": 1,
                "code": "M",
                "name": "05:30 PM",
                "status": 1,
                "tableSizeOptions": []
            }
        ],
        "categories": [
            {
                "code": "4V",
                "fare": {
                    "fareCode": {
                        "code": "I0452040"
                    }
                },
                "Cabins": [
                    {
                        "Number": "6645"
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
Date: Mon, 06 Mar 2023 10:11:53 GMT
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
      "code": "CSW0706",
      "message": "W-DEPOSIT IS NON REFUNDABLE 100 USD CHANGE FEE PER GUEST.",
      "type": "Warning"
    }
  ],
  "data": {
    "trackingInfo": {
      "requestId": "69ef24c4-daf4-4cae-afb0-0acddc86a5d8",
      "timeStamp": "06-Mar-2023 05:11:46"
    },
    "id": 66315,
    "agencyConfirmation": "VWH553C",
    "cruiseReservation": {
      "id": 114295,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "382380"
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
          "ageGroup": "Adult",
          "isPrimaryContact": true
        },
        {
          "rph": 2,
          "ageGroup": "Adult"
        }
      ],
      "cruise": {
        "packageId": 1269292
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
