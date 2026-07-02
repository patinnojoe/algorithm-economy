"""
Generate YouTube search query sampling frame.

This script harvests YouTube autocomplete suggestions
and stores them locally as a JSON file.

Author:
Innocent Josiah Patrick
"""

import json
import random
import string
import time
from pathlib import Path

import requests


# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

REGION = "NG"

OUTPUT = Path("data/cache/youtube_search_queries_ng.json")

OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True
)

AUTOCOMPLETE_URL = (
    "https://suggestqueries.google.com/complete/search"
)

USER_AGENT = (
    "Mozilla/5.0"
)

# Number of prefixes to sample.
# Full search space = 712.
# 250-400 gives very good coverage.
PREFIX_SAMPLE = 300


# -------------------------------------------------------
# Prefix Generator
# -------------------------------------------------------

def generate_prefixes():

    prefixes = []

    prefixes.extend(string.ascii_lowercase)

    prefixes.extend(string.digits)

    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            prefixes.append(a + b)

    return prefixes


# -------------------------------------------------------
# Autocomplete
# -------------------------------------------------------

def fetch_queries():

    prefixes = generate_prefixes()

    random.shuffle(prefixes)

    prefixes = prefixes[:PREFIX_SAMPLE]

    queries = set()

    headers = {
        "User-Agent": USER_AGENT
    }

    print(f"Sampling {len(prefixes)} prefixes...\n")

    for i, prefix in enumerate(prefixes, start=1):

        print(f"[{i}/{len(prefixes)}] {prefix}")

        try:

            response = requests.get(

                AUTOCOMPLETE_URL,

                params={

                    "client": "firefox",

                    "ds": "yt",

                    "gl": REGION.lower(),

                    "q": prefix

                },

                headers=headers,

                timeout=10

            )

            response.raise_for_status()

            suggestions = response.json()[1]

            queries.update(suggestions)

            time.sleep(
                random.uniform(
                    0.6,
                    1.2
                )
            )

        except Exception as e:

            print(e)

            continue

    return sorted(list(queries))


# -------------------------------------------------------
# Save
# -------------------------------------------------------

def save_queries(queries):

    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            queries,

            f,

            indent=4,

            ensure_ascii=False

        )

    print()

    print("=" * 60)

    print(f"Saved {len(queries):,} queries")

    print(OUTPUT)

    print("=" * 60)


# -------------------------------------------------------
# Main
# -------------------------------------------------------

if __name__ == "__main__":

    queries = fetch_queries()

    save_queries(queries)