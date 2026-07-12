"""Same duality, driven from the LEFT end: stack via appendleft/popleft, queue via appendleft/pop."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def leftEndStack(self, values: List[int]) -> List[int]:
        # TODO: appendleft all, then popleft all -> LIFO (reversed)
        pass

    def frontToBackQueue(self, values: List[int]) -> List[int]:
        # TODO: appendleft all, then pop all -> FIFO (same order)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.leftEndStack([1, 2, 3]))  # expected: [3, 2, 1]
    print(sol.frontToBackQueue([1, 2, 3]))  # expected: [1, 2, 3]
    print(sol.leftEndStack([5, 5, 6]))  # expected: [6, 5, 5]
    print(sol.frontToBackQueue([7]))  # expected: [7]
