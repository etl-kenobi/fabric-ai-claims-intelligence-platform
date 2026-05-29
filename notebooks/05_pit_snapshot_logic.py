from pathlib import Path

import pandas as pd


# ------------------------------------------------------------
# Base paths
# ------------------------------------------------------------

BASE_PATH = Path(__file__).resolve().parents[1]
GOLD_PATH = BASE_PATH / "data" / "gold"


# ------------------------------------------------------------
# Load Gold files
# ------------------------------------------------------------

transactions = pd.read_csv(GOLD_PATH / "fact_claim_transaction.csv")
claims = pd.read_csv(GOLD_PATH / "dim_claim.csv")


# ------------------------------------------------------------
# Prepare data types
# ------------------------------------------------------------

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)


# ------------------------------------------------------------
# Define valuation dates
# ------------------------------------------------------------

valuation_dates = [
    "2024-06-30",
    "2024-12-31"
]


# ------------------------------------------------------------
# Create PIT snapshots
# ------------------------------------------------------------

snapshots = []

for valuation_date in valuation_dates:
    valuation_ts = pd.to_datetime(valuation_date)

    transactions_as_of_date = transactions[
        transactions["transaction_date"] <= valuation_ts
    ].copy()

    snapshot = transactions_as_of_date.groupby(
        [
            "claim_id",
            "claim_number",
            "policy_id",
            "policy_number",
            "account_id",
            "account_name",
            "claim_type",
            "severity",
            "industry",
            "region"
        ],
        as_index=False
    ).agg(
        paid_amount=("paid_amount", "sum"),
        reserve_amount=("reserve_amount", "sum"),
        expense_amount=("expense_amount", "sum"),
        recovery_amount=("recovery_amount", "sum"),
        adjustment_amount=("adjustment_amount", "sum")
    )

    snapshot["valuation_date"] = valuation_date

    snapshot["incurred_amount"] = (
        snapshot["paid_amount"]
        + snapshot["reserve_amount"]
        + snapshot["expense_amount"]
        + snapshot["adjustment_amount"]
    )

    snapshot = snapshot.merge(
        claims[[
            "claim_id",
            "current_status",
            "loss_date",
            "reported_date"
        ]],
        on="claim_id",
        how="left"
    )

    snapshots.append(snapshot)


# ------------------------------------------------------------
# Combine snapshots
# ------------------------------------------------------------

fact_claim_snapshot = pd.concat(snapshots, ignore_index=True)


# ------------------------------------------------------------
# Add simple review flag
# ------------------------------------------------------------

fact_claim_snapshot["review_priority"] = fact_claim_snapshot.apply(
    lambda row: "High"
    if row["severity"] == "High" and row["incurred_amount"] >= 25000
    else "Normal",
    axis=1
)


# ------------------------------------------------------------
# Write PIT snapshot output
# ------------------------------------------------------------

fact_claim_snapshot.to_csv(
    GOLD_PATH / "fact_claim_snapshot.csv",
    index=False
)


print("PIT snapshot logic completed successfully.")
print(f"Output path: {GOLD_PATH}")
print("File created:")
print("- fact_claim_snapshot.csv")