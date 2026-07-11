"""Non-overlapping Intervals (LeetCode 435).

Return the minimum number of intervals to remove so the rest do not overlap.
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Count the minimum removals needed to make intervals non-overlapping.

        Args:
            intervals: A list of ``[start, end]`` pairs with ``start < end``.
                Intervals that only touch at an endpoint are NOT overlapping.

        Returns:
            The minimum number of intervals that must be removed.

        Example:
            >>> Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
            1
            >>> Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # expected: 1
    print(sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))          # expected: 2
    print(sol.eraseOverlapIntervals([[1, 2], [2, 3]]))                  # expected: 0
