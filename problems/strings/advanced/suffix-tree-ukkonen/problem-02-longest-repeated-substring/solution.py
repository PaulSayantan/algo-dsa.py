"""Longest Duplicate Substring.

Return any longest substring of `s` that occurs at least twice (overlaps
allowed), or "" if none exists.
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """Return a longest substring that appears at least twice in `s`.

        Args:
            s: The input string of lowercase English letters.

        Returns:
            Any one longest duplicated substring, or "" if no substring repeats.

        Example:
            >>> Solution().longestDupSubstring("banana")
            'ana'
        """
        # TODO: implement
        #   1. Append a unique terminal and build a suffix tree (Ukkonen, O(n)).
        #   2. DFS the tree tracking string depth (chars from the root).
        #   3. The deepest INTERNAL node (>= 2 children) gives the answer; its
        #      path label is the longest duplicated substring. If the only
        #      internal node is the root, return "".
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestDupSubstring("banana"))      # expected: "ana"
    print(sol.longestDupSubstring("abcd"))         # expected: ""
    print(sol.longestDupSubstring("abcabcabc"))    # expected: "abcabc"
