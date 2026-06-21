from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from .trending import safe_request
from src.config import SEARCH_QUERIES

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)


def get_search_videos(limit_per_query=500):
    videos = []

    for query in SEARCH_QUERIES:

        request = youtube.search().list(
            part="id,snippet",
            q=query,
            type="video",
            maxResults=50
        )

        count = 0

        while request and count < limit_per_query:
            response = safe_request(request)
            if not response:
                break

            video_ids = [item["id"]["videoId"] for item in response["items"]]

            video_request = youtube.videos().list(
                part="snippet,statistics,contentDetails",
                id=",".join(video_ids)
            )

            video_response = safe_request(video_request)

            if video_response:
                videos.extend(video_response["items"])

            count += 50
            request = youtube.search().list_next(request, response)

    return videos