"""Design Front Middle Back Queue — LeetCode 1670.

pushFront / pushMiddle / pushBack add an element; popFront / popMiddle / popBack
remove and return one (or -1 if empty). When the size is even the "middle" is the
FRONT of the two central positions.
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

    def popFront(self) -> int:
        # TODO
        pass

    def popMiddle(self) -> int:
        # TODO: remove index (len - 1) // 2 (front of the two middles when even)
        pass

    def popBack(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    q.pushBack(2)
    q.pushMiddle(3)
    q.pushMiddle(4)
    print(q.popFront())  # expected: 1
    print(q.popMiddle())  # expected: 3
    print(q.popMiddle())  # expected: 4
    print(q.popBack())  # expected: 2
    print(q.popFront())  # expected: -1
