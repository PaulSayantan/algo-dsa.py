"""Longest Common Substring of Two Strings.

Return the longest contiguous string that occurs in both `s1` and `s2`.
"""


class Solution:
    def longestCommonSubstring(self, s1: str, s2: str) -> str:
        """Return a longest common (contiguous) substring of `s1` and `s2`.

        Args:
            s1: The first string (over a fixed alphabet, no reserved terminals).
            s2: The second string (over a fixed alphabet, no reserved terminals).

        Returns:
            Any one longest common substring, or "" if the strings share none.

        Example:
            >>> Solution().longestCommonSubstring("xabxa", "babxba")
            'abx'
        """
        # TODO: implement
        #   1. Build a generalized suffix tree over s1 + '#' + s2 + '$' using
        #      two distinct terminals and Ukkonen's algorithm (O(n1 + n2)).
        #   2. For each leaf, record which source string it belongs to
        #      (by comparing its suffix start index to the position of '#').
        #   3. DFS bottom-up: a node "sees" string 1 and/or string 2 based on the
        #      union over its children. The deepest node that sees BOTH, with its
        #      path label trimmed at any separator, is the answer.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubstring("xabxa", "babxba"))        # expected: "abx"
    print(sol.longestCommonSubstring("GeeksforGeeks", "GeeksQuiz"))  # expected: "Geeks"
    print(repr(sol.longestCommonSubstring("abcde", "fghij")))   # expected: ""
