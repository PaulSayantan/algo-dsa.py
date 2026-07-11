"""Walls and Gates — LeetCode 286.

Empty solution template. Fill in `wallsAndGates`. The grid is modified in place.
"""

from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """Fill each empty room with the distance to its nearest gate, in place.

        Cell values: -1 is a wall, 0 is a gate, and 2147483647 (INF) is an empty room.
        After the call, every empty room reachable from a gate holds the number of
        4-directional steps to the closest gate; unreachable rooms keep INF.

        Args:
            rooms: An m x n grid of -1 (wall), 0 (gate), or 2147483647 (empty room).
                The grid is mutated in place.

        Returns:
            None. The input `rooms` grid is modified directly.

        Example:
            >>> grid = [[0, 2147483647], [2147483647, 2147483647]]
            >>> Solution().wallsAndGates(grid)
            >>> grid
            [[0, 1], [1, 2]]
        """
        # TODO: implement using Multi-Source BFS.
        pass


if __name__ == "__main__":
    INF = 2147483647
    grid = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    Solution().wallsAndGates(grid)
    print(grid)
    # Expected:
    # [[3, -1, 0, 1],
    #  [2, 2, 1, -1],
    #  [1, -1, 2, -1],
    #  [0, -1, 3, 4]]
