"""Closest Subsequence Sum — LeetCode 1755.

Return the minimum possible value of abs(subsequenceSum - goal) over all
subsequences (subsets) of `nums`.

Fill in `minAbsDifference` using Meet in the Middle: split `nums` in half,
enumerate every subset sum of each half, then for each left sum find the right
sum closest to (goal - leftSum) via sorting + binary search.
"""

from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """Return min abs(sum(subsequence) - goal).

        Args:
            nums: Integer array of length up to 40 (values may be negative).
            goal: Target sum to get as close to as possible.

        Returns:
            The minimum achievable value of abs(chosenSum - goal), where
            chosenSum ranges over all subsets of `nums` (empty subset allowed).

        Example:
            >>> Solution().minAbsDifference([5, -7, 3, 5], 6)
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: 0  (whole array sums to 6 == goal)
    print(sol.minAbsDifference([5, -7, 3, 5], 6))
    # Expected: 1  (closest achievable sum to -5 is -4)
    print(sol.minAbsDifference([7, -9, 15, -2], -5))
    # Expected: 7  (empty subset sum 0 is closest to -7)
    print(sol.minAbsDifference([1, 2, 3], -7))
