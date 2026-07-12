"""Validate Stack Sequences. Simulate an array-backed stack: push in order and
pop greedily whenever the top matches the next value to be popped."""
from typing import List  # noqa: F401


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # TODO: push each value; while top == popped[j], pop and advance j
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))  # expected: True
    print(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))  # expected: False
    print(sol.validateStackSequences([1, 2], [2, 1]))  # expected: True
    print(sol.validateStackSequences([1], [1]))  # expected: True
    print(sol.validateStackSequences([2, 1, 0], [0, 1, 2]))  # expected: True
