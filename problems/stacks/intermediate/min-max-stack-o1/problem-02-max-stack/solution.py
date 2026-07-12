"""Max Stack — LeetCode 716 (design)."""


class MaxStack:
    def __init__(self) -> None:
        # TODO
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

    def peekMax(self) -> int:
        # TODO
        pass

    def popMax(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    st = MaxStack()
    st.push(5)
    st.push(1)
    st.push(5)
    print(st.top())  # expected: 5
    print(st.popMax())  # expected: 5
    print(st.top())  # expected: 1
    print(st.peekMax())  # expected: 5
    print(st.pop())  # expected: 1
    print(st.top())  # expected: 5
