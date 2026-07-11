"""Repeated Substring Pattern — is `s` built from a repeated block?

Reduce to a substring test: `s` is periodic (a repeated smaller block) iff `s`
occurs inside `(s + s)[1:-1]`. Run that search with Boyer–Moore (string search).
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """Return True iff `s` is one substring repeated two or more times.

        Args:
            s: The string to test.

        Returns:
            True if `s` can be constructed by concatenating multiple copies of
            some proper substring of `s`; otherwise False.

        Example:
            >>> Solution().repeatedSubstringPattern("abab")
            True
            >>> Solution().repeatedSubstringPattern("aba")
            False
        """
        # TODO: implement using Boyer–Moore search of `s` inside (s + s)[1:-1]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedSubstringPattern("abab"))            # expected: True
    print(sol.repeatedSubstringPattern("aba"))             # expected: False
    print(sol.repeatedSubstringPattern("abcabcabcabc"))    # expected: True
