"""Bitwise-AND Stack — O(1) AND of all elements (design)."""


class AndStack:
    def __init__(self) -> None:
        # TODO: keep a stack of (value, and_so_far) pairs
        pass

    def push(self, x: int) -> None:
        # TODO: and_so_far = x & previous and_so_far
        pass

    def pop(self) -> None:
        # TODO
        pass

    def top(self) -> int:
        # TODO
        pass

    def andAll(self) -> int:
        # TODO: read the and field of the top pair
        pass


if __name__ == "__main__":
    st = AndStack()
    st.push(7)
    st.push(6)
    st.push(4)
    print(st.andAll())  # expected: 4
    print(st.top())  # expected: 4
    st.pop()
    print(st.andAll())  # expected: 6
    st.pop()
    print(st.andAll())  # expected: 7
    st.push(5)
    print(st.andAll())  # expected: 5
