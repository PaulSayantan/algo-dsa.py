"""LeetCode 78 - Subsets.

Fill in the body of `subsets` using backtracking. Do not hard-code answers.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Return the power set of a list of unique integers.

        Args:
            nums: A list of unique integers (1 <= len(nums) <= 10).

        Returns:
            A list containing every subset of ``nums`` (2**len(nums) of them),
            including the empty subset. Any ordering of the subsets is valid.

        Example:
            >>> sorted(map(sorted, Solution().subsets([1, 2, 3])))
            [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    # Expected (in any order): [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
    print(sol.subsets([0]))
    # Expected (in any order): [], [0]
