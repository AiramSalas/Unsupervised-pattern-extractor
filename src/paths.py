from pathlib import Path

# Project root: two levels up from src/
BASE_DIR = Path(__file__).resolve().parent.parent

# Define commonly used directories
CSV_DIR = BASE_DIR / "csv"
DATAFRAMES_DIR = BASE_DIR / "dataframes_parquet_files"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"

# Make sure folders exist
for folder in [CSV_DIR, DATAFRAMES_DIR, NOTEBOOKS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)
