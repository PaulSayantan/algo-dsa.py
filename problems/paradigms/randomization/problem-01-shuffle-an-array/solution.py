"""LeetCode 384 - Shuffle an Array.

Design a class that can return the original array and uniformly random shuffles of it.
Solve this with the Fisher-Yates (Knuth) shuffle.
"""

from __future__ import annotations

import random
from typing import List


class Solution:
    """Return uniformly random permutations of an integer array."""

    def __init__(self, nums: List[int]) -> None:
        """Initialize the object with the array to be shuffled.

        Args:
            nums: The integer array. Elements are unique.
        """
        # TODO: store the original array (and a working copy for shuffling)
        pass

    def reset(self) -> List[int]:
        """Reset the array to its original configuration and return it.

        Returns:
            The array in its original construction order.

        Example:
            >>> s = Solution([1, 2, 3])
            >>> _ = s.shuffle()
            >>> s.reset()
            [1, 2, 3]
        """
        # TODO: implement
        pass

    def shuffle(self) -> List[int]:
        """Return a uniformly random permutation of the array.

        Every one of the n! orderings must be equally likely, and successive
        calls must be independent.

        Returns:
            A random permutation of the original array.

        Example:
            >>> s = Solution([1, 2, 3])
            >>> perm = s.shuffle()      # e.g. [3, 1, 2]
            >>> sorted(perm)
            [1, 2, 3]
        """
        # TODO: implement (Fisher-Yates)
        pass


if __name__ == "__main__":
    obj = Solution([1, 2, 3])
    print(obj.shuffle())  # some permutation of [1, 2, 3]
    print(obj.reset())    # expected: [1, 2, 3]
    print(obj.shuffle())  # another (independent) permutation of [1, 2, 3]
