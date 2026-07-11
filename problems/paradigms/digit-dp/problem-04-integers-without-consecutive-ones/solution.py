"""Non-negative Integers Without Consecutive Ones (LeetCode 600).

Count integers in [0, n] whose binary representation has no two adjacent 1 bits.
Solve with a binary (base-2) Digit DP that tracks the previously placed bit.
"""

from functools import lru_cache


class Solution:
    def findIntegers(self, n: int) -> int:
        """Count integers x in [0, n] with no consecutive 1s in binary.

        Args:
            n: Inclusive upper bound of the range [0, n]. 1 <= n <= 10^9.

        Returns:
            The count of integers 0 <= x <= n whose binary form has no two
            adjacent set bits.

        Example:
            >>> Solution().findIntegers(5)
            5
        """
        # TODO: implement
        #
        # Suggested plan (binary Digit DP):
        #   bits = binary digits of n, most significant first (e.g. bin(n)[2:])
        #   dp(pos, prev_bit, tight) -> count of valid completions, where
        #       prev_bit is the bit placed at position pos-1.
        #   At each position choose bit b in {0, 1} (capped by bits[pos] if
        #   tight); forbid b == 1 when prev_bit == 1.
        #   Base case pos == len(bits): return 1 (the built number is valid).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findIntegers(5))  # expected: 5
    print(sol.findIntegers(1))  # expected: 2
    print(sol.findIntegers(2))  # expected: 3
