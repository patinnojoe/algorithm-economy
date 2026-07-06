"""
recent.py

Collect recently published YouTube videos.

This collector represents the supply side of the
Algorithmic Economy by sampling recently uploaded
videos using archived Nigerian search queries.

Author:
Innocent Josiah Patrick
"""

import json
import random
from datetime import datetime

from src.config import SEARCH_QUERY_FILE
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


# --------------------------------------------------
# Recent Upload Collector
# --------------------------------------------------

def get_recent_videos(
    limit=3000,
    pages_per_query=2,
    max_queries=25
):
    """
    Collect recently uploaded videos.

    Unlike the Search collector, queries are randomly
    sampled every run and are NOT permanently consumed.

    Parameters
    ----------
    limit : int
        Maximum videos.

    pages_per_query : int
        Maximum search pages per keyword.

    max_queries : int
        Maximum number of keywords sampled during a run.

    Returns
    -------
    list
    """

    timestamp = datetime.utcnow().isoformat()

    # -----------------------------------------
    # Load query archive
    # -----------------------------------------

    with open(
        SEARCH_QUERY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        queries = json.load(f)

    random.shuffle(queries)

    # Don't walk through the entire archive
    queries = queries[:max_queries]

    videos = []
    seen_videos = set()

    try:

        for query in queries:

            print(f"Recent Query: {query}")

            try:

                request = youtube.search().list(
                    part="id,snippet",
                    q=query,
                    type="video",
                    order="date",
                    regionCode=REGION,
                    maxResults=50
                )

                pages = 0

                for items in paginate(request):

                    if not items:
                        break

                    ids = extract_video_ids(items)

                    if not ids:
                        continue

                    details = fetch_video_details(ids)

                    if not details:
                        break

                    for video in details:

                        video_id = video["id"]

                        if video_id in seen_videos:
                            continue

                        seen_videos.add(video_id)

                        video["collection_method"] = "recent"
                        video["collection_query"] = query
                        video["collection_region"] = REGION
                        video["collection_timestamp"] = timestamp

                        videos.append(
                            parse_video(
                                video,
                                discovery_source="recent"
                            )
                        )

                        if len(videos) >= limit:

                            print(
                                f"Collected {len(videos):,} recent videos."
                            )

                            return videos

                    pages += 1

                    if pages >= pages_per_query:
                        break

            except Exception as e:

                print(
                    f"Skipping recent query '{query}' ({e})"
                )

                continue

        print(
            f"Collected {len(videos):,} recent videos."
        )

        return videos

    except KeyboardInterrupt:

        print("\nRecent collector interrupted.")

        return videos

    except Exception as e:

        print(f"\nRecent collector stopped: {e}")

        return videos


# --------------------------------------------------
# Example
# --------------------------------------------------

if __name__ == "__main__":

    videos = get_recent_videos(limit=500)

    print(f"\nCollected {len(videos)} recent videos.")