"""Lucky Numbers in a Matrix (LeetCode 1380).

Fill in the body of ``luckyNumbers`` using Row/Column Traversal.
"""

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """Return every value that is its row's minimum and its column's maximum.

        Args:
            matrix: An ``m x n`` matrix of distinct positive integers.

        Returns:
            A list of all lucky numbers (row-min and column-max simultaneously),
            in any order. There is at most one such number.

        Example:
            >>> Solution().luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]])
            [15]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))       # expected: [15]
    print(sol.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))  # expected: [12]
    print(sol.luckyNumbers([[7, 8], [1, 2]]))                             # expected: [7]
