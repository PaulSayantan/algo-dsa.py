"""Shortest Subarray with Sum at Least K — LeetCode 862.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """Return the length of the shortest subarray with sum >= k.

        The array may contain negative numbers.

        Args:
            nums: The input array of integers (negatives allowed).
            k: The minimum required subarray sum.

        Returns:
            The length of the shortest contiguous non-empty subarray whose sum is
            at least ``k``, or ``-1`` if no such subarray exists.

        Example:
            >>> Solution().shortestSubarray([2, -1, 2], 3)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestSubarray([1], 1))  # expected: 1
    print(sol.shortestSubarray([1, 2], 4))  # expected: -1
    print(sol.shortestSubarray([2, -1, 2], 3))  # expected: 3
    print(sol.shortestSubarray([84, -37, 32, 40, 95], 167))  # expected: 3
