"""Count Negative Numbers in a Sorted Matrix (LeetCode 1351).

Fill in the body of ``countNegatives`` using Row/Column Traversal.
"""

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """Return how many cells of ``grid`` hold a negative value.

        Args:
            grid: An ``m x n`` matrix sorted non-increasingly along both rows
                and columns. Values lie in the range ``[-100, 100]``.

        Returns:
            The count of cells whose value is strictly less than 0.

        Example:
            >>> Solution().countNegatives([[3, 2], [1, 0]])
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    grid1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(sol.countNegatives(grid1))          # expected: 8
    print(sol.countNegatives([[3, 2], [1, 0]]))  # expected: 0
    print(sol.countNegatives([[-1]]))         # expected: 1
