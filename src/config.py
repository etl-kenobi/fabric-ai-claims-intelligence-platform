from pathlib import Path


BASE_PATH = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_PATH / "data"

RAW_PATH = DATA_PATH / "raw"
BRONZE_PATH = DATA_PATH / "bronze"
SILVER_PATH = DATA_PATH / "silver"
GOLD_PATH = DATA_PATH / "gold"
AI_OUTPUT_PATH = DATA_PATH / "ai_outputs"