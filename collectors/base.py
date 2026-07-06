
"""
base.py

Shared utilities for interacting with the YouTube Data API v3.

Responsibilities
----------------
- Build authenticated YouTube client
- Execute safe API requests
- Automatic retry handling
- Quota tracking
- Automatic throttling
- Pagination
- Fetch complete video metadata

Author:
Innocent Josiah Patrick
"""

import os
import time
import random
import logging

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.utils.quota import quota


# --------------------------------------------------
# Environment
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

if API_KEY is None:
    raise ValueError(
        "YOUTUBE_API_KEY not found."
    )


# --------------------------------------------------
# Logging
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Build Client
# --------------------------------------------------

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY,
    cache_discovery=False
)


# --------------------------------------------------
# Configuration
# --------------------------------------------------

MAX_RETRIES = 3


# --------------------------------------------------
# Safe Request
# --------------------------------------------------

def safe_request(
    request,
    quota_cost=1
):
    """
    Execute a YouTube API request safely.

    Parameters
    ----------
    request
        Google API request object.

    quota_cost : int
        Cost of the endpoint.

    Returns
    -------
    dict | None
    """

    for attempt in range(MAX_RETRIES):

        try:

            quota.consume(quota_cost)

            quota.sleep()

            time.sleep(
                random.uniform(0.05, 0.20)
            )

            return request.execute()

        except HttpError as e:

            status = e.resp.status

            logger.warning(
                f"HTTP {status} "
                f"(Attempt {attempt+1}/{MAX_RETRIES})"
            )

            # ------------------------------------
            # Too many requests
            # ------------------------------------

            if status == 429:

                logger.warning(
                    "Rate limit reached."
                )

                quota.sleep()

                return None

            # ------------------------------------
            # Retry transient server errors
            # ------------------------------------

            if status in (
                500,
                502,
                503,
                504
            ):

                sleep = 2 ** attempt

                time.sleep(sleep)

                continue

            return None

        except RuntimeError as e:

            logger.warning(str(e))

            return None

        except Exception as e:

            logger.warning(str(e))

            return None

    logger.warning(
        "Maximum retries exceeded."
    )

    return None


# --------------------------------------------------
# Pagination
# --------------------------------------------------

def paginate(
    request,
    limit=None,
    quota_cost=100
):
    """
    Iterate through paginated YouTube requests.

    Parameters
    ----------
    request

    limit : int | None

    quota_cost : int

    Yields
    ------
    list
    """

    total = 0

    while request:

        response = safe_request(
            request=request,
            quota_cost=quota_cost
        )

        if response is None:
            break

        items = response.get(
            "items",
            []
        )

        if not items:
            break

        yield items

        total += len(items)

        logger.info(
            f"Collected {total:,} records."
        )

        if (
            limit is not None
            and total >= limit
        ):
            break

        quota.sleep()

        request = youtube.search().list_next(
            request,
            response
        )


# --------------------------------------------------
# Fetch Video Metadata
# --------------------------------------------------

def fetch_video_details(
    video_ids,
    batch_size=50
):
    """
    Fetch complete metadata for videos.

    Parameters
    ----------
    video_ids : list

    batch_size : int

    Returns
    -------
    list
    """

    videos = []

    for i in range(
        0,
        len(video_ids),
        batch_size
    ):

        batch = video_ids[
            i:i + batch_size
        ]

        request = youtube.videos().list(

            part="snippet,statistics,contentDetails",

            id=",".join(batch)

        )

        response = safe_request(
            request=request,
            quota_cost=1
        )

        if response is None:

            logger.warning(
                "Skipping metadata batch."
            )

            continue

        videos.extend(
            response.get(
                "items",
                []
            )
        )

    logger.info(
        f"Retrieved metadata for "
        f"{len(videos):,} videos."
    )

    return videos


# --------------------------------------------------
# Helpers
# --------------------------------------------------

def extract_video_ids(items):
    """
    Extract video ids from search results.
    """

    ids = []

    for item in items:

        obj = item.get("id")

        if isinstance(obj, dict):

            video_id = obj.get(
                "videoId"
            )

            if video_id:

                ids.append(video_id)

    return ids

