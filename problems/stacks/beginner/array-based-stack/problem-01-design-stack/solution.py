"""Design a Stack (array-backed). Implement push/pop/top/empty in O(1)."""
from typing import Any  # noqa: F401


class MyStack:
    def __init__(self) -> None:
        # TODO: implement
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
    print(st.empty())  # expected: True
    st.push(1)
    st.push(2)
    print(st.top())  # expected: 2
    print(st.pop())  # expected: 2
    print(st.top())  # expected: 1
    print(st.empty())  # expected: False
