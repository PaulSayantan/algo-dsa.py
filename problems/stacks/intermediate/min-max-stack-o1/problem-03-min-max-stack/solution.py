"""Min-Max Stack — O(1) getMin and getMax (design)."""


class MinMaxStack:
    def __init__(self) -> None:
        # TODO: keep a stack of (value, min_so_far, max_so_far) triples
        pass

    def push(self, x: int) -> None:
        # TODO: carry the running min and max forward
        pass

    def pop(self) -> None:
        # TODO
        pass

    def top(self) -> int:
        # TODO
        pass

    def getMin(self) -> int:
        # TODO: read the min field of the top triple
        pass

    def getMax(self) -> int:
        # TODO: read the max field of the top triple
        pass


if __name__ == "__main__":
    mms = MinMaxStack()
    mms.push(5)
    mms.push(1)
    mms.push(3)
    print(mms.getMin())  # expected: 1
    print(mms.getMax())  # expected: 5
    print(mms.top())  # expected: 3
    mms.pop()
    print(mms.getMax())  # expected: 5
    print(mms.getMin())  # expected: 1
    mms.pop()
    print(mms.getMin())  # expected: 5
    print(mms.getMax())  # expected: 5
    mms.push(-2)
    print(mms.getMin())  # expected: -2
    print(mms.getMax())  # expected: 5
