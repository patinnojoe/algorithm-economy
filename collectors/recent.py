from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from .trending import safe_request

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)


def get_recent_videos(limit=5000):
    videos = []

    request = youtube.search().list(
        part="id,snippet",
        q="a",
        order="date",
        type="video",
        maxResults=50
    )

    while request and len(videos) < limit:
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

        request = youtube.search().list_next(request, response)

    return videos