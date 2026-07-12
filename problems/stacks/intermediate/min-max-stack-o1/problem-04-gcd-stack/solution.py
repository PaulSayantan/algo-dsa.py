"""GCD Stack — O(1) gcd of all elements (design)."""
import math


class GCDStack:
    def __init__(self) -> None:
        # TODO: keep a stack of (value, gcd_so_far) pairs
        pass

    def push(self, x: int) -> None:
        # TODO: gcd_so_far = gcd(x, previous gcd_so_far)
        pass

    def pop(self) -> None:
        # TODO
        pass

    def top(self) -> int:
        # TODO
        pass

    def gcd(self) -> int:
        # TODO: read the gcd field of the top pair
        pass


if __name__ == "__main__":
    gs = GCDStack()
    gs.push(12)
    gs.push(18)
    print(gs.gcd())  # expected: 6
    gs.push(9)
    print(gs.gcd())  # expected: 3
    print(gs.top())  # expected: 9
    gs.pop()
    print(gs.gcd())  # expected: 6
    gs.push(4)
    print(gs.gcd())  # expected: 2
    gs.pop()
    gs.pop()
    print(gs.gcd())  # expected: 12
