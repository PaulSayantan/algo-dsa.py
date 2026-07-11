from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """Return the area of the largest all-'1' square in a binary matrix.

        Args:
            matrix: An m x n grid where each cell is the character '0' or '1'.

        Returns:
            The area (side length squared) of the largest square that contains
            only '1' characters. Returns 0 if the matrix has no '1'.

        Example:
            >>> Solution().maximalSquare([["1","0"],["1","1"]])
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(Solution().maximalSquare(grid))  # Expected: 4
