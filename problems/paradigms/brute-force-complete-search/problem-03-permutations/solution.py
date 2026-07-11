"""Permutations — Brute Force / Complete Search practice template.

Fill in the body of `permute`. Do NOT look at SOLUTION.md until you have tried.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Return every permutation of the distinct integers in `nums`.

        Args:
            nums: List of distinct integers, length between 1 and 6.

        Returns:
            A list of all len(nums)! permutations, each a list of integers.
            Order of the permutations does not matter.

        Example:
            >>> sorted(Solution().permute([0, 1]))
            [[0, 1], [1, 0]]
        """
        # TODO: implement using Brute Force / Complete Search
        # (recursively place each unused element in the next position).
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected (any order): the 6 orderings of 1,2,3
    print(sol.permute([1, 2, 3]))
    print(sol.permute([0, 1]))  # expected (any order): [0,1], [1,0]
    print(sol.permute([1]))     # expected: [[1]]
