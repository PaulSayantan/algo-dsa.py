"""Daily Temperatures — LeetCode 739 (monotonic stack)."""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # TODO: decreasing stack of indices; a warmer day pops cooler ones
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(sol.dailyTemperatures([30, 40, 50, 60]))  # expected: [1, 1, 1, 0]
    print(sol.dailyTemperatures([30, 60, 90]))  # expected: [1, 1, 0]
    print(sol.dailyTemperatures([55]))  # expected: [0]
