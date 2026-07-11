"""Repeated String Match — LeetCode 686.

Fill in the body using Naive Pattern Matching. Build `a` repeated just enough
times to possibly contain `b`, then search for `b` yourself (no `in` /
str.find). Only k = ceil(len(b)/len(a)) and k + 1 copies can ever be the
minimum answer.
"""

import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """Return the fewest repeats of ``a`` so that ``b`` is a substring.

        Args:
            a: The string to repeat.
            b: The pattern that must become a substring of repeated ``a``.

        Returns:
            The minimum number of copies of ``a`` whose concatenation contains
            ``b`` as a substring, or ``-1`` if no number of copies works.

        Example:
            >>> Solution().repeatedStringMatch("abcd", "cdabcdab")
            3
            >>> Solution().repeatedStringMatch("abc", "wxyz")
            -1
        """
        # TODO: implement using Naive Pattern Matching
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedStringMatch("abcd", "cdabcdab"))  # expected: 3
    print(sol.repeatedStringMatch("a", "aa"))           # expected: 2
    print(sol.repeatedStringMatch("abc", "wxyz"))       # expected: -1
