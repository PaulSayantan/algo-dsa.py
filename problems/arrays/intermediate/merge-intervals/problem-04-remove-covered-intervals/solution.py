"""Remove Covered Intervals (LeetCode 1288).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """Count intervals remaining after removing all covered intervals.

        An interval ``[a, b]`` is covered by ``[c, d]`` when ``c <= a`` and
        ``b <= d``.

        Args:
            intervals: A list of closed intervals ``[l, r]``.

        Returns:
            The number of intervals that are not covered by any other interval.

        Example:
            >>> Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]])
            2
            >>> Solution().removeCoveredIntervals([[1, 4], [2, 3]])
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))  # expected: 2
    print(sol.removeCoveredIntervals([[1, 4], [2, 3]]))          # expected: 1
    print(sol.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))  # expected: 1
