# Cabin Availability

**Path:** Create Reservation > Create Reservation With Grats For Carnival > Cabin Availability

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/cruise/listcabins`

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
            "packageId": 1281377,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "6C",
                "fare": {
                    "fareCode": {
                        "code": "PNS"
                    }
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
Date: Fri, 17 Feb 2023 14:58:39 GMT
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
  "data": {
    "trackingInfo": {
      "requestId": "88ef97f5-3ff6-4d28-bc38-5ca00b486623",
      "timeStamp": "17-Feb-2023 09:58:32",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "01-May-2023 00:00:00",
        "arrivalDateTime": "05-May-2023 00:00:00",
        "departureCityId": "LAX",
        "arrivalCityId": "LAX",
        "duration": 4
      },
      "pos": {
        "id": 2108,
        "apiId": "Carnival",
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
        "packageId": 1281377,
        "packageTourId": -1,
        "cruiseline": {
          "id": 1,
          "ships": [
            {
              "id": 14383
            }
          ]
        },
        "itinerary": {
          "id": 303143,
          "destination": {
            "id": 55
          }
        },
        "voyage": {
          "departureDateTime": "01-May-2023 00:00:00",
          "arrivalDateTime": "05-May-2023 00:00:00",
          "departureCityId": "LAX",
          "arrivalCityId": "LAX",
          "code": "20230501RD04"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "2280",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "2283",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2284",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2285",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2286",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2288",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2309",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "2312",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "2327",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "2362",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2365",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2368",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2371",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2383",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "2394",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2397",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "2409",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW AFT STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2276",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2277",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP STARBOARD",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "2292",
          "beds": [
            {
              "code": "CT",
              "name": "CK",
              "description": "Twin King Converting ",
              "type": 268
            }
          ],
          "deck": {
            "id": 9182,
            "name": "Main",
            "description": "Staterooms."
          },
          "location": "OCEANVIEW MIDSHIP PORT",
          "occupancy": {
            "min": 0,
            "max": 2
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
