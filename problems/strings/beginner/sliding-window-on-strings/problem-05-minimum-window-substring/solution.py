class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return the shortest substring of ``s`` that contains every
        character of ``t`` (including duplicates), or "" if none exists.

        Args:
            s: The string to search within.
            t: The string whose characters (with multiplicity) must be covered.

        Returns:
            The minimum-length covering substring of ``s``, or the empty
            string when no covering window exists.

        Example:
            >>> Solution().minWindow("ADOBECODEBANC", "ABC")
            'BANC'
            >>> Solution().minWindow("a", "aa")
            ''
        """
        # TODO: implement using an expand/contract sliding window with a
        # need-vs-have match counter.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # expected: "BANC"
    print(sol.minWindow("a", "a"))                # expected: "a"
    print(sol.minWindow("a", "aa"))               # expected: ""
