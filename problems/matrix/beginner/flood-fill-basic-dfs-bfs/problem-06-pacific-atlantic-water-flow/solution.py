"""Pacific Atlantic Water Flow — LeetCode 417.

Fill in the body of `pacificAtlantic`. Do not hard-code answers; implement the
traversal so it works for any valid input.
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """Find cells from which water can reach both oceans.

        The Pacific borders the top and left edges; the Atlantic borders the
        bottom and right edges. Water flows from a cell to a 4-directional
        neighbor whose height is <= the current cell's height.

        Args:
            heights: An m x n matrix of non-negative cell heights.

        Returns:
            A list of [row, col] coordinates (in any order) for every cell
            that can drain to both the Pacific and the Atlantic oceans.

        Example:
            heights = [[1,2,2],
                       [3,2,3],
                       [2,4,5]]
            -> cells reaching both oceans (order may vary)
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    h = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(sorted(sol.pacificAtlantic(h)))
    # Expected (order independent):
    # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
