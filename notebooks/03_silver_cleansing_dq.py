from pathlib import Path

import pandas as pd


# ------------------------------------------------------------
# Base paths
# ------------------------------------------------------------

BASE_PATH = Path(__file__).resolve().parents[1]

BRONZE_PATH = BASE_PATH / "data" / "bronze"
SILVER_PATH = BASE_PATH / "data" / "silver"

SILVER_PATH.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# DQ helper function
# ------------------------------------------------------------

dq_results = []


def add_dq_result(table_name, rule_name, status, failed_count, description):
    dq_results.append({
        "table_name": table_name,
        "rule_name": rule_name,
        "status": status,
        "failed_count": failed_count,
        "description": description
    })


def standardize_columns(df):
    df.columns = [
        col.strip().lower().replace(" ", "_")
        for col in df.columns
    ]
    return df


# ------------------------------------------------------------
# Load Bronze files
# ------------------------------------------------------------

accounts = pd.read_csv(BRONZE_PATH / "accounts.csv")
policies = pd.read_csv(BRONZE_PATH / "policies.csv")
claims = pd.read_csv(BRONZE_PATH / "claims.csv")
transactions = pd.read_csv(BRONZE_PATH / "claim_transactions.csv")


# ------------------------------------------------------------
# Standardize column names
# ------------------------------------------------------------

accounts = standardize_columns(accounts)
policies = standardize_columns(policies)
claims = standardize_columns(claims)
transactions = standardize_columns(transactions)


# ------------------------------------------------------------
# Basic type casting
# ------------------------------------------------------------

policies["effective_date"] = pd.to_datetime(policies["effective_date"], errors="coerce")
policies["expiry_date"] = pd.to_datetime(policies["expiry_date"], errors="coerce")

claims["loss_date"] = pd.to_datetime(claims["loss_date"], errors="coerce")
claims["reported_date"] = pd.to_datetime(claims["reported_date"], errors="coerce")

transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"], errors="coerce")
transactions["amount"] = pd.to_numeric(transactions["amount"], errors="coerce")


# ------------------------------------------------------------
# Data Quality Checks - Accounts
# ------------------------------------------------------------

duplicate_accounts = accounts["account_id"].duplicated().sum()
add_dq_result(
    "accounts",
    "duplicate_account_id_check",
    "PASS" if duplicate_accounts == 0 else "FAIL",
    int(duplicate_accounts),
    "Checks duplicate account_id values"
)

missing_account_ids = accounts["account_id"].isna().sum()
add_dq_result(
    "accounts",
    "missing_account_id_check",
    "PASS" if missing_account_ids == 0 else "FAIL",
    int(missing_account_ids),
    "Checks missing account_id values"
)


# ------------------------------------------------------------
# Data Quality Checks - Policies
# ------------------------------------------------------------

duplicate_policies = policies["policy_id"].duplicated().sum()
add_dq_result(
    "policies",
    "duplicate_policy_id_check",
    "PASS" if duplicate_policies == 0 else "FAIL",
    int(duplicate_policies),
    "Checks duplicate policy_id values"
)

invalid_policy_dates = (policies["effective_date"] > policies["expiry_date"]).sum()
add_dq_result(
    "policies",
    "invalid_policy_date_check",
    "PASS" if invalid_policy_dates == 0 else "FAIL",
    int(invalid_policy_dates),
    "Checks policies where effective_date is greater than expiry_date"
)

invalid_policy_accounts = (~policies["account_id"].isin(accounts["account_id"])).sum()
add_dq_result(
    "policies",
    "policy_account_relationship_check",
    "PASS" if invalid_policy_accounts == 0 else "FAIL",
    int(invalid_policy_accounts),
    "Checks whether policy account_id exists in accounts"
)


# ------------------------------------------------------------
# Data Quality Checks - Claims
# ------------------------------------------------------------

duplicate_claims = claims["claim_id"].duplicated().sum()
add_dq_result(
    "claims",
    "duplicate_claim_id_check",
    "PASS" if duplicate_claims == 0 else "FAIL",
    int(duplicate_claims),
    "Checks duplicate claim_id values"
)

invalid_claim_dates = (claims["loss_date"] > claims["reported_date"]).sum()
add_dq_result(
    "claims",
    "invalid_claim_date_check",
    "PASS" if invalid_claim_dates == 0 else "FAIL",
    int(invalid_claim_dates),
    "Checks claims where loss_date is greater than reported_date"
)

invalid_claim_policies = (~claims["policy_id"].isin(policies["policy_id"])).sum()
add_dq_result(
    "claims",
    "claim_policy_relationship_check",
    "PASS" if invalid_claim_policies == 0 else "FAIL",
    int(invalid_claim_policies),
    "Checks whether claim policy_id exists in policies"
)


# ------------------------------------------------------------
# Data Quality Checks - Claim Transactions
# ------------------------------------------------------------

duplicate_transactions = transactions["transaction_id"].duplicated().sum()
add_dq_result(
    "claim_transactions",
    "duplicate_transaction_id_check",
    "PASS" if duplicate_transactions == 0 else "FAIL",
    int(duplicate_transactions),
    "Checks duplicate transaction_id values"
)

invalid_transaction_claims = (~transactions["claim_id"].isin(claims["claim_id"])).sum()
add_dq_result(
    "claim_transactions",
    "transaction_claim_relationship_check",
    "PASS" if invalid_transaction_claims == 0 else "FAIL",
    int(invalid_transaction_claims),
    "Checks whether transaction claim_id exists in claims"
)

missing_amounts = transactions["amount"].isna().sum()
add_dq_result(
    "claim_transactions",
    "missing_amount_check",
    "PASS" if missing_amounts == 0 else "FAIL",
    int(missing_amounts),
    "Checks missing transaction amount values"
)

invalid_transaction_dates = transactions["transaction_date"].isna().sum()
add_dq_result(
    "claim_transactions",
    "invalid_transaction_date_check",
    "PASS" if invalid_transaction_dates == 0 else "FAIL",
    int(invalid_transaction_dates),
    "Checks invalid transaction dates"
)


# ------------------------------------------------------------
# Write Silver files
# ------------------------------------------------------------

accounts.to_csv(SILVER_PATH / "accounts.csv", index=False)
policies.to_csv(SILVER_PATH / "policies.csv", index=False)
claims.to_csv(SILVER_PATH / "claims.csv", index=False)
transactions.to_csv(SILVER_PATH / "claim_transactions.csv", index=False)

pd.DataFrame(dq_results).to_csv(SILVER_PATH / "dq_results.csv", index=False)


print("Silver cleansing and data quality checks completed successfully.")
print(f"Output path: {SILVER_PATH}")
print("Files created:")
print("- accounts.csv")
print("- policies.csv")
print("- claims.csv")
print("- claim_transactions.csv")
print("- dq_results.csv")