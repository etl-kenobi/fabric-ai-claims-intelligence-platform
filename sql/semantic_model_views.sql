-- ============================================================
-- Semantic Model Ready Views
-- Purpose: Business-friendly column names for Power BI / semantic model use
-- ============================================================

CREATE VIEW vw_claims_semantic AS
SELECT
    claim_number AS ClaimNumber,
    valuation_date AS ValuationDate,
    claim_status AS ClaimStatus,
    claim_type AS ClaimType,
    severity AS Severity,
    account_name AS AccountName,
    industry AS Industry,
    region AS Region,
    paid_amount AS PaidAmount,
    reserve_amount AS ReserveAmount,
    expense_amount AS ExpenseAmount,
    recovery_amount AS RecoveryAmount,
    adjustment_amount AS AdjustmentAmount,
    incurred_amount AS IncurredAmount,
    review_priority AS ReviewPriority
FROM vw_claim_financial_snapshot;


CREATE VIEW vw_claims_ai_ready AS
SELECT
    ClaimNumber,
    ValuationDate,
    ClaimStatus,
    ClaimType,
    Severity,
    AccountName,
    Region,
    PaidAmount,
    ReserveAmount,
    ExpenseAmount,
    IncurredAmount,
    ReviewPriority,
    CONCAT(
        'As of ', ValuationDate,
        ', claim ', ClaimNumber,
        ' is ', ClaimStatus,
        ' with ', Severity,
        ' severity. Total incurred amount is ',
        CAST(IncurredAmount AS VARCHAR(50)),
        '. Review priority is ',
        ReviewPriority,
        '.'
    ) AS ClaimNarrative
FROM vw_claims_semantic;