"""Teemo Attacking (LeetCode 495).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """Return the total number of seconds Ashe is poisoned.

        Each attack at second ``t`` poisons the half-open window
        ``[t, t + duration)``. Overlapping/refreshing windows should be
        merged so time is not double-counted.

        Args:
            timeSeries: Non-decreasing attack times.
            duration: How many seconds a single attack poisons for.

        Returns:
            The total length of the union of all poison windows.

        Example:
            >>> Solution().findPoisonedDuration([1, 4], 2)
            4
            >>> Solution().findPoisonedDuration([1, 2], 2)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPoisonedDuration([1, 4], 2))       # expected: 4
    print(sol.findPoisonedDuration([1, 2], 2))       # expected: 3
    print(sol.findPoisonedDuration([0, 5, 10], 3))   # expected: 9
