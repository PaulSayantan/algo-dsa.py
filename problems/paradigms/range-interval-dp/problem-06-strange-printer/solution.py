"""Strange Printer (LeetCode 664).

Fill in the body of `strangePrinter` using Range / Interval DP.
"""


class Solution:
    def strangePrinter(self, s: str) -> int:
        """Return the minimum number of printer turns to produce ``s``.

        Each turn prints a contiguous run of a single character, covering
        whatever was there before.

        Args:
            s: A non-empty string of lowercase English letters (length <= 100).

        Returns:
            The minimum number of turns needed to print ``s``.

        Example:
            >>> Solution().strangePrinter("aaabbb")
            2
        """
        # TODO: interval DP over dp[i][j]; merge turns when s[k] == s[i]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.strangePrinter("aaabbb"))  # expected: 2
    print(sol.strangePrinter("aba"))     # expected: 2
    print(sol.strangePrinter("abcba"))   # expected: 3
