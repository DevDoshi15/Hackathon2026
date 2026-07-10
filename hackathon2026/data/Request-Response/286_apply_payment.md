# Apply Payment

**Path:** Apply Payment - After Reservation is Created > Apply Payment

---

## Request Details

**Method:** `POST`

**URL:** `{{BaseUrl}}/v2/reservation/pay`

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
    "id": 66110,
    "cruiseReservation": {
        "id": 114090,
        "syncInfo": {
            "supplierSyncInfo": {
                "token": "417983",
                "lastSyncOn": "20-Feb-2023 05:29:55",
                "lastModifiedOn": "20-Feb-2023 05:44:54"
            },
            "apiSyncInfo": {
                "token": "X7sgay0T20iRYDSnVxpdSYJiRWwAVpMA",
                "sessionId": "a7346091-1a57-495d-8262-456c00569300",
                "lastSyncOn": "20-Feb-2023 05:29:59"
            }
        }
    },
    "paymentToProcess": {
        "cardToken": "f5d94630-61d8-4bf5-811d-1ca43a2882dd",
        "amount": 1053.46
    }
}
```

---

*Generated from Postman Collection: NitroAPI Sandbox*
