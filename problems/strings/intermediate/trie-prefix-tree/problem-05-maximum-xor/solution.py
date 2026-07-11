"""LeetCode 421 - Maximum XOR of Two Numbers in an Array.

Find the maximum XOR of any pair using a binary Trie over the bits of each number.
"""
from __future__ import annotations

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """Return the maximum value of nums[i] XOR nums[j] over all pairs.

        Args:
            nums: List of non-negative integers (each fits in 32 bits).

        Returns:
            The largest XOR obtainable from any two elements (i and j may be
            equal, though equal indices give 0 and never help the maximum).

        Example:
            >>> Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
            28
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))  # expected: 28  (5 ^ 25)
    print(sol.findMaximumXOR([8, 10, 2]))            # expected: 10  (8 ^ 2)
