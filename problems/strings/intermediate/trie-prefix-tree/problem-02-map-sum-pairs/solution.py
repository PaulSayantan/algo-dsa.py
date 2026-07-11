"""LeetCode 677 - Map Sum Pairs.

A key-value store that can return the sum of values over all keys sharing a prefix.
"""
from __future__ import annotations


class MapSum:
    """Prefix-sum map: insert key/value pairs, query sums by prefix.

    Example:
        >>> m = MapSum()
        >>> m.insert("apple", 3)
        >>> m.sum("ap")          # 3
        >>> m.insert("app", 2)
        >>> m.sum("ap")          # 5
    """

    def __init__(self) -> None:
        """Initialize an empty map-sum structure."""
        # TODO: implement
        pass

    def insert(self, key: str, val: int) -> None:
        """Insert or overwrite ``key`` with value ``val``.

        Args:
            key: The lowercase string key.
            val: The integer value associated with the key. If the key already
                exists its value is replaced (not accumulated).

        Returns:
            None. The structure is mutated in place.
        """
        # TODO: implement
        pass

    def sum(self, prefix: str) -> int:
        """Return the sum of values of every key beginning with ``prefix``.

        Args:
            prefix: The prefix to aggregate over.

        Returns:
            The integer sum of the current values of all matching keys; 0 if none.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    m = MapSum()
    m.insert("apple", 3)
    print(m.sum("ap"))     # expected: 3
    m.insert("app", 2)
    print(m.sum("ap"))     # expected: 5
    m.insert("apple", 7)   # overwrite apple 3 -> 7
    print(m.sum("ap"))     # expected: 9  (apple=7 + app=2)
