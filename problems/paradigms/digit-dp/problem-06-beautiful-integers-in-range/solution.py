"""Number of Beautiful Integers in the Range (LeetCode 2827).

Count integers in [low, high] that are divisible by k AND have equal counts of
even and odd digits. Solve with Digit DP using prefix counting f(high)-f(low-1),
tracking the running remainder mod k and the even-minus-odd digit balance.
"""

from functools import lru_cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        """Count beautiful integers in the inclusive range [low, high].

        A beautiful integer has an equal number of even and odd digits and is
        divisible by k.

        Args:
            low: Lower bound of the range, 0 < low <= high.
            high: Upper bound of the range, high <= 10^9.
            k: Divisor, 0 < k <= 20.

        Returns:
            The count of integers x with low <= x <= high that are beautiful.

        Example:
            >>> Solution().numberOfBeautifulIntegers(10, 20, 3)
            2
        """
        # TODO: implement
        #
        # Suggested plan (Digit DP with prefix counting):
        #   Define count_up_to(N): number of beautiful integers in [0, N].
        #   Answer = count_up_to(high) - count_up_to(low - 1).
        #
        #   For count_up_to(N):
        #     digits = decimal digits of N (most significant first)
        #     dp(pos, rem, balance, tight, started) -> count of completions,
        #       where rem = (number so far) mod k,
        #             balance = (#even digits) - (#odd digits) among real digits,
        #             started = whether a nonzero digit has been placed.
        #     Leading zeros (not started, d == 0) must NOT change balance or rem
        #       in a way that fakes a real digit; keep started False for them.
        #     Base case: return 1 if (started and rem == 0 and balance == 0)
        #       else 0.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfBeautifulIntegers(10, 20, 3))  # expected: 2
    print(sol.numberOfBeautifulIntegers(1, 10, 1))   # expected: 1
    print(sol.numberOfBeautifulIntegers(5, 5, 2))    # expected: 0
