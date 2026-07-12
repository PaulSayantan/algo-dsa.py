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
    print(q.popMiddle())  # expected: -1
    q.pushMiddle(10)
    q.pushMiddle(20)
    q.pushFront(5)
    q.pushBack(30)
    print(q.popMiddle())  # expected: 20
    print(q.popFront())  # expected: 5
    q.pushMiddle(15)
    print(q.popBack())  # expected: 30
    print(q.popMiddle())  # expected: 10
    print(q.popMiddle())  # expected: 15
    print(q.popBack())  # expected: -1
