-- ============================================================
-- Gold Layer Views
-- Purpose: Business-ready views over Gold claim datasets
-- ============================================================

-- Claim financial snapshot view
CREATE VIEW vw_claim_financial_snapshot AS
SELECT
    claim_id,
    claim_number,
    policy_id,
    policy_number,
    account_id,
    account_name,
    claim_type,
    severity,
    industry,
    region,
    valuation_date,
    current_status AS claim_status,
    paid_amount,
    reserve_amount,
    expense_amount,
    recovery_amount,
    adjustment_amount,
    incurred_amount,
    review_priority
FROM fact_claim_snapshot;


-- Claim transaction detail view
CREATE VIEW vw_claim_transaction_detail AS
SELECT
    transaction_id,
    claim_id,
    claim_number,
    policy_id,
    policy_number,
    account_id,
    account_name,
    claim_type,
    severity,
    industry,
    region,
    transaction_date,
    transaction_type,
    amount,
    currency,
    paid_amount,
    reserve_amount,
    expense_amount,
    recovery_amount,
    adjustment_amount
FROM fact_claim_transaction;