class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Return the length of the longest substring of ``s`` containing at
        most ``k`` distinct characters.

        Args:
            s: The input string.
            k: The maximum number of distinct characters allowed in a window.

        Returns:
            The length of the longest substring with at most ``k`` distinct
            characters (0 when ``k`` is 0 or ``s`` is empty).

        Example:
            >>> Solution().lengthOfLongestSubstringKDistinct("eceba", 2)
            3
            >>> Solution().lengthOfLongestSubstringKDistinct("aa", 1)
            2
        """
        # TODO: implement using a sliding window with a character-count map.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))   # expected: 3
    print(sol.lengthOfLongestSubstringKDistinct("aa", 1))      # expected: 2
    print(sol.lengthOfLongestSubstringKDistinct("abaccc", 2))  # expected: 4
    print(sol.lengthOfLongestSubstringKDistinct("abc", 0))     # expected: 0
