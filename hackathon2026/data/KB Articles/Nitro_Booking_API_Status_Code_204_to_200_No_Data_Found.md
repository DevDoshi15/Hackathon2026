URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000053643005/en

ID: 80395000053643005
# Nitro/Booking API: Changed Status Code from 204 to 200 in Case of No Data Found

## Overview
This article documents a behavior change in the **Nitro/Booking API**: how the API now responds when **no data is found** for a request.

---

## What's Changed?

- The Nitro/Booking API will now return **HTTP Status Code `200 OK`** along with **advisories**, **instead of `204 No Content`**, when no data is found.
- **Response body change**: Instead of a **blank response body**, the response body will now include:
  - `"isSucceed": false`
  - An **error advisory** with:
    - `"message": "No Data Found"`
    - `"code": "2004"`
    - `"type": "Error"`

---

## How It Worked Before

**Example: Cruise Itinerary lookup** — when no itinerary details are found for the given `Id`:

- **HTTP Status Code**: `204 No Content`
- **Response Body**: Blank

### Example Request (Before Behavior)
```
GET {{BaseUrl}}/v2/cruise/Itinerary/33647
```

### Example Response (Before Behavior)
- **Status**: `204 No Content`
- **Body**: Empty (no content returned)

![Before: 204 No Content with blank body](before_204_no_content.png)

---

## How It Works Now

**Example: Cruise Itinerary lookup** — when no itinerary details are found for the given `Id`:

- **HTTP Status Code**: `200 OK` (instead of `204 No Content`)
- **Response Body**: Populated with `isSucceed: false` and an error advisory

### Example Request (New Behavior)
```
GET {{NitroApiUrl}}/v2/cruise/Itinerary/123456
```

### Example Response (New Behavior)
```json
{
    "isSucceed": false,
    "advisories": [
        {
            "code": "2004",
            "message": "No Data Found",
            "type": "Error"
        }
    ]
}
```

![After: 200 OK with isSucceed false and No Data Found advisory](after_200_ok_no_data_found.png)

---

## Field Reference (New Response Body)

| Field | Description |
|---|---|
| `isSucceed` | Boolean. Now returned as `false` when no data is found for the request (previously the response body was blank with no such field). |
| `advisories` | Array of advisory objects returned when the request did not succeed / has additional info. |
| `advisories[].code` | Advisory code. `2004` = "No Data Found" for this scenario. |
| `advisories[].message` | Human-readable advisory message. `"No Data Found"` for this scenario. |
| `advisories[].type` | Advisory type/severity. `"Error"` for this scenario. |

---

## Key Takeaways

- **Do not rely on HTTP `204 No Content` anymore** to detect a "no data found" condition for endpoints affected by this change (e.g., Cruise Itinerary lookup by Id).
- Integrations/consumers must instead check for **`HTTP 200 OK`** combined with **`isSucceed: false`** and an **advisory with code `2004`** to correctly detect the "No Data Found" condition.
- This is a **breaking change** for any client-side logic that specifically checked for status code `204` to detect empty/no-data responses — that logic must be updated to check the new `isSucceed` + advisory pattern instead.
- Advisory code **`2004`** is now the standard identifier for "No Data Found" scenarios on affected endpoints.
