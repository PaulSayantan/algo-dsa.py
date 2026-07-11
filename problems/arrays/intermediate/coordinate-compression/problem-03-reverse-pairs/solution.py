"""Reverse Pairs (LeetCode 493).

Fill in the body of `reversePairs`. The intended approach compresses the union of
`nums` and `2*nums`, then uses a Fenwick tree. Do NOT peek at SOLUTION.md first.
"""

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """Count pairs (i, j) with i < j and nums[i] > 2 * nums[j].

        Args:
            nums: The input array of integers.

        Returns:
            The number of reverse pairs.

        Example:
            >>> Solution().reversePairs([1, 3, 2, 3, 1])
            2
        """
        # TODO: implement
        # Hint: build sorted-unique coords from nums + [2*x for x in nums].
        #       Sweep left-to-right; before inserting nums[i], count how many
        #       already-inserted values v satisfy v > 2*nums[i] via a BIT suffix query.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reversePairs([1, 3, 2, 3, 1]))  # expected: 2
    print(sol.reversePairs([2, 4, 3, 5, 1]))  # expected: 3
    print(sol.reversePairs([5, 5, 5]))         # expected: 0
