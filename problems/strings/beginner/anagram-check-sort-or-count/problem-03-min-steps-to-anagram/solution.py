"""LeetCode 1347 - Minimum Number of Steps to Make Two Strings Anagram.

Fill in the body of `minSteps`. Do not change the signature.
"""

from collections import Counter  # noqa: F401  (available if you choose to use it)


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """Return the fewest single-character replacements in `t` to make it an anagram of `s`.

        Args:
            s: The target string (lowercase English letters).
            t: The string to edit; same length as `s`. Only replacements are allowed.

        Returns:
            The minimum number of characters in `t` that must be replaced so that
            `t` becomes an anagram of `s`.

        Example:
            >>> Solution().minSteps("bab", "aba")
            1
            >>> Solution().minSteps("leetcode", "practice")
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSteps("bab", "aba"))          # expected: 1
    print(sol.minSteps("leetcode", "practice"))  # expected: 5
    print(sol.minSteps("anagram", "mangaar"))  # expected: 0
