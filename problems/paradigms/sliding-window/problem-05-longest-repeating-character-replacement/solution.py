"""Longest Repeating Character Replacement (LeetCode 424).

Fill in the body using the Sliding Window technique.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Return the longest run of one letter obtainable with at most k replacements.

        Args:
            s: The input string of uppercase English letters.
            k: The maximum number of characters that may be replaced.

        Returns:
            The length of the longest substring that can be made to consist of a
            single repeated letter using at most k replacements.

        Example:
            >>> Solution().characterReplacement("AABABBA", 1)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))     # expected: 4
    print(sol.characterReplacement("AABABBA", 1))  # expected: 4
    print(sol.characterReplacement("AAAA", 0))     # expected: 4
