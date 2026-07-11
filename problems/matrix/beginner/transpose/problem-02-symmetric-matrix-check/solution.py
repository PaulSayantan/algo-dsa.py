from typing import List


class Solution:
    def isSymmetric(self, matrix: List[List[int]]) -> bool:
        """Return whether a square matrix equals its own transpose.

        A matrix M is symmetric iff M[i][j] == M[j][i] for all i, j.

        Args:
            matrix: An n x n grid of integers, n >= 1.

        Returns:
            True if the matrix is symmetric, False otherwise.

        Example:
            >>> Solution().isSymmetric([[1, 2], [2, 1]])
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isSymmetric([[1, 2, 3], [2, 4, 5], [3, 5, 6]]))
    # Expected: True
    print(sol.isSymmetric([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Expected: False
    print(sol.isSymmetric([[9]]))
    # Expected: True
