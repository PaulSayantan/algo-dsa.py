"""Sliding Window Median — LeetCode 480."""
from typing import List
import bisect  # noqa: F401


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # TODO: keep the window sorted; read the middle
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # expected: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    print(sol.medianSlidingWindow([1, 2, 3, 4], 2))  # expected: [1.5, 2.5, 3.5]
    print(sol.medianSlidingWindow([5, 5, 8, 1, 4, 7, 1, 3, 8, 4], 8))  # expected: [4.5, 4.5, 4.0]
