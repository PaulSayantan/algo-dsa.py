"""Longest Common Subpath (LeetCode 1923).

Practice this with binary search on the subpath length plus double hashing of
integer-sequence windows, intersecting hash sets across all paths.
"""

from __future__ import annotations

from typing import List


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        """Return the length of the longest subpath common to every path.

        Args:
            n: Number of cities (city ids range over 0..n-1). Used to pick a
               hashing base larger than any single city value.
            paths: A list of integer sequences; each is one friend's path.

        Returns:
            The length of the longest contiguous block of city ids that
            appears (as a contiguous subpath) in every path; 0 if none.

        Example:
            >>> Solution().longestCommonSubpath(5, [[0,1,2,3,4],[2,3,4],[4,0,1,2,3]])
            2
            >>> Solution().longestCommonSubpath(3, [[0],[1],[2]])
            0
        """
        # TODO: implement
        # Suggested approach:
        #   1. Choose two moduli and two bases (base > n so city ids are valid
        #      "digits"). Precompute B^L for the current length L per modulus.
        #   2. window_hashes(path, L): roll a two-modulus hash over every
        #      length-L window, returning the set of (v1, v2) pairs.
        #   3. common(L): start with the hash-pair set of the shortest path,
        #      intersect it with every other path's set; return True iff the
        #      final intersection is non-empty.
        #   4. Binary search the largest L in [1, min path length] with
        #      common(L) True; return it (0 if none).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubpath(5, [[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3]]))  # expected: 2
    print(sol.longestCommonSubpath(3, [[0], [1], [2]]))                                 # expected: 0
    print(sol.longestCommonSubpath(5, [[0, 1, 2, 3, 4], [4, 3, 2, 1, 0]]))              # expected: 1
