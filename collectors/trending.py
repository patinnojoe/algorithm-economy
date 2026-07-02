"""
trending.py

Collect videos promoted by YouTube's Trending algorithm
within the Nigerian YouTube ecosystem.

Population:
    Videos surfaced through the YouTube Trending page
    for Nigeria (regionCode="NG").

Author:
Innocent Josiah Patrick
"""

from datetime import datetime
from src.utils.parser import parse_video

from .base import youtube, paginate


REGION = "NG"


def get_trending_videos(limit=200):
    """
    Collect trending videos from YouTube Nigeria.

    Parameters
    ----------
    limit : int
        Maximum number of videos to collect.

    Returns
    -------
    list
        List of YouTube video objects.
    """

    print("Collecting Trending Videos (Nigeria)...")

    videos = []

    timestamp = datetime.utcnow().isoformat()

    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        chart="mostPopular",
        regionCode=REGION,
        maxResults=50
    )

    collected = 0

    for items in paginate(request, limit=limit):

        for video in items:

            video["collection_method"] = "trending"

            video["collection_region"] = REGION

            video["collection_timestamp"] = timestamp

            # videos.append(video)
            videos.append(
                parse_video(
                    video,
                    source="trending"
                ))

        collected += len(items)

        if collected >= limit:
            break

    print(f"Collected {len(videos)} trending videos from Nigeria.")

    return videos


if __name__ == "__main__":

    videos = get_trending_videos(limit=200)

    print(f"\nTotal Videos: {len(videos)}")