"""Count Submatrices With All Ones (LeetCode 1504).

Return the number of all-1 submatrices. Empty solution template —
fill in the logic yourself.
"""

from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """Count the all-1 submatrices (rectangles) in ``mat``.

        Args:
            mat: An m x n binary matrix of 0s and 1s.

        Returns:
            The total number of distinct axis-aligned rectangles that
            consist entirely of 1s.

        Example:
            >>> Solution().numSubmat([[1, 0, 1], [1, 1, 0], [1, 1, 0]])
            13
        """
        # TODO: implement.
        # Hint: build height[j] = consecutive 1s ending at the current row in
        # column j, then for each row count rectangles whose bottom edge is on
        # that row. A monotonic stack maintains a running sum f[j] of rectangles
        # ending at column j, reusing the previous shorter bar's contribution.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubmat([[1, 0, 1],
                         [1, 1, 0],
                         [1, 1, 0]]))            # expected: 13
    print(sol.numSubmat([[0, 1, 1, 0],
                         [0, 1, 1, 1],
                         [1, 1, 1, 0]]))         # expected: 24
    print(sol.numSubmat([[1, 1, 1, 1, 1, 1]]))   # expected: 21
