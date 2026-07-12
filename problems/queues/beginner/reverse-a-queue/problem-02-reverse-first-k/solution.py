"""Reverse only the first k elements of a queue, keeping the rest in order."""
from typing import List  # noqa: F401


class Solution:
    def reverseFirstK(self, q: List[int], k: int) -> List[int]:
        # TODO: push the first k onto a stack, pop them back (reversed), then append the rest
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseFirstK([1, 2, 3, 4, 5], 3))  # expected: [3, 2, 1, 4, 5]
    print(sol.reverseFirstK([5, 3, 2, 1, 7, 10], 3))  # expected: [2, 3, 5, 1, 7, 10]
    print(sol.reverseFirstK([1, 2, 3], 0))  # expected: [1, 2, 3]
