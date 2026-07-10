URL: https://supportdesk.odysol.com/agent/odysseus/odysseus-solutions-support/knowledge-base/page?articlestatus=published#Solutions/dv/80395000040396289/en/Article

ID:80395000040396289

---

title: Certification Use Cases
category: Knowledge Base
version: 1.0
last\_updated: 2026-07-10
tags:

* Certification
* API Integration
* Testing
* Use Cases

\---

# Certification Use Cases

## Overview

This document provides the certification use cases for clients integrating with the Odysseus Booking API.

The document is intended to guide clients through the certification process by outlining the required scenarios, submission requirements, and feedback process.

> \*\*Note:\*\* This document is a living document and will continue to be enhanced over time.

\---

# Certification Process

The certification process consists of **two steps**.

## Step 1 – Execute Certification Use Cases

Clients must use the provided certification spreadsheet containing the required test scenarios.

For each scenario, clients should:

* Execute the use case.
* Update the scenario status as **Pass** or **Fail**.
* Record any questions, observations, or issues in the **Comments** section of the spreadsheet.

\---

## Step 2 – Submit API Logs

Clients must provide the API logs used to execute each certification scenario.

### Submission Requirements

* Create a single ZIP archive.
* Organize the ZIP file into subfolders, with one folder for each certification use case.
* Include all relevant request and response JSON files for every API call performed during the scenario.

### Required Logs

The submitted logs should contain the **complete booking flow**, including all intermediate API requests and responses.

Examples include:

* Search
* Fare Codes
* Categories
* Cabins
* Pricing
* Create Booking
* Read Booking
* Any additional APIs involved in the scenario

Providing only the Create Booking request and response is **not sufficient** for certification validation.

\---

# Important Notes

* Submit API request and response logs as **attachments**.
* Do **not** submit screenshots of requests or responses.
* JSON request and response files are required to allow proper validation and troubleshooting.

\---

# Certification Feedback

All certification communication must be managed through the assigned support ticket.

This includes:

* Certification submissions
* Questions
* Feedback
* Issue tracking
* Validation results

Using the support ticket ensures efficient tracking and faster turnaround throughout the certification process.

Client-specific project management or issue tracking tools are not used for certification activities.

\---

# Best Practices

* Complete every required certification scenario.
* Keep request and response logs organized by use case.
* Include the full booking flow for each scenario.
* Clearly document any issues or questions in the certification spreadsheet.
* Use the assigned support ticket for all certification communication.

