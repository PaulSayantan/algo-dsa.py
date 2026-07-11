"""Count of Range Sum (LeetCode 327).

Count the number of range sums S(i, j) that lie in [lower, upper]. Solve in
O(n log n) using prefix sums plus a Segment Tree over the compressed prefix-sum
value domain.

Fill in the method body. Do NOT use the naive O(n^2) enumeration of all range sums.
"""
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """Count pairs (i, j), i <= j, with lower <= sum(nums[i..j]) <= upper.

        Args:
            nums: The input integer array.
            lower: Inclusive lower bound on the range sum.
            upper: Inclusive upper bound on the range sum.

        Returns:
            The number of contiguous sub-arrays whose sum lies in [lower, upper].

        Example:
            Solution().countRangeSum([-2, 5, -1], -2, 2)  # -> 3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().countRangeSum([-2, 5, -1], -2, 2))  # expected: 3
    print(Solution().countRangeSum([2, -1, 1], 1, 2))    # expected: 4
