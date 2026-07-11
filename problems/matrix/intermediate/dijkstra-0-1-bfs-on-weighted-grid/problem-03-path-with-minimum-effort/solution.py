"""Path With Minimum Effort (LeetCode 1631).

Fill in the body using Dijkstra with a minimax ("max" instead of "+")
relaxation. Do not modify the signature.
"""
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """Return the minimum possible effort of a path from (0, 0) to the
        bottom-right cell, where a path's effort is the maximum absolute height
        difference between two consecutive cells on it.

        Moves are 4-directional. You are minimising the single worst step
        (a bottleneck / minimax objective), not the sum of steps.

        Args:
            heights: A rows x columns matrix of positive cell heights.

        Returns:
            The minimum achievable effort (a non-negative integer).

        Example:
            >>> Solution().minimumEffortPath([[1, 2, 2],
            ...                               [3, 8, 2],
            ...                               [5, 3, 5]])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumEffortPath([[1, 2, 2],
                                 [3, 8, 2],
                                 [5, 3, 5]]))              # expected: 2
    print(sol.minimumEffortPath([[1, 2, 3],
                                 [3, 8, 4],
                                 [5, 3, 5]]))              # expected: 1
    print(sol.minimumEffortPath([[1, 2, 1, 1, 1],
                                 [1, 2, 1, 2, 1],
                                 [1, 2, 1, 2, 1],
                                 [1, 2, 1, 2, 1],
                                 [1, 1, 1, 2, 1]]))        # expected: 0
