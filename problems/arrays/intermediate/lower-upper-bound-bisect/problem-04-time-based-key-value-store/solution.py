"""Time Based Key-Value Store (LeetCode 981).

Design a store that keeps multiple timestamped values per key and, on lookup,
returns the value with the largest timestamp <= the query timestamp.
"""


class TimeMap:
    def __init__(self) -> None:
        """Initialize the data structure.

        Suggested internal state: a dict mapping each key to a pair of parallel
        lists (sorted timestamps, corresponding values). Since set() is called
        with strictly increasing timestamps per key, appends keep them sorted.
        """
        # TODO: implement
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Store `value` under `key` at time `timestamp`.

        Args:
            key: The key to store under.
            value: The value to associate with (key, timestamp).
            timestamp: A positive integer time; strictly increasing per key.

        Returns:
            None.
        """
        # TODO: implement
        pass

    def get(self, key: str, timestamp: int) -> str:
        """Return the value with the largest stored timestamp <= `timestamp`.

        Args:
            key: The key to look up.
            timestamp: The query time.

        Returns:
            The value set at the largest timestamp <= `timestamp` for `key`,
            or "" if no such value exists.

        Example:
            >>> tm = TimeMap()
            >>> tm.set("foo", "bar", 1)
            >>> tm.get("foo", 3)
            'bar'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))   # expected: "bar"
    print(tm.get("foo", 3))   # expected: "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))   # expected: "bar2"
    print(tm.get("foo", 5))   # expected: "bar2"
    print(tm.get("foo", 0))   # expected: "" (nothing set at or before t=0)
