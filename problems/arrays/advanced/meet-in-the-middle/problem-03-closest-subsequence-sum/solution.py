"""Closest Subsequence Sum (LeetCode 1755) — empty solution template.

Fill in `Solution.minAbsDifference` using the Meet in the Middle technique.
"""

from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """Return the minimum possible value of abs(subsequence_sum - goal).

        Args:
            nums: A list of up to 40 integers (may be negative, zero, or positive).
            goal: The target value the subsequence sum should be closest to.

        Returns:
            The minimum achievable abs(sum(chosen) - goal) over all subsequences
            (the empty subsequence, with sum 0, is allowed).

        Example:
            >>> Solution().minAbsDifference([5, -7, 3, 5], 6)
            0
            >>> Solution().minAbsDifference([7, -9, 15, -2], -5)
            1
        """
        # TODO: implement using Meet in the Middle
        pass


if __name__ == "__main__":
    print(Solution().minAbsDifference([5, -7, 3, 5], 6))      # expected: 0
    print(Solution().minAbsDifference([7, -9, 15, -2], -5))   # expected: 1
    print(Solution().minAbsDifference([1, 2, 3], -7))         # expected: 7
