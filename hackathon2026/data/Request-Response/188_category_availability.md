# Category Availability

**Path:** Create Reservation > Group Reservation > Royal Carribean Cruiseline > Category Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listCategories`

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
        "cruise": {
            "packageId": 1269434
        },
        "fareCodes": [
            {
                "code": "I1071484_GRP",
                "groups": [ // group code to be used for fetching the categories
                    {
                        "code": "1179594"
                    }
                ]
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 52,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 57
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
Date: Tue, 14 Mar 2023 09:39:17 GMT
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
  "data": {
    "trackingInfo": {
      "requestId": "87f0ba17-75d0-4779-b913-fb500ecb3928",
      "timeStamp": "14-Mar-2023 05:39:15",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "24-Apr-2023 00:00:00",
        "arrivalDateTime": "28-Apr-2023 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "MIA",
        "duration": 4
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
        "packageId": 1269434,
        "packageTourId": -1,
        "cruiseline": {
          "id": 8,
          "ships": [
            {
              "id": 116
            }
          ]
        },
        "itinerary": {
          "id": 364180,
          "destination": {
            "id": 7
          }
        },
        "tourCode": "FR4BH098",
        "voyage": {
          "departureDateTime": "24-Apr-2023 00:00:00",
          "arrivalDateTime": "28-Apr-2023 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "MIA",
          "code": "FR4BH098"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "code": "2B",
          "type": 3,
          "externalSessionInfo": {
            "externalId": "1"
          },
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2B",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 539,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 51.48,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 10,
            "guarantee": false
          }
        },
        {
          "code": "2D",
          "type": 3,
          "externalSessionInfo": {
            "externalId": "2"
          },
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2D",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 479,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 44.28,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 10,
            "guarantee": false
          }
        },
        {
          "code": "2N",
          "type": 2,
          "externalSessionInfo": {
            "externalId": "3"
          },
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2N",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 389,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 33.48,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 10,
            "guarantee": false
          }
        },
        {
          "code": "2T",
          "type": 1,
          "externalSessionInfo": {
            "externalId": "4"
          },
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2T",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 359,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 29.88,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 5,
            "guarantee": false
          }
        },
        {
          "code": "2V",
          "type": 1,
          "externalSessionInfo": {
            "externalId": "5"
          },
          "fares": [
            {
              "status": 1,
              "upgradeFrom": "2V",
              "fareCode": {
                "code": "I1071484_GRP",
                "type": 0,
                "refundableType": 1
              },
              "prices": [
                {
                  "id": 1,
                  "amount": 349,
                  "type": "AVGPP",
                  "details": {
                    "taxInclusive": false,
                    "nccfInclusive": true,
                    "airInclusive": false
                  }
                },
                {
                  "id": 3,
                  "amount": 115,
                  "type": "AVGPP"
                },
                {
                  "id": 2,
                  "amount": 110,
                  "type": "AVGPP"
                },
                {
                  "id": 98,
                  "amount": 28.68,
                  "type": "AVGPP"
                }
              ]
            }
          ],
          "details": {
            "cabinCount": 5,
            "guarantee": false
          }
        }
      ]
    },
    "customers": [
      {
        "rph": 1,
        "age": 52,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
