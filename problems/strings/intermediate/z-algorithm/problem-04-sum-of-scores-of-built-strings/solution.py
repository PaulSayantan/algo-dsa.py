"""LeetCode 2223 - Sum of Scores of Built Strings.

The score of the built string of length i is the longest common prefix of s
with its suffix of length i, which is exactly a Z-array value. The answer is
the sum of the Z-array of s (with z[0] = n).
"""

from typing import List


class Solution:
    def sumScores(self, s: str) -> int:
        """Return the sum of scores of all built strings of s.

        The built string of length ``i`` is the suffix ``s[len(s) - i:]``, and
        its score is the length of the longest common prefix it shares with the
        full string ``s``.

        Args:
            s: A non-empty lowercase string.

        Returns:
            The sum over all built strings of their score.

        Example:
            >>> Solution().sumScores("babab")
            9
            >>> Solution().sumScores("azbazbzaz")
            14
        """
        # TODO: implement
        pass

    def _z_array(self, s: str) -> List[int]:
        """Optional helper: compute the Z-array of ``s`` in O(len(s)) time.

        Args:
            s: The string whose Z-array should be computed.

        Returns:
            A list ``z`` where ``z[i]`` is the length of the longest substring
            starting at ``i`` that is also a prefix of ``s`` (with ``z[0]``
            conventionally set to ``len(s)``).
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumScores("babab"))       # expected: 9
    print(sol.sumScores("azbazbzaz"))   # expected: 14
