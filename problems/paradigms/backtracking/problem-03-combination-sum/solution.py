"""LeetCode 39 - Combination Sum.

Fill in the body of `combinationSum` using backtracking. Do not hard-code
answers.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Return all unique combinations of candidates that sum to target.

        Each candidate may be used an unlimited number of times. Combinations
        are unordered multisets, so [2, 2, 3] and [3, 2, 2] are the same.

        Args:
            candidates: A list of distinct positive integers.
            target: The positive integer the chosen numbers must sum to.

        Returns:
            A list of unique combinations (each a list of ints) summing to
            target. Any ordering of the combinations is valid.

        Example:
            >>> Solution().combinationSum([2, 3, 6, 7], 7)
            [[2, 2, 3], [7]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
    # Expected (in any order): [2,2,3], [7]
    print(sol.combinationSum([2, 3, 5], 8))
    # Expected (in any order): [2,2,2,2], [2,3,3], [3,5]
