# Category Availability

**Path:** Create Reservation > RCCL switching to CruiseOnly when Cruise + Air is not available > Category Availability

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
            "type": "Post",
            "GateWayCity": {
                "id": "PTY" // flight departure city. If the Air is not available then it will switch to cruise only i.e. "airInclusive": false, in the response
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
            "packageId": 1317656
        }
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
Date: Mon, 08 May 2023 15:52:50 GMT
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
    "advisories": [
        {
            "code": "WRN0605",
            "message": "THE DEPOSIT AMOUNT MAY CHANGE. PLEASE REVIEW FINAL CONFIRMATION.",
            "description": "RCCL-",
            "type": "Warning"
        }
    ],
    "data": {
        "trackingInfo": {
            "requestId": "c259ee09-5d64-4c0b-9d23-15ba24d6faab",
            "timeStamp": "08-May-2023 11:52:46",
            "token": "EQTEMPKEN"
        },
        "cruiseReservation": {
            "departureArrivalInfo": {
                "departureDateTime": "23-Jun-2023 00:00:00",
                "arrivalDateTime": "30-Jun-2023 00:00:00",
                "departureCityId": "SEA",
                "arrivalCityId": "SEA",
                "duration": 7
            },
            "pos": {
                "id": 2227,
                "apiId": "RCCL",
                "officeId": "O100US6797",
                "system": "Test",
                "currency": "USD",
                "type": "Any"
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
                "packageId": 1317656,
                "packageTourId": -1,
                "cruiseline": {
                    "id": 8,
                    "ships": [
                        {
                            "id": 13717
                        }
                    ]
                },
                "itinerary": {
                    "id": 364268,
                    "destination": {
                        "id": 1
                    }
                },
                "tourCode": "OV07A221",
                "voyage": {
                    "departureDateTime": "23-Jun-2023 00:00:00",
                    "arrivalDateTime": "30-Jun-2023 00:00:00",
                    "departureCityId": "SEA",
                    "arrivalCityId": "SEA",
                    "code": "OV07A221"
                },
                "transportationType": 29 // This sailing will be considered as Cruise Only as its not supporting Cruise + Air option
            },
            "fareCodes": [
                {
                    "code": "BESTRATE",
                    "name": "Best Rate",
                    "description": "Restrictions May Apply",
                    "type": 0,
                    "refundableType": 1,
                    "bookOnline": true,
                    "isEligible": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "Restrictions May Apply",
                        "fareTypeDescription": "Public fare - base or best rate",
                        "remarks": "Restrictions May Apply",
                        "qualifierCodes": ""
                    }
                },
                {
                    "code": "I9623245",
                    "name": "BROCHURE",
                    "description": "BROCHURE PRICE",
                    "type": 0,
                    "refundableType": 1,
                    "bookOnline": true,
                    "isEligible": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "remarks": "BROCHURE PRICE"
                    }
                },
                {
                    "code": "I9630794",
                    "name": "STANDARD",
                    "description": "STANDARD",
                    "type": 0,
                    "refundableType": 1,
                    "bookOnline": true,
                    "isEligible": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "remarks": "STANDARD"
                    }
                },
                {
                    "code": "G0738129",
                    "name": "BOGO60 NRD",
                    "description": "GS and above",
                    "type": 0,
                    "refundableType": 2,
                    "dynamicRules": [
                        {
                            "type": 10
                        }
                    ],
                    "bookOnline": true,
                    "isEligible": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "fareTypeDescription": "Discount",
                        "remarks": "GS and above",
                        "qualifierCodes": "2"
                    }
                },
                {
                    "code": "G0737880",
                    "name": "BOGO60 NRD",
                    "description": "JS Below",
                    "type": 0,
                    "refundableType": 2,
                    "dynamicRules": [
                        {
                            "type": 10
                        }
                    ],
                    "specialFare": 1,
                    "bookOnline": true,
                    "isEligible": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "fareTypeDescription": "Discount",
                        "remarks": "JS Below",
                        "qualifierCodes": "2"
                    }
                },
                {
                    "code": "I9624697",
                    "name": "CAT-TEST",
                    "description": "CAT-TEST",
                    "type": 0,
                    "refundableType": 1,
                    "isEligible": true,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "fareTypeDescription": "Discount",
                        "remarks": "CAT-TEST"
                    }
                },
                {
                    "code": "I9630801",
                    "name": "Promo Loyalty",
                    "description": "Promo Loyalty",
                    "type": 0,
                    "refundableType": 1,
                    "status": 1,
                    "details": {
                        "agencyDescription": "",
                        "fareTypeDescription": "Discount",
                        "remarks": "Promo Loyalty"
                    }
                }
            ],
            "categories": [
                {
                    "id": 332537361,
                    "code": "RL",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "RL",
                            "status": 1,
                            "fareCode": {
                                "code": "G0738129",
                                "name": "BOGO60 NRD",
                                "description": "GS and above",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "GS and above"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 10696,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false // In case Air is not available, it will be considered as CruiseOnly if airInclusive is false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1255.32,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "RL",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 15255,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1802.4,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "RL",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 15280,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1805.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "A",
                        "description": "Y"
                    }
                },
                {
                    "id": 61348,
                    "code": "OL",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "OL",
                            "status": 1,
                            "fareCode": {
                                "code": "G0738129",
                                "name": "BOGO60 NRD",
                                "description": "GS and above",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "GS and above"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 7995,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 931.2,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "OL",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 11397,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1339.44,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "OL",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 11422,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1342.44,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "A",
                        "description": "N"
                    }
                },
                {
                    "id": 332533228,
                    "code": "GL",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "GL",
                            "status": 1,
                            "fareCode": {
                                "code": "G0738129",
                                "name": "BOGO60 NRD",
                                "description": "GS and above",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "GS and above"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 7196,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 835.32,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "GL",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 10255,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1202.4,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "GL",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 10280,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1205.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "A",
                        "description": "N"
                    }
                },
                {
                    "id": 332587682,
                    "code": "SL",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "SL",
                            "status": 1,
                            "fareCode": {
                                "code": "G0738129",
                                "name": "BOGO60 NRD",
                                "description": "GS and above",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "GS and above"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6445.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 745.26,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "SL",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 9183,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1073.76,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "SL",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 9208,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 1076.76,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "B",
                        "description": "Y"
                    }
                },
                {
                    "id": 332679868,
                    "code": "OS",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "OS",
                            "status": 1,
                            "fareCode": {
                                "code": "G0738129",
                                "name": "BOGO60 NRD",
                                "description": "GS and above",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "GS and above"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 4895.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 559.26,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "OS",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6969,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 808.08,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "OS",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 6994,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 811.08,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "B",
                        "description": "N"
                    }
                },
                {
                    "id": 332672520,
                    "code": "GT",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "GT",
                            "status": 1,
                            "fareCode": {
                                "code": "G0738129",
                                "name": "BOGO60 NRD",
                                "description": "GS and above",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "GS and above"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 5695.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 655.26,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "GT",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 8112,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 945.24,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "GT",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 8137,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 948.24,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "B",
                        "description": "N"
                    }
                },
                {
                    "id": 64076,
                    "code": "GB",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "GB",
                            "status": 1,
                            "fareCode": {
                                "code": "G0738129",
                                "name": "BOGO60 NRD",
                                "description": "GS and above",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "GS and above"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 3895.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 439.26,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "GB",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 5540,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 636.6,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "GB",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 5565,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 639.6,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "B",
                        "description": "N"
                    }
                },
                {
                    "id": 332489423,
                    "code": "GS",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "GS",
                            "status": 1,
                            "fareCode": {
                                "code": "G0738129",
                                "name": "BOGO60 NRD",
                                "description": "GS and above",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "GS and above"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 3345,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false // In case cruiseline is not supporting Cruise + Air reservation it will return false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 373.2,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "GS",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 4754,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 542.28,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "GS",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 4779,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 545.28,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "B",
                        "description": "N"
                    }
                },
                {
                    "id": 64078,
                    "code": "J1",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "J1",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2088,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 222.36,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "J1",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2968,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 327.96,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "J1",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2993,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 330.96,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "C",
                        "description": "Y"
                    }
                },
                {
                    "id": 332643809,
                    "code": "J3",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "J3",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2010,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 213,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "J3",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2857,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 314.64,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "J3",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2882,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 317.64,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "C",
                        "description": "N"
                    }
                },
                {
                    "id": 64080,
                    "code": "J4",
                    "type": 4,
                    "fares": [
                        {
                            "upgradeFrom": "J4",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1971.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 208.38,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "J4",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2802,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 308.04,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "J4",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2827,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 311.04,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Deluxe",
                        "name": "C",
                        "description": "N"
                    }
                },
                {
                    "id": 332173675,
                    "code": "1C",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "1C",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1458.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 146.82,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1C",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2069,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 220.08,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1C",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 2094,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 223.08,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "Y"
                    }
                },
                {
                    "id": 332173462,
                    "code": "2C",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "2C",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1248.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 121.62,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2C",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1769,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 184.08,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2C",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1794,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 187.08,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332351847,
                    "code": "4C",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "4C",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1239,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 120.48,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "4C",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1755,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 182.4,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "4C",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1780,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 185.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 256874351,
                    "code": "CB",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "CB",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1278.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 125.22,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "CB",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1812,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 189.24,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "CB",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1837,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 192.24,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332111678,
                    "code": "1D",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "1D",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1388.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 138.42,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1D",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1969,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 208.08,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1D",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1994,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 211.08,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332130411,
                    "code": "3D",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "3D",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1379,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 137.28,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "3D",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1955,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 206.4,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "3D",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1980,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 209.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332111164,
                    "code": "2D",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "2D",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1169,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 112.08,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2D",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1655,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 170.4,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2D",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1680,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 173.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332130624,
                    "code": "4D",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "4D",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1148.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 109.62,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "4D",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1626,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 166.92,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "4D",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1651,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 169.92,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332084164,
                    "code": "1E",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "1E",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1148.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 109.62,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1E",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1626,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 166.92,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1E",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1651,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 169.92,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332084644,
                    "code": "2E",
                    "type": 3,
                    "fares": [
                        {
                            "upgradeFrom": "2E",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 989,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 90.48,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2E",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1398,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 139.56,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2E",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1423,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 142.56,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Balcony",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 256874345,
                    "code": "3M",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "3M",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1332,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 131.64,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "3M",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1888,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 198.36,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "3M",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1913,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 201.36,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Outside",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 256874349,
                    "code": "4M",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "4M",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1291.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 126.78,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "4M",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1830,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 191.4,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "4M",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1855,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 194.4,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Outside",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332051879,
                    "code": "1N",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "1N",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1220,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 118.2,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1N",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1728,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 179.16,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1N",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1753,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 182.16,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Outside",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332051880,
                    "code": "2N",
                    "type": 2,
                    "fares": [
                        {
                            "upgradeFrom": "2N",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1104.5,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 104.34,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2N",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1563,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 159.36,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2N",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1588,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 162.36,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Outside",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 256874352,
                    "code": "CI",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "CI",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1038,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 96.36,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "CI",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1468,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 147.96,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "CI",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1493,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 150.96,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Inside",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 64067,
                    "code": "1U",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "1U",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1082,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 101.64,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1U",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1531,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 155.52,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "1U",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1556,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 158.52,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Inside",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332051884,
                    "code": "3U",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "3U",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1071,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 100.32,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "3U",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1515,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 153.6,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "3U",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1540,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 156.6,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Inside",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332051882,
                    "code": "2U",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "2U",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1016,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 93.72,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2U",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1437,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 144.24,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "2U",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1462,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 147.24,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Inside",
                        "name": "G",
                        "description": "N"
                    }
                },
                {
                    "id": 332051886,
                    "code": "4U",
                    "type": 1,
                    "fares": [
                        {
                            "upgradeFrom": "4U",
                            "status": 1,
                            "fareCode": {
                                "code": "G0737880",
                                "name": "BOGO60 NRD",
                                "description": "JS Below",
                                "type": 0,
                                "refundableType": 2,
                                "dynamicRules": [
                                    {
                                        "type": 10
                                    }
                                ],
                                "specialFare": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "JS Below"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1005,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 92.4,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "4U",
                            "status": 1,
                            "fareCode": {
                                "code": "I9624697",
                                "name": "CAT-TEST",
                                "description": "CAT-TEST",
                                "type": 0,
                                "refundableType": 1,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "fareTypeDescription": "Discount",
                                    "remarks": "CAT-TEST"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1421,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 142.32,
                                    "type": "AVGPP"
                                }
                            ]
                        },
                        {
                            "upgradeFrom": "4U",
                            "status": 1,
                            "fareCode": {
                                "code": "I9630794",
                                "name": "STANDARD",
                                "description": "STANDARD",
                                "type": 0,
                                "refundableType": 1,
                                "bookOnline": true,
                                "isEligible": true,
                                "status": 1,
                                "details": {
                                    "agencyDescription": "",
                                    "remarks": "STANDARD"
                                }
                            },
                            "prices": [
                                {
                                    "id": 1,
                                    "amount": 1446,
                                    "details": {
                                        "taxInclusive": false,
                                        "nccfInclusive": true,
                                        "airInclusive": false
                                    },
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 3,
                                    "amount": 233.75,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 2,
                                    "amount": 235,
                                    "type": "AVGPP"
                                },
                                {
                                    "id": 98,
                                    "amount": 145.32,
                                    "type": "AVGPP"
                                }
                            ]
                        }
                    ],
                    "details": {
                        "guarantee": false
                    },
                    "location": {
                        "code": "Inside",
                        "name": "G",
                        "description": "N"
                    }
                }
            ]
        },
        "customers": [
            {
                "title": "MR",
                "gender": "Male",
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
                "gender": "Male",
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
