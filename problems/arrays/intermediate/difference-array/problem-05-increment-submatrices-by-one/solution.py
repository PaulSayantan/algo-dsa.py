from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """Apply 2D range-increment queries to an n x n zero matrix.

        Each query [row1, col1, row2, col2] adds 1 to every cell in the
        submatrix bounded by top-left (row1, col1) and bottom-right (row2, col2),
        inclusive.

        Args:
            n: The dimension of the square matrix (n x n), initially all zeros.
            queries: A list of [row1, col1, row2, col2] submatrix increments.

        Returns:
            The n x n matrix after applying every query.

        Example:
            >>> Solution().rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]])
            [[1, 1, 0], [1, 2, 1], [0, 1, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]]))  # expected: [[1, 1, 0], [1, 2, 1], [0, 1, 1]]
    print(sol.rangeAddQueries(2, [[0, 0, 1, 1]]))                # expected: [[1, 1], [1, 1]]
