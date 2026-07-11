from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        """Compute the per-cell diagonal distinct-value difference matrix.

        For each cell ``(r, c)`` on its main (``\\``) diagonal, let ``topLeft``
        be the count of distinct values strictly above-left and
        ``bottomRight`` be the count of distinct values strictly below-right.
        The answer for that cell is ``abs(topLeft - bottomRight)``.

        Args:
            grid: An ``m x n`` matrix of integers with ``m, n >= 1``.

        Returns:
            An ``m x n`` matrix ``answer`` where ``answer[r][c]`` is the
            absolute difference of distinct-value counts on ``(r, c)``'s
            main diagonal.

        Example:
            >>> Solution().differenceOfDistinctValues(
            ...     [[1, 2, 3], [3, 1, 5], [3, 2, 1]])
            [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.differenceOfDistinctValues([[1, 2, 3], [3, 1, 5], [3, 2, 1]]))
    # Expected: [[1, 1, 0], [1, 0, 1], [0, 1, 1]]

    print(sol.differenceOfDistinctValues([[1]]))
    # Expected: [[0]]

    print(sol.differenceOfDistinctValues([[5, 5], [5, 5]]))
    # Expected: [[1, 0], [0, 1]]
