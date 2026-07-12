"""Partially-retroactive stack (replay model) (design)."""


class RetroStack:
    def __init__(self) -> None:
        # TODO: store (time, seq, kind, value) ops
        pass

    def insertPush(self, t: int, x: int) -> None:
        # TODO
        pass

    def insertPop(self, t: int) -> None:
        # TODO
        pass

    def top(self) -> int:
        # TODO: replay timeline in time order; return current top or -1
        pass


if __name__ == "__main__":
    rs = RetroStack()
    rs.insertPush(10, 1)
    rs.insertPush(20, 2)
    print(rs.top())  # expected: 2
    rs.insertPush(15, 5)
    print(rs.top())  # expected: 2
    rs.insertPop(25)
    print(rs.top())  # expected: 5
    rs.insertPop(5)
    print(rs.top())  # expected: 5
