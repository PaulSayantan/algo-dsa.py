"""LeetCode 72 - Edit Distance (Levenshtein distance).

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of edits to turn word1 into word2.

        Allowed operations, each costing 1: insert a character, delete a
        character, or replace a character.

        Args:
            word1: The source string (lowercase English letters, may be empty).
            word2: The target string (lowercase English letters, may be empty).

        Returns:
            The minimum number of single-character insert/delete/replace
            operations needed to transform word1 into word2.

        Example:
            >>> Solution().minDistance("horse", "ros")
            3
        """
        # TODO: implement using a 2D DP table where dp[i][j] is the edit
        # distance between word1[:i] and word2[:j].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("horse", "ros"))            # expected: 3
    print(sol.minDistance("intention", "execution"))  # expected: 5
    print(sol.minDistance("", "abc"))                 # expected: 3
