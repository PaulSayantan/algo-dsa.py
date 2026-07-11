"""Repeated Substring Pattern — LeetCode 459.

Return True iff `s` can be built by repeating one of its strictly shorter
substrings two or more times. Solve with the KMP (Knuth-Morris-Pratt)
period property.
"""

from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """Decide whether `s` is a repetition of a shorter block.

        Args:
            s: The input string of lowercase letters.

        Returns:
            True if some substring `t` with len(t) < len(s) satisfies
            s = t + t + ... + t (>= 2 copies); False otherwise.

        Example:
            >>> Solution().repeatedSubstringPattern("abab")
            True
            >>> Solution().repeatedSubstringPattern("aba")
            False
        """
        # TODO: implement
        pass

    def _build_lps(self, pattern: str) -> List[int]:
        """Build the KMP failure/prefix (LPS) array for `pattern`.

        Args:
            pattern: The pattern string.

        Returns:
            A list `lps` where `lps[i]` is the length of the longest proper
            prefix of `pattern[0..i]` that is also a suffix of `pattern[0..i]`.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedSubstringPattern("abab"))          # expected: True
    print(sol.repeatedSubstringPattern("aba"))           # expected: False
    print(sol.repeatedSubstringPattern("abcabcabcabc"))  # expected: True
