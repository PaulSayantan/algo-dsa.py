"""LeetCode 78 - Subsets (power set).

Fill in the body of `subsets`. Use bitmask enumeration: iterate every mask
from 0 to 2**n - 1 and build the corresponding subset.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Return the power set of `nums`.

        Args:
            nums: A list of unique integers.

        Returns:
            A list containing every subset of `nums` (2**len(nums) subsets),
            in any order.

        Example:
            >>> Solution().subsets([1, 2, 3])  # doctest: +SKIP
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        """
        # TODO: for mask in range(1 << len(nums)):
        #           include nums[j] when (mask >> j) & 1 is set.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))  # expected: 8 subsets (power set of {1,2,3})
    print(sol.subsets([0]))        # expected: [[], [0]]
    print(sol.subsets([9, 8]))     # expected: 4 subsets (power set of {9,8})
