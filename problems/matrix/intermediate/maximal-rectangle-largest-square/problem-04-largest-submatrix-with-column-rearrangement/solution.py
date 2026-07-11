from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """Return the largest all-1 submatrix area when columns may be reordered.

        Args:
            matrix: An m x n grid of 0s and 1s. Columns may be permuted freely.

        Returns:
            The maximum area of a submatrix consisting entirely of 1s, achievable
            by choosing the best permutation of the columns.

        Example:
            >>> Solution().largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]])
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
    ]
    print(Solution().largestSubmatrix(grid))  # Expected: 4
