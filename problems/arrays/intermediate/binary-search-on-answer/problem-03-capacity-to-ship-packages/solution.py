"""Capacity To Ship Packages Within D Days — LeetCode 1011.

Find the least ship capacity that lets all packages ship, in the given order,
within `days` days. Solve with Binary Search on Answer over the capacity range
[max(weights), sum(weights)].
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """Return the minimum weight capacity to ship everything within `days`.

        Args:
            weights: Package weights in the fixed order they must be loaded.
            days: Maximum number of days allowed to ship all packages.

        Returns:
            The smallest capacity c such that the packages can be partitioned
            into at most `days` contiguous groups, each with sum <= c.

        Example:
            >>> Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
            15
        """
        # TODO: implement using Binary Search on Answer over
        #       [max(weights), sum(weights)].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # expected: 15
    print(sol.shipWithinDays([3, 2, 2, 4, 1, 4], 3))               # expected: 6
    print(sol.shipWithinDays([1, 2, 3, 1, 1], 4))                  # expected: 3
