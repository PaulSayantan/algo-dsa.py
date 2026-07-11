"""LeetCode 421 - Maximum XOR of Two Numbers in an Array.

Fill in the body of `findMaximumXOR`. Aim to beat the O(n^2) brute force by
building the answer bit by bit from the most significant bit downward.
"""
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """Return the maximum value of nums[i] XOR nums[j] over all pairs.

        Args:
            nums: A non-empty list of non-negative integers.

        Returns:
            The largest pairwise XOR achievable from elements of `nums`.

        Example:
            >>> Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
            28
        """
        # TODO: greedy prefix approach (or binary trie).
        #   answer = 0
        #   for bit from high to low:
        #       candidate = answer | (1 << bit)
        #       prefixes = { num >> bit for num in nums }
        #       if any p in prefixes with (candidate ^ p) in prefixes: answer = candidate
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))  # expected: 28
    print(sol.findMaximumXOR([2, 4]))                # expected: 6
    print(sol.findMaximumXOR([0]))                   # expected: 0
