"""Longest Happy Prefix — LeetCode 1392.

Return the longest proper prefix of `s` that is also a suffix, or "" if none.
This is exactly the final value of the KMP (Knuth-Morris-Pratt) failure/LPS
array.
"""

from typing import List


class Solution:
    def longestPrefix(self, s: str) -> str:
        """Return the longest non-empty proper prefix that is also a suffix.

        Args:
            s: The input string of lowercase letters.

        Returns:
            The longest happy prefix of `s`, or "" if no proper prefix is
            also a suffix.

        Example:
            >>> Solution().longestPrefix("level")
            'l'
            >>> Solution().longestPrefix("ababab")
            'abab'
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
    print(sol.longestPrefix("level"))         # expected: "l"
    print(sol.longestPrefix("ababab"))        # expected: "abab"
    print(sol.longestPrefix("leetcodeleet"))  # expected: "leet"
    print(sol.longestPrefix("a"))             # expected: ""
