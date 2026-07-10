URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000052038106/en

ID: 80395000052038106

---
# Title: HTTP Status Codes, Errors and Advisories
category: Core Concepts
endpoint: All Nitro Booking API Endpoints
tags:
  - http-status
  - errors
  - advisories
  - troubleshooting
last_updated: 2026-07
---

# HTTP Status Codes, Errors and Advisories

## Purpose

Every Nitro Booking API response should be interpreted using **three pieces of information**:

1. HTTP Status Code
2. `isSucceed`
3. `advisories`

The HTTP status indicates whether communication with the API succeeded, while `isSucceed` and `advisories` determine whether the requested business operation actually succeeded.

---

# Response Evaluation Flow

```text
Receive Response
        │
        ▼
Check HTTP Status
        │
        ├── 200 → Request reached Nitro successfully
        │        │
        │        ▼
        │    Check isSucceed
        │        │
        │        ├── true
        │        │      │
        │        │      └── Check advisories
        │        │
        │        └── false
        │               │
        │               └── Review Error advisory
        │
        └── Non-200
                 │
                 └── Infrastructure / Authentication / Permission / Server issue
```

---

# HTTP Status Codes

| Status | Meaning | Description |
|---------|----------|-------------|
|200|OK|Communication with Nitro API succeeded. Business success depends on `isSucceed`.|
|401|Unauthorized|Invalid ClientId, ClientSecret, Access Token, SiteItemId or non-whitelisted IP.|
|403|Forbidden|Client is authenticated but doesn't have permission for the endpoint.|
|404|Not Found|Endpoint does not exist.|
|429|Too Many Requests|Rate limit exceeded.|
|500|Internal Server Error|Unexpected server error.|
|503|Service Unavailable|API unavailable or under maintenance.|

---

# Understanding isSucceed

## isSucceed = true

The requested operation completed successfully.

Warnings or informative advisories may still exist.

Example

```json
"isSucceed": true
```

---

## isSucceed = false

The requested operation failed.

One or more Error advisories explain the reason.

Example

```json
"isSucceed": false
```

---

# Advisory Types

Nitro supports three advisory types.

## Error

The requested operation failed.

Typical causes

- Validation failure
- Missing mandatory field
- Invalid value
- Authentication failure
- Supplier error
- Internal error

Example

```json
{
    "code":"4000",
    "message":"Date of Birth must not be empty for 0",
    "type":"Error"
}
```

Result

- isSucceed = false
- Booking not completed

---

## Warning

Operation succeeded but additional attention is required.

Usually supplier generated.

Example

```json
{
    "code":"WRN0605",
    "message":"The Deposit Amount May Change. Please Review Final Confirmation.",
    "type":"Warning"
}
```

Result

- isSucceed = true
- Booking continues
- Display warning to user or travel agent

---

## Informative

Operation succeeded.

Additional information only.

No action required.

---

# Common Scenarios

## Missing Mandatory Field

Response

- HTTP 200
- isSucceed = false
- Error advisory

Example

```
Date of Birth must not be empty
```

Cause

Mandatory validation failure.

Resolution

Populate the missing field.

---

## Supplier Warning

Response

- HTTP 200
- isSucceed = true
- Warning advisory

Example

```
Deposit amount may change.
```

Booking continues successfully.

---

## Invalid Date Format

Example

```
Invalid Value for departureDate - to.
```

Cause

Incorrect request date format.

Resolution

Use the documented Nitro date format.

---

## Internal Server Error

Response

- HTTP 500

Example

```
Some Internal Server Error Occurred.
```

Resolution

Retry later and contact engineering if persistent.

---

## Authorization Failure

Response

- HTTP 401 Unauthorized

Possible causes

- Invalid ClientId
- Invalid ClientSecret
- Expired Access Token
- Invalid SiteItemId
- IP not whitelisted

Resolution

Generate a new token or verify API credentials.

---

# Best Practices

- Never rely on HTTP 200 alone.
- Always inspect `isSucceed`.
- Always parse the `advisories` array.
- Treat Warning advisories separately from Error advisories.
- Log advisory code and message for troubleshooting.
- Surface supplier warnings to agents whenever possible.

---

# Decision Matrix

| HTTP | isSucceed | Advisory | Meaning |
|------|-----------|----------|---------|
|200|true|None|Success|
|200|true|Warning|Success with warning|
|200|true|Informative|Success with information|
|200|false|Error|Business validation failed|
|401|-|-|Authentication failed|
|403|-|-|Permission denied|
|404|-|-|Endpoint not found|
|429|-|-|Rate limited|
|500|-|-|Server error|
|503|-|-|Service unavailable|

---

# Related Articles

- Authentication
- Generate Token
- Refresh Token
- Booking Flow
- Common Validation Errors
- Troubleshooting Guide
