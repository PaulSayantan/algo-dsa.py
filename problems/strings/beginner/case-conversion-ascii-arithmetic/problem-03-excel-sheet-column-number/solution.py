"""LeetCode 171 - Excel Sheet Column Number.

Convert a spreadsheet column title (e.g. "AB") into its 1-based column number by
reading the letters as base-26 digits via ASCII arithmetic.
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """Return the 1-based column number for an Excel column title.

        Args:
            columnTitle: A non-empty string of uppercase English letters,
                length 1..7, in the range ["A", "FXSHRXW"].

        Returns:
            The corresponding column number, where "A" -> 1, "Z" -> 26,
            "AA" -> 27, and so on.

        Example:
            >>> Solution().titleToNumber("AB")
            28
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.titleToNumber("A"))   # expected: 1
    print(sol.titleToNumber("AB"))  # expected: 28
    print(sol.titleToNumber("ZY"))  # expected: 701
