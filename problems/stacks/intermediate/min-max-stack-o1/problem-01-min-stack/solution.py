"""Min Stack — LeetCode 155 (design)."""


class MinStack:
    def __init__(self) -> None:
        # TODO
        pass

    def push(self, val: int) -> None:
        # TODO
        pass

    def pop(self) -> None:
        # TODO
        pass

    def top(self) -> int:
        # TODO
        pass

    def getMin(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())  # expected: -3
    ms.pop()
    print(ms.top())  # expected: 0
    print(ms.getMin())  # expected: -2
