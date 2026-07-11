"""Number of Digit One (LeetCode 233).

Count the total number of times the digit 1 appears across all integers in the
range [0, n]. Solve with Digit DP over the decimal digits of n.
"""

from functools import lru_cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        """Count total occurrences of the digit 1 in every integer in [0, n].

        Args:
            n: Upper bound of the inclusive range [0, n]. 0 <= n <= 10^9.

        Returns:
            The total count of '1' digits appearing across 0, 1, 2, ..., n.

        Example:
            >>> Solution().countDigitOne(13)
            6
        """
        # TODO: implement
        #
        # Suggested plan (Digit DP):
        #   digits = list of decimal digits of n (most significant first)
        #   dp(pos, count, tight) -> total number of '1's contributed by all
        #       completions of the number, where `count` is the number of '1's
        #       already placed in positions [0, pos) and `tight` says whether
        #       the prefix equals n's prefix.
        #   At pos == len(digits): return count.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDigitOne(13))  # expected: 6
    print(sol.countDigitOne(0))   # expected: 0
    print(sol.countDigitOne(20))  # expected: 12
