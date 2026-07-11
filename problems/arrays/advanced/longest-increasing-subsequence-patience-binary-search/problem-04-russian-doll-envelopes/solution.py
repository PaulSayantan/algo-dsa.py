"""Russian Doll Envelopes (LeetCode 354).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """Return the maximum number of envelopes that can be nested.

        An envelope [w1, h1] fits into [w2, h2] iff w1 < w2 and h1 < h2
        (both strictly).

        Args:
            envelopes: A list of [width, height] pairs.

        Returns:
            The length of the longest chain of strictly-nesting envelopes.

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
    print(sol.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))  # expected: 3
    print(sol.maxEnvelopes([[1, 1], [1, 1], [1, 1]]))          # expected: 1
    print(sol.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]))
    # expected: 4
