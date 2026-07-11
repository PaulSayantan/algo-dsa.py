"""Find the Index of the First Occurrence in a String (LeetCode 28).

Solve this with the Rabin-Karp rolling-hash technique.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of ``needle`` in ``haystack``.

        Args:
            haystack: The text to search within.
            needle: The pattern to search for.

        Returns:
            The 0-based index of the first occurrence of ``needle`` inside
            ``haystack``, or ``-1`` if it does not occur. By convention, an
            empty ``needle`` returns ``0``.

        Example:
            >>> Solution().strStr("sadbutsad", "sad")
            0
            >>> Solution().strStr("leetcode", "leeto")
            -1
        """
        # TODO: implement using Rabin-Karp (polynomial rolling hash)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))   # expected: 0
    print(sol.strStr("leetcode", "leeto"))  # expected: -1
    print(sol.strStr("hello", "ll"))        # expected: 2
