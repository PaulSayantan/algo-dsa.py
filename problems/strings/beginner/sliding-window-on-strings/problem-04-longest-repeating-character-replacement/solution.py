class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Return the length of the longest substring that can be turned into
        a single repeated character using at most ``k`` replacements.

        Args:
            s: The input string of uppercase English letters.
            k: The maximum number of characters that may be replaced.

        Returns:
            The length of the longest achievable uniform substring.

        Example:
            >>> Solution().characterReplacement("ABAB", 2)
            4
            >>> Solution().characterReplacement("AABABBA", 1)
            4
        """
        # TODO: implement using a sliding window tracking the most frequent
        # character count in the window.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))     # expected: 4
    print(sol.characterReplacement("AABABBA", 1))  # expected: 4
    print(sol.characterReplacement("AAAA", 0))     # expected: 4
