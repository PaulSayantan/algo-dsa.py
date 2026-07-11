"""Longest Substring Without Repeating Characters — empty solution template.

Fill in the body of `lengthOfLongestSubstring`. Do not hard-code answers.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the length of the longest substring with all-distinct characters.

        Args:
            s: The input string (may be empty).

        Returns:
            The length of the longest contiguous substring of `s` containing no
            repeated character.

        Example:
            >>> Solution().lengthOfLongestSubstring("abcabcbb")
            3
        """
        # TODO: implement using a variable-size sliding window
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # expected: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # expected: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # expected: 3
    print(sol.lengthOfLongestSubstring(""))          # expected: 0
