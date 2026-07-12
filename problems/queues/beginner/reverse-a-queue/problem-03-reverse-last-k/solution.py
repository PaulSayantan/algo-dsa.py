"""Reverse only the last k elements of a queue, keeping the front in order."""
from typing import List  # noqa: F401


class Solution:
    def reverseLastK(self, q: List[int], k: int) -> List[int]:
        # TODO: keep the first len-k as-is, then push the last k onto a stack and pop them back
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseLastK([1, 2, 3, 4, 5], 3))  # expected: [1, 2, 5, 4, 3]
    print(sol.reverseLastK([10, 20, 30, 40], 2))  # expected: [10, 20, 40, 30]
    print(sol.reverseLastK([1, 2, 3], 0))  # expected: [1, 2, 3]
