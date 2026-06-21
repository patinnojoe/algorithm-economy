from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)


def safe_request(request, retries=3):
    for i in range(retries):
        try:
            return request.execute()
        except Exception as e:
            print(f"Retry {i+1}: {e}")
            time.sleep(2 ** i)
    return None


def get_trending_videos(limit=5000):
    videos = []

    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        chart="mostPopular",
        maxResults=50,
        regionCode="US"
    )

    while request and len(videos) < limit:
        response = safe_request(request)
        if not response:
            break

        videos.extend(response.get("items", []))

        request = youtube.videos().list_next(request, response)

    return videos