"""Palindrome Partitioning II via an Eertree with series links.

Return the minimum number of cuts to split s into palindromic pieces.
"""

from __future__ import annotations


class Solution:
    def minCut(self, s: str) -> int:
        """Return the minimum number of cuts so every piece of ``s`` is a palindrome.

        A partition into ``k`` palindromic substrings uses ``k - 1`` cuts; this
        returns the smallest achievable ``k - 1``.

        Args:
            s: A non-empty string of lowercase English letters.

        Returns:
            The minimum number of cuts (0 if ``s`` is already a palindrome).

        Example:
            >>> Solution().minCut("aab")
            1
        """
        # TODO: implement
        # Suggested plan (Eertree + series links, O(n log n)):
        #   1. Build the eertree incrementally. For each node also store:
        #        diff[v]   = length[v] - length[suffix_link[v]]
        #        slink[v]  = series link (skips a whole run of equal diff)
        #   2. Keep dp[i] = min pieces to partition the first i characters,
        #      dp[0] = 0. Also keep g[v], a helper aggregate per series.
        #   3. After adding s[i-1], walk the O(log i) series links from `last`.
        #      For each series head v:
        #        g[v] = dp[i - (length[slink[v]] + diff[v])]
        #        if diff[v] == diff[suffix_link[v]]:
        #            g[v] = min(g[v], g[suffix_link[v]])
        #        dp[i] = min(dp[i], g[v] + 1)
        #   4. Answer is dp[n] - 1 (pieces minus one = cuts).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCut("aab"))      # expected: 1
    print(sol.minCut("a"))        # expected: 0
    print(sol.minCut("bananas"))  # expected: 2
