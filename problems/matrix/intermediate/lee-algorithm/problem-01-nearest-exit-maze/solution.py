"""Nearest Exit from Entrance in Maze (LeetCode 1926).

Fill in the body using the Lee Algorithm (BFS). Do not modify the signature.
"""
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """Return the fewest steps from the entrance to the nearest border exit.

        Args:
            maze: An m x n grid where '.' is an empty cell and '+' is a wall.
            entrance: [row, col] of the starting empty cell. It does NOT count
                as an exit even though it may lie on the border.

        Returns:
            The number of steps in the shortest path to the nearest exit (an
            empty border cell other than the entrance), or -1 if unreachable.

        Example:
            >>> Solution().nearestExit(
            ...     [["+","+",".","+"],
            ...      [".",".",".","+"],
            ...      ["+","+","+","."]], [1, 2])
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nearestExit(
        [["+", "+", ".", "+"],
         [".", ".", ".", "+"],
         ["+", "+", "+", "."]], [1, 2]))  # expected: 1
    print(sol.nearestExit(
        [["+", "+", "+"],
         [".", ".", "."],
         ["+", "+", "+"]], [1, 0]))       # expected: 2
    print(sol.nearestExit([[".", "+"]], [0, 0]))  # expected: -1
