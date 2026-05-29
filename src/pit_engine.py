import pandas as pd


def filter_transactions_as_of_date(transactions_df, valuation_date):
    """
    Returns claim transactions where transaction_date is less than or equal to valuation_date.
    """
    transactions = transactions_df.copy()

    transactions["transaction_date"] = pd.to_datetime(
        transactions["transaction_date"],
        errors="coerce"
    )

    valuation_ts = pd.to_datetime(valuation_date)

    return transactions[transactions["transaction_date"] <= valuation_ts].copy()


def calculate_incurred_amount(row):
    """
    Calculates simplified incurred amount.

    In this portfolio project:
    Incurred Amount = Paid + Reserve + Expense + Adjustment
    """
    return (
        row.get("paid_amount", 0)
        + row.get("reserve_amount", 0)
        + row.get("expense_amount", 0)
        + row.get("adjustment_amount", 0)
    )


def assign_review_priority(severity, incurred_amount, threshold=25000):
    """
    Assigns review priority based on severity and incurred amount.
    """
    if severity == "High" and incurred_amount >= threshold:
        return "High"

    return "Normal"