"""Number of Provinces — LeetCode 547.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Count connected components (provinces) in an adjacency matrix.

        Args:
            isConnected: An ``n x n`` symmetric matrix where
                ``isConnected[i][j] == 1`` means city ``i`` and city ``j`` are
                directly connected. The diagonal is all ``1``s.

        Returns:
            The number of provinces (connected components of cities).

        Example:
            >>> Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    # Expected: 2

    print(sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    # Expected: 3

    print(sol.findCircleNum(
        [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    ))
    # Expected: 2
