# Category Availability

**Path:** Create Reservation > Create Reservation With Air For P&O Cruise line > Category Availability

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
    "trackingInfo": {
        "token": "EQTEMPKEN"
    },
    "cruiseReservation": {
        "CruiselineAir": { //mandatory element for cruise + Air
            "type": "RoundTrip",
            "GateWayCity": {
                "id": "MAN" // flight departure city
            }
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
            "packageId": 1501519
        },
        "fareCodes": [
            {
                "code": "KD1"
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
                "country": {
                    "id": "GB"
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
                "country": {
                    "id": "GB"
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
Date: Wed, 08 Feb 2023 08:47:52 GMT
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
            "requestId": "30a02013-9d8f-4a7e-a08c-22841520be58",
            "timeStamp": "23-Jun-2026 07:32:40",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "03-Jun-2027 00:00:00",
                "arrivalDateTime": "10-Jun-2027 00:00:00",
                "departureCityId": "VLT",
                "arrivalCityId": "VLT",
                "duration": 7
            },
            "pos": {
                "id": 3487,
                "officeId": "O212GBTP17",
                "currency": "GBP",
                "type": "B2B",
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
                "currencyId": "GBP",
                "countryId": "GB"
            },
            "externalSessionInfo": {
                "externalId": "a@#$A721"
            },
            "type": "Cruise",
            "cruise": {
                "packageId": 1501519,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 16,
                    "ships": [
                        {
                            "id": 13257,
                            "code": "AZ"
                        }
                    ]
                },
                "voyage": {
                    "departureDateTime": "03-Jun-2027 00:00:00",
                    "arrivalDateTime": "10-Jun-2027 00:00:00",
                    "departureCityId": "VLT",
                    "arrivalCityId": "VLT",
                    "code": "A721"
                },
                "itinerary": {
                    "id": 433252,
                    "destination": {
                        "id": 51
                    }
                },
                "transportationType": 29
            },
            "categories": [
                {
                    "id": 60438,
                    "code": "B2",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "B2",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2909,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 336,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "SU"
                    }
                },
                {
                    "id": 60458,
                    "code": "B4",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "B4",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2859,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 330,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "SU"
                    }
                },
                {
                    "id": 56813,
                    "code": "DA",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "DA",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2359,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 270,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60407,
                    "code": "DB",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "DB",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2299,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 262.8,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60487,
                    "code": "DD",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "DD",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2169,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 247.2,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60349,
                    "code": "DE",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "DE",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2079,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 236.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60388,
                    "code": "HA",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "HA",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1829,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 206.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60355,
                    "code": "HB",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "HB",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1769,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 199.2,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60397,
                    "code": "HC",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "HC",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1699,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 190.8,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60375,
                    "code": "HD",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "HD",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1689,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 189.6,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60391,
                    "code": "HE",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "HE",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1669,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 187.2,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 3
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 60484,
                    "code": "HF",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "HF",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1629,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 182.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 2
                        }
                    },
                    "location": {
                        "code": "OB"
                    }
                },
                {
                    "id": 54047,
                    "code": "LB",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "LB",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1459,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 162,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60770,
                    "code": "LC",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "LC",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1429,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 158.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60424,
                    "code": "LE",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "LE",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1429,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 158.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 2
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60479,
                    "code": "MB",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "MB",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1399,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 154.8,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60467,
                    "code": "MC",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "MC",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1399,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 154.8,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60369,
                    "code": "MF",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "MF",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1359,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 150,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 2
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60774,
                    "code": "NB",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "NB",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1379,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 152.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60773,
                    "code": "NC",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "NC",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1339,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 147.6,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60441,
                    "code": "NF",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "NF",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1279,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 140.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 2
                        }
                    },
                    "location": {
                        "code": "OS"
                    }
                },
                {
                    "id": 60776,
                    "code": "OB",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "OB",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1389,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 153.6,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 2
                        }
                    },
                    "location": {
                        "code": "IS"
                    }
                },
                {
                    "id": 60368,
                    "code": "PA",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "PA",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1329,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 146.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "IS"
                    }
                },
                {
                    "id": 60775,
                    "code": "PB",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "PB",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1319,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 145.2,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "IS"
                    }
                },
                {
                    "id": 60389,
                    "code": "PC",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "PC",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1299,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 142.8,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "IS"
                    }
                },
                {
                    "id": 60480,
                    "code": "PD",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "PD",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1279,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 140.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "IS"
                    }
                },
                {
                    "id": 60381,
                    "code": "PE",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "PE",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1259,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 138,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "IS"
                    }
                },
                {
                    "id": 60417,
                    "code": "PF",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "PF",
                            "status": 1,
                            "fareCode": {
                                "code": "KD1",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {}
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1179,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": true  // this is Air Inclusive Indicator 
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 0,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 109,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 128.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "occupancy": {
                            "max": 4
                        }
                    },
                    "location": {
                        "code": "IS"
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
