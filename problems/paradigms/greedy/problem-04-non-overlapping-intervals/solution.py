"""Non-overlapping Intervals — LeetCode 435.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Return the minimum number of intervals to remove to make the rest disjoint.

        Intervals that touch only at an endpoint (e.g. [1, 2] and [2, 3]) are
        considered non-overlapping.

        Args:
            intervals: List of [start, end] pairs with start < end.

        Returns:
            The minimum count of intervals to remove so no two remaining overlap.

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
