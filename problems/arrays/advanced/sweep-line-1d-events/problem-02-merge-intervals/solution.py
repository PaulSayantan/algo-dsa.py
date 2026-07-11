"""Merge Intervals (LeetCode 56).

Fill in `Solution.merge` using a 1D sweep line over start/end events.
This file is an intentionally empty template — no working solution is provided.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge all overlapping (or touching) closed intervals.

        Model each closed interval [s, e] as a +1 event at s and a -1 event at e.
        Sweeping the events while tracking the number of open intervals, a merged
        output interval spans from the moment the open-count leaves 0 until it
        returns to 0. Because intervals are closed, starts must be processed
        before ends at equal coordinates so touching intervals fuse.

        Args:
            intervals: List of [start, end] closed intervals (start <= end).

        Returns:
            A list of non-overlapping intervals covering the same points,
            sorted by start coordinate.

        Example:
            >>> Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
            [[1, 6], [8, 10], [15, 18]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # expected: [[1, 6], [8, 10], [15, 18]]
    print(sol.merge([[1, 4], [4, 5]]))                     # expected: [[1, 5]]
    print(sol.merge([[1, 4], [2, 3]]))                     # expected: [[1, 4]]
