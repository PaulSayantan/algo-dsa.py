"""Numbers At Most N Given Digit Set (LeetCode 902).

Count positive integers <= n that can be written using ONLY the characters in
`digits` (each usable any number of times). Solve with Digit DP that separates
"shorter than n" numbers (fully free) from "same length as n" numbers (bounded).
"""

from functools import lru_cache
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """Count positive integers <= n writable with the allowed digit set.

        Args:
            digits: Sorted list of distinct decimal digit characters from '1'
                to '9' (never '0'). Each may be reused arbitrarily.
            n: Inclusive upper bound. 1 <= n <= 10^9.

        Returns:
            How many positive integers x <= n use only characters in `digits`.

        Example:
            >>> Solution().atMostNGivenDigitSet(["1", "3", "5", "7"], 100)
            20
        """
        # TODO: implement
        #
        # Suggested plan (Digit DP):
        #   s = str(n); L = len(s); k = len(digits)
        #   1) Count all writable numbers with fewer than L digits:
        #        sum(k ** length for length in range(1, L))
        #   2) Count writable numbers with exactly L digits that are <= n via a
        #      tight walk: at each position pick an allowed digit d:
        #        - d < s[pos]: all remaining positions are free -> add k ** rest
        #        - d == s[pos]: stay tight, continue to next position
        #        - d > s[pos]: stop (would exceed n)
        #      If every position matches exactly, n itself is writable -> add 1.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.atMostNGivenDigitSet(["1", "3", "5", "7"], 100))        # expected: 20
    print(sol.atMostNGivenDigitSet(["1", "4", "9"], 1000000000))      # expected: 29523
    print(sol.atMostNGivenDigitSet(["7"], 8))                         # expected: 1
