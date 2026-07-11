"""Edit Distance (Levenshtein) — LeetCode 72.

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of insert/delete/replace ops to turn word1 into word2.

        Args:
            word1: The source string (lowercase letters, length 0..500).
            word2: The target string (lowercase letters, length 0..500).

        Returns:
            The Levenshtein edit distance between word1 and word2.

        Example:
            >>> Solution().minDistance("horse", "ros")
            3
        """
        # TODO: implement using memoization (top-down) or tabulation (bottom-up).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("horse", "ros"))            # expected: 3
    print(sol.minDistance("intention", "execution"))  # expected: 5
    print(sol.minDistance("", "abc"))                 # expected: 3
