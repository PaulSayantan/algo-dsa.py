"""Count fixed-size windows whose range (max - min) <= threshold."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def countStableWindows(self, nums: List[int], k: int, threshold: int) -> int:
        # TODO: two monotonic deques; count windows where max - min <= threshold
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countStableWindows([1, 3, -1, -3, 5, 3, 6, 7], 3, 4))  # expected: 3
    print(sol.countStableWindows([4, 2, 7, 1, 1, 2], 2, 3))  # expected: 3
    print(sol.countStableWindows([1, 1, 1, 1], 2, 0))  # expected: 3
    print(sol.countStableWindows([10, 2, 8], 3, 5))  # expected: 0
