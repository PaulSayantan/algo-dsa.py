"""Daily Temperatures — LeetCode 739.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Compute, for each day, how many days until a strictly warmer day.

        Args:
            temperatures: Daily temperatures, one integer per day.

        Returns:
            A list ``answer`` of the same length where ``answer[i]`` is the number
            of days after day ``i`` until a warmer temperature occurs, or ``0`` if
            no warmer day exists after day ``i``.

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
    print(sol.dailyTemperatures([30, 40, 50, 60]))  # expected: [1, 1, 1, 0]
    print(sol.dailyTemperatures([90, 60, 60, 90]))  # expected: [0, 2, 1, 0]
