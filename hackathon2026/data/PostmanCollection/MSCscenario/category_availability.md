# Category Availability

**Path:** Create Reservation > Create Reservation For MSC > Category Availability

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
//This request contains only mandatory elements
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
            "packageId": 1324816
        }
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
Date: Fri, 17 Feb 2023 09:23:53 GMT
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
            "requestId": "e8be7d3c-ab1f-421c-8730-1f4f460ae418",
            "timeStamp": "17-Feb-2023 04:23:49",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "01-Apr-2023 00:00:00",
                "arrivalDateTime": "08-Apr-2023 00:00:00",
                "departureCityId": "MRS",
                "arrivalCityId": "MRS",
                "duration": 7
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
                "packageId": 1324816,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 982,
                    "ships": [
                        {
                            "id": 14091
                        }
                    ]
                },
                "itinerary": {
                    "id": 362627,
                    "destination": {
                        "id": 18
                    }
                },
                "voyage": {
                    "departureDateTime": "01-Apr-2023 00:00:00",
                    "arrivalDateTime": "08-Apr-2023 00:00:00",
                    "departureCityId": "MRS",
                    "arrivalCityId": "MRS",
                    "code": "GR20230401MRSMRS"
                },
                "transportationType": 29
            },
            "fareCodes": [
                {
                    "code": "EZAT35DZE",
                    "name": "ESCAPE TO SEA CRUISE ONLY",
                    "bookOnline": true,
                    "type": 0,
                    "refundableType": 1,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "fareTypeDescription": "EZAT"
                    },
                    "groups": [
                        {}
                    ]
                },
                {
                    "code": "GRUS306R3",
                    "name": "BROCHURE RATES",
                    "bookOnline": true,
                    "type": 0,
                    "refundableType": 1,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "fareTypeDescription": "EZBR"
                    },
                    "groups": [
                        {}
                    ],
                    "dynamicRules": [
                        {
                            "type": 24
                        },
                        {
                            "type": 25
                        }
                    ]
                }
            ],
            "categories": [
                {
                    "code": "IR1",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "IR1",
                            "fareCode": {
                                "code": "EZAT35DZE",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 718,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "636713197",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true, // wherever "autoInclude" is received, needs to be sent back in the subsequent requests of PriceBooking and CreateBooking.
                                    "additionalCode": "636713325",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "636713572",
                                    "combinableCodes": []
                                }
                            ]
                        },
                        {
                            "status": 1,
                            "upgradeFrom": "IR1",
                            "fareCode": {
                                "code": "GRUS306R3",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1699,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "183426727",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "183426728",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "183426779",
                                    "combinableCodes": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "code": "IR2",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "IR2",
                            "fareCode": {
                                "code": "EZAT35DZE",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 748,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "636713206",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "636713337",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "636713589",
                                    "combinableCodes": []
                                }
                            ]
                        },
                        {
                            "status": 1,
                            "upgradeFrom": "IR2",
                            "fareCode": {
                                "code": "GRUS306R3",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1759,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "183426729",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "183426730",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "183426780",
                                    "combinableCodes": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "code": "OM2",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "OM2",
                            "fareCode": {
                                "code": "EZAT35DZE",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 888,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "636713248",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "636713359",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "636713618",
                                    "combinableCodes": []
                                }
                            ]
                        },
                        {
                            "status": 1,
                            "upgradeFrom": "OM2",
                            "fareCode": {
                                "code": "GRUS306R3",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2039,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "183426735",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "183426736",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "183426783",
                                    "combinableCodes": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "code": "BP",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "BP",
                            "fareCode": {
                                "code": "EZAT35DZE",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1048,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "636713151",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "636713448",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "636713641",
                                    "combinableCodes": []
                                }
                            ]
                        },
                        {
                            "status": 1,
                            "upgradeFrom": "BP",
                            "fareCode": {
                                "code": "GRUS306R3",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2359,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "183426745",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "183426746",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "183426774",
                                    "combinableCodes": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "code": "BR1",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "BR1",
                            "fareCode": {
                                "code": "EZAT35DZE",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1108,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "636713156",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "636713405",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "636713711",
                                    "combinableCodes": []
                                }
                            ]
                        },
                        {
                            "status": 1,
                            "upgradeFrom": "BR1",
                            "fareCode": {
                                "code": "GRUS306R3",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2479,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "183426747",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "183426748",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "183426775",
                                    "combinableCodes": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "code": "BR2",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "BR2",
                            "fareCode": {
                                "code": "EZAT35DZE",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1158,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "636713166",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "636713419",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "636713726",
                                    "combinableCodes": []
                                }
                            ]
                        },
                        {
                            "status": 1,
                            "upgradeFrom": "BR2",
                            "fareCode": {
                                "code": "GRUS306R3",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2579,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "183426749",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "183426750",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "183426776",
                                    "combinableCodes": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "code": "BR3",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "BR3",
                            "fareCode": {
                                "code": "EZAT35DZE",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1188,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "636713181",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "636713431",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "636713743",
                                    "combinableCodes": []
                                }
                            ]
                        },
                        {
                            "status": 1,
                            "upgradeFrom": "BR3",
                            "fareCode": {
                                "code": "GRUS306R3",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2639,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "EXP2B",
                                    "name": "Fantastica Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "183426751",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "183426752",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "183426777",
                                    "combinableCodes": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "code": "BA",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "BA",
                            "fareCode": {
                                "code": "EZAT35DZE",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1348,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "SPABAEXP",
                                    "name": "Balinese Massage 50 Minute",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 108,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 216,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 30,
                                    "additionalCode": "636713031",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "636713085",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "EXP3B",
                                    "name": "Aurea Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "636713459",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "636713755",
                                    "combinableCodes": []
                                }
                            ]
                        },
                        {
                            "status": 1,
                            "upgradeFrom": "BA",
                            "fareCode": {
                                "code": "GRUS306R3",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2959,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 65.1,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 159,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": [
                                {
                                    "code": "EXP3B",
                                    "name": "Aurea Experience Benefits",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 23,
                                    "autoInclude": true,
                                    "additionalCode": "183426753",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "600",
                                    "name": "MINERAL WATER AND COFFEE IN DINING ROOM",
                                    "description": "",
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
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 6,
                                    "autoInclude": true,
                                    "additionalCode": "183426754",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "SPABAEXP",
                                    "name": "Balinese Massage 50 Minute",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 108,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 216,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 30,
                                    "additionalCode": "183426769",
                                    "combinableCodes": []
                                },
                                {
                                    "code": "TRIOPR",
                                    "name": "Trilogy - Three Exclusive Dining Experiences",
                                    "description": "",
                                    "prices": [
                                        {
                                            "amount": 100,
                                            "type": "AVGPP"
                                        },
                                        {
                                            "amount": 200,
                                            "type": "TOTAL"
                                        }
                                    ],
                                    "startDate": "01-Apr-2023",
                                    "endDate": "01-Apr-2023",
                                    "type": 16,
                                    "additionalCode": "183426773",
                                    "combinableCodes": []
                                }
                            ]
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
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
