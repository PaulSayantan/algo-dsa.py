"""LeetCode 848 - Shifting Letters.

Apply cumulative (suffix-sum) shifts to a lowercase string, rotating each letter
within the alphabet using ASCII arithmetic and modulo 26.
"""

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """Return ``s`` after applying the cumulative shifts.

        Shift ``i`` advances the first ``i + 1`` characters forward by
        ``shifts[i]``, wrapping 'z' -> 'a'. Equivalently, position ``j`` is shifted
        by the suffix sum ``shifts[j] + ... + shifts[-1]``.

        Args:
            s: A string of lowercase English letters (1 <= len <= 10**5).
            shifts: A list of non-negative integers, same length as ``s``, each in
                the range [0, 10**9].

        Returns:
            The resulting string after all shifts are applied.

        Example:
            >>> Solution().shiftingLetters("abc", [3, 5, 9])
            'rpl'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shiftingLetters("abc", [3, 5, 9]))  # expected: "rpl"
    print(sol.shiftingLetters("aaa", [1, 2, 3]))  # expected: "gfd"
    print(sol.shiftingLetters("z", [52]))         # expected: "z"
