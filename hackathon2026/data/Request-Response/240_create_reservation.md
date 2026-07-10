# Create Reservation

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 4 – All Adults (NCL) > Create Reservation

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
            "packageId": 1312610,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "H5",
                "fare": {
                    "fareCode": {
                        "code": "BESTFARE"
                    }
                },
                "cabins": [
                    {
                        "number": "17104"
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
            "dateOfBirth": "02-Jan-1993",
            "age": 30,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 4,
            "firstName": "Johny",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1983",
            "age": 40,
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
Date: Fri, 31 Mar 2023 08:52:28 GMT
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
      "requestId": "ae4613af-a52b-4c0c-8300-5b98f0762a52",
      "timeStamp": "31-Mar-2023 04:52:10",
      "token": "EQTEMPKEN"
    },
    "id": 66843,
    "agencyConfirmation": "3ZLE77J",
    "cruiseReservation": {
      "id": 114823,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "52023472"
      },
      "pos": {
        "id": 2250,
        "apiId": "NCL",
        "officeId": "O100US6797",
        "system": "Test",
        "currency": "USD",
        "type": "B2C"
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
          "odyCustomerRef": 60899
        },
        {
          "rph": 4,
          "ageGroup": "Adult",
          "odyCustomerRef": 60900
        }
      ],
      "cruise": {
        "packageId": 1312610,
        "packageTourId": -1
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
        "dateOfBirth": "02-Jan-1993",
        "age": 30,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 4,
        "firstName": "Johny",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1983",
        "age": 40,
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
