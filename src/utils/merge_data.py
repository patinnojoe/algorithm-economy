"""
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

from src.utils.storage import save_raw


# --------------------------------------------------
# Collect
# --------------------------------------------------

print("\nCollecting Trending...")

trending = get_trending_videos(
    limit=3000
)

print(f"Trending : {len(trending):,}")






print("\nCollecting Recent...")

recent = get_recent_videos(
    limit=3000
)

print(f"Recent    : {len(recent):,}")


# --------------------------------------------------
# Merge
# --------------------------------------------------

df = pd.concat(
    [
        pd.DataFrame(trending),
        pd.DataFrame(recent),
    ],
    ignore_index=True
)

print(f"\nRows before merge: {len(df):,}")


# --------------------------------------------------
# Preserve all discovery pathways
# --------------------------------------------------

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

    "source": lambda x: ",".join(
        sorted(set(x))
    )
}

df = (
    df.groupby(
        "video_id",
        as_index=False
    )
    .agg(aggregation)
)

print(f"Rows after merge : {len(df):,}")


# --------------------------------------------------
# Save
# --------------------------------------------------

save_raw(df)

print("\nDataset successfully created.")