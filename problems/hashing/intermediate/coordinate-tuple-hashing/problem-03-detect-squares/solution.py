"""Detect Squares — LeetCode 2013 (design)."""
from collections import defaultdict  # noqa: F401
from typing import List


class DetectSquares:
    def __init__(self) -> None:
        # TODO: hash point counts
        pass

    def add(self, point: List[int]) -> None:
        # TODO
        pass

    def count(self, point: List[int]) -> int:
        # TODO: for each diagonal corner, multiply the counts of the other 3
        pass


if __name__ == "__main__":
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    print(ds.count([11, 10]))  # expected: 1
    print(ds.count([14, 8]))  # expected: 0
    ds.add([11, 2])
    print(ds.count([11, 10]))  # expected: 2
