URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000040396116/en

ID: 80395000040396116
# Nitro Booking API: Payment Options

## Overview

Clients integrating with the NITRO Booking API must account for three distinct payment options, each with different PCI compliance implications and processing flows. The option a client falls under depends on how the customer's credit card is handled: passed through to the cruise line, processed directly by the agency, or routed through a supplier-hosted payment gateway.

---

## Option 1: Customer Credit Card Is Passed to the Cruise Line

### PCI Compliance
- Clients using this option will most likely fall under **PCI compliance**.
- Recommendation: all transactions must be processed over **SSL with the latest encryption**, following current PCI requirements.
- Once card info is passed via the API, **do not store it** on the client's end.
- If details must be retained for logging purposes, they must be **masked**, e.g.: `41*********1111`.

### Process Flow (2 steps)
1. **TokenizeCard**
   - The agency sends card information along with the billing address.
   - The API returns a **token** in response.
2. **Create Booking**
   - The token is sent along with the amount to be charged and any other options supported by the API.

### Post-Booking Payments
- For payments made **after** a booking is created, the same tokenize-then-charge process applies:
  - First tokenize the card info.
  - Then send that token in the payment message.
  - **Status:** This message was scheduled to be available by **Jan 15, 2023**.

---

## Option 2: Customer Credit Card Is Processed by the Agency

- The customer's payment is simply **recorded** in Odysseus.
- Can optionally trigger a **"confirm" message** for cruise lines that support it.
  - **Status (at time of writing):** the confirm message was yet to be scoped, targeted for availability in **Q1 2023**.
- **PCI implications:**
  - If the agency uses a **hosted payment gateway solution**, they are likely **out of scope of PCI**.
  - If the agency is **not** using a hosted solution, the agency is **responsible for its own PCI compliance**.

---

## Option 3: Supplier-Hosted Payment Gateways

- Applies to specific suppliers that operate their own payment gateways, e.g. **Virgin Voyages**, **Explora Journeys**.
- Clients using **Option 1** with these suppliers will need to add support for this separately.
  - **Status:** planned for **Q1 2023** release.
- This capability requires development on the Odysseus side and was, at time of writing, **still being scoped**.

### Interim Recommendation
- Until the Odysseus-side solution is available: **disable online payments for these suppliers** and process those payments **manually**.

### Planned Solution Design
- Odysseus plans to create a **hosted page** that:
  1. The client calls.
  2. Redirects from Odysseus servers to the **cruise line's hosted page** to complete the transaction.
  3. Sends the client an update once complete.
- **Implication:** the user must be **redirected away** from the client's own screen for these hosted pages.
  - **iFrame embedding is not an option** for this flow.
- **Reason:** certain messages/checks are performed in the background by Odysseus, so clients must follow the Odysseus-hosted process for these specific cruise lines.

---

## Cross-Cutting Recommendation: Booking-Before-Payment Sequencing

- For **any** payment option used in the initial create-booking flow, it is recommended to:
  1. **Create the booking first.**
  2. **Attempt payment after.**
- The create-booking call can run as a background process to confirm the booking is created successfully (no errors) before payment is attempted.
- **This sequencing is mandatory for Option 3** (supplier-hosted payment gateways) — booking must be created before payment is attempted.

---

## Quick Reference

| Option | Card Handled By | PCI Scope | Status Notes |
|---|---|---|---|
| 1 | Passed to cruise line via API (tokenized) | Client likely in PCI scope | Post-booking payment message targeted for Jan 15, 2023 |
| 2 | Processed by agency, recorded in Odysseus | Out of PCI scope if using hosted gateway; in scope if not | Confirm message targeted for Q1 2023 |
| 3 | Supplier-hosted gateway (e.g. Virgin Voyages, Explora Journeys) | Handled via Odysseus-hosted redirect flow | Targeted for Q1 2023; interim recommendation is manual processing; booking-before-payment is mandatory |
