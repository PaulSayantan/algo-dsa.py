"""Implement Stack using Queues — LeetCode 225 (design)."""
from collections import deque  # noqa: F401


class MyStack:
    def __init__(self) -> None:
        # TODO: a single queue with push-time rotation
        pass

    def push(self, x: int) -> None:
        # TODO
        pass

    def pop(self) -> int:
        # TODO
        pass

    def top(self) -> int:
        # TODO
        pass

    def empty(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    st = MyStack()
    st.push(1)
    st.push(2)
    print(st.top())  # expected: 2
    print(st.pop())  # expected: 2
    print(st.top())  # expected: 1
    print(st.empty())  # expected: False
    print(st.pop())  # expected: 1
    print(st.empty())  # expected: True
