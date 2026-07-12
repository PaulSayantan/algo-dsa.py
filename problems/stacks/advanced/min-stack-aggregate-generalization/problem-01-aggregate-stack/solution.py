"""Stack with O(1) min/max/gcd over all elements (design)."""
from math import gcd  # noqa: F401


class AggregateStack:
    def __init__(self) -> None:
        # TODO: each frame carries (value, min, max, gcd)
        pass

    def push(self, x: int) -> None:
        # TODO
        pass

    def pop(self) -> None:
        # TODO
        pass

    def getMin(self) -> int:
        # TODO
        pass

    def getMax(self) -> int:
        # TODO
        pass

    def getGcd(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    st = AggregateStack()
    st.push(12)
    st.push(18)
    print(st.getMin())  # expected: 12
    print(st.getMax())  # expected: 18
    print(st.getGcd())  # expected: 6
    st.push(4)
    print(st.getMin())  # expected: 4
    print(st.getGcd())  # expected: 2
    st.pop()
    print(st.getGcd())  # expected: 6
    print(st.getMax())  # expected: 18
