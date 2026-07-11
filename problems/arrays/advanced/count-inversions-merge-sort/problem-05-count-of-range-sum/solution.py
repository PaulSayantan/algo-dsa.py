"""Count of Range Sum (LeetCode 327).

Fill in `Solution.countRangeSum`. Build the prefix-sum array P (length n+1)
and count pairs a < b with lower <= P[b] - P[a] <= upper using the merge-sort
counting technique.
"""
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """Count subarrays of nums whose sum lies in [lower, upper] inclusive.

        Args:
            nums: A list of integers, length 1 <= n <= 10^5.
            lower: Inclusive lower bound of the target sum range.
            upper: Inclusive upper bound of the target sum range (upper >= lower).

        Returns:
            The number of index pairs (i, j), i <= j, with
            lower <= sum(nums[i..j]) <= upper.

        Example:
            >>> Solution().countRangeSum([-2, 5, -1], -2, 2)
            3
        """
        # TODO: implement using Count Inversions (merge sort)
        pass


if __name__ == "__main__":
    print(Solution().countRangeSum([-2, 5, -1], -2, 2))  # expected: 3
    print(Solution().countRangeSum([0], 0, 0))           # expected: 1
