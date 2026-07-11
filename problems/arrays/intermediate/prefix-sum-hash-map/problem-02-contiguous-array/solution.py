"""Contiguous Array (LeetCode 525).

Fill in the body of `findMaxLength`. Do not modify the signature.
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """Return the length of the longest subarray with equal 0s and 1s.

        Args:
            nums: A binary array whose elements are each 0 or 1.

        Returns:
            The maximum length of a contiguous subarray containing an equal
            number of 0s and 1s, or 0 if no such subarray exists.

        Example:
            >>> Solution().findMaxLength([0, 1, 0])
            2
        """
        # TODO: remap 0 -> -1, keep a running prefix sum, and use a hash map
        # from prefix-sum value to its earliest index to find the longest
        # subarray whose sum is 0.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0, 1]))                        # expected: 2
    print(sol.findMaxLength([0, 1, 0]))                     # expected: 2
    print(sol.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))      # expected: 6
