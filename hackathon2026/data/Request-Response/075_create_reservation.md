# Create Reservation

**Path:** Create Reservation > Create Reservation With Air For SilverSea > Create Reservation

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
                "id": "NYC"
            }
        },
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
        "supplierCommunicationInfo":{
            "agency":{
                "phone1":{
                    "countryCode": "1",
                    "number": "1234567890"
                },
                "email": "john@domain.com"
            },
            "agent":{
                "phone1":{
                    "countryCode": "1",
                    "number": "1234567890"
                },
                "email": "john@domain.com"
            }
        },
        "cruise": {
            "packageId": 1252535,
            "packageTourId": -1
        },
        "categories": [
            {
                "Fare": {
                    "fareCode": {
                        "Code": "03",
                        "externalSessionInfo": {
                            "externalId": "03"
                        }
                    }
                },
                "Code": "SV",
                "cabins": [
                    {
                        "number": "704"
                    }
                ]
            }
        ],
        "addOns": [
            {
                "code": "E",
                "name": "Economy Class Air",
                "description": "",
                "occupancy": {
                    "min": 0,
                    "max": 0
                },
                "currency": "USD",
                "autoInclude": false,
                "combinableCodes": []
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "title": "MR",
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
                }
            }
        },
        {
            "rph": 2,
            "title": "MR",
            "firstName": "Jack",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1988",
            "gender": "Male",
            "age": 35,
            "address": {
                "city": {
                    "name": "MIAMI"
                },
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "FL"
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
Date: Fri, 10 Feb 2023 13:33:29 GMT
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
      "requestId": "d6f30daf-feac-4dc0-b17b-e986922a8fc0",
      "timeStamp": "10-Feb-2023 08:32:28",
      "token": "EQTEMPKEN"
    },
    "id": 65952,
    "agencyConfirmation": "M6FJOAF",
    "cruiseReservation": {
      "id": 113932,
      "status": 6,
      "reservationReferences": {
        "confirmationNumber": "23323"
      },
      "pos": {
        "id": 2122,
        "apiId": "SSC",
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
        "packageId": 1252535,
        "packageTourId": -1
      }
    },
    "customers": [
      {
        "title": "MR",
        "rph": 1,
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "02-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      },
      {
        "title": "MR",
        "rph": 2,
        "firstName": "Jack",
        "lastName": "Doe",
        "dateOfBirth": "01-Jan-1988",
        "age": 35,
        "address": {
          "city": {
            "name": "MIAMI"
          },
          "country": {
            "id": "US"
          },
          "state": {
            "id": "FL"
          }
        }
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
