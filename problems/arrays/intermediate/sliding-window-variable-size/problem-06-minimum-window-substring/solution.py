"""Minimum Window Substring — empty solution template.

Fill in the body of `minWindow`. Do not hard-code answers.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return the shortest substring of s covering all characters of t.

        Args:
            s: The string to search within.
            t: The string whose characters (with multiplicity) must be covered.

        Returns:
            The smallest substring of `s` that contains every character of `t`
            (counting duplicates), or "" if no such substring exists.

        Example:
            >>> Solution().minWindow("ADOBECODEBANC", "ABC")
            'BANC'
        """
        # TODO: implement using a variable-size sliding window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # expected: "BANC"
    print(sol.minWindow("a", "a"))                # expected: "a"
    print(sol.minWindow("a", "aa"))               # expected: ""
