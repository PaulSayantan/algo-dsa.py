from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Return the total units of water trapped by the elevation map.

        The water resting above bar i equals
        min(max height to its left, max height to its right) - height[i],
        clamped at 0.

        Args:
            height: A list of non-negative bar heights, each of width 1.

        Returns:
            The total amount of trapped water.

        Example:
            >>> Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
            6
        """
        # TODO: implement (prefix maximum from the left, suffix maximum from the
        #       right, then sum min(left_max, right_max) - height[i])
        pass


if __name__ == "__main__":
    # Sample runs — expected outputs shown as comments, not asserted.
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # expected: 6
    print(sol.trap([4, 2, 0, 3, 2, 5]))                    # expected: 9
