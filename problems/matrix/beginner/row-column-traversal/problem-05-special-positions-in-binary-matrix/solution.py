"""Special Positions in a Binary Matrix (LeetCode 1582).

Fill in the body of ``numSpecial`` using Row/Column Traversal.
"""

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """Count cells that hold the only 1 in both their row and their column.

        Args:
            mat: An ``m x n`` binary matrix; each entry is 0 or 1.

        Returns:
            The number of special positions: cells equal to 1 whose row sum and
            column sum are both exactly 1.

        Example:
            >>> Solution().numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]])
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))  # expected: 1
    print(sol.numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # expected: 3
    mat = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(sol.numSpecial(mat))                                # expected: 2
