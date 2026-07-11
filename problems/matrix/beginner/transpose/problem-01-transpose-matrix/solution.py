from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """Return the transpose of a (possibly rectangular) matrix.

        The transpose of an m x n matrix is the n x m matrix whose entry at
        (i, j) equals the original entry at (j, i).

        Args:
            matrix: An m x n grid of integers, m, n >= 1.

        Returns:
            The transposed n x m grid, a brand-new list of lists.

        Example:
            >>> Solution().transpose([[1, 2, 3], [4, 5, 6]])
            [[1, 4], [2, 5], [3, 6]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(sol.transpose([[1, 2, 3], [4, 5, 6]]))
    # Expected: [[1, 4], [2, 5], [3, 6]]
    print(sol.transpose([[7]]))
    # Expected: [[7]]
