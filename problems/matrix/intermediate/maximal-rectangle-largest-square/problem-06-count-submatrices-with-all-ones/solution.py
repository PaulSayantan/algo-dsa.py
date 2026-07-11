from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """Count the number of all-1 submatrices in a binary matrix.

        Args:
            mat: An m x n grid where each cell is 0 or 1.

        Returns:
            The total number of axis-aligned rectangular submatrices (of any
            height and width) whose entries are all 1.

        Example:
            >>> Solution().numSubmat([[1,0,1]])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0],
    ]
    print(Solution().numSubmat(grid))  # Expected: 13
