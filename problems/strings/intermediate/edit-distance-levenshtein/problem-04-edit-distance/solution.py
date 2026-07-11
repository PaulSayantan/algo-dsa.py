"""Edit Distance (LeetCode 72) — classic Levenshtein distance.

Compute the minimum number of insert / delete / replace operations to convert
one string into another.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the Levenshtein edit distance between word1 and word2.

        Allowed operations, each costing one step: insert a character, delete a
        character, or replace a character.

        Args:
            word1: The source string to transform.
            word2: The target string to reach.

        Returns:
            The minimum number of single-character insertions, deletions, and
            replacements required to turn word1 into word2.

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
    print(sol.minDistance("horse", "ros"))            # expected: 3
    print(sol.minDistance("intention", "execution"))  # expected: 5
    print(sol.minDistance("", "abc"))                 # expected: 3
