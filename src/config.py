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

# for data collection search
SEARCH_QUERIES = [
    "music", "education", "finance", "sports",
    "comedy", "technology", "travel", "gaming",
    "fitness", "food"
]


CATEGORY_MAP = {
    1: "Film & Animation",
    2: "Autos & Vehicles",
    10: "Music",
    15: "Pets & Animals",
    17: "Sports",
    19: "Travel & Events",
    20: "Gaming",
    22: "People & Blogs",
    23: "Comedy",
    24: "Entertainment",
    25: "News & Politics",
    26: "Howto & Style",
    27: "Education",
    28: "Science & Tech",
    29: "Nonprofits"
}


