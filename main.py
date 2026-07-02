"""
main.py

Build the raw YouTube dataset.

Pipeline

Trending
+
Search
+
Recent

↓

Merge

↓

Deduplicate

↓

Save
"""

import pandas as pd

from collectors.trending import get_trending_videos
from collectors.recent import get_recent_videos
from collectors.search import get_search_videos

from src.utils.io import save_raw

from src.config import (
    TRENDING_LIMIT,
    RECENT_LIMIT,
    SEARCH_LIMIT
)


def build_dataset():

    print("\nCollecting Trending...")
    trending = get_trending_videos(TRENDING_LIMIT)
    print(f"Trending : {len(trending):,}")

    print("\nCollecting Search...")
    search = get_search_videos(SEARCH_LIMIT)
    print(f"Search     : {len(search):,}")
   


    print("\nCollecting Recent...")
    recent = get_recent_videos(RECENT_LIMIT)
    print(f"Recent    : {len(recent):,}")

    # -------------------------------------
    # Merge datasets
    # -------------------------------------

    df = pd.concat(
        [
            pd.DataFrame(trending),
            pd.DataFrame(recent),
            pd.DataFrame(search),
        ],
        ignore_index=True,
    )

    print(f"\nRows before merge: {len(df):,}")

    # -------------------------------------
    # Merge duplicate videos while preserving
    # discovery pathways
    # -------------------------------------

    aggregation = {
        "title": "first",
        "description": "first",

        "channel_id": "first",
        "channel_title": "first",

        "published_at": "first",
        "category_id": "first",

        "tags": "first",
        "duration": "first",

        "views": "first",
        "likes": "first",
        "comments": "first",
        "engagement_rate": "first",

        "collection_query": "first",
        "collection_region": "first",

        "collected_at": "first",

        "source": lambda x: ",".join(sorted(set(x))),
    }

    df = (
        df.groupby(
            "video_id",
            as_index=False
        )
        .agg(aggregation)
    )

    print(f"Rows after merge : {len(df):,}")

    # -------------------------------------
    # Save
    # -------------------------------------

    save_raw(df)

    print("\nDataset successfully created.")

    return df


if __name__ == "__main__":
    build_dataset()