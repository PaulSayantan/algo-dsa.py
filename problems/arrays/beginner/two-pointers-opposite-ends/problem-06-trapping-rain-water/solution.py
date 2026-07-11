"""Trapping Rain Water — LeetCode 42.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Return the total units of rain water trapped by the elevation map.

        Args:
            height: A list of non-negative bar heights, each of width 1.

        Returns:
            The total amount of water trapped between the bars after raining.

        Example:
            >>> Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
            6
        """
        # TODO: implement using two pointers (opposite ends)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # expected: 6
    print(sol.trap([4, 2, 0, 3, 2, 5]))                     # expected: 9
    print(sol.trap([3, 0, 2]))                              # expected: 2
