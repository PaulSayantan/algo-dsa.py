"""Longest Substring Without Repeating Characters (LeetCode 3).

Fill in the body using the Sliding Window technique.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the length of the longest substring with all distinct characters.

        Args:
            s: The input string (may be empty).

        Returns:
            The length of the longest contiguous substring of s that contains no
            repeated character.

        Example:
            >>> Solution().lengthOfLongestSubstring("abcabcbb")
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # expected: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # expected: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # expected: 3
    print(sol.lengthOfLongestSubstring(""))          # expected: 0
