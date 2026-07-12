"""Persistent (immutable) stack keyed by version id (design)."""


class PersistentStack:
    def __init__(self) -> None:
        # TODO: version 0 is empty; store head node per version
        pass

    def push(self, version: int, x: int) -> int:
        # TODO: return the new version id
        pass

    def pop(self, version: int) -> int:
        # TODO: return the new version id (value discarded here)
        pass

    def top(self, version: int) -> int:
        # TODO
        pass

    def empty(self, version: int) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    ps = PersistentStack()
    v1 = ps.push(0, 10)
    v2 = ps.push(v1, 20)
    v3 = ps.push(v1, 30)
    print(ps.top(v2))  # expected: 20
    print(ps.top(v3))  # expected: 30
    print(ps.top(v1))  # expected: 10
    v4 = ps.pop(v2)
    print(ps.top(v4))  # expected: 10
    print(ps.empty(v4))  # expected: False
    print(ps.empty(0))  # expected: True
