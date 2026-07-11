"""Sliding Puzzle — LeetCode 773.

Empty solution template. Fill in `slidingPuzzle`.
"""

from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """Return the least number of moves to solve the 2x3 sliding puzzle, or -1 if
        the target configuration is unreachable.

        A move swaps the blank (0) with a 4-directionally adjacent tile. The solved
        board is [[1, 2, 3], [4, 5, 0]].

        Args:
            board: A 2x3 grid containing each value 0..5 exactly once.

        Returns:
            The minimum number of moves to reach the solved board, or -1 if impossible.

        Example:
            >>> Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]])
            5
        """
        # TODO: implement using A* Search with a Manhattan-distance-sum heuristic.
        pass


if __name__ == "__main__":
    print(Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
    # Expected: 1
    print(Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
    # Expected: -1
    print(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
    # Expected: 5
