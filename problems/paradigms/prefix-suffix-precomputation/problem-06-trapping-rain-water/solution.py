"""Trapping Rain Water — LeetCode 42.

Fill in the body of `trap`. Do not change the signature.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Return the total units of rain water trapped by the elevation map.

        Water above bar ``i`` equals
        ``max(0, min(max height to its left, max height to its right) - height[i])``.

        Args:
            height: Non-negative bar heights, each of width 1.

        Returns:
            The total amount of trapped water.

        Example:
            >>> Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # expected: 6
    print(sol.trap([4, 2, 0, 3, 2, 5]))                     # expected: 9
    print(sol.trap([2, 0, 2]))                              # expected: 2
