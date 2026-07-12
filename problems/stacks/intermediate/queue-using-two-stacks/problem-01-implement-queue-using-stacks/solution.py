"""Implement Queue using Stacks — LeetCode 232 (design)."""


class MyQueue:
    def __init__(self) -> None:
        # TODO: two stacks
        pass

    def push(self, x: int) -> None:
        # TODO
        pass

    def pop(self) -> int:
        # TODO
        pass

    def peek(self) -> int:
        # TODO
        pass

    def empty(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())  # expected: 1
    print(q.pop())  # expected: 1
    print(q.empty())  # expected: False
    q.push(3)
    print(q.pop())  # expected: 2
    print(q.pop())  # expected: 3
    print(q.empty())  # expected: True
