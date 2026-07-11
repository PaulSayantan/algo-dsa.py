"""LeetCode 46 - Permutations.

Fill in the body of `permute` using backtracking. Do not hard-code answers.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Return every permutation of a list of distinct integers.

        Args:
            nums: A list of distinct integers (1 <= len(nums) <= 6).

        Returns:
            A list of all len(nums)! permutations of ``nums``. Any ordering of
            the permutations is valid.

        Example:
            >>> sorted(Solution().permute([1, 2, 3]))
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))
    # Expected (in any order): [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
    print(sol.permute([0, 1]))
    # Expected (in any order): [0,1],[1,0]
