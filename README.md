# Fabric AI Claims Intelligence Platform

A Microsoft Fabric-style portfolio project demonstrating how an insurance claims lakehouse can be designed for trusted reporting, point-in-time analytics, semantic model consumption, and AI-enabled claim intelligence.

The project combines Azure/Fabric data engineering patterns with practical AI use cases such as claim summarization, semantic search, and natural language Q&A over curated Gold layer data.

## Business Problem

Insurance claims reporting requires reliable historical analysis, clean transaction data, valuation-date based reporting, and consistent business-ready outputs for analysts, actuaries, claims managers, and finance teams.

Traditional reporting platforms often struggle with:

- Multiple claim transaction versions
- Changing claim statuses over time
- Point-in-time valuation requirements
- Data quality issues across source systems
- Manual interpretation of claim movement
- Lack of AI-ready curated data for search and summarization

This project simulates a modern claims intelligence platform that prepares trusted enterprise data for both reporting and AI consumption.

## Solution Overview

The platform follows a Medallion Lakehouse architecture:

1. Bronze Layer: Raw ingestion of claims, policies, accounts, and claim transactions
2. Silver Layer: Cleansing, standardization, validation, and data quality checks
3. Gold Layer: Reporting-ready dimensional model and claim financial facts
4. PIT Layer: Point-in-time valuation logic for paid, reserve, incurred, and claim status
5. AI Layer: Claim narratives, semantic search documents, and natural language Q&A patterns

## Architecture

```text
Synthetic Insurance Source Data
        ↓
Bronze Layer
        ↓
Silver Cleansing + Data Quality
        ↓
Gold Claims Model
        ↓
PIT Valuation Logic
        ↓
Semantic Model Views
        ↓
AI Claim Intelligence Layer




````

## Key Features

- Synthetic insurance claims, policy, account, and claim transaction datasets
- Bronze, Silver, and Gold Lakehouse architecture pattern
- Raw-to-curated data flow similar to enterprise Azure/Fabric data platforms
- Data quality checks for duplicates, nulls, invalid dates, negative financial values, and referential integrity
- Point-in-time claim valuation logic for reporting as of selected valuation dates
- Claim-level financial analysis for paid amount, reserve amount, expense amount, recovery amount, and incurred amount
- Reporting-ready Gold model designed for semantic model and Power BI-style consumption
- SQL views to support analytics and business-friendly reporting
- AI-ready claim narratives generated from trusted Gold/PIT data
- Semantic search design pattern for retrieving relevant claims using natural language
- Natural language Q&A pattern over curated claim summaries and financial metrics

## Technology Stack

- Microsoft Fabric-style Lakehouse architecture
- Azure Data Engineering design patterns
- Python / PySpark-style processing
- SQL
- Delta Lake concepts
- Medallion architecture
- Data Quality framework
- Semantic Model-ready views
- Azure AI Search compatible design
- LLM-ready data preparation
- GitHub portfolio documentation

## Repository Structure

```text
fabric-ai-claims-intelligence-platform/
│
├── architecture/
│   └── architecture_overview.md
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── ai_outputs/
│
├── docs/
│   ├── business_use_case.md
│   ├── technical_design.md
│   ├── data_model.md
│   ├── pit_logic.md
│   ├── ai_layer_design.md
│   └── interview_story.md
│
├── notebooks/
│   ├── 01_generate_synthetic_data.py
│   ├── 02_bronze_ingestion.py
│   ├── 03_silver_cleansing_dq.py
│   ├── 04_gold_claims_model.py
│   ├── 05_pit_snapshot_logic.py
│   └── 06_ai_claim_intelligence.py
│
├── sql/
│   ├── gold_views.sql
│   ├── semantic_model_views.sql
│   └── sample_pit_queries.sql
│
├── ai_layer/
│   ├── claim_summary_prompt.md
│   ├── semantic_search_design.md
│   ├── ai_search_index_schema.json
│   └── sample_ai_output.json
│
├── src/
│   ├── config.py
│   ├── dq_rules.py
│   ├── pit_engine.py
│   └── claim_narrative_generator.py
│
└── tests/
````

## Current Status

This project is currently in progress.

The initial version focuses on building a clear, GitHub-ready portfolio structure with business context, architecture, documentation, and a phased implementation plan.

### Completed

* Repository created
* Project folder structure created
* README documentation started
* Business and technical scope defined
* AI-enabled claims intelligence concept defined

### In Progress

* Synthetic insurance claims data generation
* Bronze, Silver, and Gold layer implementation
* Data quality rule framework
* PIT valuation logic
* AI claim narrative generation

### Planned Enhancements

* Add runnable Python scripts for generating synthetic claims data
* Add Bronze ingestion logic
* Add Silver cleansing and validation logic
* Add Gold dimensional model creation
* Add point-in-time snapshot calculation
* Add AI-ready claim summary output
* Add semantic search design using Azure AI Search pattern
* Add natural language Q&A examples over curated claim data
* Add architecture diagrams and sample output screenshots

## AI Enablement Scope

This project does not aim to train a machine learning model. Instead, it demonstrates a practical enterprise data engineering pattern where trusted curated data is prepared for downstream AI consumption.

The AI layer focuses on:

1. **Claim Summarization**
   Creating business-readable summaries from structured Gold/PIT claim records.

2. **Semantic Search Readiness**
   Converting curated claim records into search-ready documents that can be indexed by tools such as Azure AI Search.

3. **Natural Language Analytics Pattern**
   Showing how users could ask business questions over curated claim data, such as:

   * Which open claims have high reserve exposure?
   * Which claims changed materially between two valuation dates?
   * Which claims have high incurred amount as of the selected PIT date?
   * Which claims may need management review based on severity and financial exposure?

4. **RAG-Compatible Data Preparation**
   Preparing structured and narrative outputs that can support Retrieval-Augmented Generation patterns without exposing raw or untrusted source data directly to an AI tool.

## Example AI-Ready Claim Output

```json
{
  "claim_number": "CLM-10045",
  "valuation_date": "2024-12-31",
  "claim_status": "Open",
  "severity": "High",
  "paid_amount": 12500.00,
  "reserve_amount": 40000.00,
  "incurred_amount": 52500.00,
  "claim_summary": "As of 2024-12-31, claim CLM-10045 is open with high severity. The claim has a paid amount of 12,500.00, reserve amount of 40,000.00, and total incurred amount of 52,500.00. This claim shows material financial exposure and may require management review."
}
```
## Local Claims Q&A Agent Demo

This project includes a lightweight local Q&A agent that reads AI-ready PIT claim documents and answers business-style questions over curated Gold/PIT data.

Demo with screenshots: [Local Claims Q&A Agent Demo](docs/local_qa_agent_demo.md)


## Business Value

This project demonstrates how a modern data engineering platform can support both traditional reporting and AI-assisted analytics.

Business users can benefit from:

* Trusted claims reporting
* Historical valuation-date analysis
* Improved data quality visibility
* Business-friendly claim summaries
* Faster claim review workflows
* AI-ready data products for search, summarization, and Q&A

## Important Note

This is a portfolio project using fully synthetic insurance data. It does not contain confidential client data, proprietary implementation details, internal system names, real source mappings, or production logic from any organization.

The project is inspired by common enterprise insurance reporting patterns and is designed purely for learning, demonstration, and portfolio purposes.

## Author

Rahul Gurjar
Azure Data Engineer
GitHub: https://github.com/etl-kenobi
Portfolio: https://rahulgurjar.cloud

```
```
