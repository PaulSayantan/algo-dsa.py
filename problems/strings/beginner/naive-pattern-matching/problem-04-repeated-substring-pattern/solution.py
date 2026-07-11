"""Repeated Substring Pattern — LeetCode 459.

Fill in the body using Naive Pattern Matching. Two idiomatic routes:

  (a) Reduction: search for `s` inside (s + s)[1:-1]; return whether it is
      found. Do the search yourself (no `in` operator).

  (b) Direct: for each divisor length L of len(s) with L < len(s), use naive
      matching to check that the block s[0:L] tiles s.

Either approach must implement the character comparison manually.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """Return whether ``s`` is some substring repeated two or more times.

        Args:
            s: The string to test.

        Returns:
            ``True`` if there is a substring ``t`` with
            ``1 <= len(t) < len(s)`` such that repeating ``t`` yields ``s``,
            otherwise ``False``.

        Example:
            >>> Solution().repeatedSubstringPattern("abab")
            True
            >>> Solution().repeatedSubstringPattern("aba")
            False
        """
        # TODO: implement using Naive Pattern Matching
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedSubstringPattern("abab"))          # expected: True
    print(sol.repeatedSubstringPattern("aba"))           # expected: False
    print(sol.repeatedSubstringPattern("abcabcabcabc"))  # expected: True
