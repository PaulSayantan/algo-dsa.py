"""Kth Largest Element in a Stream — LeetCode 703.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]) -> None:
        """Initialize the tracker with target rank k and an initial stream.

        Args:
            k: The rank to report on each add (1 = largest, 2 = second largest, ...).
            nums: The initial stream of integers (may be empty).
        """
        # TODO: implement
        pass

    def add(self, val: int) -> int:
        """Append val to the stream and return the current kth largest element.

        Args:
            val: The new value entering the stream.

        Returns:
            The kth largest element considering all values added so far.

        Example:
            >>> kl = KthLargest(3, [4, 5, 8, 2])
            >>> kl.add(3)
            4
            >>> kl.add(5)
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    print(kl.add(3))   # expected: 4
    print(kl.add(5))   # expected: 5
    print(kl.add(10))  # expected: 5
    print(kl.add(9))   # expected: 8
    print(kl.add(4))   # expected: 8
