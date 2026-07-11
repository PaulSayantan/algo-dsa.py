"""Reverse Pairs (LeetCode 493).

Fill in `Solution.reversePairs` using the merge-sort inversion-counting
technique adapted for the condition nums[i] > 2 * nums[j].
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """Count pairs (i, j) with i < j and nums[i] > 2 * nums[j].

        Args:
            nums: A list of integers, length 1 <= n <= 5 * 10^4.

        Returns:
            The number of reverse pairs as an integer.

        Example:
            >>> Solution().reversePairs([1, 3, 2, 3, 1])
            2
        """
        # TODO: implement using Count Inversions (merge sort)
        pass


if __name__ == "__main__":
    print(Solution().reversePairs([1, 3, 2, 3, 1]))  # expected: 2
    print(Solution().reversePairs([2, 4, 3, 5, 1]))  # expected: 3
