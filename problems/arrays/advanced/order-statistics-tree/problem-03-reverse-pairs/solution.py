"""LeetCode 493 - Reverse Pairs.

Solve with an Order-Statistics Tree: scan left to right and, before inserting
nums[j], count how many stored keys are strictly greater than 2 * nums[j].

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """Count pairs (i, j) with i < j and nums[i] > 2 * nums[j].

        Args:
            nums: The input integer array.

        Returns:
            The number of reverse pairs.

        Example:
            Solution().reversePairs([1, 3, 2, 3, 1])  # -> 2
        """
        # TODO: implement (left-to-right scan; count keys > 2*nums[j], then insert)
        pass


if __name__ == "__main__":
    print(Solution().reversePairs([1, 3, 2, 3, 1]))  # expected 2
    print(Solution().reversePairs([2, 4, 3, 5, 1]))  # expected 3
