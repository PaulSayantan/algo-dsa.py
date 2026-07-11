"""Merge Intervals (LeetCode 56).

Merge all overlapping intervals and return the consolidated, non-overlapping set.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge overlapping intervals.

        Args:
            intervals: A list of ``[start, end]`` pairs with ``start <= end``.
                Intervals that touch at an endpoint are considered overlapping.

        Returns:
            A list of merged, non-overlapping ``[start, end]`` intervals, sorted by
            start time.

        Example:
            >>> Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
            [[1, 6], [8, 10], [15, 18]]
            >>> Solution().merge([[1, 4], [4, 5]])
            [[1, 5]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # expected: [[1, 6], [8, 10], [15, 18]]
    print(sol.merge([[1, 4], [4, 5]]))                     # expected: [[1, 5]]
    print(sol.merge([[1, 4], [0, 4]]))                     # expected: [[0, 4]]
