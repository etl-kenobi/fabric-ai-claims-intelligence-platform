from datetime import datetime
from pathlib import Path

import pandas as pd


# ------------------------------------------------------------
# Base paths
# ------------------------------------------------------------

BASE_PATH = Path(__file__).resolve().parents[1]

RAW_PATH = BASE_PATH / "data" / "raw"
BRONZE_PATH = BASE_PATH / "data" / "bronze"

BRONZE_PATH.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Source files to ingest
# ------------------------------------------------------------

source_files = [
    "accounts.csv",
    "policies.csv",
    "claims.csv",
    "claim_transactions.csv"
]


# ------------------------------------------------------------
# Bronze ingestion
# ------------------------------------------------------------

for file_name in source_files:
    source_file_path = RAW_PATH / file_name
    target_file_path = BRONZE_PATH / file_name

    if not source_file_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_file_path}")

    df = pd.read_csv(source_file_path)

    # Add simple ingestion metadata
    df["ingestion_timestamp"] = datetime.utcnow().isoformat()
    df["source_file_name"] = file_name
    df["source_layer"] = "raw"
    df["target_layer"] = "bronze"

    df.to_csv(target_file_path, index=False)

    print(f"Ingested {file_name} into Bronze layer")


print("Bronze ingestion completed successfully.")
print(f"Output path: {BRONZE_PATH}")