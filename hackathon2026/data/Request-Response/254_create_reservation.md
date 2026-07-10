# Create Reservation

**Path:** Create Reservation > Create Reservation - Payment Declined Flag > Create Reservation

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
// When the reservation is created successfully with the cruise line, but the payment fails,
// then a flag "PaymentDeclined" will be received in the response under "flags" element, along with optional advisory(ies)
{
    "cruiseReservation": {
        "cruise": {
            "packageId": 1313282,
            "packageTourId": -1
        },
        "categories": [
            {
                "code": "H1",
                "fare": {
                    "fareCode": {
                        "code": "DISC35"
                    }
                },
                "cabins": [
                    {
                        "number": "14500"
                    }
                ]
            }
        ],
        "dinings": [
            {
                "id": 4,
                "code": "FREEST",
                "name": "Freestyle",
                "status": 1
            }
        ]
    },
    "paymentToProcess": {
        "cardToken": "dfcc86da-f268-438c-8302-a5f9d57d92cf", // We are using the same token generated in tokenized card
        "amount": 34315.04,
        "currency": "USD"
    },
    "customers": [
        {
            "rph": 1,
            "firstName": "John",
            "lastName": "Doe",
            "dateOfBirth": "02-Jan-1970",
            "age": 53,
            "address": {
                "country": {
                    "id": "US"
                },
                "state": {
                    "id": "IL"
                },
                "city": {
                    "name": "Chicago"
                }
            },
            "ContactInfo": {
                "Email": "john@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "416-555-4566"
                }
            }
        },
        {
            "rph": 2,
            "firstName": "Maria",
            "lastName": "Doe",
            "dateOfBirth": "01-Jan-1965",
            "age": 58,
            "address": {
                "country": {
                    "id": "US"
                }
            },
            "ContactInfo": {
                "Email": "maria@domain.com",
                "Phone1": {
                    "CountryCode": "1",
                    "Number": "416-555-4566"
                }
            }
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
Date: Wed, 06 Sep 2023 10:03:32 GMT
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
    "advisories": [
        {
            "code": "",
            "message": "Lbl_BkgEml_CruiseOptionPaymentFailed",
            "description": "NCL",
            "type": "Warning"
        },
        {
            "description": "NCL Consumer Advice: ****A valid Passport is strongly recommended for all guests for any itinerary where there is a stop in a foreign port.  In addition to a passport, a visa maybe required.  Visa requirements vary by country and are subject to change.  For the appropriate requirements based on itinerary and nationality, please visit www.ncl.com and click on traveldocs or contact \nyour local immigration office.  ****It is the guest's responsibility to obtain required visas and other documentation prior to sailing, including vaccinations for infectious diseases. ****Guest without proper documentation maybe denied boarding. ****Terms and conditions are in the Norwegian Cruise Line brochure and are also available at www.ncl.com",
            "type": "Information"
        }
    ],
    "data": {
        "trackingInfo": {
            "requestId": "eb7df3e6-5db4-4c0b-9948-17f3e2e8c1db",
            "timeStamp": "06-Sep-2023 06:03:14",
            "token": "EQTEMPKEN"
        },
        "id": 80707,
        "agencyConfirmation": "IOWVCCV",
        "cruiseReservation": {
            "id": 128603,
            "status": 6,
            "reservationReferences": {
                "confirmationNumber": "70000052"
            },
            "pos": {
                "id": 2520,
                "officeId": "O100US6797",
                "currency": "USD",
                "type": "B2B",
                "system": "Test",
                "apiId": "NCL"
            },
            "customerReferences": [
                {
                    "rph": 1,
                    "ageGroup": "Adult",
                    "odyCustomerRef": 65991,
                    "isPrimaryContact": true
                },
                {
                    "rph": 2,
                    "ageGroup": "Adult",
                    "odyCustomerRef": 64840
                }
            ],
            "currencyInfo": {
                "currencyId": "USD"
            },
            "flags": [ // Here we get booking flags
                {
                    "type": "PaymentDeclined",
                    "status": "Active"
                }
            ],
            "cruise": {
                "packageId": 1313282,
                "packageTourId": -1
            },
            "rulesInfo": {
                "applicableRules": [
                    {
                        "id": 1728342,
                        "name": "Cruise Discount (5$)",
                        "groupName": "excl_1728342",
                        "type": 1,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728343,
                        "name": "Cruise Markup (25$)",
                        "groupName": "excl_1728343",
                        "type": 2,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728420,
                        "name": "VAO Exclusive",
                        "groupName": "excl_1728420",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "va_earlysaver.png"
                        }
                    },
                    {
                        "id": 1728421,
                        "name": "VAO One Exclusive",
                        "groupName": "excl_1728421",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "pink-circle.png"
                        }
                    },
                    {
                        "id": 1728422,
                        "name": "VAO Non Exclusive",
                        "groupName": "nonexcl",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "CruiseCategory",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "va_anchor-vODY-635382737153437500.png"
                        }
                    },
                    {
                        "id": 1728423,
                        "name": "VAO Two Non Exclusive",
                        "groupName": "nonexcl",
                        "type": 3,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "CruiseCategory",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": "va_sale.png"
                        }
                    },
                    {
                        "id": 1728419,
                        "name": "Cruise Addon",
                        "groupName": "excl_1728419",
                        "type": 9,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728344,
                        "name": "Cruise Service Fee (20$)",
                        "groupName": "excl_1728344",
                        "type": 13,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "",
                            "agencyDetails": "",
                            "redemptionDetails": "",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728415,
                        "name": "Package Service Doc (10)",
                        "groupName": "P1",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728416,
                        "name": "Package Service Doc One (15)",
                        "groupName": "P1",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728417,
                        "name": "Package Service Travel (25) BEST Value YES",
                        "groupName": "P2",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    },
                    {
                        "id": 1728418,
                        "name": "Package Service Travel (20) BEST Value NO",
                        "groupName": "P2",
                        "type": 18,
                        "externalGroupId": "",
                        "externalId": "",
                        "details": {
                            "displayToCustomer": true,
                            "displayStep": "All",
                            "customerDetails": "<strong>Customer Details</strong> added here",
                            "agencyDetails": "Agency Details Added Here",
                            "redemptionDetails": "Redemption details goes here",
                            "customLink": "",
                            "imageUrl": ""
                        }
                    }
                ]
            },
            "categories": [
                {
                    "id": 60316,
                    "code": "H1",
                    "fares": [
                        {
                            "fareCode": {
                                "code": "DISC35",
                                "type": 0
                            }
                        }
                    ]
                }
            ]
        },
        "customers": [
            {
                "gender": "Male",
                "rph": 1,
                "firstName": "John",
                "lastName": "Doe",
                "dateOfBirth": "02-Jan-1970",
                "age": 53,
                "address": {
                    "city": {
                        "name": "Chicago"
                    },
                    "country": {
                        "id": "US"
                    },
                    "state": {
                        "id": "IL"
                    }
                },
                "contactInfo": {
                    "email": "john@domain.com",
                    "phone1": {
                        "countryCode": "1",
                        "number": "416-555-4566"
                    }
                }
            },
            {
                "gender": "Male",
                "rph": 2,
                "firstName": "Maria",
                "lastName": "Doe",
                "dateOfBirth": "01-Jan-1965",
                "age": 58,
                "address": {
                    "country": {
                        "id": "US"
                    }
                },
                "contactInfo": {
                    "email": "maria@domain.com",
                    "phone1": {
                        "countryCode": "1",
                        "number": "416-555-4566"
                    }
                }
            }
        ]
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
