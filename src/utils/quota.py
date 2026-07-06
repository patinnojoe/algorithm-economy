"""
quota.py

Utilities for quota management and request throttling.

Author:
Innocent Josiah Patrick
"""

import time


class QuotaManager:
    """
    Simple in-memory YouTube quota tracker.

    Default YouTube quota:
        10,000 units/day
    """

    def __init__(
        self,
        limit=9500,
        request_delay=0.4
    ):
        self.limit = limit
        self.used = 0
        self.request_delay = request_delay

    # -----------------------------------------
    # Consume quota
    # -----------------------------------------

    def consume(self, units):

        self.used += units

        if self.used >= self.limit:

            raise RuntimeError(
                f"Quota exceeded ({self.used}/{self.limit})"
            )

    # -----------------------------------------
    # Remaining quota
    # -----------------------------------------

    def remaining(self):

        return self.limit - self.used

    # -----------------------------------------
    # Reset
    # -----------------------------------------

    def reset(self):

        self.used = 0

    # -----------------------------------------
    # Throttle requests
    # -----------------------------------------

    def sleep(self):

        time.sleep(self.request_delay)


# --------------------------------------------------
# Global quota manager
# --------------------------------------------------

quota = QuotaManager()