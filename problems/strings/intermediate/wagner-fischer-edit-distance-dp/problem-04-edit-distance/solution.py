"""Edit Distance (LeetCode 72) — classic Levenshtein distance.

Empty solution template — fill in the logic yourself.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of edits to convert word1 into word2.

        A single edit is one insertion, one deletion, or one substitution of a character.
        This is the Levenshtein distance between the two strings.

        Args:
            word1: The source string to transform.
            word2: The target string to reach.

        Returns:
            The minimum number of insert/delete/replace operations to turn word1 into word2.

        Example:
            >>> Solution().minDistance("horse", "ros")
            3
            >>> Solution().minDistance("intention", "execution")
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("horse", "ros"))              # expected: 3
    print(sol.minDistance("intention", "execution"))    # expected: 5
    print(sol.minDistance("", "abc"))                    # expected: 3
    print(sol.minDistance("abc", "abc"))                 # expected: 0
