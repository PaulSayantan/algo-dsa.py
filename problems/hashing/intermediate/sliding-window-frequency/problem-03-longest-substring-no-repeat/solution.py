"""Longest Substring Without Repeating Characters — LeetCode 3."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: map char -> last index; jump left past any repeat
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # expected: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))  # expected: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))  # expected: 3
    print(sol.lengthOfLongestSubstring(""))  # expected: 0
    print(sol.lengthOfLongestSubstring("au"))  # expected: 2
