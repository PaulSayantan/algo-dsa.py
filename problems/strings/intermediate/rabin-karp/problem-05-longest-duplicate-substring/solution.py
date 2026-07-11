"""Longest Duplicate Substring (LeetCode 1044).

Solve this with binary search on the answer length + Rabin-Karp membership test.
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """Return a longest substring of ``s`` that occurs at least twice.

        Occurrences may overlap. If no substring repeats, return the empty
        string. When several longest duplicates exist, any one of them is
        acceptable.

        Args:
            s: The input string of lowercase English letters.

        Returns:
            A duplicated substring of maximum length, or ``""`` if none exists.

        Example:
            >>> Solution().longestDupSubstring("banana")
            'ana'
            >>> Solution().longestDupSubstring("abcd")
            ''
        """
        # TODO: implement using binary search on length + Rabin-Karp rolling hash
        pass


if __name__ == "__main__":
    sol = Solution()
    print(repr(sol.longestDupSubstring("banana")))  # expected: 'ana'
    print(repr(sol.longestDupSubstring("abcd")))     # expected: ''
    print(repr(sol.longestDupSubstring("aaaaa")))    # expected: 'aaaa'
