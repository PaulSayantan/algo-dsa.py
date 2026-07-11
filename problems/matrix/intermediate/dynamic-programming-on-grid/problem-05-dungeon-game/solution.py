"""Dungeon Game — LeetCode 174.

Return the minimum initial health a knight needs to travel from the
top-left to the bottom-right of a dungeon (moving only right or down) while
keeping his health strictly positive at every room.
"""
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """Return the minimum initial health needed to rescue the princess.

        Args:
            dungeon: An m x n grid of integers. Negative values are demons
                (health loss), positive values are magic orbs (health gain),
                and 0 is an empty room.

        Returns:
            The smallest positive starting health such that, following some
            right/down path from the top-left to the bottom-right room, the
            knight's health never drops to 0 or below.

        Example:
            >>> Solution().calculateMinimumHP(
            ...     [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
            ... )
            7
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # 7
    print(sol.calculateMinimumHP([[0]]))  # expected: 1
    print(sol.calculateMinimumHP([[100]]))  # expected: 1
