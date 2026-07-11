"""LeetCode 168 - Excel Sheet Column Title.

Convert a positive integer into its spreadsheet column title (bijective base-26),
building each letter with ASCII arithmetic (``chr(ord('A') + offset)``).
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """Return the Excel column title for a 1-based column number.

        Args:
            columnNumber: A positive integer, 1 <= columnNumber <= 2**31 - 1.

        Returns:
            The column title string, where 1 -> "A", 26 -> "Z", 27 -> "AA", etc.

        Example:
            >>> Solution().convertToTitle(28)
            'AB'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToTitle(1))    # expected: "A"
    print(sol.convertToTitle(28))   # expected: "AB"
    print(sol.convertToTitle(701))  # expected: "ZY"
