"""Front Middle Back Queue — non-destructive peek operations.

pushFront / pushMiddle / pushBack add an element; peekFront / peekMiddle /
peekBack return (WITHOUT removing) the value at that position, or -1 if empty.
When the size is even the "middle" is the FRONT of the two central positions.
"""


class FrontMiddleBackQueue:
    def __init__(self) -> None:
        # TODO: an ordered container of the elements
        pass

    def pushFront(self, val: int) -> None:
        # TODO
        pass

    def pushMiddle(self, val: int) -> None:
        # TODO: insert at index len // 2 so it lands on the front-middle
        pass

    def pushBack(self, val: int) -> None:
        # TODO
        pass

    def peekFront(self) -> int:
        # TODO: return index 0 without removing, or -1 if empty
        pass

    def peekMiddle(self) -> int:
        # TODO: return index (len - 1) // 2 without removing, or -1 if empty
        pass

    def peekBack(self) -> int:
        # TODO: return index -1 without removing, or -1 if empty
        pass


if __name__ == "__main__":
    q = FrontMiddleBackQueue()
    print(q.peekMiddle())  # expected: -1
    q.pushBack(1)
    q.pushBack(2)
    q.pushBack(3)
    q.pushBack(4)
    print(q.peekFront())  # expected: 1
    print(q.peekMiddle())  # expected: 2
    print(q.peekBack())  # expected: 4
    q.pushMiddle(9)
    print(q.peekMiddle())  # expected: 9
    q.pushFront(0)
    print(q.peekMiddle())  # expected: 2
    print(q.peekFront())  # expected: 0
