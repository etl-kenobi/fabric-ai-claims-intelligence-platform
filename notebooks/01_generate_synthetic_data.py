import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


# ------------------------------------------------------------
# Base paths
# ------------------------------------------------------------

BASE_PATH = Path(__file__).resolve().parents[1]
RAW_PATH = BASE_PATH / "data" / "raw"

RAW_PATH.mkdir(parents=True, exist_ok=True)

random.seed(42)


# ------------------------------------------------------------
# Generate synthetic accounts
# ------------------------------------------------------------

accounts = []

industries = [
    "Manufacturing",
    "Retail",
    "Healthcare",
    "Logistics",
    "Financial Services",
    "Construction",
    "Technology"
]

regions = [
    "North America",
    "Europe",
    "APAC",
    "Middle East"
]

for i in range(1, 11):
    accounts.append({
        "account_id": f"ACC-{i:03d}",
        "account_name": f"Global Insurance Account {i}",
        "industry": random.choice(industries),
        "region": random.choice(regions)
    })


# ------------------------------------------------------------
# Generate synthetic policies
# ------------------------------------------------------------

policies = []

policy_types = [
    "General Liability",
    "Workers Compensation",
    "Property",
    "Auto Liability",
    "Professional Liability"
]

for i in range(1, 16):
    account = random.choice(accounts)

    policies.append({
        "policy_id": f"POL-{i:03d}",
        "account_id": account["account_id"],
        "policy_number": f"PN-{10000 + i}",
        "policy_type": random.choice(policy_types),
        "effective_date": "2024-01-01",
        "expiry_date": "2024-12-31"
    })


# ------------------------------------------------------------
# Generate synthetic claims
# ------------------------------------------------------------

claims = []

claim_types = [
    "Bodily Injury",
    "Property Damage",
    "Legal Expense",
    "Medical",
    "Auto Damage"
]

claim_statuses = [
    "Open",
    "Closed",
    "Reopened"
]

severities = [
    "Low",
    "Medium",
    "High"
]

for i in range(1, 31):
    policy = random.choice(policies)

    loss_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 300))
    reported_date = loss_date + timedelta(days=random.randint(1, 20))

    claims.append({
        "claim_id": f"CLM-{i:04d}",
        "claim_number": f"CLM-{10000 + i}",
        "policy_id": policy["policy_id"],
        "claim_type": random.choice(claim_types),
        "loss_date": loss_date.date().isoformat(),
        "reported_date": reported_date.date().isoformat(),
        "current_status": random.choice(claim_statuses),
        "severity": random.choice(severities)
    })


# ------------------------------------------------------------
# Generate synthetic claim transactions
# ------------------------------------------------------------

transactions = []

transaction_types = [
    "Paid",
    "Reserve",
    "Expense",
    "Recovery",
    "Adjustment"
]

transaction_id = 1

for claim in claims:
    transaction_count = random.randint(2, 6)

    for _ in range(transaction_count):
        base_date = datetime.fromisoformat(claim["reported_date"])
        transaction_date = base_date + timedelta(days=random.randint(1, 250))
        transaction_type = random.choice(transaction_types)

        amount = round(random.uniform(500, 25000), 2)

        # Recovery is represented as negative movement for demonstration
        if transaction_type == "Recovery":
            amount = -amount

        transactions.append({
            "transaction_id": f"TXN-{transaction_id:05d}",
            "claim_id": claim["claim_id"],
            "transaction_date": transaction_date.date().isoformat(),
            "transaction_type": transaction_type,
            "amount": amount,
            "currency": "USD"
        })

        transaction_id += 1


# ------------------------------------------------------------
# Write CSV files
# ------------------------------------------------------------

pd.DataFrame(accounts).to_csv(RAW_PATH / "accounts.csv", index=False)
pd.DataFrame(policies).to_csv(RAW_PATH / "policies.csv", index=False)
pd.DataFrame(claims).to_csv(RAW_PATH / "claims.csv", index=False)
pd.DataFrame(transactions).to_csv(RAW_PATH / "claim_transactions.csv", index=False)

print("Synthetic insurance source data generated successfully.")
print(f"Output path: {RAW_PATH}")
print("Files created:")
print("- accounts.csv")
print("- policies.csv")
print("- claims.csv")
print("- claim_transactions.csv")