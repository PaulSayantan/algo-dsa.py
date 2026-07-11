"""LeetCode 3 - Longest Substring Without Repeating Characters.

Find the length of the longest substring with all-distinct characters using a
sliding window whose pointers each move forward only, giving O(n) total work.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the length of the longest substring with no repeated character.

        Args:
            s: The input string (may be empty).

        Returns:
            The length of the longest substring of ``s`` in which every character
            is distinct.

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
