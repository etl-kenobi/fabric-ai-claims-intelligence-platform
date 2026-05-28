# Architecture Overview

## Overview

This project follows a Microsoft Fabric-style Medallion Lakehouse architecture for insurance claims reporting and AI-enabled claim intelligence.

The architecture is designed to show how raw operational insurance data can be transformed into trusted reporting data and then extended into AI-ready outputs.

## High-Level Architecture

```text
Synthetic Insurance Source Data
        ↓
Bronze Raw Layer
        ↓
Silver Cleansing and Data Quality Layer
        ↓
Gold Reporting Model
        ↓
Point-in-Time Snapshot Layer
        ↓
Semantic Model Views
        ↓
AI Claim Intelligence Layer
```

## Source Layer

The source layer represents synthetic Salesforce-style insurance data.

Source entities include:

* Accounts
* Policies
* Claims
* Claim Transactions
* Date Dimension

These datasets are fully synthetic and are used only for portfolio demonstration.

## Bronze Layer

The Bronze layer stores raw ingested files.

Purpose:

* Preserve raw source structure
* Capture ingestion metadata
* Maintain traceability
* Support reprocessing
* Keep source data separate from curated data

Example outputs:

```text
data/bronze/accounts.csv
data/bronze/policies.csv
data/bronze/claims.csv
data/bronze/claim_transactions.csv
```

## Silver Layer

The Silver layer applies cleansing and validation.

Typical responsibilities:

* Standardize column names
* Cast date fields
* Cast numeric fields
* Remove duplicates
* Validate nulls
* Validate claim-policy relationships
* Validate transaction dates
* Validate financial amounts
* Generate data quality results

Example outputs:

```text
data/silver/accounts.csv
data/silver/policies.csv
data/silver/claims.csv
data/silver/claim_transactions.csv
data/silver/dq_results.csv
```

## Gold Layer

The Gold layer creates business-ready structures.

Typical outputs:

```text
dim_account
dim_policy
dim_claim
dim_date
fact_claim_transaction
fact_claim_snapshot
```

The Gold layer supports:

* Claims analytics
* Financial reporting
* Semantic model consumption
* PIT reporting
* AI-ready data preparation

## Point-in-Time Snapshot Layer

The PIT layer calculates claim values as of selected valuation dates.

Core rule:

```text
transaction_date <= valuation_date
```

The PIT layer calculates:

* Paid Amount
* Reserve Amount
* Expense Amount
* Recovery Amount
* Incurred Amount
* Claim Status
* Claim movement between PIT1 and PIT2

## Semantic Model Layer

The semantic model layer exposes business-friendly reporting views.

Example views:

```text
vw_claim_financials
vw_claims_semantic
vw_pit_claim_movement
```

These views are designed to support Power BI-style reporting and business-friendly consumption.

## AI Claim Intelligence Layer

The AI layer prepares curated claim outputs for AI use cases.

It produces:

* Claim summaries
* Search-ready documents
* AI-ready JSON outputs
* Natural language Q&A examples
* RAG-compatible claim context

The AI layer does not consume raw source data directly. It uses trusted Gold/PIT outputs.

## End-to-End Flow

```text
1. Generate synthetic insurance source data
2. Store raw data in the Bronze layer
3. Cleanse and validate data in the Silver layer
4. Create Gold facts and dimensions
5. Calculate PIT claim snapshots
6. Expose semantic model-ready SQL views
7. Generate AI-ready claim summaries and search documents
```

## Architecture Principles

* Raw data should remain traceable
* Cleansing and validation should happen before reporting
* Gold data should be business-friendly
* PIT logic should be valuation-date driven
* AI should consume curated data, not raw transactional data
* Outputs should be understandable to business users
* The design should be modular and easy to extend

## Optional Fabric Mapping

This local portfolio structure can be mapped to Microsoft Fabric as follows:

| Local Project Area | Fabric Equivalent                                           |
| ------------------ | ----------------------------------------------------------- |
| data/raw           | Source files / Landing area                                 |
| data/bronze        | Bronze Lakehouse tables                                     |
| data/silver        | Silver Lakehouse tables                                     |
| data/gold          | Gold Lakehouse tables                                       |
| notebooks          | Fabric Notebooks                                            |
| sql                | SQL Endpoint views                                          |
| ai_layer           | Fabric Data Agent / Azure AI Search / Copilot-ready outputs |
| docs               | Project documentation                                       |

## Important Note

This architecture is a portfolio-friendly simulation of an enterprise insurance data platform. It does not include confidential implementation details, client-specific data, or proprietary system design.
