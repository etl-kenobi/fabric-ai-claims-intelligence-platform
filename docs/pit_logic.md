# Point-in-Time Logic

## Overview

Point-in-Time reporting allows business users to analyze claims as they existed at a specific valuation date.

In insurance reporting, claim values can change over time due to payments, reserve changes, expenses, recoveries, adjustments, or status changes. PIT logic helps reconstruct the claim position at a selected date instead of only showing the latest available values.

## Why PIT Logic Is Needed

Without PIT logic, reports may only show current claim values.

This can be misleading when users need to answer historical questions such as:

* What was the paid amount at month-end?
* What was the reserve amount at year-end?
* What was the incurred value as of a specific reporting date?
* Which claims changed materially between two valuation dates?
* Which claims were open at PIT1 but closed at PIT2?

## Basic PIT Rule

The basic rule for PIT calculation is:

```text
Include only claim transactions where transaction_date <= valuation_date
```

Example:

```text
Valuation Date: 2024-12-31
```

Only transactions on or before 2024-12-31 should be included in the PIT snapshot.

## PIT Snapshot Grain

The PIT snapshot table uses the following grain:

```text
One row per claim per valuation date
```

Example:

```text
Claim Number | Valuation Date | Paid Amount | Reserve Amount | Incurred Amount | Status
CLM-10045    | 2024-06-30     | 5,000       | 25,000         | 30,000          | Open
CLM-10045    | 2024-12-31     | 12,500      | 40,000         | 52,500          | Open
```

This structure allows comparison between two valuation dates.

## Core Measures

### Paid Amount as of Valuation Date

Calculated by summing all paid transactions up to the valuation date.

```text
Paid Amount = SUM(Paid Transactions where transaction_date <= valuation_date)
```

### Reserve Amount as of Valuation Date

Calculated based on reserve transactions available up to the valuation date.

Depending on business rules, reserve may be treated as:

* Latest reserve position
* Cumulative reserve movement
* Open reserve balance

For this portfolio project, reserve is treated as a cumulative amount for simplified demonstration.

### Expense Amount as of Valuation Date

Calculated by summing expense transactions up to the valuation date.

### Recovery Amount as of Valuation Date

Calculated by summing recovery transactions up to the valuation date.

### Incurred Amount as of Valuation Date

Simplified formula:

```text
Incurred Amount = Paid Amount + Reserve Amount + Expense Amount
```

Recoveries may be analyzed separately or netted based on business rules.

## PIT1 and PIT2 Comparison

The project supports comparison between two selected valuation dates:

```text
PIT1 = Earlier valuation date
PIT2 = Later valuation date
```

Example comparison questions:

* How much did paid amount increase from PIT1 to PIT2?
* Did reserve amount increase or decrease?
* Did claim status change?
* Did incurred amount move materially?
* Which claims require review?

## Example PIT Movement

```text
Claim: CLM-10045

PIT1 Date: 2024-06-30
Paid Amount: 5,000
Reserve Amount: 25,000
Incurred Amount: 30,000
Status: Open

PIT2 Date: 2024-12-31
Paid Amount: 12,500
Reserve Amount: 40,000
Incurred Amount: 52,500
Status: Open

Movement:
Paid Movement = 7,500
Reserve Movement = 15,000
Incurred Movement = 22,500
```

## Business Interpretation

The claim remained open between PIT1 and PIT2, but the incurred amount increased materially. This may indicate higher claim exposure and may require claim review or management attention.

## AI Use Case

PIT outputs can be converted into business-readable summaries.

Example:

```text
As of 2024-12-31, claim CLM-10045 remains open with total incurred amount of 52,500. The claim increased by 22,500 compared to the previous valuation date, mainly due to reserve and paid movement. This claim may require review due to material financial exposure.
```

This type of summary can be used for:

* Claim review workflows
* Executive summaries
* Semantic search
* Natural language Q&A
* RAG-style AI applications

## Simplification Note

This portfolio project uses simplified PIT logic for demonstration.

A real enterprise implementation may require additional rules for:

* Transaction sequencing
* Latest reserve position
* Claim reopen scenarios
* Currency conversion
* Multi-calendar reporting
* Multi-tenant isolation
* Audit and reconciliation controls
