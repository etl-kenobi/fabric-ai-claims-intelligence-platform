# Data Model

## Overview

The data model is designed to support insurance claims reporting, point-in-time valuation, semantic model consumption, and AI-ready claim intelligence.

The model follows a dimensional structure with business-friendly dimensions and claim financial fact tables.

## Core Entities

### Account

Represents the insured account, customer, or business entity associated with a policy.

Typical attributes:

* Account ID
* Account Name
* Industry
* Region
* Client Segment

### Policy

Represents the insurance policy linked to a claim.

Typical attributes:

* Policy ID
* Policy Number
* Account ID
* Policy Type
* Effective Date
* Expiry Date

### Claim

Represents the claim header information.

Typical attributes:

* Claim ID
* Claim Number
* Policy ID
* Claim Type
* Loss Date
* Reported Date
* Current Claim Status
* Severity

### Claim Transaction

Represents financial movement against a claim.

Typical transaction types:

* Paid
* Reserve
* Expense
* Recovery
* Adjustment

Typical attributes:

* Transaction ID
* Claim ID
* Transaction Date
* Transaction Type
* Amount
* Currency

### Date

Represents calendar attributes used for reporting and slicing.

Typical attributes:

* Date Key
* Calendar Date
* Year
* Quarter
* Month
* Month Name

## Gold Layer Tables

### dim_account

Stores account-level business attributes.

Purpose:

* Customer/account analysis
* Region-level analysis
* Industry-level analysis

### dim_policy

Stores policy-level business attributes.

Purpose:

* Policy type analysis
* Policy period analysis
* Account-policy relationship

### dim_claim

Stores claim-level attributes.

Purpose:

* Claim type analysis
* Severity analysis
* Claim status analysis
* Loss and reported date analysis

### dim_date

Stores calendar attributes.

Purpose:

* Date slicing
* Valuation date selection
* Month-end/year-end reporting

### fact_claim_transaction

Stores individual financial transactions.

Purpose:

* Transaction-level analysis
* Financial movement tracking
* PIT calculation source

Example measures:

* Transaction Amount
* Paid Amount
* Reserve Amount
* Expense Amount
* Recovery Amount

### fact_claim_snapshot

Stores point-in-time claim values as of selected valuation dates.

Purpose:

* PIT reporting
* Period comparison
* Claim movement analysis
* Semantic model consumption
* AI-ready claim summary generation

Example measures:

* Paid Amount as of Valuation Date
* Reserve Amount as of Valuation Date
* Expense Amount as of Valuation Date
* Recovery Amount as of Valuation Date
* Incurred Amount as of Valuation Date

## Relationship Design

Typical relationships:

```text
dim_account.account_id → dim_policy.account_id
dim_policy.policy_id → dim_claim.policy_id
dim_claim.claim_id → fact_claim_transaction.claim_id
dim_claim.claim_id → fact_claim_snapshot.claim_id
dim_date.date → fact_claim_transaction.transaction_date
dim_date.date → fact_claim_snapshot.valuation_date
```

## Reporting Grain

### fact_claim_transaction

Grain:

```text
One row per claim financial transaction
```

### fact_claim_snapshot

Grain:

```text
One row per claim per valuation date
```

This allows the same claim to appear multiple times across different valuation dates for PIT comparison.

## Key Business Metrics

* Claim Count
* Open Claim Count
* Closed Claim Count
* Paid Amount
* Reserve Amount
* Expense Amount
* Recovery Amount
* Incurred Amount
* High Severity Claim Count
* Claims with Material Movement

## AI-Ready Data Model Output

The AI layer uses curated outputs from the Gold/PIT layer.

Example AI-ready fields:

* Claim Number
* Valuation Date
* Claim Status
* Claim Type
* Severity
* Paid Amount
* Reserve Amount
* Incurred Amount
* Claim Summary

These fields can be converted into searchable claim documents for semantic retrieval and natural language analytics.
