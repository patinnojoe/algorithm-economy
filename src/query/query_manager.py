"""
query_manager.py

Manage archived search queries.

Queries are sampled WITHOUT replacement
across multiple collection runs.

Author:
Innocent Josiah Patrick
"""

import json
import random

from pathlib import Path

from src.config import (
    SEARCH_QUERY_FILE,
    SEARCH_USED_FILE
)


class QueryManager:

    def __init__(self):

        self.master = self._load_master()

        self.used = self._load_used()

    # -----------------------------------------

    def _load_master(self):

        with open(
            SEARCH_QUERY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    # -----------------------------------------

    def _load_used(self):

        if not SEARCH_USED_FILE.exists():

            SEARCH_USED_FILE.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(
                SEARCH_USED_FILE,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump([], f)

            return set()

        with open(
            SEARCH_USED_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return set(json.load(f))

    # -----------------------------------------

    def remaining_queries(self):

        remaining = list(

            set(self.master) - self.used

        )

        random.shuffle(remaining)

        return remaining

    # -----------------------------------------

    def mark_used(self, query):

        self.used.add(query)

        with open(
            SEARCH_USED_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                sorted(list(self.used)),
                f,
                indent=4,
                ensure_ascii=False
            )

    # -----------------------------------------

    def remaining(self):

        return len(self.master) - len(self.used)

    # -----------------------------------------

    def reset(self):

        self.used = set()

        with open(
            SEARCH_USED_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump([], f, indent=4)

    # -----------------------------------------

    def stats(self):

        return {

            "total": len(self.master),

            "used": len(self.used),

            "remaining": self.remaining()

        }