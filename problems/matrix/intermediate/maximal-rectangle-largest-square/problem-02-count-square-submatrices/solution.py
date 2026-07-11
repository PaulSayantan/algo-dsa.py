from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """Count square submatrices that contain only 1s.

        Args:
            matrix: An m x n grid where each cell is 0 or 1.

        Returns:
            The total number of axis-aligned square submatrices (of any side
            length) whose entries are all 1.

        Example:
            >>> Solution().countSquares([[1,0,1],[1,1,0],[1,1,0]])
            7
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]
    print(Solution().countSquares(grid))  # Expected: 15
