"""LeetCode 327 - Count of Range Sum.

Solve with an Order-Statistics Tree over prefix sums: for each right endpoint
P[r], range-count how many earlier prefix sums fall in
[P[r] - upper, P[r] - lower], then insert P[r].

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """Count range sums S(i, j) with lower <= S(i, j) <= upper.

        Args:
            nums: The input integer array.
            lower: Inclusive lower bound of the range-sum interval.
            upper: Inclusive upper bound of the range-sum interval.

        Returns:
            The number of pairs (i, j), i <= j, whose subarray sum is in
            [lower, upper].

        Example:
            Solution().countRangeSum([-2, 5, -1], -2, 2)  # -> 3
        """
        # TODO: implement
        # - maintain an OST of prefix sums; start by inserting P[0] = 0
        # - for each prefix sum P[r] (r = 1..n): add
        #     count(<= P[r] - lower) - count(< P[r] - upper)
        #   then insert P[r]
        pass


if __name__ == "__main__":
    print(Solution().countRangeSum([-2, 5, -1], -2, 2))  # expected 3
    print(Solution().countRangeSum([0], 0, 0))           # expected 1
