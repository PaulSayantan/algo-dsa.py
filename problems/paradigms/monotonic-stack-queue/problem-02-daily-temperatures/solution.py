"""Daily Temperatures — LeetCode 739.

Fill in the body of `dailyTemperatures`. Do not modify the signature.
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Return, for each day, how many days until a strictly warmer temperature.

        Args:
            temperatures: A list of daily temperatures.

        Returns:
            A list `answer` where `answer[i]` is the number of days after day `i`
            until a strictly warmer day, or 0 if no warmer day exists.

        Example:
            >>> Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
            [1, 1, 4, 2, 1, 1, 0, 0]
        """
        # TODO: implement using a monotonic stack of indices (non-increasing temps).
        # On a warmer day, pop resolved indices and record the index distance.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(sol.dailyTemperatures([30, 40, 50, 60]))
    # expected: [1, 1, 1, 0]
