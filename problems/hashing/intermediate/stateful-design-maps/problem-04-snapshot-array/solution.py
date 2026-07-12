"""Snapshot Array — LeetCode 1146."""
from collections import defaultdict  # noqa: F401


class SnapshotArray:
    def __init__(self, length: int) -> None:
        # TODO: per-index history of (snap_id, value); a snapshot counter
        pass

    def set(self, index: int, val: int) -> None:
        # TODO
        pass

    def snap(self) -> int:
        # TODO: return the id of the snapshot just taken
        pass

    def get(self, index: int, snap_id: int) -> int:
        # TODO: value at the largest snap <= snap_id (default 0)
        pass


if __name__ == "__main__":
    sa = SnapshotArray(3)
    sa.set(0, 5)
    print(sa.snap())  # expected: 0
    sa.set(0, 6)
    print(sa.get(0, 0))  # expected: 5
    print(sa.get(0, 1) if False else sa.get(1, 0))  # expected: 0
    print(sa.snap())  # expected: 1
    print(sa.get(0, 1))  # expected: 6
