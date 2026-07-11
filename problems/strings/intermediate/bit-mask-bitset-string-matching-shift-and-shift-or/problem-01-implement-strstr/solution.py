"""LeetCode 28 - Implement strStr() via Shift-And bit-parallel matching.

Fill in the body of `strStr`. Do NOT use `str.find` / the `in` operator; the point
of the exercise is to implement the Shift-And bitmask automaton yourself.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of `needle` in `haystack`.

        Args:
            haystack: The text to search within.
            needle: The pattern to search for. If empty, return 0.

        Returns:
            The 0-based index of the first character of the first occurrence of
            `needle` in `haystack`, or -1 if `needle` does not occur.

        Example:
            >>> Solution().strStr("sadbutsad", "sad")
            0
            >>> Solution().strStr("leetcode", "leeto")
            -1

        Approach (Shift-And):
            - Build B[c] = OR of (1 << j) over all positions j where needle[j] == c.
            - Maintain state D. For each text char c:
                  D = ((D << 1) | 1) & B.get(c, 0)
              A full match ends at index i when D has bit (m - 1) set.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))   # expected: 0
    print(sol.strStr("leetcode", "leeto"))  # expected: -1
    print(sol.strStr("hello", "ll"))        # expected: 2
