"""Count fixed-size windows whose range (max - min) exactly equals target."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def countExactRangeWindows(self, nums: List[int], k: int, target: int) -> int:
        # TODO: two monotonic deques; count windows where max - min == target
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countExactRangeWindows([4, 2, 7, 1, 1, 2], 2, 3))  # expected: 0
    print(sol.countExactRangeWindows([5, 3, 5, 3, 5], 2, 2))  # expected: 4
    print(sol.countExactRangeWindows([1, 3, -1, -3, 5, 3, 6, 7], 3, 4))  # expected: 2
    print(sol.countExactRangeWindows([1, 1, 1, 1], 2, 0))  # expected: 3
    print(sol.countExactRangeWindows([10, 2, 8], 3, 5))  # expected: 0
