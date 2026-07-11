"""Unique Paths — LeetCode 62.

Count the number of distinct right/down paths from the top-left to the
bottom-right of an ``m x n`` grid.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Return the number of unique top-left to bottom-right paths.

        Args:
            m: The number of rows in the grid (1 <= m <= 100).
            n: The number of columns in the grid (1 <= n <= 100).

        Returns:
            The number of distinct paths that move only right or down.

        Example:
            >>> Solution().uniquePaths(3, 7)
            28
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3, 7))  # expected: 28
    print(sol.uniquePaths(3, 2))  # expected: 3
    print(sol.uniquePaths(1, 1))  # expected: 1
