from pathlib import Path
import os
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent

# helper variables for commonly used folders
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT_DIR / "outputs"
load_dotenv(ROOT_DIR / ".env")


# helper for fetching content from youtube

API_KEY = os.getenv("YOUTUBE_API_KEY")

REGION_CODE = "US"   # keep global but default trending region
MAX_RESULTS = 50

# sampling sizes
TRENDING_LIMIT = 5000
RECENT_LIMIT = 5000
SEARCH_LIMIT = 5000
CHANNEL_LIMIT = 5000

SEARCH_QUERIES = [
    "music", "education", "finance", "sports",
    "comedy", "technology", "travel", "gaming",
    "fitness", "food"
]


