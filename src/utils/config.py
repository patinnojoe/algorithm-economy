from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# helper variables for commonly used folders
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT_DIR / "outputs"