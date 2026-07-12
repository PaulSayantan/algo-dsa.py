"""Design a Count-Min Sketch (d rows x w cols of counters)."""
from typing import List  # noqa: F401


class CountMinSketch:
    def __init__(self, depth: int = 3, width: int = 50) -> None:
        # TODO: d x w table of zero counters
        pass

    def update(self, x: int, count: int = 1) -> None:
        # TODO: add count to one counter per row
        pass

    def estimate(self, x: int) -> int:
        # TODO: return the MIN counter across the d rows
        pass


if __name__ == "__main__":
    cms = CountMinSketch(3, 50)
    cms.update(5, 3)
    cms.update(7, 2)
    print(cms.estimate(5))  # expected: 3
    print(cms.estimate(7))  # expected: 2
    print(cms.estimate(9))  # expected: 0
