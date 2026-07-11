"""LeetCode 835 - Largest Image Overlap.

Fill in `largestOverlap` using Convolution / FFT on 2D data (cross-correlation).
"""
from __future__ import annotations

from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """Return the maximum number of overlapping 1s over all translations.

        For each shift (dr, dc), the overlap is the number of cells where
        img1[i][j] == 1 and img2[i + dr][j + dc] == 1 (indices in bounds). This
        is the cross-correlation of the two binary images; the answer is its peak.

        Args:
            img1: n x n binary matrix (entries 0 or 1).
            img2: n x n binary matrix (entries 0 or 1).

        Returns:
            The largest overlap (a non-negative integer) achievable by translating
            one image over the other.

        Example:
            >>> Solution().largestOverlap(
            ...     [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
            ...     [[0, 0, 0], [0, 1, 1], [0, 0, 1]],
            ... )
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
    img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
    print(Solution().largestOverlap(img1, img2))
    # Expected: 3

    print(Solution().largestOverlap([[1]], [[1]]))
    # Expected: 1
