"""Minimum Number of Arrows to Burst Balloons (LeetCode 452).

Find the fewest vertical arrows needed so every balloon interval is hit.
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Return the minimum number of arrows that burst every balloon.

        Args:
            points: A list of ``[x_start, x_end]`` balloon intervals with
                ``x_start < x_end``. An arrow at ``x`` bursts a balloon when
                ``x_start <= x <= x_end`` (endpoints included).

        Returns:
            The minimum number of arrows required.

        Example:
            >>> Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
            2
            >>> Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # expected: 2
    print(sol.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))     # expected: 4
    print(sol.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))     # expected: 2
