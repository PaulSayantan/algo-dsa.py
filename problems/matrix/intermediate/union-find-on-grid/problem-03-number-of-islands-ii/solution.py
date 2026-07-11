"""LeetCode 305 - Number of Islands II.

Solve with an incremental (online) Union-Find on Grid. Activate each cell as it
arrives, add 1 to a running island count, then union with any already-active
4-directional neighbor, subtracting 1 per successful merge.
"""
from typing import List


class Solution:
    def numIslands2(
        self, m: int, n: int, positions: List[List[int]]
    ) -> List[int]:
        """Report the island count after each addLand operation.

        Args:
            m: Number of rows in the grid.
            n: Number of columns in the grid.
            positions: A list of [row, col] cells turned into land, in order.

        Returns:
            A list ``result`` where ``result[i]`` is the number of islands after
            applying ``positions[0..i]``. Duplicate positions are no-ops.

        Example:
            >>> Solution().numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
            [1, 1, 2, 3]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))
    # expected: [1, 1, 2, 3]
