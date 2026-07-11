"""Kth Largest Element in a Stream (LeetCode 703).

Fill in the class below. Do NOT sort the whole stream on every call — maintain a
size-k min-heap so `add` runs in O(log k).
"""

from typing import List


class KthLargest:
    """Streaming structure that reports the k-th largest element seen so far.

    Example:
        obj = KthLargest(3, [4, 5, 8, 2])
        obj.add(3)   # -> 4
        obj.add(5)   # -> 5
        obj.add(10)  # -> 5
        obj.add(9)   # -> 8
        obj.add(4)   # -> 8
    """

    def __init__(self, k: int, nums: List[int]) -> None:
        """Initialize with the target rank k and an initial stream.

        Args:
            k: The rank (1-indexed) of the largest element to report.
            nums: The initial batch of integers in the stream (may be empty).
        """
        # TODO: implement
        pass

    def add(self, val: int) -> int:
        """Append `val` to the stream and return the current k-th largest value.

        Args:
            val: The next integer arriving in the stream.

        Returns:
            The k-th largest element among all integers seen so far.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))   # expected: 4
    print(obj.add(5))   # expected: 5
    print(obj.add(10))  # expected: 5
    print(obj.add(9))   # expected: 8
    print(obj.add(4))   # expected: 8
