"""Partition to K Equal Sum Subsets (LeetCode 698).

Decide whether `nums` can be split into `k` subsets of equal sum.

Solve this with Bitmask DP: a `mask` records which elements are already used.
For each reachable mask, store the sum accumulated *in the current, still-open
bucket* modulo the per-bucket target. Adding an element that does not overflow
the target extends the mask; when a bucket exactly hits the target it "closes"
and the next element starts a fresh bucket.
"""

from __future__ import annotations

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """Return True iff nums can be partitioned into k equal-sum subsets.

        Args:
            nums: List of positive integers (1 <= len(nums) <= 16).
            k: Number of subsets required (1 <= k <= len(nums)).

        Returns:
            True if the elements can be divided into exactly k non-empty
            subsets all having the same sum, False otherwise.

        Example:
            >>> Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))  # expected: True
    print(sol.canPartitionKSubsets([1, 2, 3, 4], 3))            # expected: False
    print(sol.canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5], 4))   # expected: False
