from pathlib import Path
import json

import pandas as pd


# ------------------------------------------------------------
# Base paths
# ------------------------------------------------------------

BASE_PATH = Path(__file__).resolve().parents[1]

GOLD_PATH = BASE_PATH / "data" / "gold"
AI_OUTPUT_PATH = BASE_PATH / "data" / "ai_outputs"

AI_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Load PIT snapshot data
# ------------------------------------------------------------

snapshot = pd.read_csv(GOLD_PATH / "fact_claim_snapshot.csv")


# ------------------------------------------------------------
# Claim summary generation
# ------------------------------------------------------------

def generate_claim_summary(row):
    return (
        f"As of {row['valuation_date']}, claim {row['claim_number']} is "
        f"{row['current_status']} with {row['severity']} severity. "
        f"The claim has paid amount of {row['paid_amount']:.2f}, "
        f"reserve amount of {row['reserve_amount']:.2f}, "
        f"expense amount of {row['expense_amount']:.2f}, "
        f"and total incurred amount of {row['incurred_amount']:.2f}. "
        f"Review priority is {row['review_priority']}."
    )


snapshot["claim_summary"] = snapshot.apply(generate_claim_summary, axis=1)


# ------------------------------------------------------------
# Create AI-ready JSON documents
# ------------------------------------------------------------

ai_documents = []

for _, row in snapshot.iterrows():
    ai_documents.append({
        "document_id": f"{row['claim_number']}_{row['valuation_date']}",
        "claim_id": row["claim_id"],
        "claim_number": row["claim_number"],
        "valuation_date": row["valuation_date"],
        "claim_status": row["current_status"],
        "claim_type": row["claim_type"],
        "severity": row["severity"],
        "account_name": row["account_name"],
        "industry": row["industry"],
        "region": row["region"],
        "paid_amount": float(row["paid_amount"]),
        "reserve_amount": float(row["reserve_amount"]),
        "expense_amount": float(row["expense_amount"]),
        "recovery_amount": float(row["recovery_amount"]),
        "incurred_amount": float(row["incurred_amount"]),
        "review_priority": row["review_priority"],
        "claim_summary": row["claim_summary"]
    })


# ------------------------------------------------------------
# Write AI outputs
# ------------------------------------------------------------

snapshot.to_csv(
    AI_OUTPUT_PATH / "claim_ai_summaries.csv",
    index=False
)

with open(AI_OUTPUT_PATH / "claim_ai_documents.json", "w", encoding="utf-8") as file:
    json.dump(ai_documents, file, indent=2)


# ------------------------------------------------------------
# Create sample natural language questions
# ------------------------------------------------------------

sample_questions = [
    "Which open claims have high incurred amount as of 2024-12-31?",
    "Which high severity claims require management review?",
    "Which claims have high reserve exposure?",
    "Summarize claims by region and severity.",
    "Which claims changed materially between valuation dates?"
]

with open(AI_OUTPUT_PATH / "sample_natural_language_questions.txt", "w", encoding="utf-8") as file:
    for question in sample_questions:
        file.write(question + "\n")


print("AI claim intelligence outputs generated successfully.")
print(f"Output path: {AI_OUTPUT_PATH}")
print("Files created:")
print("- claim_ai_summaries.csv")
print("- claim_ai_documents.json")
print("- sample_natural_language_questions.txt")