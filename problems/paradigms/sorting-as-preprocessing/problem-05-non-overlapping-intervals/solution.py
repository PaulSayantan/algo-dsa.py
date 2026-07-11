"""Non-overlapping Intervals — LeetCode 435.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Return the minimum number of intervals to remove to eliminate overlaps.

        Intervals that only touch at an endpoint (e.g. [1,2] and [2,3]) are NOT
        considered overlapping and may both remain.

        Args:
            intervals: A list of [start, end] intervals.

        Returns:
            The minimum count of intervals whose removal makes the rest
            non-overlapping.

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
