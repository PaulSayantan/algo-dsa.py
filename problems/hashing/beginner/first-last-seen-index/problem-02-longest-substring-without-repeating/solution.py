"""Longest Substring Without Repeating Characters — LeetCode 3."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: track each char's last-seen index; jump the window start past repeats
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # expected: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))  # expected: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))  # expected: 3
    print(sol.lengthOfLongestSubstring(""))  # expected: 0
    print(sol.lengthOfLongestSubstring("au"))  # expected: 2
    print(sol.lengthOfLongestSubstring("dvdf"))  # expected: 3
