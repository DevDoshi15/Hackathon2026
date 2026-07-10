# Create Reservation

**Path:** Create Reservation > Create Reservation With Combinable FareCodes > Create Reservation

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
            "packageId": 1269619,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "2N",
                "fare": {
                    "fareCode": {
                        "code": "G0738129",
                        "combinableFares": [
                            {
                                "code": "I7996069",
                                "type": 0
                            },
                            {
                                "code": "I7997687",
                                "type": 0
                            }
                        ]
                    }
                },
                "cabins": [
                    {
                        "number": "2616"
                    }
                ]
            }
        ],
        "dinings": [
            {
                "id": 1,
                "code": "M",
                "name": "05:30 PM",
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
Date: Mon, 20 Feb 2023 09:34:29 GMT
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
      "requestId": "abbf43b1-ccf0-45b3-b972-08179fbf6a6d",
      "timeStamp": "20-Feb-2023 04:34:06",
      "token": "EQTEMPKEN"
    },
    "id": 66110,
    "agencyConfirmation": "L1D5DDJ",
    "cruiseReservation": {
      "id": 114090,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "378173"
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
          "isPrimaryContact": true
        },
        {
          "rph": 2
        }
      ],
      "cruise": {
        "packageId": 1269619,
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
