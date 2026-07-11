"""Palindrome Partitioning II (LeetCode 132).

Fill in the body of `minCut` using Range / Interval DP for the palindrome table.
"""


class Solution:
    def minCut(self, s: str) -> int:
        """Return the minimum number of cuts for a palindrome partitioning.

        Args:
            s: A non-empty string of lowercase English letters (length <= 2000).

        Returns:
            The minimum number of cuts so that every resulting substring is a
            palindrome. A single palindromic string needs 0 cuts.

        Example:
            >>> Solution().minCut("aab")
            1
        """
        # TODO: build isPal[i][j] via interval DP, then a linear min-cut DP
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCut("aab"))     # expected: 1
    print(sol.minCut("a"))       # expected: 0
    print(sol.minCut("aabaa"))   # expected: 0
    print(sol.minCut("abccbc"))  # expected: 2
