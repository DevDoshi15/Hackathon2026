# Create Reservation

**Path:** Create Reservation > Create Reservation For MSC > Create Reservation

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
        "pos": {
            "Currency": "USD"
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
            "packageId": 1324816
        },
        "dinings": [
            {
                "id": 42,
                "code": "CL",
                "name": "Classic Late Seating",
                "description": "N",
                "status": 1,
                "tableSizeOptions": []
            }
        ],
        "categories": [
            {
                "code": "IR1",
                "fare": {
                    "fareCode": {
                        "code": "EZAT35DZE"
                    }
                },
                "cabins": [
                    {
                        "number": "10320"
                    }
                ]
            }
        ],
        "addOns": [
            {
                "code": "EXP2B",
                "name": "Fantastica Experience Benefits",
                "description": "",
                "prices": [
                    {
                        "amount": 0.0,
                        "type": "AVGPP"
                    },
                    {
                        "amount": 0.0,
                        "type": "TOTAL"
                    }
                ],
                "startDate": "01-Apr-2023",
                "endDate": "01-Apr-2023",
                "type": 23,
                "autoInclude": true,
                "additionalCode": "636713325",
                "combinableCodes": []
            },
            {
                "code": "600",
                "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                "description": "",
                "prices": [
                    {
                        "amount": 0.0,
                        "type": "AVGPP"
                    },
                    {
                        "amount": 0.0,
                        "type": "TOTAL"
                    }
                ],
                "startDate": "01-Apr-2023",
                "endDate": "01-Apr-2023",
                "type": 6,
                "autoInclude": true,
                "additionalCode": "636713572",
                "combinableCodes": []
            }
        ],
        "Insurance": {
            "code": "CSA2CP", // Insurance code received in the Hold Cabin (for MSC, RCCL and NCL) or in Fare Availability (for Carnival) in response
            "type": 2, // type 2 = supplier insurance
            "CustomerReferences": [
                {
                    "rph": 1 //customer for which insurance prices are to be retrieved
                }
            ]
        }
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
Date: Fri, 17 Feb 2023 12:16:40 GMT
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
      "requestId": "dae4e6bc-07fc-4851-9ef2-224e70e4e95e",
      "timeStamp": "17-Feb-2023 07:16:11",
      "token": "EQTEMPKEN"
    },
    "id": 66087,
    "agencyConfirmation": "K2M3T1J",
    "cruiseReservation": {
      "id": 114067,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "45605618"
      },
      "pos": {
        "id": 2119,
        "apiId": "MSC",
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
        "packageId": 1324816
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
