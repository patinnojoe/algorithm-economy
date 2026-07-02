"""
search.py

Collect YouTube videos from archived search queries.

Each search query is used only once across
all collection runs.

Author:
Innocent Josiah Patrick
"""

from datetime import datetime

from src.utils.parser import parse_video
from src.query.query_manager import QueryManager

from .base import (

    youtube,

    paginate,

    fetch_video_details,

    extract_video_ids

)

REGION = "NG"


def get_search_videos(
    limit=5000,
    pages_per_query=2
):

    timestamp = datetime.utcnow().isoformat()

    manager = QueryManager()

    print(manager.stats())

    queries = manager.remaining_queries()

    if len(queries) == 0:

        print("No search queries remaining.")

        return []

    videos = []

    seen_videos = set()

    for query in queries:

        print(f"Searching: {query}")

        request = youtube.search().list(

            part="id,snippet",

            q=query,

            type="video",

            regionCode=REGION,

            maxResults=50

        )

        pages = 0

        for items in paginate(request):

            ids = extract_video_ids(items)

            if not ids:
                continue

            details = fetch_video_details(ids)

            for video in details:

                video_id = video["id"]

                if video_id in seen_videos:
                    continue

                seen_videos.add(video_id)

                video["collection_method"] = "search"

                video["collection_query"] = query

                video["collection_region"] = REGION

                video["collection_timestamp"] = timestamp

                videos.append(

                    parse_video(
                        video,
                        source="search"
                    )

                )

                if len(videos) >= limit:

                    manager.mark_used(query)

                    print(
                        f"Collected {len(videos):,} videos."
                    )

                    return videos

            pages += 1

            if pages >= pages_per_query:
                break

        # mark keyword immediately after processing
        manager.mark_used(query)

    print(
        f"Collected {len(videos):,} videos."
    )

    return videos


if __name__ == "__main__":

    videos = get_search_videos(limit=500)

    print(len(videos))