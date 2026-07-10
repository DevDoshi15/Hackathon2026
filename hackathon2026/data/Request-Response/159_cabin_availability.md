# Cabin Availability

**Path:** Create Reservation > Create Reservation With Packages > Auto-Inclusion of Packages > Create Reservation WITH DoNotAutoIncludePackages Preference > Cabin Availability

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
            "packageId": 1353443
        },
        "categories": [
            {
                "code": "C",
                "fare": {
                    "fareCode": {
                        "code": "QA1" // We will pass the farecode along with category to fetch the list of cabins & packages
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
Date: Fri, 03 Nov 2023 08:15:03 GMT
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
      "requestId": "507fdfb5-63d7-44f8-8a89-fd5235495ebd",
      "timeStamp": "03-Nov-2023 04:15:02",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "03-Feb-2024 00:00:00",
        "arrivalDateTime": "10-Feb-2024 00:00:00",
        "departureCityId": "FLL",
        "arrivalCityId": "FLL",
        "duration": 7
      },
      "pos": {
        "id": 2519,
        "officeId": "O100US6797",
        "currency": "USD",
        "type": "Any",
        "system": "Test",
        "apiId": "Carnival"
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
      "currencyInfo": {
        "currencyId": "USD",
        "countryId": "US"
      },
      "cruise": {
        "packageId": 1353443,
        "packageTourId": -1,
        "cruiseline": {
          "id": 5,
          "ships": [
            {
              "id": 13250
            }
          ]
        },
        "itinerary": {
          "id": 370945,
          "destination": {
            "id": 9
          }
        },
        "voyage": {
          "departureDateTime": "03-Feb-2024 00:00:00",
          "arrivalDateTime": "10-Feb-2024 00:00:00",
          "departureCityId": "FLL",
          "arrivalCityId": "FLL",
          "code": "I416"
        },
        "transportationType": 29
      },
      "categories": [
        {
          "id": 52916,
          "code": "C",
          "fares": [
            {
              "fareCode": {
                "code": "QA1",
                "type": 0
              }
            }
          ]
        }
      ],
      "cabins": [
        {
          "number": "1079",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1080",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1077",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1075",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1076",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1072",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1071",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        },
        {
          "number": "1067",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1070",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 3
          }
        },
        {
          "number": "1066",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1065",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1061",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1062",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1060",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1057",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1047",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1050",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Port Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "1045",
          "smokingInfo": {
            "allowed": false,
            "description": "No Preference"
          },
          "beds": [
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            },
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            }
          ],
          "bathOptions": [
            {
              "code": "TS",
              "name": "Tub With Shower"
            }
          ],
          "deck": {
            "id": 5149,
            "name": "Main Deck",
            "description": "The Mainstage, Future Cruises, Atrium, Shore Excursions, Front Office. Staterooms."
          },
          "location": "Midship Starboard Oceanview",
          "occupancy": {
            "min": 0,
            "max": 4
          }
        },
        {
          "number": "GUAR",
          "isGuarantee": true,
          "beds": [
            {
              "code": "T2",
              "description": "Twin Beds ",
              "type": 261,
              "count": 1
            },
            {
              "code": "QN",
              "description": "Queen Bed ",
              "type": 243,
              "count": 1
            }
          ],
          "location": "Oceanview",
          "occupancy": {
            "min": 0,
            "max": 2
          }
        }
      ]
    },
    "customers": [
      {
        "gender": "Male",
        "rph": 1,
        "age": 52,
        "address": {
          "country": {
            "id": "US"
          }
        }
      },
      {
        "gender": "Male",
        "rph": 2,
        "age": 57
      }
    ]
  }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
