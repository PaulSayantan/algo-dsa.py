"""Persistent functional deque (two-list representation) (design)."""


class FunctionalDeque:
    def __init__(self) -> None:
        # TODO: versions[0] = (front=(), back=())
        pass

    def pushFront(self, v: int, x: int) -> int:
        # TODO: return new version id
        pass

    def pushBack(self, v: int, x: int) -> int:
        # TODO: return new version id
        pass

    def front(self, v: int) -> int:
        # TODO
        pass

    def back(self, v: int) -> int:
        # TODO
        pass


if __name__ == "__main__":
    fd = FunctionalDeque()
    v1 = fd.pushBack(0, 1)
    v2 = fd.pushBack(v1, 2)
    v3 = fd.pushFront(v2, 0)
    print(fd.front(v3))  # expected: 0
    print(fd.back(v3))  # expected: 2
    print(fd.front(v2))  # expected: 1
    print(fd.back(v1))  # expected: 1
    v4 = fd.pushFront(v3, -5)
    print(fd.front(v4))  # expected: -5
    print(fd.back(v4))  # expected: 2
