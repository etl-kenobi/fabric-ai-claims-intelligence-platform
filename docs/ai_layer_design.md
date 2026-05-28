# AI Layer Design

## Overview

The AI layer in this project demonstrates how trusted insurance claims data can be prepared for downstream AI consumption.

The goal is not to train a machine learning model. The goal is to show how a Data Engineer can create clean, governed, business-ready data outputs that can be safely used by AI tools for summarization, semantic search, and natural language analytics.

## Why an AI Layer Is Needed

Enterprise AI systems are only as reliable as the data they consume.

Raw claim transaction data is often too technical, fragmented, and difficult for business users or AI tools to interpret directly. Before AI can provide useful answers, the data needs to be:

* Cleaned
* Standardized
* Validated
* Modeled
* Contextualized
* Converted into business-readable outputs

This project demonstrates that pattern using curated Gold/PIT claim records.

## AI Layer Inputs

The AI layer uses outputs from the Gold and PIT layers.

Typical input fields include:

* Claim ID
* Claim Number
* Valuation Date
* Claim Status
* Claim Type
* Severity
* Paid Amount
* Reserve Amount
* Expense Amount
* Recovery Amount
* Incurred Amount
* Account / Policy context

## AI Layer Outputs

The AI layer produces:

* Claim summaries
* Claim financial narratives
* Search-ready claim documents
* Prompt-ready structured records
* Natural language Q&A examples
* RAG-compatible claim outputs

## Capability 1: Claim Summarization

Claim summarization converts structured claim data into business-readable text.

Example structured input:

```json
{
  "claim_number": "CLM-10045",
  "valuation_date": "2024-12-31",
  "claim_status": "Open",
  "severity": "High",
  "paid_amount": 12500.00,
  "reserve_amount": 40000.00,
  "incurred_amount": 52500.00
}
```

Example generated summary:

```text
As of 2024-12-31, claim CLM-10045 is open with high severity. The claim has a paid amount of 12,500, reserve amount of 40,000, and total incurred amount of 52,500. This claim shows material financial exposure and may require management review.
```

## Capability 2: Semantic Search Readiness

The project prepares claim records as search-ready documents.

A search-ready document may include:

* Claim metadata
* Financial metrics
* Valuation date
* Claim status
* Severity
* Business summary
* Keywords and tags

Example user query:

```text
Find open high severity claims with high reserve exposure.
```

The system can retrieve claim documents that match the meaning of the query instead of relying only on exact keyword search.

## Capability 3: Natural Language Q&A Pattern

The project demonstrates how users could ask natural language questions over curated Gold/PIT data.

Example questions:

```text
Which open claims have the highest incurred amount as of 2024-12-31?
```

```text
Which claims had material reserve movement between PIT1 and PIT2?
```

```text
Summarize high severity open claims with reserve amount above 25,000.
```

The intended pattern is:

```text
User Question
    ↓
Retrieve relevant curated claim records
    ↓
Apply business filters or aggregation
    ↓
Generate grounded business response
```

## Capability 4: RAG-Compatible Data Preparation

Retrieval-Augmented Generation requires trusted documents that can be retrieved and passed into an AI model as context.

This project prepares RAG-compatible claim records by converting structured Gold/PIT data into readable and searchable documents.

Example RAG document:

```json
{
  "document_id": "CLM-10045_2024-12-31",
  "claim_number": "CLM-10045",
  "valuation_date": "2024-12-31",
  "claim_status": "Open",
  "severity": "High",
  "business_context": "High severity open claim with material financial exposure.",
  "claim_summary": "As of 2024-12-31, claim CLM-10045 is open with high severity. The claim has total incurred amount of 52,500."
}
```

## AI Design Principles

The AI layer follows these principles:

* Use curated Gold/PIT data, not raw source data
* Keep summaries grounded in available fields
* Do not invent missing facts
* Keep business language clear and explainable
* Preserve claim identifiers and valuation dates
* Make outputs suitable for semantic search and Q&A
* Keep confidential or sensitive data out of generated examples

## What This Project Demonstrates

This project shows that a Data Engineer can support AI use cases by building the trusted data foundation required for AI systems.

It demonstrates:

* AI-ready data preparation
* Claim narrative generation
* Search-ready document design
* RAG-compatible data outputs
* Natural language analytics patterns
* Practical AI enablement on top of enterprise data engineering

## Future Enhancements

Future versions can include:

* Local semantic search prototype
* Azure AI Search index implementation
* Vector embedding generation
* OpenAI/Azure OpenAI prompt integration
* Fabric Data Agent-style Q&A design
* Power BI / Copilot style analytics use cases
