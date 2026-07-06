"""
trending.py

Collect videos promoted by YouTube's Trending algorithm
within the Nigerian YouTube ecosystem.

Population
----------
Videos surfaced through the YouTube Most Popular endpoint
for Nigeria (regionCode="NG").

Author:
Innocent Josiah Patrick
"""

from datetime import datetime

from src.utils.parser import parse_video

from .base import (
    youtube,
    paginate,
)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

REGION = "NG"


# --------------------------------------------------
# Trending Collector
# --------------------------------------------------

def get_trending_videos(limit=200):
    """
    Collect videos promoted by YouTube's Trending algorithm.

    Parameters
    ----------
    limit : int
        Maximum number of videos to collect.

    Returns
    -------
    list
        Parsed discovery records.
    """

    print("Collecting Trending Videos (Nigeria)...")

    timestamp = datetime.utcnow().isoformat()

    videos = []

    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        chart="mostPopular",
        regionCode=REGION,
        maxResults=50
    )

    try:

        for items in paginate(request, limit=limit):

            for video in items:

                video["collection_method"] = "trending"
                video["collection_query"] = None
                video["collection_region"] = REGION
                video["collection_timestamp"] = timestamp

                videos.append(
                    parse_video(
                        video,
                        discovery_source="trending"
                    )
                )

                if len(videos) >= limit:
                    break

            if len(videos) >= limit:
                break

    except Exception as e:

        print(f"Trending collector stopped: {e}")

    print(
        f"Collected {len(videos):,} trending videos from Nigeria."
    )

    return videos


# --------------------------------------------------
# Example
# --------------------------------------------------

if __name__ == "__main__":

    videos = get_trending_videos(limit=200)

    print(f"\nCollected {len(videos)} trending videos.")