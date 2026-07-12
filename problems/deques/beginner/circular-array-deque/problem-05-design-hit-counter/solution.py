"""Design Hit Counter — LeetCode 362.

Count hits in the trailing 300-second window using two fixed circular arrays of
length 300 indexed by ``timestamp % 300``: a stale bucket is transparently
recycled, so both hit and getHits are O(300) space and time, never O(#hits).
"""
from typing import List  # noqa: F401


class MyHitCounter:
    def __init__(self) -> None:
        # TODO: two length-300 buffers — bucket timestamps and bucket counts
        pass

    def hit(self, timestamp: int) -> None:
        # TODO: idx = timestamp % 300; overwrite a stale bucket, else increment
        pass

    def getHits(self, timestamp: int) -> int:
        # TODO: sum counts of buckets whose timestamp is within the 300s window
        pass


if __name__ == "__main__":
    hc = MyHitCounter()
    hc.hit(1)
    hc.hit(2)
    hc.hit(3)
    print(hc.getHits(4))  # expected: 3
    hc.hit(300)
    print(hc.getHits(300))  # expected: 4
    print(hc.getHits(301))  # expected: 3

    wrap = MyHitCounter()
    wrap.hit(1)
    wrap.hit(301)  # 301 % 300 == 1 -> recycles the stale bucket from second 1
    print(wrap.getHits(301))  # expected: 1
    print(wrap.getHits(601))  # expected: 0
