"""
Clean archived YouTube search queries.

Author:
Innocent Josiah Patrick
"""

import json
import re
from pathlib import Path


RAW_FILE = Path("data/cache/youtube_search_queries_ng.json")
OUTPUT_FILE = Path("data/cache/youtube_search_queries_ng_clean.json")


REMOVE_QUERIES = {
    "السد",
    "جذبني",
    "حب",
    "دورا",
    "ذئب",
    "سيد",
    "سين",
    "علاش",
    "كوبا",
    "كيفو",
    "ماجد",
}


def clean_query(query):

    query = query.lower().strip()

    # collapse whitespace
    query = re.sub(r"\s+", " ", query)

    return query


def main():

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        queries = json.load(f)

    cleaned = []

    seen = set()

    for query in queries:

        query = clean_query(query)

        if not query:
            continue

        if len(query) == 1:
            continue

        if query.isdigit():
            continue

        if query in REMOVE_QUERIES:
            continue

        if query in seen:
            continue

        seen.add(query)

        cleaned.append(query)

    cleaned.sort()

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            cleaned,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(f"Raw: {len(queries):,}")
    print(f"Clean: {len(cleaned):,}")


if __name__ == "__main__":
    main()