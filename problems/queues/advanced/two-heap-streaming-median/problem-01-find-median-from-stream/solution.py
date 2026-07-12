"""Find Median from Data Stream — LeetCode 295 (design)."""
import heapq  # noqa: F401


class MedianFinder:
    def __init__(self) -> None:
        # TODO: two heaps (low max-heap, high min-heap)
        pass

    def addNum(self, num: int) -> None:
        # TODO
        pass

    def findMedian(self) -> float:
        # TODO
        pass


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # expected: 1.5
    mf.addNum(3)
    print(mf.findMedian())  # expected: 2.0
    mf.addNum(4)
    print(mf.findMedian())  # expected: 2.5
