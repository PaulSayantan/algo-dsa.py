"""LeetCode 42 - Trapping Rain Water.

Compute the total water trapped by an elevation map. A monotonic decreasing
stack settles water layer by layer, touching each bar a constant number of times
for O(n) total work.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Return the total units of water trapped by the elevation map.

        Args:
            height: Non-negative bar heights; each bar has width 1.

        Returns:
            The total amount of water that can be trapped after raining.

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
    print(sol.trap([3, 0, 2]))                              # expected: 2
