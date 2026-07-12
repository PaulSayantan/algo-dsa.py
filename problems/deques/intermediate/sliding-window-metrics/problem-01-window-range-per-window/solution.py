"""Per-window range (max - min) via two monotonic deques."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def windowRanges(self, nums: List[int], k: int) -> List[int]:
        # TODO: run a max-deque and a min-deque together; emit max - min per window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.windowRanges([1, 3, -1, -3, 5, 3, 6, 7], 3))  # expected: [4, 6, 8, 8, 3, 4]
    print(sol.windowRanges([4, 2, 7, 1], 2))  # expected: [2, 5, 6]
    print(sol.windowRanges([5, 5, 5], 2))  # expected: [0, 0]
    print(sol.windowRanges([10, 2, 8], 3))  # expected: [8]
