# Category Availability

**Path:** Create Reservation > Occupancy Based Samples > Occupancy For 3 (2 Adults + 1 Child) Kids Special Package (RCCL) > Category Availability

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
// This request contains only mandatory elements
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1269434
        },
        "fareCodes": [
            {
                "code": "I9610792"
            }
        ]
    },
    "customers": [
        {
            "rph": 1,
            "age": 31,
            "address": {
                "country": {
                    "id": "US"
                }
            }
        },
        {
            "rph": 2,
            "age": 30
        },
        {
            "rph": 3,
            "age": 10
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
Date: Mon, 27 Mar 2023 11:08:30 GMT
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
 // e.g. The average price per passenger (AVGPP) will be calculated by dividing the sum of the adult prices by 3.
{
    "isSucceed": true,    
    "data": {
        "trackingInfo": {
            "requestId": "7220a028-888e-450b-9e97-2f69fa2ee48b",
            "timeStamp": "27-Mar-2023 07:08:29",
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
                "id": 2227,
                "apiId": "RCCL",
                "officeId": "O100US6797",
                "system": "Test",
                "currency": "USD",
                "type": "B2B"
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
                },
                {
                    "rph": 3,
                    "ageGroup": "Child"
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
                    "code": "VP",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "VP",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 1339
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 150
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 652.6666666666666,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 69.52,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "J3",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "J3",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 1201
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 150
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 546,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 56.72,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "J4",
                    "type": 4,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "J4",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 927,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 499,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 499,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "1B",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "1B",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 1061
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 75
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 492.6666666666667,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 50.32,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "3B",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "3B",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 1045
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 75
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 478.6666666666667,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 48.64,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "2B",
                    "type": 3,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "2B",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 769.6666666666666,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "4B",
                    "type": 3,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "4B",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 760.3333333333334,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "CB",
                    "type": 3,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "CB",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 751,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "1D",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "1D",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 993
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 75
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 438.6666666666667,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 43.84,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "5D",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "5D",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 959
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 75
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 412,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 40.64,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "2D",
                    "type": 3,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "2D",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 703,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "4D",
                    "type": 3,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "4D",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 693.6666666666666,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 427,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "1K",
                    "type": 2,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "1K",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 1043
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 546,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 56.72,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "1L",
                    "type": 2,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "1L",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 881
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 419.3333333333333,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 41.52,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "3M",
                    "type": 2,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "3M",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 855
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 399.3333333333333,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 39.12,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "4M",
                    "type": 2,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "4M",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 646.3333333333334,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 341,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 341,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "1N",
                    "type": 2,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "1N",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 803
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 359.3333333333333,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 34.32,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "3N",
                    "type": 2,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "3N",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 779
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 338.6666666666667,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 31.84,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "2N",
                    "type": 2,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "2N",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 569.6666666666666,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 341,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 341,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "4N",
                    "type": 2,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "4N",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 560.3333333333334,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 341,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 341,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "1Q",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "1Q",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 842
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 432,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 43.04,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "1R",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "1R",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 806
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 406,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 39.92,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "CP",
                    "type": 1,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "CP",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 541.3333333333334,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 284,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 284,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "2T",
                    "type": 1,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "2T",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 512.6666666666666,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 284,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 284,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "1V",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "1V",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 712
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 332.6666666666667,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 31.12,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "3V",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "3V",
                            "fareCode": {
                                "code": "I9610792",
                                "name": "Kids Sail Free",
                                "type": 0,
                                "refundableType": 1,
                                "status": 1,
                                "details": {},
                                "supplierRules": [
                                    {
                                        "description": "Kids Sail Free",
                                        "discountType": 2,
                                        "amount": 670
                                    },
                                    {
                                        "description": "Kids Sail Free",
                                        "currency": "USD",
                                        "type": 1,
                                        "discountType": 2,
                                        "amount": 50
                                    }
                                ]
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 298.6666666666667,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 27.04,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "2V",
                    "type": 1,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "2V",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 494,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 284,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 284,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "4V",
                    "type": 1,
                    "fares": [
                        {
                            "status": 2,
                            "upgradeFrom": "4V",
                            "fareCode": {
                                "code": "I0507023",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "status": 2,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 484,
                                    "type": "AVGPP",
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 113.25,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 110,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 1,
                                    "amount": 284,
                                    "type": "ADDADT"
                                },
                                {
                                    "id": 1,
                                    "amount": 284,
                                    "type": "ADDCHD"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                }
            ]
        },
        "customers": [
            {
                "rph": 1,
                "age": 31,
                "address": {
                    "country": {
                        "id": "US"
                    }
                }
            },
            {
                "rph": 2,
                "age": 30
            },
            {
                "rph": 3,
                "age": 10
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
