from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """Return the area of the largest all-'1' rectangle in a binary matrix.

        Args:
            matrix: A rows x cols grid where each cell is the character
                '0' or '1'.

        Returns:
            The area of the largest axis-aligned rectangle whose cells are all
            '1'. Returns 0 if the matrix contains no '1'.

        Example:
            >>> Solution().maximalRectangle([["1","1"],["1","1"]])
            4
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
    print(Solution().maximalRectangle(grid))  # Expected: 6
