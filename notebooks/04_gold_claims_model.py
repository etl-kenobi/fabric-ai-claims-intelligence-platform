from pathlib import Path

import pandas as pd


# ------------------------------------------------------------
# Base paths
# ------------------------------------------------------------

BASE_PATH = Path(__file__).resolve().parents[1]

SILVER_PATH = BASE_PATH / "data" / "silver"
GOLD_PATH = BASE_PATH / "data" / "gold"

GOLD_PATH.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Load Silver files
# ------------------------------------------------------------

accounts = pd.read_csv(SILVER_PATH / "accounts.csv")
policies = pd.read_csv(SILVER_PATH / "policies.csv")
claims = pd.read_csv(SILVER_PATH / "claims.csv")
transactions = pd.read_csv(SILVER_PATH / "claim_transactions.csv")


# ------------------------------------------------------------
# Create dimensions
# ------------------------------------------------------------

dim_account = accounts[[
    "account_id",
    "account_name",
    "industry",
    "region"
]].drop_duplicates()

dim_policy = policies[[
    "policy_id",
    "policy_number",
    "account_id",
    "policy_type",
    "effective_date",
    "expiry_date"
]].drop_duplicates()

dim_claim = claims[[
    "claim_id",
    "claim_number",
    "policy_id",
    "claim_type",
    "loss_date",
    "reported_date",
    "current_status",
    "severity"
]].drop_duplicates()


# ------------------------------------------------------------
# Create fact_claim_transaction
# ------------------------------------------------------------

fact_claim_transaction = transactions[[
    "transaction_id",
    "claim_id",
    "transaction_date",
    "transaction_type",
    "amount",
    "currency"
]].copy()

fact_claim_transaction = fact_claim_transaction.merge(
    dim_claim[[
        "claim_id",
        "claim_number",
        "policy_id",
        "claim_type",
        "severity"
    ]],
    on="claim_id",
    how="left"
)

fact_claim_transaction = fact_claim_transaction.merge(
    dim_policy[[
        "policy_id",
        "policy_number",
        "account_id",
        "policy_type"
    ]],
    on="policy_id",
    how="left"
)

fact_claim_transaction = fact_claim_transaction.merge(
    dim_account[[
        "account_id",
        "account_name",
        "industry",
        "region"
    ]],
    on="account_id",
    how="left"
)


# ------------------------------------------------------------
# Add basic financial classification columns
# ------------------------------------------------------------

fact_claim_transaction["paid_amount"] = fact_claim_transaction.apply(
    lambda row: row["amount"] if row["transaction_type"] == "Paid" else 0,
    axis=1
)

fact_claim_transaction["reserve_amount"] = fact_claim_transaction.apply(
    lambda row: row["amount"] if row["transaction_type"] == "Reserve" else 0,
    axis=1
)

fact_claim_transaction["expense_amount"] = fact_claim_transaction.apply(
    lambda row: row["amount"] if row["transaction_type"] == "Expense" else 0,
    axis=1
)

fact_claim_transaction["recovery_amount"] = fact_claim_transaction.apply(
    lambda row: row["amount"] if row["transaction_type"] == "Recovery" else 0,
    axis=1
)

fact_claim_transaction["adjustment_amount"] = fact_claim_transaction.apply(
    lambda row: row["amount"] if row["transaction_type"] == "Adjustment" else 0,
    axis=1
)


# ------------------------------------------------------------
# Write Gold files
# ------------------------------------------------------------

dim_account.to_csv(GOLD_PATH / "dim_account.csv", index=False)
dim_policy.to_csv(GOLD_PATH / "dim_policy.csv", index=False)
dim_claim.to_csv(GOLD_PATH / "dim_claim.csv", index=False)
fact_claim_transaction.to_csv(GOLD_PATH / "fact_claim_transaction.csv", index=False)


print("Gold claims model created successfully.")
print(f"Output path: {GOLD_PATH}")
print("Files created:")
print("- dim_account.csv")
print("- dim_policy.csv")
print("- dim_claim.csv")
print("- fact_claim_transaction.csv")