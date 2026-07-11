"""Count of Range Sum (LeetCode 327).

Fill in the body of `countRangeSum`. The intended approach compresses the prefix
sums and uses a Fenwick tree. Do NOT read SOLUTION.md until you have attempted it.
"""

from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """Count range sums S(i, j) that lie in [lower, upper].

        A range sum is S(i, j) = nums[i] + ... + nums[j] for some i <= j.

        Args:
            nums: The input array of integers.
            lower: Inclusive lower bound on the range sum.
            upper: Inclusive upper bound on the range sum.

        Returns:
            The number of index pairs (i, j) with i <= j such that
            lower <= S(i, j) <= upper.

        Example:
            >>> Solution().countRangeSum([-2, 5, -1], -2, 2)
            3
        """
        # TODO: implement
        # Hint: prefix sums P[0..n]; a valid j,i pair satisfies
        #       P[k] - upper <= P[i] <= P[k] - lower for i < k.
        #       Compress all P values, then sweep k inserting P[i] into a BIT.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countRangeSum([-2, 5, -1], -2, 2))  # expected: 3
    print(sol.countRangeSum([0], 0, 0))            # expected: 1
    print(sol.countRangeSum([1, -1, 1], 0, 1))     # expected: 5
