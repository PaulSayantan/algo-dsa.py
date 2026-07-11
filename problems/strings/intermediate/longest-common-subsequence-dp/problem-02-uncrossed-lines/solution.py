"""LeetCode 1035 — Uncrossed Lines.

Fill in the body of `maxUncrossedLines`. Do not edit the signature.
"""
from __future__ import annotations

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """Return the maximum number of non-crossing connecting lines.

        Args:
            nums1: The first integer array written on the top line.
            nums2: The second integer array written on the bottom line.

        Returns:
            The maximum number of connecting lines that can be drawn without
            any two lines crossing.

        Example:
            >>> Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxUncrossedLines([1, 4, 2], [1, 2, 4]))                 # expected: 2
    print(sol.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))  # expected: 3
    print(sol.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))   # expected: 2
