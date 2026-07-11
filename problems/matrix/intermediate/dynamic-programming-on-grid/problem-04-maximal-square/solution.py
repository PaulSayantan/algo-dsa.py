"""Maximal Square — LeetCode 221.

Return the area of the largest square containing only '1's inside a binary
matrix whose entries are the characters '0' and '1'.
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """Return the area of the largest all-ones square submatrix.

        Args:
            matrix: An m x n grid whose entries are the characters '0' or '1'.

        Returns:
            The area (side length squared) of the largest square that
            contains only '1' entries. Returns 0 if there are no '1's.

        Example:
            >>> Solution().maximalSquare(
            ...     [["1", "0", "1", "0", "0"],
            ...      ["1", "0", "1", "1", "1"],
            ...      ["1", "1", "1", "1", "1"],
            ...      ["1", "0", "0", "1", "0"]]
            ... )
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.maximalSquare(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
    )  # expected: 4
    print(sol.maximalSquare([["0", "1"], ["1", "0"]]))  # expected: 1
    print(sol.maximalSquare([["0"]]))  # expected: 0
