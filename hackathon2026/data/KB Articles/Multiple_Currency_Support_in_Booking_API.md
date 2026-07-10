URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000048672115/en

ID: 80395000048672115
# Multiple Currency Support in Booking API

## Overview
This article explains how to request multiple currencies via the Booking API, how Point of Sale (POS) determines currency behavior, and important caveats around currency handling, exchange rates, and cruise line support.

---

## 1. POS Auto-Attachment

- If POS is **not sent** in the request, POS information is **automatically attached** from the affiliate / parent site setup.
- If the site is configured with **multiple POS support** and no POS is specified in the request, the system will **pick the first option available based on priority**.
- POS setup/configuration:
  - **Production**: Done in Admin under **OfficeID / API Setup**. Only accessible by the client in production.
  - **Sandbox**: Not self-service. Client must **create a support ticket** to request access/setup.

---

## 2. Specifying POS in the Request

There are two accepted ways to specify POS in a request:

### Option A — POS by `id`
```json
{
  "cruiseReservation": {
    "cruise": {
      "packageId": 1269434
    },
    "pos": {
      "id": 2255
    }
  }
}
```
- The `id` value (e.g., `2255`) is **different per client**.
- It can be looked up via the **`listpos`** message.

### Option B — POS by `officeId` + `currency`
```json
{
  "cruiseReservation": {
    "cruise": {
      "packageId": 1269434
    },
    "pos": {
      "officeId": "O*******P17",
      "currency": "CAD"
    }
  }
}
```
- `officeId` = **Odysseus ProfileID**.
- `officeId` is unique per client, **but a client may have multiple ProfileIDs** set up.
- `currency` specifies the desired currency (e.g., `CAD`).

---

## 3. Reviewing the Response

- **Always review the currency returned in the response** — it may not match what was requested (see rules below).
- Some price elements — for example, **Onboard Credits** — may still be returned in a **different currency** than the rest of the response. This must be accounted for. This behavior occurs specifically in the **price message**.

---

## 4. Exchange Rate Behavior

- Even if exchange rates are **set up and enabled**, the **API ignores exchange rates**.
  - Prices via the API are **always returned without exchange rates applied**, in the **source currency**.
- This differs from the **Odysseus UI**, which **does apply exchange rates**.
  - **Example**: If a site is set up as CAD and the client requests a Disney Cruise:
    - **Odysseus UI**: Prices display in **CAD** (sourced in USD, then exchange rate applied). If no exchange rate is set up, UI will show **USD**.
    - **API**: Prices are returned in **USD** (source currency), regardless of UI display.

---

## 5. Changing POS / Currency Before Fare Code Availability

- POS can be changed **before Fare Code Availability**.
- POS can drive both **currency** and, depending on client setup, the **agency**.
- For cruise lines that support **multiple currencies for the same OfficeID / ProfileID / PCC**:
  - A different currency can be requested.
  - **Each currency requires its own unique request.**
  - All respective information must be **maintained consistently throughout the entire booking flow** for that currency/request.

---

## 6. Default POS Selection (No POS Sent)

- If POS is not sent, the system automatically selects the **first POS configured** for the site.
- For most clients, this may be the **only POS configured**.

---

## 7. Invalid/Incorrect POS Handling

- If **incorrect POS information** is sent:
  - The system does **not validate or block** the request.
  - The system **automatically falls back** to the **first available correct and valid POS setup** for that site.
  - The response will reflect **whichever POS was actually used** (not necessarily what was sent).

---

## 8. Currency Mismatches in the Booking Flow

- If a client requests a currency (e.g., **CAD**) that:
  - The **cruise line does not support**, or
  - The client's **agency is set up as USD** (mismatch with requested currency),
- Then the **cruise line may respond in one of two ways**:
  1. Return an **error**, or
  2. Return prices in **USD** instead of the requested currency.

---

## Key Takeaways / Rules Summary Table

| Scenario | Behavior |
|---|---|
| No POS sent, single POS configured | Auto-attached from site/affiliate setup |
| No POS sent, multiple POS configured | First POS by priority is used |
| POS sent via `id` | Client-specific; look up via `listpos` |
| POS sent via `officeId` + `currency` | `officeId` = Odysseus ProfileID (client may have several) |
| Incorrect/invalid POS sent | Not validated/blocked; falls back to first valid POS for site |
| Exchange rates enabled | Ignored by API; prices always in source currency |
| Odysseus UI vs API currency | UI applies exchange rates; API does not |
| Onboard Credits pricing | May be returned in a different currency than the rest of the price message |
| Requesting unsupported currency | Cruise line may return an error OR return USD prices |
| Changing currency mid-flow | Must be done before Fare Code Availability; each currency = separate unique request maintained throughout flow |
| Sandbox POS setup | Requires a support ticket (not self-service like production) |
