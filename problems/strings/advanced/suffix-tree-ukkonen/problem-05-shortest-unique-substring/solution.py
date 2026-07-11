"""Shortest Unique Substring.

Return the shortest substring of `s` that occurs exactly once.
"""


class Solution:
    def shortestUniqueSubstring(self, s: str) -> str:
        """Return a shortest substring of `s` that occurs exactly once.

        Args:
            s: The input string of lowercase English letters.

        Returns:
            Any one shortest unique substring. Never empty for non-empty `s`
            (the whole string always occurs exactly once).

        Example:
            >>> Solution().shortestUniqueSubstring("cabca")
            'b'
        """
        # TODO: implement
        #   1. Append a unique terminal and build a suffix tree (Ukkonen, O(n)).
        #   2. Precompute leaf-counts per node (one DFS).
        #   3. A point with leaf-count == 1 spells a unique substring. The
        #      shortest one ends on the FIRST character of a leaf edge whose
        #      parent has leaf-count > 1: its length is parent_string_depth + 1.
        #      Scan those, skip anything that would include the sentinel, and
        #      keep the minimum length.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestUniqueSubstring("cabca"))    # expected: "b"
    print(sol.shortestUniqueSubstring("aabaaab"))   # expected: "ba"
    print(sol.shortestUniqueSubstring("aaaa"))      # expected: "aaaa"
