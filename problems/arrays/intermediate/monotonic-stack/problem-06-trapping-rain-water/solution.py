"""Trapping Rain Water — LeetCode 42.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Compute the total units of rain water trapped by the elevation map.

        Each bar has width 1. Water above position ``i`` rises to
        ``min(max_left, max_right)`` and the trapped amount there is that level
        minus ``height[i]`` when positive.

        Args:
            height: Non-negative bar heights of the elevation map.

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
    print(sol.trap([4, 2, 0, 3, 2, 5]))                    # expected: 9
    print(sol.trap([3, 0, 2, 0, 4]))                       # expected: 7
