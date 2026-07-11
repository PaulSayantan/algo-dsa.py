"""Minimum Window Substring (LeetCode 76).

Fill in the body using the Sliding Window technique.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return the shortest substring of s that contains all characters of t.

        Every character of t must appear in the window at least as many times as it
        appears in t. If no such window exists, return the empty string.

        Args:
            s: The string to search within.
            t: The string whose characters (with multiplicity) must be covered.

        Returns:
            The minimum-length covering substring of s, or "" if none exists.

        Example:
            >>> Solution().minWindow("ADOBECODEBANC", "ABC")
            'BANC'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # expected: "BANC"
    print(sol.minWindow("a", "a"))                 # expected: "a"
    print(sol.minWindow("a", "aa"))                # expected: ""
