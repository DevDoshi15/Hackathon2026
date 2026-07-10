URL:https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page#Solutions/dv/80395000054876005/en

ID: 80395000054876005
# Domain Tables: Rule Types (Odysseus Rule Engine)

## Overview
This is the domain/enum reference table for **Rule Types** in the **Odysseus Rule Engine**. Each value represents a distinct type of business rule the engine can apply (pricing adjustments, fees, commissions, display behavior, promotions, etc.).

---

## Value Reference Table

| Value | Name | Description |
|---|---|---|
| `0` | `Undefined` | Undefined — **Not Supported**. |
| `1` | `Discount` | Discount. |
| `2` | `Markup` | Markup. |
| `3` | `ValueAddOffer` | Value Added Offer. |
| `4` | `InsuranceIncluded` | Insurance Included. |
| `5` | `OnBoardCredit` | Onboard Credit. |
| `6` | `RewardPoints` | Reward Points. |
| `7` | `BookingFee` | Tracks booking costs to an agency. |
| `8` | `PaymentDepositDiscount` | Deposit Fix — helps adjust deposit amount up or down. |
| `9` | `AddOnOptions` | Add-on options (e.g., Best Price Guarantee). |
| `10` | `NonRefundableDeposit` | Non-Refundable Deposit — **Not Supported**. |
| `11` | `AgentCommission` | Agent Commission. |
| `12` | `BestPriceGuarantee` | Defines a service fee applied for ensuring best price booking — **not supported yet**. |
| `13` | `ServiceFee` | Defines a service fee, if any, to be added at time of payment. |
| `14` | `SupplierCommission` | Estimated Supplier Commission. |
| `15` | `AddOnHotel` | Add-On Hotel. |
| `16` | `AddOnFlights` | Add-On Flights. |
| `17` | `FixedPrice` | Creates a dynamic discount or markup so the package price matches the rule value. |
| `18` | `PackageService` | Defines additional services selectable by the customer during the booking process. |
| `19` | `PaymentInstallmentsOptions` | Defines monthly/quarterly payment installment options. |
| `30` | `ValueAddOfferAffiliate` | Affiliate Value Added Offer. |
| `40` | `ValueAddOfferConsolidator` | Consolidator Value Added Offer. |
| `50` | `MasterPromotion` | Defines a maximum amount for all applicable `ValueAddOffer`, `OnBoardCredit`, and `RewardPoints` rules combined. |
| `51` | `RuleDiscount` | Defines a discount on the calculated amount of another rule. |
| `52` | `RuleMarkup` | Defines a markup on the calculated amount of another rule. |
| `100` | `PaymentProcessingFee` | Payment Processing Fee — **Not supported yet**. |
| `101` | `ExcludePackage` | Exclude package — mainly used for air. |
| `102` | `DisplayPriceOnly` | Display Price Only / Call Center Fare. |
| `103` | `AirDisplayName` | Modify Air Display Name. |
| `104` | `AirTicketType` | Modify Air Ticket Type. |
| `105` | `BookWithAgent` | Book With Agent. |
| `106` | `Recommended` | Moves affected packages to the top of the list and increases their priority. |
| `107` | `DisplayPrice` | Tells the system to display this price instead of the calculated price. |
| `108` | `ProductExperience` | Experience Type Tag, sourced from Rule Tag Types. |
| `109` | `FareCodeModify` | Fare Code Modify. |
| `110` | `MerchantFlag` | Merchant flag to be set based on fare rules. |
| `111` | `DynamicNetRateCalculation` | Dynamic net rate calculation. |
| `201` | `SupplierPromoCodeInclude` | Supplier Promotion Code (RCCL brands). |
| `202` | `BookingOption` | TourCode / TicketDesignator / Remarks. |
| `401` | `Advertising` | Placeholder for advertising. |

---

## Grouping Notes (by value range)

- **0**: `Undefined` — not supported.
- **1–19**: Core pricing, commission, fee, and package-service rules (Discount, Markup, Value Add Offer, Insurance, Onboard Credit, Reward Points, Booking Fee, Deposit adjustments, Add-On options, Agent Commission, Best Price Guarantee, Service Fee, Supplier Commission, Add-On Hotel/Flights, Fixed Price, Package Service, Payment Installments).
- **30, 40**: Value Add Offer variants scoped to specific parties — **Affiliate** (`30`) and **Consolidator** (`40`).
- **50–52**: "Meta" rules that apply to or cap **other rules** (Master Promotion cap, Rule Discount, Rule Markup).
- **100–111**: Display, air-specific, and merchandising/flagging rules (Payment Processing Fee, Exclude Package, Display Price Only, Air Display Name, Air Ticket Type, Book With Agent, Recommended, Display Price, Product Experience, Fare Code Modify, Merchant Flag, Dynamic Net Rate Calculation).
- **201–202**: Supplier-specific / booking-option rules (Supplier Promo Code, Booking Option — TourCode/TicketDesignator/Remarks).
- **401**: Advertising placeholder.

---

## Not-Currently-Supported Values

The following values are explicitly marked as **not supported** in the source enum and should be treated accordingly by the agent (i.e., flag them as unsupported rather than presenting them as usable rule types):

| Value | Name | Status |
|---|---|---|
| `0` | `Undefined` | Not Supported |
| `10` | `NonRefundableDeposit` | Not Supported |
| `12` | `BestPriceGuarantee` | Not supported yet |
| `100` | `PaymentProcessingFee` | Not supported yet |

---

## Key Takeaways

- Rule Type values are **not sequential** — they're grouped into logical bands (1–19 core rules, 30/40 affiliate/consolidator offers, 50–52 meta-rules-on-rules, 100–111 display/air/merchandising, 201–202 supplier-specific, 401 advertising).
- Some values are **reserved/defined but not yet functional** (`0`, `10`, `12`, `100`) — the agent should call this out if asked about these rule types rather than implying they're active.
- `MasterPromotion (50)` acts as a **cap/ceiling** across `ValueAddOffer`, `OnBoardCredit`, and `RewardPoints` rules — it doesn't define a benefit itself, it constrains the combined total of other rules.
- `RuleDiscount (51)` and `RuleMarkup (52)` apply **on top of another rule's calculated amount** — these are second-order rules, not direct price adjustments to the package itself.
- `SupplierPromoCodeInclude (201)` is specifically noted as relevant to **RCCL brands**.
