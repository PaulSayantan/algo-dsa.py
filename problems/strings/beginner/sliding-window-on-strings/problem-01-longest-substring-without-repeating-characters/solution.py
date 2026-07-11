class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the length of the longest substring of ``s`` that contains
        no repeating characters.

        Args:
            s: The input string (may be empty).

        Returns:
            The length of the longest substring with all-distinct characters.

        Example:
            >>> Solution().lengthOfLongestSubstring("abcabcbb")
            3
            >>> Solution().lengthOfLongestSubstring("bbbbb")
            1
        """
        # TODO: implement using a sliding window that shrinks on duplicates.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # expected: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # expected: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # expected: 3
    print(sol.lengthOfLongestSubstring(""))          # expected: 0
