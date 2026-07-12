"""Per-window (max + min) via two monotonic deques."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def windowMaxPlusMin(self, nums: List[int], k: int) -> List[int]:
        # TODO: run a max-deque and a min-deque together; emit max + min per window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.windowMaxPlusMin([4, 2, 7, 1], 2))  # expected: [6, 9, 8]
    print(sol.windowMaxPlusMin([1, 3, -1, -3, 5, 3, 6, 7], 3))  # expected: [2, 0, 2, 2, 9, 10]
    print(sol.windowMaxPlusMin([5, 5, 5], 2))  # expected: [10, 10]
    print(sol.windowMaxPlusMin([10, 2, 8], 3))  # expected: [12]
    print(sol.windowMaxPlusMin([2, 1, 4, 3], 1))  # expected: [4, 2, 8, 6]
