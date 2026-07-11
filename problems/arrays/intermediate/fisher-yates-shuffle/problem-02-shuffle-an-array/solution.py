"""LeetCode 384 - Shuffle an Array.

Design a class supporting reset() (restore original) and shuffle()
(uniformly random permutation). Implement Fisher-Yates by hand.
"""
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        """Initialize with the array to shuffle.

        Args:
            nums: The original integer array (all elements unique).
        """
        # TODO: implement
        # Hint: store an immutable copy of the original so reset() can
        # always restore it, and a working copy that shuffle() rearranges.
        pass

    def reset(self) -> List[int]:
        """Reset the array to its original configuration and return it.

        Returns:
            The array in its original order.
        """
        # TODO: implement
        pass

    def shuffle(self) -> List[int]:
        """Return a uniformly random permutation of the array.

        Returns:
            A new arrangement of the elements; every one of the n! orderings
            is equally likely.

        Example:
            >>> obj = Solution([1, 2, 3])
            >>> sorted(obj.shuffle())
            [1, 2, 3]
        """
        # TODO: implement
        # Hint: Fisher-Yates on the working copy: for i from n-1 down to 1,
        # swap index i with a uniformly random index in [0, i].
        pass


if __name__ == "__main__":
    obj = Solution([1, 2, 3])
    print(sorted(obj.shuffle()))  # expected: [1, 2, 3] (same multiset, random order)
    print(obj.reset())            # expected: [1, 2, 3]
    print(sorted(obj.shuffle()))  # expected: [1, 2, 3] (same multiset, random order)
