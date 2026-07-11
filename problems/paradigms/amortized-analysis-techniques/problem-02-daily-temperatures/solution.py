"""LeetCode 739 - Daily Temperatures.

For each day, find how many days until a warmer temperature, using a monotonic
stack that yields O(n) total work by amortized analysis.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Return, for each day, the number of days to wait for a warmer one.

        Args:
            temperatures: Daily temperatures.

        Returns:
            A list ``answer`` where ``answer[i]`` is the number of days after day
            ``i`` until a strictly warmer temperature, or 0 if none exists.

        Example:
            >>> Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
            [1, 1, 4, 2, 1, 1, 0, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(sol.dailyTemperatures([30, 40, 50, 60]))
    # expected: [1, 1, 1, 0]
    print(sol.dailyTemperatures([90, 80, 70]))
    # expected: [0, 0, 0]
