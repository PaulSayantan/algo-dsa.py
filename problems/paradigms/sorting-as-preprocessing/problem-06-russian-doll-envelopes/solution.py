"""Russian Doll Envelopes — LeetCode 354.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """Return the maximum number of envelopes that can be Russian-doll nested.

        Envelope [w1, h1] fits inside [w2, h2] only if w1 < w2 AND h1 < h2 (both
        dimensions strictly greater). Rotation is not allowed.

        Args:
            envelopes: A list of [width, height] pairs.

        Returns:
            The length of the longest strictly-nesting chain of envelopes.

        Example:
            >>> Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
            3
            >>> Solution().maxEnvelopes([[1, 1], [1, 1], [1, 1]])
            1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))              # expected: 3
    print(sol.maxEnvelopes([[1, 1], [1, 1], [1, 1]]))                      # expected: 1
    print(sol.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]))      # expected: 4
