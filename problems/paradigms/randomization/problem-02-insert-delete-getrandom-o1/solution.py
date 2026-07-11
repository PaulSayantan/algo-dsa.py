"""LeetCode 380 - Insert Delete GetRandom O(1).

Design a set supporting insert, remove, and uniform-random access, each in average O(1).
Combine a dynamic array (for O(1) uniform sampling by index) with a value -> index hash map
(for O(1) deletion via swap-with-last).
"""

from __future__ import annotations

import random


class RandomizedSet:
    """A set with average O(1) insert, remove, and uniform getRandom."""

    def __init__(self) -> None:
        """Initialize an empty randomized set."""
        # TODO: set up the backing array and the value -> index map
        pass

    def insert(self, val: int) -> bool:
        """Insert val if not already present.

        Args:
            val: The value to insert.

        Returns:
            True if val was newly inserted, False if it was already present.

        Example:
            >>> rs = RandomizedSet()
            >>> rs.insert(1)
            True
            >>> rs.insert(1)
            False
        """
        # TODO: implement
        pass

    def remove(self, val: int) -> bool:
        """Remove val if present (swap with last element to keep O(1)).

        Args:
            val: The value to remove.

        Returns:
            True if val was present and removed, False otherwise.

        Example:
            >>> rs = RandomizedSet()
            >>> rs.insert(1)
            True
            >>> rs.remove(1)
            True
            >>> rs.remove(1)
            False
        """
        # TODO: implement
        pass

    def getRandom(self) -> int:
        """Return a uniformly random element currently in the set.

        Returns:
            An element chosen uniformly at random. Guaranteed non-empty when called.

        Example:
            >>> rs = RandomizedSet()
            >>> rs.insert(42)
            True
            >>> rs.getRandom()
            42
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    rs = RandomizedSet()
    print(rs.insert(1))     # expected: True
    print(rs.remove(2))     # expected: False
    print(rs.insert(2))     # expected: True
    print(rs.getRandom())   # expected: 1 or 2, uniformly at random
    print(rs.remove(1))     # expected: True
    print(rs.insert(2))     # expected: False
    print(rs.getRandom())   # expected: 2 (only element left)
