"""Subsets (power set) — Brute Force / Complete Search practice template.

Fill in the body of `subsets`. Do NOT look at SOLUTION.md until you have tried.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Return every subset of `nums` (the power set).

        Args:
            nums: List of unique integers, length between 1 and 10.

        Returns:
            A list of all 2**len(nums) subsets, each subset itself a list of
            integers. Order of the subsets does not matter.

        Example:
            >>> sorted(map(sorted, Solution().subsets([1, 2, 3])))
            [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        """
        # TODO: implement using Brute Force / Complete Search
        # (iterate every bitmask in range(1 << len(nums))).
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected (any order): [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets([0]))  # expected (any order): [], [0]
