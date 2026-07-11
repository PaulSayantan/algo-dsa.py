"""Map of Highest Peak — LeetCode 1765.

Empty solution template. Fill in `highestPeak`.
"""

from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """Assign heights maximizing the tallest peak, returning the height matrix.

        Rules: water cells (isWater == 1) must have height 0, every height is
        non-negative, and 4-directionally adjacent cells differ by at most 1. Under
        these rules the maximal height of any cell equals its distance to the nearest
        water cell.

        Args:
            isWater: An m x n matrix; 1 marks a water cell, 0 marks a land cell, with
                at least one water cell present.

        Returns:
            An m x n matrix of non-negative heights satisfying all rules and
            maximizing the maximum height. Any valid optimal assignment is accepted.

        Example:
            >>> Solution().highestPeak([[0, 1], [0, 0]])
            [[1, 0], [2, 1]]
        """
        # TODO: implement using Multi-Source BFS.
        pass


if __name__ == "__main__":
    print(Solution().highestPeak([[0, 1], [0, 0]]))
    # Expected: [[1, 0], [2, 1]]
    print(Solution().highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
    # Expected: [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
