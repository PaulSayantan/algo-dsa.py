"""Fully-persistent deque keyed by version (design)."""


class PersistentDeque:
    def __init__(self) -> None:
        # TODO: versions[0] = empty
        pass

    def pushBack(self, v: int, x: int) -> int:
        # TODO
        pass

    def pushFront(self, v: int, x: int) -> int:
        # TODO
        pass

    def popFront(self, v: int) -> int:
        # TODO: return new version id (value peekable via front before)
        pass

    def front(self, v: int) -> int:
        # TODO
        pass

    def back(self, v: int) -> int:
        # TODO
        pass


if __name__ == "__main__":
    pd = PersistentDeque()
    v1 = pd.pushBack(0, 10)
    v2 = pd.pushBack(v1, 20)
    v3 = pd.pushFront(v2, 5)
    print(pd.front(v3))  # expected: 5
    print(pd.back(v3))  # expected: 20
    v4 = pd.popFront(v3)
    print(pd.front(v4))  # expected: 10
    print(pd.back(v2))  # expected: 20
    v5 = pd.pushBack(v1, 99)
    print(pd.back(v5))  # expected: 99
    print(pd.front(v5))  # expected: 10
