"""LeetCode 215 - Kth Largest Element in an Array.

Return the k-th largest element (in sorted order, counting duplicates). Aim for average
O(n) using randomized quickselect: partition around a randomly chosen pivot and recurse
into only the side that contains the answer.
"""

from __future__ import annotations

from typing import List


class Solution:
    """Find the k-th largest element via randomized quickselect."""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the k-th largest element of nums.

        The k-th largest is measured in sorted order counting duplicates, not the
        k-th distinct value.

        Args:
            nums: The array of integers (1 <= len(nums)).
            k: 1-based rank from the largest (1 <= k <= len(nums)).

        Returns:
            The k-th largest element.

        Example:
            >>> Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
            5
            >>> Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
            4
        """
        # TODO: implement (randomized quickselect)
        pass


if __name__ == "__main__":
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))            # expected: 5
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # expected: 4
    print(Solution().findKthLargest([1], 1))                           # expected: 1
