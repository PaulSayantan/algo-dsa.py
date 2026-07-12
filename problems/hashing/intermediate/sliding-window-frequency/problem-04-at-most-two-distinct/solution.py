"""Longest Substring with At Most Two Distinct Characters — LeetCode 159."""
from collections import defaultdict  # noqa: F401


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # TODO: grow the window; shrink left while more than 2 distinct chars
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstringTwoDistinct("eceba"))  # expected: 3
    print(sol.lengthOfLongestSubstringTwoDistinct("ccaabbb"))  # expected: 5
    print(sol.lengthOfLongestSubstringTwoDistinct("a"))  # expected: 1
    print(sol.lengthOfLongestSubstringTwoDistinct("abaccc"))  # expected: 4
