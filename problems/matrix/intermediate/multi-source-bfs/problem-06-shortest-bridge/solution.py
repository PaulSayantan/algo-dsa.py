"""Shortest Bridge — LeetCode 934.

Empty solution template. Fill in `shortestBridge`.
"""

from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """Return the minimum number of 0s to flip to connect the two islands.

        The grid contains exactly two 4-directionally connected islands of 1s. This is
        the shortest number of water cells lying strictly between them along the
        closest path.

        Args:
            grid: An n x n binary matrix; 1 is land, 0 is water, with exactly two
                islands.

        Returns:
            The smallest count of water cells (0s) that must be flipped to 1 to merge
            the two islands into one.

        Example:
            >>> Solution().shortestBridge([[0, 1], [1, 0]])
            1
        """
        # TODO: implement using flood fill + Multi-Source BFS.
        pass


if __name__ == "__main__":
    print(Solution().shortestBridge([[0, 1], [1, 0]]))  # Expected: 1
    print(Solution().shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))  # Expected: 2
    print(
        Solution().shortestBridge(
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ]
        )
    )  # Expected: 1
