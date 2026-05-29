-- ============================================================
-- Sample PIT Reporting Queries
-- Purpose: Example analytical queries over PIT claim snapshots
-- ============================================================

-- 1. Claims as of year-end valuation date
SELECT
    claim_number,
    valuation_date,
    claim_status,
    severity,
    paid_amount,
    reserve_amount,
    incurred_amount,
    review_priority
FROM vw_claim_financial_snapshot
WHERE valuation_date = '2024-12-31';


-- 2. High incurred open claims
SELECT
    claim_number,
    account_name,
    region,
    severity,
    paid_amount,
    reserve_amount,
    incurred_amount
FROM vw_claim_financial_snapshot
WHERE claim_status = 'Open'
  AND incurred_amount >= 25000
ORDER BY incurred_amount DESC;


-- 3. Claims requiring high review priority
SELECT
    claim_number,
    valuation_date,
    claim_status,
    severity,
    incurred_amount,
    review_priority
FROM vw_claim_financial_snapshot
WHERE review_priority = 'High'
ORDER BY incurred_amount DESC;


-- 4. PIT movement between two valuation dates
WITH pit1 AS (
    SELECT
        claim_number,
        incurred_amount AS incurred_pit1,
        paid_amount AS paid_pit1,
        reserve_amount AS reserve_pit1
    FROM vw_claim_financial_snapshot
    WHERE valuation_date = '2024-06-30'
),
pit2 AS (
    SELECT
        claim_number,
        incurred_amount AS incurred_pit2,
        paid_amount AS paid_pit2,
        reserve_amount AS reserve_pit2
    FROM vw_claim_financial_snapshot
    WHERE valuation_date = '2024-12-31'
)
SELECT
    pit2.claim_number,
    pit1.paid_pit1,
    pit2.paid_pit2,
    pit2.paid_pit2 - pit1.paid_pit1 AS paid_movement,
    pit1.reserve_pit1,
    pit2.reserve_pit2,
    pit2.reserve_pit2 - pit1.reserve_pit1 AS reserve_movement,
    pit1.incurred_pit1,
    pit2.incurred_pit2,
    pit2.incurred_pit2 - pit1.incurred_pit1 AS incurred_movement
FROM pit2
LEFT JOIN pit1
    ON pit2.claim_number = pit1.claim_number
ORDER BY incurred_movement DESC;