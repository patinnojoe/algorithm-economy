"""
search.py

Collect YouTube videos from archived Nigerian
search queries.

Each search query is sampled only once across
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
    extract_video_ids,
)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

REGION = "NG"


# --------------------------------------------------
# Search Collector
# --------------------------------------------------

def get_search_videos(
    limit=1000,
    pages_per_query=1,
    save_interval=20
):
    """
    Collect YouTube videos using archived Nigerian
    search queries.

    Parameters
    ----------
    limit : int
        Maximum number of videos.

    pages_per_query : int
        Maximum pages per keyword.

    save_interval : int
        Persist used-query cache every N keywords.
    """

    timestamp = datetime.utcnow().isoformat()

    manager = QueryManager()

    print(manager.stats())

    queries = manager.remaining_queries()

    if not queries:

        print("No remaining search queries.")

        return []

    videos = []

    seen_videos = set()

    processed_queries = 0

    try:

        for query in queries:

            if len(videos) >= limit:
                break

            print(f"Searching: {query}")

            try:

                request = youtube.search().list(

                    part="id,snippet",

                    q=query,

                    type="video",

                    regionCode=REGION,

                    maxResults=50

                )

                pages = 0

                for items in paginate(request):

                    if not items:
                        break

                    ids = extract_video_ids(items)

                    if not ids:
                        break

                    details = fetch_video_details(ids)

                    if not details:
                        break

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
                                discovery_source="search"
                            )

                        )

                        if len(videos) >= limit:
                            break

                    pages += 1

                    if (
                        pages >= pages_per_query
                        or len(videos) >= limit
                    ):
                        break

            except Exception as e:

                print(
                    f"Skipping query '{query}' ({e})"
                )

            finally:

                # keyword is consumed once attempted

                manager.mark_used(query)

                processed_queries += 1

                if processed_queries % save_interval == 0:

                    manager.save()

        manager.save()

        print(
            f"Collected {len(videos):,} search videos "
            f"from {processed_queries:,} queries."
        )

        return videos

    except KeyboardInterrupt:

        print("\nInterrupted. Saving progress...")

        manager.save()

        return videos

    except Exception as e:

        print(f"\nSearch collector stopped: {e}")

        manager.save()

        return videos


# --------------------------------------------------
# Example
# --------------------------------------------------

if __name__ == "__main__":

    videos = get_search_videos(limit=500)

    print(f"\nCollected {len(videos)} search videos.")