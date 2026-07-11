"""Count Special Integers (LeetCode 2376).

Count integers in [1, n] whose digits are all distinct. Solve with Digit DP
whose state carries a 10-bit mask of digits already used, plus tight and
leading-zero flags.
"""

from functools import lru_cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        """Count special integers (all digits distinct) in the range [1, n].

        Args:
            n: Inclusive upper bound. 1 <= n <= 2 * 10^9.

        Returns:
            The count of integers x with 1 <= x <= n whose decimal digits are
            pairwise distinct.

        Example:
            >>> Solution().countSpecialNumbers(20)
            19
        """
        # TODO: implement
        #
        # Suggested plan (Digit DP with bitmask):
        #   digits = decimal digits of n (most significant first)
        #   dp(pos, mask, tight, started) -> count of valid completions, where
        #       mask has bit d set if digit d has already been placed in a
        #       "real" (post-leading-zero) position, and `started` indicates
        #       whether any nonzero digit has been placed yet.
        #   When not started, placing a 0 keeps started False and does NOT set
        #       any mask bit (leading zeros are not "used" digits).
        #   Skip a digit d if it is already in `mask`.
        #   Base case pos == len(digits): return 1 if started else 0
        #       (the empty number 0 is excluded from [1, n]).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSpecialNumbers(20))   # expected: 19
    print(sol.countSpecialNumbers(5))    # expected: 5
    print(sol.countSpecialNumbers(135))  # expected: 110
