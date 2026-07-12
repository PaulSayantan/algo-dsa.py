"""Two-Queue Stack (push-efficient): O(1) push, O(n) pop/top via two queues."""
from collections import deque  # noqa: F401


class MyStack:
    def __init__(self) -> None:
        # TODO: two queues; push enqueues, pop/top drain-and-swap
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
    st.push(3)
    st.push(5)
    st.push(7)
    print(st.top())  # expected: 7
    print(st.pop())  # expected: 7
    print(st.top())  # expected: 5
    st.push(9)
    print(st.pop())  # expected: 9
    print(st.pop())  # expected: 5
    print(st.pop())  # expected: 3
    print(st.empty())  # expected: True
