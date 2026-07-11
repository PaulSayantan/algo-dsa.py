"""Maximum Length of Repeated Subarray (LeetCode 718).

Return the maximum length of a contiguous subarray common to both ``nums1`` and
``nums2`` (the array version of longest common substring).

Intended technique: Generalized Suffix Structure. Treat the arrays as strings
over the integer alphabet and build one generalized suffix automaton over both.
Mark each state with the set of source arrays whose occurrences pass through it
(propagate marks up the suffix-link tree), then take the largest ``len[v]`` over
states owned by both arrays.
"""

from __future__ import annotations

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """Length of the longest contiguous subarray common to both arrays.

        Args:
            nums1: First integer array.
            nums2: Second integer array.

        Returns:
            The maximum length of a subarray present in both ``nums1`` and
            ``nums2``; 0 if they share no common value.

        Example:
            >>> Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
            3
            >>> Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # expected: 3
    print(sol.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))  # expected: 5
    print(sol.findLength([1, 2, 3], [4, 5, 6]))              # expected: 0
