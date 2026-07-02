import time


class QuotaManager:

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
    time.sleep(seconds)