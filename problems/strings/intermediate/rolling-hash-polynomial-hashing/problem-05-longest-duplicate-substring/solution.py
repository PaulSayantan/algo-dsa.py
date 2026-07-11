"""Longest Duplicate Substring (LeetCode 1044).

Return a longest substring that occurs at least twice in ``s`` (overlaps
allowed), using binary search on length + a polynomial rolling hash per check.
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """Return any longest substring that appears more than once in ``s``.

        Args:
            s: The input string (lowercase English letters).

        Returns:
            A duplicate substring of maximum length, or ``""`` if ``s`` has no
            substring that repeats.

        Example:
            >>> Solution().longestDupSubstring("banana")  # one valid answer
            'ana'
            >>> Solution().longestDupSubstring("abcd")
            ''
        """
        # TODO: implement with binary search on length + rolling hash.
        #   - search(L): roll a length-L polynomial hash across s; keep a dict
        #     {hash: [start indices]} and, on a hash hit, verify equality; return
        #     a start index if a duplicate of length L exists, else -1.
        #   - Binary search the largest L in [1, n-1] for which search(L) != -1
        #     and return s[start:start + L].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestDupSubstring("banana"))  # expected: a length-3 dup, e.g. "ana"
    print(sol.longestDupSubstring("abcd"))     # expected: ""
    print(sol.longestDupSubstring("aaaaa"))    # expected: "aaaa"
