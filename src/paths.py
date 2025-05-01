from pathlib import Path

# Project root: two levels up from src/
BASE_DIR = Path(__file__).resolve().parent.parent

# Define commonly used directories
CSV_DIR = BASE_DIR / "csv"
DATAFRAMES_DIR = BASE_DIR / "dataframes_parquet_files"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"
HOURLY_HEATMAPS_DIR = BASE_DIR / "hourly_heatmaps"
HOURLY_HEATMAPS_IMAGES_DIR = BASE_DIR / "hourly_heatmaps_images"
HOURLY_GREYSCALE_HEATMAPS_IMAGES_DIR = BASE_DIR / "hourly_greyscale_heatmaps_images"

# Make sure folders exist
for folder in [CSV_DIR, DATAFRAMES_DIR, NOTEBOOKS_DIR, HOURLY_HEATMAPS_DIR, 
               HOURLY_HEATMAPS_IMAGES_DIR, HOURLY_GREYSCALE_HEATMAPS_IMAGES_DIR]:
    folder.mkdir(parents=True, exist_ok=True)
