"""Time Based Key-Value Store — LeetCode 981."""
from collections import defaultdict  # noqa: F401


class TimeMap:
    def __init__(self) -> None:
        # TODO: key -> list of (timestamp, value), timestamps increasing
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        # TODO
        pass

    def get(self, key: str, timestamp: int) -> str:
        # TODO: binary-search the largest timestamp <= query; "" if none
        pass


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))  # expected: 'bar'
    print(tm.get("foo", 3))  # expected: 'bar'
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))  # expected: 'bar2'
    print(tm.get("foo", 5))  # expected: 'bar2'
    print(tm.get("foo", 0))  # expected: ''
