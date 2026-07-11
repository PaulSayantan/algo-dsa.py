"""Implement strStr() — LeetCode 28.

Fill in the body using Naive Pattern Matching. Do not use built-in
substring search (e.g. str.find / str.index / the `in` operator) — the point
is to practice sliding the pattern over the text yourself.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of ``needle`` in ``haystack``.

        Args:
            haystack: The text to search within.
            needle: The pattern to search for.

        Returns:
            The 0-based index of the first occurrence of ``needle`` in
            ``haystack``, or ``-1`` if ``needle`` does not occur.

        Example:
            >>> Solution().strStr("hello", "ll")
            2
            >>> Solution().strStr("leetcode", "leeto")
            -1
        """
        # TODO: implement using Naive Pattern Matching
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))   # expected: 0
    print(sol.strStr("leetcode", "leeto"))  # expected: -1
    print(sol.strStr("hello", "ll"))        # expected: 2
