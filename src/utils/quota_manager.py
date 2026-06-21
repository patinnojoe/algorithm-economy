import time


class QuotaManager:
    """
    Simple in-memory quota tracker.
    YouTube API default quota ~10,000 units/day.
    """

    def __init__(self, limit=9500):
        self.limit = limit
        self.used = 0

    def consume(self, units):
        self.used += units

        if self.used > self.limit:
            raise Exception(
                f"Quota exceeded: {self.used}/{self.limit}"
            )

    def remaining(self):
        return self.limit - self.used

    def reset(self):
        self.used = 0


def rate_limit_sleep(seconds=1):
    """
    Basic throttle to avoid API burst limits.
    """
    time.sleep(seconds)