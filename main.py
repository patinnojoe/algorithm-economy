"""
main.py

Build the YouTube discovery dataset.

Pipeline

Trending
+
Search
+
Recent

↓

Discovery Log

↓

Save

Author:
Innocent Josiah Patrick
"""

import pandas as pd

from collectors.trending import get_trending_videos
from collectors.search import get_search_videos
from collectors.recent import get_recent_videos

from src.utils.io import save_raw

from src.config import (
    TRENDING_LIMIT,
    SEARCH_LIMIT,
    RECENT_LIMIT,
)


# --------------------------------------------------
# Safe Collector
# --------------------------------------------------

def run_collector(name, func, limit):

    print(f"\nCollecting {name}...")

    try:

        data = func(limit=limit)

        print(f"{name:<10}: {len(data):,}")

        return data

    except Exception as e:

        print(f"{name} failed: {e}")

        return []


# --------------------------------------------------
# Build Discovery Dataset
# --------------------------------------------------

def build_dataset():

    discovery = []

    # ------------------------------------------
    # Trending
    # ------------------------------------------

    discovery.extend(
        run_collector(
            "Trending",
            get_trending_videos,
            TRENDING_LIMIT
        )
    )

    # ------------------------------------------
    # Search
    # ------------------------------------------

    discovery.extend(
        run_collector(
            "Search",
            get_search_videos,
            SEARCH_LIMIT
        )
    )

    # ------------------------------------------
    # Recent
    # ------------------------------------------

    discovery.extend(
        run_collector(
            "Recent",
            get_recent_videos,
            RECENT_LIMIT
        )
    )

    # ------------------------------------------
    # Build DataFrame
    # ------------------------------------------

    discovery_df = pd.DataFrame(discovery)

    print(
        f"\nDiscovery Events : {len(discovery_df):,}"
    )

    if not discovery_df.empty:

        print(
            f"Unique Videos     : "
            f"{discovery_df['video_id'].nunique():,}"
        )

    # ------------------------------------------
    # Save
    # ------------------------------------------

    save_raw(discovery_df)

    print("\nDiscovery dataset successfully created.")

    return discovery_df


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":

    build_dataset()