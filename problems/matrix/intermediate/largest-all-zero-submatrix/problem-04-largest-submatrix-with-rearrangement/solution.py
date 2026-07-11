"""Largest Submatrix With Rearrangements (LeetCode 1727).

Columns may be reordered freely; return the area of the largest all-1
submatrix. Empty solution template — fill in the logic yourself.
"""

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """Return the largest all-1 submatrix area allowing column reorder.

        Args:
            matrix: An m x n binary matrix of 0s and 1s.

        Returns:
            The maximum number of cells in an all-1 rectangle obtainable
            after optionally permuting the columns.

        Example:
            >>> Solution().largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]])
            4
        """
        # TODO: implement.
        # Hint: turn each column into consecutive-1 heights ending at the row,
        # then (because columns can be reordered) sort each row's heights
        # descending and take max((k + 1) * heights_sorted[k]).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestSubmatrix([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1]]))     # expected: 4
    print(sol.largestSubmatrix([[1, 0, 1, 0, 1]]))  # expected: 3
    print(sol.largestSubmatrix([[1, 1, 0],
                                [1, 0, 1]]))     # expected: 2
