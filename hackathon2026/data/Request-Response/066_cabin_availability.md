# Cabin Availability

**Path:** Create Reservation > Create Reservation With Air For NCL > Cabin Availability

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
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "MIA" // flight departure city
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
        "cruise": {
            "packageId": 1330418,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "H6",
                "type": 4,
                "fare": {
                    "farecode": {
                        "code": "DISC50" // select the fare and category code, which has "airInclusive": true in the list categories respone (prices element), to select Cruise + Air
                    }
                }
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
Date: Wed, 08 Feb 2023 09:02:01 GMT
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
      "requestId": "0e2523d6-d463-4ea0-a8f1-16e5f2536339",
      "timeStamp": "08-Feb-2023 04:01:54",
      "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
      "departureArrivalInfo": {
        "departureDateTime": "07-Apr-2024 00:00:00",
        "arrivalDateTime": "28-Apr-2024 00:00:00",
        "departureCityId": "MIA",
        "arrivalCityId": "SEA",
        "duration": 21
      },
      "pos": {
        "id": 2112,
        "apiId": "NCL",
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
        "packageId": 1330418,
        "packageTourId": -1,
        "cruiseline": {
          "id": 6,
          "ships": [
            {
              "id": 14090
            }
          ]
        },
        "itinerary": {
          "id": 363268,
          "destination": {
            "id": 49
          }
        },
        "voyage": {
          "departureDateTime": "07-Apr-2024 00:00:00",
          "arrivalDateTime": "28-Apr-2024 00:00:00",
          "departureCityId": "MIA",
          "arrivalCityId": "SEA",
          "code": "19257773"
        },
        "transportationType": 29
      },
      "cabins": [
        {
          "number": "18104",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9347,
            "name": "Deck 18",
            "description": "Horizon Lounge, The Haven Courtyard, The Haven Lounge, The Haven Restaurant, Sun Deck, Aqua Racer, Laser Tag, Race Track, Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "18108",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9347,
            "name": "Deck 18",
            "description": "Horizon Lounge, The Haven Courtyard, The Haven Lounge, The Haven Restaurant, Sun Deck, Aqua Racer, Laser Tag, Race Track, Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "18116",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9347,
            "name": "Deck 18",
            "description": "Horizon Lounge, The Haven Courtyard, The Haven Lounge, The Haven Restaurant, Sun Deck, Aqua Racer, Laser Tag, Race Track, Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "18118",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9347,
            "name": "Deck 18",
            "description": "Horizon Lounge, The Haven Courtyard, The Haven Lounge, The Haven Restaurant, Sun Deck, Aqua Racer, Laser Tag, Race Track, Staterooms."
          },
          "position": "Forward",
          "location": "Port",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "18704",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9347,
            "name": "Deck 18",
            "description": "Horizon Lounge, The Haven Courtyard, The Haven Lounge, The Haven Restaurant, Sun Deck, Aqua Racer, Laser Tag, Race Track, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "18708",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9347,
            "name": "Deck 18",
            "description": "Horizon Lounge, The Haven Courtyard, The Haven Lounge, The Haven Restaurant, Sun Deck, Aqua Racer, Laser Tag, Race Track, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "18710",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9347,
            "name": "Deck 18",
            "description": "Horizon Lounge, The Haven Courtyard, The Haven Lounge, The Haven Restaurant, Sun Deck, Aqua Racer, Laser Tag, Race Track, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        },
        {
          "number": "18714",
          "beds": [
            {
              "code": "28",
              "name": "MT",
              "description": "Single Sofa ",
              "type": 254
            },
            {
              "code": "27",
              "name": "MT",
              "description": "Double Sofa ",
              "type": 217
            },
            {
              "code": "35",
              "name": "MT",
              "description": "Pullman ",
              "type": 240
            },
            {
              "code": "30",
              "name": "MT",
              "description": "King Bed ",
              "type": 226
            }
          ],
          "deck": {
            "id": 9347,
            "name": "Deck 18",
            "description": "Horizon Lounge, The Haven Courtyard, The Haven Lounge, The Haven Restaurant, Sun Deck, Aqua Racer, Laser Tag, Race Track, Staterooms."
          },
          "position": "Forward",
          "location": "Starboard",
          "occupancy": {
            "min": 0,
            "max": 6
          }
        }
      ],
      "addOns": [
        {
          "code": "AFREESC",
          "name": "OTH_Free Pre Paid Service Charges Guest 1 & 2",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG",
            "RRNCLU",
            "TPNET27",
            "TPNET35",
            "TPNET44"
          ]
        },
        {
          "code": "AFREESC2",
          "name": "OTH_Free Pre Paid Service Charges Guest 1&2",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "RRNCLU",
            "TPNET27",
            "TPNET35",
            "TPNET44"
          ]
        },
        {
          "code": "CHOALL4M",
          "name": "FAS_Ultimate Beverage, Dining Package, Internet, Shorex Credit",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "KOSHER MEAL",
            "PPSRVCHG",
            "RRNCLU",
            "SALESPPG",
            "TPNET27",
            "TPNET35",
            "TPNET44",
            "WTHPPG"
          ]
        },
        {
          "code": "CMIPPSVC",
          "name": "OTH_CMI- Free pre paid service charges 1st & 2nd guests",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "DISC50",
            "EASYFARE",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "EASYFARE",
          "name": "OTH_Early Booking Fare - Upgrades - A/S",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "CHOALL4M",
            "CMIPPSVC",
            "DISC50",
            "FLEXNET",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG",
            "RRNCLU",
            "SALESPPG",
            "WTHPPG"
          ]
        },
        {
          "code": "FLEXNET",
          "name": "OTH_NET RATES",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG"
          ]
        },
        {
          "code": "FREESRVC",
          "name": "OTH_Free Pre Paid Service Charges",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "RRNCLU",
            "TPNET27",
            "TPNET35",
            "TPNET44"
          ]
        },
        {
          "code": "FREESVC2",
          "name": "OTH_Free Pre-Paid Service Charges",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "RRNCLU",
            "TPNET27",
            "TPNET35",
            "TPNET44"
          ]
        },
        {
          "code": "FSALEPPG",
          "name": "Field Sales Pre Paid Service Charges",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "RRNCLU",
            "TPNET27",
            "TPNET35",
            "TPNET44"
          ]
        },
        {
          "code": "HSBVSXIN",
          "name": "FAS_Ultimate Beverage, Internet, Shorex Credit",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "KOSHER MEAL",
            "PPSRVCHG",
            "RRNCLU",
            "SALESPPG",
            "TPNET27",
            "TPNET35",
            "TPNET44",
            "WTHPPG"
          ]
        },
        {
          "code": "HSDISXIN",
          "name": "FAS_Specialty Dining Package, Internet, Shorex Credit",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "KOSHER MEAL",
            "PPSRVCHG",
            "RRNCLU",
            "SALESPPG",
            "TPNET27",
            "TPNET35",
            "TPNET44",
            "WTHPPG"
          ]
        },
        {
          "code": "HSINTSHO",
          "name": "FAS_Internet, Shorex Credit",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "KOSHER MEAL",
            "PPSRVCHG",
            "RRNCLU",
            "SALESPPG",
            "TPNET27",
            "TPNET35",
            "TPNET44",
            "WTHPPG"
          ]
        },
        {
          "code": "KOSHER MEAL",
          "name": "OTH_Kosher Meal",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "CHOALL4M",
            "CMIPPSVC",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "PPSRVCHG",
            "RRNCLU",
            "SALESPPG",
            "TPNET27",
            "TPNET35",
            "TPNET44",
            "WTHPPG"
          ]
        },
        {
          "code": "PPSRVCHG",
          "name": "OTH_Prepaid Service Charges",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "CHOALL4M",
            "CMIPPSVC",
            "DISC50",
            "EASYFARE",
            "FLEXNET",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "RRNCLU",
            "TPNET27",
            "TPNET35",
            "TPNET44"
          ]
        },
        {
          "code": "RRNCLU",
          "name": "OTH_Travel Agent Reduce Rate % Off Cruise Fare",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG",
            "SALESPPG",
            "WTHPPG"
          ]
        },
        {
          "code": "SALESPPG",
          "name": "Free Pre Paid Service Charges Guest 1&2",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "RRNCLU",
            "TPNET27",
            "TPNET35",
            "TPNET44"
          ]
        },
        {
          "code": "TPNET27",
          "name": "TPNET27",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "CHOALL4M",
            "DISC50",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG",
            "SALESPPG",
            "WTHPPG"
          ]
        },
        {
          "code": "TPNET35",
          "name": "TPNET35",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "CHOALL4M",
            "DISC50",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG",
            "SALESPPG",
            "WTHPPG"
          ]
        },
        {
          "code": "TPNET44",
          "name": "TPNET44",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "AFREESC",
            "AFREESC2",
            "CHOALL4M",
            "DISC50",
            "FREESRVC",
            "FREESVC2",
            "FSALEPPG",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "PPSRVCHG",
            "SALESPPG",
            "WTHPPG"
          ]
        },
        {
          "code": "WTHPPG",
          "name": "OTH_Free Pre Paid Service Charges Guest 1 & 2",
          "prices": [
            {
              "amount": 0,
              "type": "AVGPP"
            },
            {
              "amount": 0,
              "type": "TOTAL"
            }
          ],
          "combinableCodes": [
            "CHOALL4M",
            "DISC50",
            "EASYFARE",
            "HSBVSXIN",
            "HSDISXIN",
            "HSINTSHO",
            "KOSHER MEAL",
            "RRNCLU",
            "TPNET27",
            "TPNET35",
            "TPNET44"
          ]
        }
      ]
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
