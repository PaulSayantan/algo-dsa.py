"""LeetCode 493 - Reverse Pairs.

Fill in the body using a Binary Indexed Tree (Fenwick Tree) over
coordinate-compressed values. Count pairs (i, j) with i < j and
nums[i] > 2 * nums[j].
"""

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """Count reverse pairs: i < j with nums[i] > 2 * nums[j].

        Args:
            nums: The input integer array (values may be negative and large).

        Returns:
            The number of index pairs (i, j) with i < j and nums[i] > 2*nums[j].

        Example:
            >>> Solution().reversePairs([1, 3, 2, 3, 1])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reversePairs([1, 3, 2, 3, 1]))   # expected: 2
    print(sol.reversePairs([2, 4, 3, 5, 1]))   # expected: 3
    print(sol.reversePairs([5, 4, 3, 2, 1]))   # expected: 4
