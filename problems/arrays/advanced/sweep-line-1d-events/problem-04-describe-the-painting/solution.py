"""Describe the Painting (LeetCode 1943).

Fill in `Solution.splitPainting` using a 1D sweep line over weighted events that
EMITS output segments. This file is an intentionally empty template — no working
solution is provided.
"""

from typing import List


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        """Describe the mixed painting as non-overlapping [left, right, sum] pieces.

        Each input segment [s, e, c] adds +c at s and -c at e (a weighted event).
        Sweep the sorted distinct coordinates keeping a running color sum; for
        every gap between consecutive coordinates over which the running sum is
        positive, emit [prev, cur, runningSum]. A boundary is placed at every
        coordinate where a segment starts or ends (i.e. wherever the active color
        set changes), so neighbors can share a sum yet stay separate.

        Args:
            segments: List of [start, end, color] with start < end, color >= 1.

        Returns:
            A list of [left, right, mixedColorSum] pieces sorted by left.

        Example:
            >>> Solution().splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]])
            [[1, 4, 14], [4, 7, 16]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]))
    # expected: [[1, 4, 14], [4, 7, 16]]
    print(sol.splitPainting([[1, 7, 9], [6, 8, 15], [8, 10, 7]]))
    # expected: [[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]
    print(sol.splitPainting([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]))
    # expected: [[1, 4, 12], [4, 7, 12]]
