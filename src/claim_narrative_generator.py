def generate_claim_narrative(
    claim_number,
    valuation_date,
    claim_status,
    severity,
    paid_amount,
    reserve_amount,
    expense_amount,
    incurred_amount,
    review_priority
):
    """
    Generates a business-friendly claim narrative from curated Gold/PIT claim fields.
    """
    return (
        f"As of {valuation_date}, claim {claim_number} is {claim_status} "
        f"with {severity} severity. The claim has paid amount of {paid_amount:.2f}, "
        f"reserve amount of {reserve_amount:.2f}, expense amount of {expense_amount:.2f}, "
        f"and total incurred amount of {incurred_amount:.2f}. "
        f"Review priority is {review_priority}."
    )