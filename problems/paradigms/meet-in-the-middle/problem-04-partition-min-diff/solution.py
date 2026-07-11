"""Partition Array Into Two Halves to Minimize Sum Difference — LeetCode 2035.

Given `nums` of length 2n, split it into two size-n arrays minimizing the
absolute difference of their sums. Return that minimum difference.

Fill in `minimumDifference` using Meet in the Middle grouped by cardinality:
enumerate each half's subset sums bucketed by how many elements are chosen,
then match a k-element pick on the left with an (n-k)-element pick on the right
via sorting + binary search.
"""

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """Return the minimum abs difference of the two size-n partition sums.

        Args:
            nums: Integer array of length 2 * n (values may be negative).

        Returns:
            The minimum achievable value of
            abs(sum(firstHalf) - sum(secondHalf)) over all partitions of `nums`
            into two arrays of exactly n elements each.

        Example:
            >>> Solution().minimumDifference([3, 9, 7, 3])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Expected: 2
    print(sol.minimumDifference([3, 9, 7, 3]))
    # Expected: 72
    print(sol.minimumDifference([-36, 36]))
    # Expected: 0
    print(sol.minimumDifference([2, -1, 0, 4, -2, -9]))
