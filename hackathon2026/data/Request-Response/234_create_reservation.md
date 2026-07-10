# Create Reservation

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 4 – All Adults (RCCL) > Create Reservation

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
                "code": "ZI",
                "fare": {
                    "fareCode": {
                        "code": "G0738129"
                    }
                },
                "cabins": [
                    {
                        "number": "GTY"
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
            "dateOfBirth": "12-Jan-1993",
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 4,
            "firstName": "Martina",
            "lastName": "Doe",
            "dateOfBirth": "12-Jan-1993",
            "age": 30,
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
Date: Mon, 27 Mar 2023 10:12:44 GMT
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
      "requestId": "c031dd2c-a101-4bf4-b3be-e4b0ceb13028",
      "timeStamp": "27-Mar-2023 06:12:32",
      "token": "EQTEMPKEN"
    },
    "id": 66740,
    "agencyConfirmation": "JZA7SRH",
    "cruiseReservation": {
      "id": 114720,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "388465"
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
          "ageGroup": "Adult",
          "odyCustomerRef": 60847
        },
        {
          "rph": 4,
          "ageGroup": "Adult",
          "odyCustomerRef": 60848
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
        "dateOfBirth": "12-Jan-1993",
        "age": 30,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 4,
        "firstName": "Martina",
        "lastName": "Doe",
        "dateOfBirth": "12-Jan-1993",
        "age": 30,
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
