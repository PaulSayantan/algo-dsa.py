"""Rotated Digits (LeetCode 788).

Count the "good" numbers in [1, n]: numbers whose digits are all rotatable
(none of 3, 4, 7) and that contain at least one digit that changes under a
180-degree rotation (one of 2, 5, 6, 9). Solve with Digit DP.
"""

from functools import lru_cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        """Count good numbers in the inclusive range [1, n].

        A number is good if every digit is in {0,1,2,5,6,8,9} and at least one
        digit is in {2,5,6,9}.

        Args:
            n: Upper bound of the range [1, n]. 1 <= n <= 10^4.

        Returns:
            The number of good integers x with 1 <= x <= n.

        Example:
            >>> Solution().rotatedDigits(10)
            4
        """
        # TODO: implement
        #
        # Suggested plan (Digit DP):
        #   digits = decimal digits of n (most significant first)
        #   INVALID = {3, 4, 7}; CHANGES = {2, 5, 6, 9}
        #   dp(pos, changed, tight) -> count of valid completions, where
        #       `changed` records whether a rotation-changing digit has been
        #       placed yet in positions [0, pos).
        #   At pos == len(digits): return 1 if `changed` else 0.
        #   (Optionally track a leading-zero flag; here the number 0 is naturally
        #    excluded because it never sets `changed`.)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotatedDigits(10))  # expected: 4
    print(sol.rotatedDigits(20))  # expected: 9
    print(sol.rotatedDigits(1))   # expected: 0
