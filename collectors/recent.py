"""
recent.py

Collect recently published YouTube videos.

This collector represents the supply side of the
Algorithmic Economy by sampling newly uploaded videos.

Author:
Innocent Josiah Patrick
"""

from datetime import datetime

from src.utils.parser import parse_video

from .base import (
    youtube,
    paginate,
    fetch_video_details,
    extract_video_ids,
)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

REGION = "NG"

DEFAULT_QUERY = "a"


# --------------------------------------------------
# Recent Upload Collector
# --------------------------------------------------

def get_recent_videos(limit=3000):
    """
    Collect recently uploaded YouTube videos.

    Parameters
    ----------
    limit : int
        Maximum number of videos to collect.

    Returns
    -------
    list
        Parsed video records.
    """

    timestamp = datetime.utcnow().isoformat()

    videos = []

    seen = set()

    request = youtube.search().list(
        part="id,snippet",
        q=DEFAULT_QUERY,
        type="video",
        order="date",
        regionCode=REGION,
        maxResults=50
    )

    for items in paginate(request, limit=limit):

        ids = extract_video_ids(items)

        details = fetch_video_details(ids)

        for video in details:

            video_id = video["id"]

            if video_id in seen:
                continue

            seen.add(video_id)

            video["collection_method"] = "recent"
            video["collection_region"] = REGION
            video["collection_timestamp"] = timestamp

            videos.append(
                parse_video(
                    video,
                    source="recent"
                )
            )

            if len(videos) >= limit:
                return videos

    return videos


# --------------------------------------------------
# Example
# --------------------------------------------------

if __name__ == "__main__":

    videos = get_recent_videos(limit=500)

    print(f"Collected {len(videos)} recent videos.")