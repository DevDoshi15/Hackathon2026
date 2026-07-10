# Category Availability

**Path:** Create Reservation > Create Reservation With Air For NCL > Category Availability

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
            "packageId": 1330418
        },
        "fareCodes": [
            {
                "code": "DISC50"
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
            "requestId": "3dc98800-91f9-4871-8849-993192b362ce",
            "timeStamp": "08-Feb-2023 03:47:44",
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
            "categories": [
                {
                    "code": "H2",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "H2",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 24187,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": true
                    }
                },
                {
                    "code": "H5",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "H5",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 15110,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "H6",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "H6",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 14787,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true // indicates these are prices inclulde air fare
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "HB",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "HB",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 14619,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "HC",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "HC",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 14494,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "HE",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "HE",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 13264,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "HF",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "HF",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 13025,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "HG",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "HG",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 12464,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "H9",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "H9",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 12464,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "M9",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "M9",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 7665,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "M4",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "M4",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6674,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "M6",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "M6",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6907,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "MA",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "MA",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6715,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "MB",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "MB",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6690,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "MC",
                    "type": 4,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "MC",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6682,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "B9",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "B9",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6782,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "B1",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "B1",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 7190,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "B4",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "B4",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6299,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "B6",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "B6",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6757,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "BA",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "BA",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6290,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "BB",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "BB",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6274,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "BF",
                    "type": 3,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "BF",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6257,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "OA",
                    "type": 2,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "OA",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 5587,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "OB",
                    "type": 2,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "OB",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 5464,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "I4",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "I4",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 4894,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "IA",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "IA",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 4887,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "IB",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "IB",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 4879,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "IC",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "IC",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 4864,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
                        }
                    ],
                    "details": {
                        "guarantee": false
                    }
                },
                {
                    "code": "IF",
                    "type": 1,
                    "fares": [
                        {
                            "status": 1,
                            "upgradeFrom": "IF",
                            "fareCode": {
                                "code": "DISC50",
                                "type": 0,
                                "refundableType": 1
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 4848,
                                    "type": "AVGPP",
                                    "details": {
                                        "airInclusive": true
                                    }
                                },
                                {
                                    "id": 3,
                                    "amount": 626.37,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 650,
                                    "type": "AVGPP"
                                }
                            ],
                            "addOns": []
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
