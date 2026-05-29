# Claim Summary Prompt Template

## Purpose

This prompt template demonstrates how curated Gold/PIT claim data can be converted into a business-readable claim summary.

The prompt is designed for downstream AI tools such as Azure OpenAI, Fabric Data Agent-style experiences, Copilot-style analytics, or any LLM-based summarization workflow.

## Prompt

You are an insurance claims analyst.

Create a concise business summary for the following claim record.

Use only the fields provided. Do not invent facts, assumptions, legal conclusions, or medical details.

## Input Fields

- Claim Number
- Valuation Date
- Claim Status
- Claim Type
- Severity
- Paid Amount
- Reserve Amount
- Expense Amount
- Recovery Amount
- Incurred Amount
- Review Priority

## Expected Output

Generate one short business-friendly claim summary.

The summary should:

- Mention the valuation date
- Mention claim status and severity
- Mention paid, reserve, expense, and incurred amount
- Mention whether the claim may require review
- Avoid unsupported assumptions
- Keep the response clear and suitable for business users

## Example Input

```json
{
  "claim_number": "CLM-10045",
  "valuation_date": "2024-12-31",
  "claim_status": "Open",
  "claim_type": "Bodily Injury",
  "severity": "High",
  "paid_amount": 12500.00,
  "reserve_amount": 40000.00,
  "expense_amount": 2500.00,
  "recovery_amount": 0.00,
  "incurred_amount": 55000.00,
  "review_priority": "High"
}
