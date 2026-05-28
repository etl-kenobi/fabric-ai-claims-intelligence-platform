# Technical Design

## Overview

This project demonstrates a Microsoft Fabric-style insurance claims lakehouse designed for reporting, point-in-time analytics, semantic model consumption, and AI-enabled claim intelligence.

The technical design follows a Medallion Lakehouse architecture where raw source data is progressively transformed into trusted, business-ready, and AI-ready data products.

## Source Data

The project uses fully synthetic insurance data representing a Salesforce-style operational source system.

The source entities include:

* Accounts
* Policies
* Claims
* Claim Transactions
* Date Dimension

These datasets simulate common insurance reporting entities without using any real client or confidential data.

## Processing Layers

### Bronze Layer

The Bronze layer stores raw ingested data with minimal transformation.

Purpose:

* Preserve source structure
* Maintain raw records for traceability
* Capture ingestion metadata
* Support reprocessing if required

Example datasets:

* bronze_accounts
* bronze_policies
* bronze_claims
* bronze_claim_transactions

### Silver Layer

The Silver layer applies cleansing, standardization, validation, and business rule checks.

Typical transformations:

* Standardize column names
* Cast date and numeric fields
* Remove duplicate records
* Validate required fields
* Check invalid transaction dates
* Check negative or unexpected financial values
* Validate relationships between claims, policies, and accounts

Example datasets:

* silver_accounts
* silver_policies
* silver_claims
* silver_claim_transactions
* silver_dq_results

### Gold Layer

The Gold layer creates reporting-ready facts and dimensions.

Purpose:

* Support analytics and reporting
* Provide clean business-friendly structures
* Prepare semantic model-ready views
* Support PIT valuation logic
* Support AI-ready outputs

Example datasets:

* dim_account
* dim_policy
* dim_claim
* dim_date
* fact_claim_transaction
* fact_claim_snapshot

## Point-in-Time Layer

The PIT layer calculates claim financials and status as of selected valuation dates.

Core logic:

```text
Include claim transactions where transaction_date <= valuation_date
```

The PIT layer supports metrics such as:

* Paid Amount as of valuation date
* Reserve Amount as of valuation date
* Expense Amount as of valuation date
* Recovery Amount as of valuation date
* Incurred Amount as of valuation date
* Claim Status as of valuation date

## AI Intelligence Layer

The AI layer converts trusted Gold and PIT outputs into business-readable and search-ready formats.

AI-enabled outputs include:

* Claim summaries
* Claim financial narratives
* Search-ready claim documents
* Natural language Q&A examples
* RAG-compatible claim records

The AI layer is designed to demonstrate how curated enterprise data can be safely exposed to downstream AI tools without relying directly on raw transactional data.

## High-Level Flow

```text
Synthetic Source Data
        ↓
Bronze Raw Layer
        ↓
Silver Cleansing and DQ Layer
        ↓
Gold Reporting Model
        ↓
PIT Snapshot Layer
        ↓
Semantic Model Views
        ↓
AI Claim Intelligence Layer
```

## Design Principles

* Keep raw data immutable
* Apply validation before reporting
* Separate facts and dimensions
* Use valuation-date logic for historical reporting
* Generate business-friendly outputs for AI consumption
* Avoid exposing raw or untrusted data directly to AI tools
* Keep implementation modular and easy to extend

## Current Implementation Scope

The first version of this project focuses on:

* Project structure
* Documentation
* Synthetic data generation
* Basic Bronze/Silver/Gold processing
* PIT snapshot calculation
* AI-ready claim summary generation

Future enhancements can include:

* Fabric notebook version
* Delta Lake table implementation
* Azure AI Search index creation
* Power BI semantic model design
* Natural language Q&A prototype
