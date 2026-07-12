"""Design a stack that stays sorted with the smallest element on top."""
from typing import Optional


class SortedStack:
    def __init__(self) -> None:
        # TODO: keep one list ordered so the smallest value sits at the top
        pass

    def push(self, x: int) -> None:
        # TODO: pop smaller elements onto a temp stack, push x, restore
        pass

    def pop(self) -> Optional[int]:
        # TODO: remove and return the top (minimum), or None if empty
        pass

    def peek(self) -> Optional[int]:
        # TODO: return the top (minimum) without removing, or None if empty
        pass

    def isEmpty(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    st = SortedStack()
    st.push(5)
    st.push(2)
    st.push(8)
    print(st.peek())  # expected: 2
    st.push(1)
    print(st.peek())  # expected: 1
    st.pop()
    print(st.peek())  # expected: 2
    print(st.isEmpty())  # expected: False
    print(st.pop())  # expected: 2
    print(st.peek())  # expected: 5
